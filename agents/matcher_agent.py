from typing import Dict, Any
from .base_agent import BaseAgent
from db.database import JobDatabase
import ast

import json


from typing import Dict, Any, List
from .base_agent import BaseAgent
from db.database import JobDatabase
import json
import ast
import re
import sqlite3


class MatcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Matcher",
            instructions="""Match candidate profiles with job positions.
            Consider: skills match, experience level, location preferences.
            Provide detailed reasoning and compatibility scores.
            Return matches in JSON format with title, match_score, and location fields.""",
        )
        self.db = JobDatabase()

    async def run(self, messages: list) -> Dict[str, Any]:
        """Match candidate with available positions"""
        print("🎯 Matcher: Finding suitable job matches")

        try:
            # Convert single quotes to double quotes to make it valid JSON
            content = messages[-1].get("content", "{}").replace("'", '"')
            analysis_results = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"Error parsing analysis results: {e}")
            return {
                "matched_jobs": [],
                "match_timestamp": "2024-03-14",
                "number_of_matches": 0,
            }

        # Extract skills and experience level from analysis
        skills_analysis = analysis_results.get("skills_analysis", {})
        if not skills_analysis:
            print("No skills analysis provided in the input.")
            return {
                "matched_jobs": [],
                "match_timestamp": "2024-03-14",
                "number_of_matches": 0,
            }

        # Extract technical skills and experience level directly
        skills = skills_analysis.get("technical_skills", [])
        experience_level = skills_analysis.get("experience_level", "Mid-level")

        if not isinstance(skills, list) or not skills:
            print("No valid skills found, defaulting to an empty list.")
            skills = []

        if experience_level not in ["Junior", "Mid-level", "Senior"]:
            print("Invalid experience level detected, defaulting to Mid-level.")
            experience_level = "Mid-level"

        print(f" ==>>> Skills: {skills}, Experience Level: {experience_level}")
        # Search jobs database
        matching_jobs = self.search_jobs(skills, experience_level)

        # Calculate match scores
        scored_jobs = []
        for job in matching_jobs:
            # Calculate match score based on requirements overlap
            required_skills = set(job["requirements"])
            candidate_skills = set(skills)
            overlap = len(required_skills.intersection(candidate_skills))
            total_required = len(required_skills)
            match_score = (
                int((overlap / total_required) * 100) if total_required > 0 else 0
            )

            # Lower threshold for matching to 30%
            if match_score >= 30:  # Include jobs with >30% match
                scored_jobs.append(
                    {
                        "title": f"{job['title']} at {job['company']}",
                        "match_score": f"{match_score}%",
                        "location": job["location"],
                        "salary_range": job["salary_range"],
                        "requirements": job["requirements"],
                    }
                )

        print(f" ==>>> Scored Jobs: {scored_jobs}")
        # Sort by match score
        scored_jobs.sort(key=lambda x: int(x["match_score"].rstrip("%")), reverse=True)

        return {
            "matched_jobs": scored_jobs[:3],  # Top 3 matches
            "match_timestamp": "2024-03-14",
            "number_of_matches": len(scored_jobs),
        }

    def search_jobs(
        self, skills: List[str], experience_level: str
    ) -> List[Dict[str, Any]]:
        """Search jobs based on skills and experience level"""
        query = """
        SELECT * FROM jobs
        WHERE experience_level = ?
        AND (
        """
        query_conditions = []
        params = [experience_level]

        # Create LIKE conditions for each skill
        for skill in skills:
            query_conditions.append("requirements LIKE ?")
            params.append(f"%{skill}%")

        query += " OR ".join(query_conditions) + ")"

        try:
            with sqlite3.connect(self.db.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(query, params)
                rows = cursor.fetchall()

                return [
                    {
                        "id": row["id"],
                        "title": row["title"],
                        "company": row["company"],
                        "location": row["location"],
                        "type": row["type"],
                        "experience_level": row["experience_level"],
                        "salary_range": row["salary_range"],
                        "description": row["description"],
                        "requirements": json.loads(row["requirements"]),
                        "benefits": (
                            json.loads(row["benefits"]) if row["benefits"] else []
                        ),
                    }
                    for row in rows
                ]
        except Exception as e:
            print(f"Error searching jobs: {e}")
            return []


