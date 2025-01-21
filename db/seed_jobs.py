from pathlib import Path
import sys

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

from db.database import JobDatabase


def seed_jobs():
    """Seed the database with sample job listings"""
    db = JobDatabase()

    jobs = [
        {
            "title": "Senior Software Engineer",
            "company": "TechCorp",
            "location": "Remote",
            "type": "Full-time",
            "experience_level": "Senior",
            "salary_range": "$120,000 - $180,000",
            "description": "Lead development of cloud-native applications using modern technologies.",
            "requirements": [
                "Python",
                "JavaScript",
                "React",
                "AWS",
                "Kubernetes",
                "5+ years experience",
            ],
            "benefits": [
                "Health insurance",
                "401(k) matching",
                "Remote work",
                "Learning budget",
            ],
        },
        {
            "title": "Data Scientist",
            "company": "DataCo",
            "location": "New York, NY",
            "type": "Full-time",
            "experience_level": "Mid-level",
            "salary_range": "$100,000 - $140,000",
            "description": "Build and deploy machine learning models for predictive analytics.",
            "requirements": [
                "Python",
                "SQL",
                "Machine Learning",
                "Statistics",
                "3+ years experience",
            ],
            "benefits": ["Health insurance", "Stock options", "Flexible hours"],
        },
        {
            "title": "Frontend Developer",
            "company": "WebTech",
            "location": "Remote",
            "type": "Full-time",
            "experience_level": "Mid-level",
            "salary_range": "$90,000 - $130,000",
            "description": "Create responsive web applications using modern frontend technologies.",
            "requirements": [
                "JavaScript",
                "TypeScript",
                "React",
                "CSS",
                "3+ years experience",
            ],
            "benefits": ["Health insurance", "Remote work", "Professional development"],
        },
        {
            "title": "Project Manager",
            "company": "BizGroup",
            "location": "San Francisco, CA",
            "type": "Full-time",
            "experience_level": "Mid-level",
            "salary_range": "$80,000 - $110,000",
            "description": "Manage multiple projects and coordinate with cross-functional teams.",
            "requirements": [
                "Project management",
                "Agile methodologies",
                "Communication skills",
                "3+ years experience",
            ],
            "benefits": ["Health insurance", "401(k)", "Paid time off"],
        },
        {
            "title": "Graphic Designer",
            "company": "DesignCo",
            "location": "Austin, TX",
            "type": "Part-time",
            "experience_level": "Entry-level",
            "salary_range": "$40,000 - $60,000",
            "description": "Design marketing materials and digital content for clients.",
            "requirements": [
                "Adobe Creative Suite",
                "Illustration skills",
                "Creativity",
                "1+ year experience",
            ],
            "benefits": ["Flexible schedule", "Remote options"],
        },
        {
            "title": "Marketing Specialist",
            "company": "MarketMasters",
            "location": "Chicago, IL",
            "type": "Full-time",
            "experience_level": "Mid-level",
            "salary_range": "$70,000 - $90,000",
            "description": "Develop and implement marketing campaigns for various products.",
            "requirements": [
                "SEO",
                "Content marketing",
                "Google Analytics",
                "2+ years experience",
            ],
            "benefits": [
                "Health insurance",
                "Paid vacation",
                "Professional development",
            ],
        },
        {
            "title": "Customer Support Representative",
            "company": "SupportHub",
            "location": "Remote",
            "type": "Full-time",
            "experience_level": "Entry-level",
            "salary_range": "$35,000 - $50,000",
            "description": "Assist customers with inquiries and resolve technical issues.",
            "requirements": [
                "Customer service skills",
                "Basic technical troubleshooting",
                "Strong communication",
            ],
            "benefits": ["Remote work", "Health insurance", "Paid training"],
        },
        {
            "title": "Cybersecurity Analyst",
            "company": "SecureIT",
            "location": "Washington, DC",
            "type": "Full-time",
            "experience_level": "Mid-level",
            "salary_range": "$95,000 - $130,000",
            "description": "Monitor and respond to security incidents and protect company data.",
            "requirements": [
                "Cybersecurity certifications (CISSP, CEH)",
                "Network security",
                "3+ years experience",
            ],
            "benefits": ["Health insurance", "401(k)", "Professional development"],
        },
        {
            "title": "HR Coordinator",
            "company": "PeopleFirst",
            "location": "Boston, MA",
            "type": "Full-time",
            "experience_level": "Entry-level",
            "salary_range": "$45,000 - $60,000",
            "description": "Support HR functions including recruitment, onboarding, and employee relations.",
            "requirements": [
                "HR experience",
                "Communication skills",
                "Organizational skills",
                "1+ year experience",
            ],
            "benefits": ["Health insurance", "Paid time off", "Retirement plan"],
        },
        {
            "title": "Mechanical Engineer",
            "company": "BuildWorks",
            "location": "Houston, TX",
            "type": "Full-time",
            "experience_level": "Mid-level",
            "salary_range": "$85,000 - $120,000",
            "description": "Design and test mechanical components for manufacturing.",
            "requirements": [
                "CAD software",
                "Mechanical design",
                "Manufacturing experience",
                "3+ years experience",
            ],
            "benefits": ["Health insurance", "Paid vacation", "401(k) matching"],
        },
        {
            "title": "Barista",
            "company": "CoffeeHouse",
            "location": "Portland, OR",
            "type": "Part-time",
            "experience_level": "Entry-level",
            "salary_range": "$15 - $18 per hour",
            "description": "Prepare coffee and serve customers in a friendly environment.",
            "requirements": [
                "Customer service skills",
                "Barista experience (preferred)",
                "Positive attitude",
            ],
            "benefits": ["Flexible hours", "Employee discount"],
        },
        {
            "title": "UX Researcher",
            "company": "DesignLabs",
            "location": "Remote",
            "type": "Full-time",
            "experience_level": "Mid-level",
            "salary_range": "$85,000 - $110,000",
            "description": "Conduct user research to improve product designs and user experiences.",
            "requirements": [
                "User research methods",
                "Interviewing skills",
                "Data analysis",
                "2+ years experience",
            ],
            "benefits": ["Health insurance", "Remote work", "Professional development"],
        },
        {
            "title": "Electrician",
            "company": "BrightSpark",
            "location": "Denver, CO",
            "type": "Full-time",
            "experience_level": "Mid-level",
            "salary_range": "$50,000 - $75,000",
            "description": "Install and maintain electrical systems in residential and commercial buildings.",
            "requirements": [
                "Electrician license",
                "Experience with electrical systems",
                "3+ years experience",
            ],
            "benefits": ["Health insurance", "Paid time off", "401(k)"],
        },
        {
            "title": "Junior Software Engineer",
            "company": "Innovatech",
            "location": "Remote",
            "type": "Full-time",
            "experience_level": "Junior",
            "salary_range": "$70,000 - $90,000",
            "description": "Assist in the development and maintenance of web applications.",
            "requirements": [
                "Python",
                "JavaScript",
                "Basic knowledge of React",
                "1+ year experience",
            ],
            "benefits": ["Health insurance", "401(k) matching", "Remote work"],
        },
        {
            "title": "Product Designer",
            "company": "CreateSpace",
            "location": "San Francisco, CA",
            "type": "Full-time",
            "experience_level": "Mid-level",
            "salary_range": "$100,000 - $130,000",
            "description": "Design and prototype new product features based on user needs.",
            "requirements": [
                "Sketch",
                "Figma",
                "User-centered design principles",
                "2+ years experience",
            ],
            "benefits": [
                "Health insurance",
                "Paid vacation",
                "Professional development",
            ],
        },
    ]

    for job in jobs:
        db.add_job(job)

    print("Database seeded successfully!")


if __name__ == "__main__":
    seed_jobs()