"""
Portfolio content data structure.
Centralized location for all portfolio content to separate data from UI logic.

Replace the placeholder values below with your own details.
"""

PERSONAL_INFO = {
    "name": "Your Name",
    "title": "Software Engineer",
    "company": "Acme Corp",
    "company_url": "https://example.com",
    "tagline": "Backend Engineer | Distributed Systems · Cloud · APIs",
    "bio": """I am a <strong>Software Engineer</strong> who enjoys building scalable backend systems and automation-driven solutions. Write a short paragraph here about your background, interests, and what you are currently working on.""",
    "email": "you@example.com",
    "phone": "+1-555-0100",
    "location": "City, Country",
    "website": "https://example.com",
    "years_of_experience": "3+",
}

SOCIAL_LINKS = {
    "linkedin": "https://www.linkedin.com/in/your-handle",
    "github": "https://github.com/your-username",
    "email": "mailto:you@example.com",
    "website": "https://example.com",
    "twitter": "",  # Optional
}

WORK_EXPERIENCE = [
    {
        "company": "Acme Corp",
        "position": "Software Engineer",
        "duration": "Jan 2024 - Present",
        "location": "Remote",
        "description": "Backend Engineering | Distributed Systems",
        "achievements": [
            "Designed and maintained backend services handling high-volume data processing",
            "Improved observability through structured logging, metrics, and tracing",
            "Built user-facing features such as dashboards, reporting, and analytics",
            "Integrated LLM-based enrichment into existing data pipelines"
        ],
        "tech_stack": ["Python", "FastAPI", "PostgreSQL", "Redis", "Docker", "AWS"]
    },
    {
        "company": "Example Labs",
        "position": "Junior Software Engineer",
        "duration": "Jun 2021 - Dec 2023",
        "location": "City, Country",
        "description": "Automation | Microservices",
        "achievements": [
            "Automated recurring engineering tasks, reducing manual workload",
            "Built ETL pipelines and scheduled jobs for data ingestion",
            "Migrated synchronous workflows to a queue-based, event-driven architecture"
        ],
        "tech_stack": ["Python", "Django REST", "Celery", "RabbitMQ", "Docker", "CI/CD"]
    }
]

PROJECTS = [
    {
        "name": "Sample Project One",
        "description": "A short description of what this project does and the problem it solves.",
        "tech_stack": ["Python", "FastAPI", "PostgreSQL"],
        "highlights": [
            "Key feature or accomplishment",
            "Another notable detail",
            "Measurable result or impact"
        ],
        "github": "",
        "demo": "",
        "image": ""
    },
    {
        "name": "Sample Project Two",
        "description": "A data or machine learning project showcasing analysis and modeling skills.",
        "tech_stack": ["Python", "Pandas", "scikit-learn"],
        "highlights": [
            "Data cleaning and exploration",
            "Model training and evaluation",
            "Interactive visualizations"
        ],
        "github": "",
        "demo": "",
        "image": ""
    },
    {
        "name": "Sample Project Three",
        "description": "A cloud or DevOps project demonstrating deployment and infrastructure skills.",
        "tech_stack": ["Docker", "AWS", "CI/CD"],
        "highlights": [
            "Containerized deployment",
            "Automated build and release pipeline"
        ],
        "github": "",
        "demo": "",
        "image": ""
    }
]

# Skill values (0-100) are used for proficiency levels; only names are displayed.
SKILLS = {
    "Languages": {
        "Python": 90,
        "SQL": 85,
        "Bash": 80
    },
    "Backend": {
        "FastAPI": 90,
        "Django REST": 85,
        "Celery": 85,
        "AsyncIO": 80
    },
    "Databases": {
        "PostgreSQL": 85,
        "MongoDB": 80,
        "Redis": 85
    },
    "Infrastructure": {
        "Docker": 90,
        "AWS": 80,
        "Nginx": 75,
        "CI/CD Pipelines": 80
    },
    "GenAI": {
        "LLM Integration": 80,
        "RAG Pipelines": 80,
        "Vector Databases": 75
    }
}

EDUCATION = [
    {
        "degree": "B.Sc. in Computer Science",
        "institution": "Example University",
        "status": "Completed",
        "highlights": []
    },
    {
        "degree": "M.Sc. in Computer Science",
        "institution": "Sample Institute of Technology",
        "status": "Pursuing",
        "highlights": []
    }
]

CERTIFICATIONS = [
    {
        "name": "Sample Professional Certificate",
        "issuer": "Certification Provider",
        "date": "2024",
        "url": "#",
        "skills": ["Python", "Automation"]
    },
    {
        "name": "Sample Cloud Certification",
        "issuer": "Cloud Provider",
        "date": "2023",
        "url": "#",
        "skills": ["Cloud", "Architecture"]
    }
]
