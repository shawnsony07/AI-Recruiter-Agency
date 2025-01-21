
# AI Recruiter Agency 🤖

An intelligent recruitment analysis system powered by Ollama (LLaMA 3.2) and Swarm Framework that automates resume processing, candidate screening, and job matching through coordinated AI agents.
## Features ✨

•	Intelligent Resume Analysis: Extract and analyze key       information from PDF resumes

•	Skills Assessment: Comprehensive evaluation of candidate skills and experience

•	Automated Job Matching: Match candidates with suitable positions based on skills and requirements

•	Smart Screening: AI-powered candidate screening with detailed reporting

•	Intelligent Recommendations: Generate actionable insights and recommendations

•	User-Friendly Interface: Modern web interface built with Streamlit


## Technology Stack 🛠️

•	Backend: Python

•	AI Model: Ollama (LLaMA 3.2)

•	Framework: Swarm Framework for AI agent coordination

•	Frontend: Streamlit

•	File Processing: PDF processing capabilities

•	Logging: Custom logging system


## Prerequisites 📋

•	Python 3.8+

•	Ollama 

•	Required Python packages (listed in requirements.txt)

## Installation 🚀

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ai-recruiter-agency.git
cd ai-recruiter-agency
```
2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Set up Ollama:

```bash
# Install Ollama following the official documentation
# Pull the LLaMA 3.2 model
ollama pull llama2:3.2
```
## Project Structure 📁

ai-recruiter-agency/

├── app.py                  # Main Streamlit application

├── agents/

│   └── orchestrator.py     # AI agent orchestration

├── utils/

│   ├── logger.py          # Logging configuration

│   └── exceptions.py      # Custom exceptions

├── uploads/               # Temporary storage for uploads

├── results/              # Analysis results storage

└── requirements.txt      # Project dependencies
## Usage 💡

1. Start the application:

```bash
streamlit run app.py
```

2. Access the web interface at  http://localhost:8501
3. Upload a PDF resume and wait for the analysis results
4. View the results across four categories:
•	Analysis

•	Job Matches

•	Screening

•	Recommendations



## Configuration ⚙️

Create a .env file in the project root:

env
```bash
OLLAMA_API_URL=http://localhost:11434
LOG_LEVEL=INFO
```
## Deployment 🌐

### Local Deployment

1.	Ensure all prerequisites are installed
2.	Follow the installation steps
3.	Run the application using Streamlit

### Docker Deployment

1. Build the Docker image:

```bash
docker build -t ai-recruiter-agency .
```

2. Run the container:

```bash
docker run -p 8501:8501 ai-recruiter-agency
```

### Cloud Deployment
The application can be deployed to various cloud platforms:

•	Streamlit Cloud: Direct deployment with GitHub repository

•	Heroku: Using the Procfile included in the repository

•	AWS/GCP: Using container services (ECS/GKE)



## API Documentation 📚

The Orchestrator Agent provides the following main methods:
python
```bash
async def process_application(resume_data: dict) -> dict:
    """
    Process a resume through the AI recruitment pipeline
    
    Parameters:
    resume_data (dict): Dictionary containing resume file path and metadata
    
    Returns:
        dict: Analysis results including skills, matches, and recommendations
    """
```
## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## License

[MIT](https://choosealicense.com/licenses/mit/)

