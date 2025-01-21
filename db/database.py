import sqlite3
from pathlib import Path
from typing import Dict, List, Any
import json
import os


class JobDatabase:
    def __init__(self):
        # Get the directory where database.py is located
        current_dir = Path(__file__).parent
        self.db_path = current_dir / "jobs.sqlite"
        self.schema_path = current_dir / "schema.sql"
        self._init_db()

    def _init_db(self):
        """Initialize the database with schema"""
        if not self.schema_path.exists():
            raise FileNotFoundError(f"Schema file not found at {self.schema_path}")

        with open(self.schema_path) as f:
            schema = f.read()

        with sqlite3.connect(self.db_path) as conn:
            conn.executescript(schema)

    def add_job(self, job_data: Dict[str, Any]) -> int:
        """Add a new job to the database"""
        query = """
        INSERT INTO jobs (
            title, company, location, type, experience_level,
            salary_range, description, requirements, benefits
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                query,
                (
                    job_data["title"],
                    job_data["company"],
                    job_data["location"],
                    job_data["type"],
                    job_data["experience_level"],
                    job_data.get("salary_range"),
                    job_data["description"],
                    json.dumps(job_data["requirements"]),
                    json.dumps(job_data.get("benefits", [])),
                ),
            )
            return cursor.lastrowid

    def get_all_jobs(self) -> List[Dict[str, Any]]:
        """Retrieve all jobs from the database"""
        query = "SELECT * FROM jobs ORDER BY created_at DESC"

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query)
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
                    "benefits": json.loads(row["benefits"]) if row["benefits"] else [],
                    "created_at": row["created_at"],
                }
                for row in rows
            ]

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


# import sqlite3
# from pathlib import Path
# from typing import Dict, List, Any
# import json


# class JobDatabase:
#     def __init__(self):
#         self.db_path = Path("./jobs.sqlite")
#         self.db_path.parent.mkdir(exist_ok=True)
#         self._init_db()

#     def _init_db(self):
#         """Initialize the database with schema"""
#         with open("./schema.sql") as f:
#             schema = f.read()

#         with sqlite3.connect(self.db_path) as conn:
#             conn.executescript(schema)

#     def add_job(self, job_data: Dict[str, Any]) -> int:
#         """Add a new job to the database"""
#         query = """
#         INSERT INTO jobs (
#             title, company, location, type, experience_level,
#             salary_range, description, requirements, benefits
#         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
#         """

#         with sqlite3.connect(self.db_path) as conn:
#             cursor = conn.cursor()
#             cursor.execute(
#                 query,
#                 (
#                     job_data["title"],
#                     job_data["company"],
#                     job_data["location"],
#                     job_data["type"],
#                     job_data["experience_level"],
#                     job_data.get("salary_range"),
#                     job_data["description"],
#                     json.dumps(job_data["requirements"]),
#                     json.dumps(job_data.get("benefits", [])),
#                 ),
#             )
#             return cursor.lastrowid

#     def get_all_jobs(self) -> List[Dict[str, Any]]:
#         """Retrieve all jobs from the database"""
#         query = "SELECT * FROM jobs ORDER BY created_at DESC"

#         with sqlite3.connect(self.db_path) as conn:
#             conn.row_factory = sqlite3.Row
#             cursor = conn.cursor()
#             cursor.execute(query)
#             rows = cursor.fetchall()

#             return [
#                 {
#                     "id": row["id"],
#                     "title": row["title"],
#                     "company": row["company"],
#                     "location": row["location"],
#                     "type": row["type"],
#                     "experience_level": row["experience_level"],
#                     "salary_range": row["salary_range"],
#                     "description": row["description"],
#                     "requirements": json.loads(row["requirements"]),
#                     "benefits": json.loads(row["benefits"]) if row["benefits"] else [],
#                     "created_at": row["created_at"],
#                 }
#                 for row in rows
#             ]

#     def search_jobs(
#         self, skills: List[str], experience_level: str = None
#     ) -> List[Dict[str, Any]]:
#         """Search jobs based on skills and experience level"""
#         query = """
#         SELECT * FROM jobs
#         WHERE requirements LIKE ?
#         """
#         params = [f"%{skill}%" for skill in skills]

#         if experience_level:
#             query += "AND experience_level = ?"
#             params.append(experience_level)

#         with sqlite3.connect(self.db_path) as conn:
#             conn.row_factory = sqlite3.Row
#             cursor = conn.cursor()

#             results = []
#             for param in params[:-1] if experience_level else params:
#                 cursor.execute(query, (param,))
#                 results.extend(cursor.fetchall())

#             # Remove duplicates and convert to dict
#             unique_jobs = {
#                 row["id"]: {
#                     "id": row["id"],
#                     "title": row["title"],
#                     "company": row["company"],
#                     "location": row["location"],
#                     "type": row["type"],
#                     "experience_level": row["experience_level"],
#                     "salary_range": row["salary_range"],
#                     "description": row["description"],
#                     "requirements": json.loads(row["requirements"]),
#                     "benefits": json.loads(row["benefits"]) if row["benefits"] else [],
#                     "created_at": row["created_at"],
#                 }
#                 for row in results
#             }

#             return list(unique_jobs.values())