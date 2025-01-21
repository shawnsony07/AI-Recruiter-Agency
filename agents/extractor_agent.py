from typing import Dict, Any
from pdfminer.high_level import extract_text  # pip install pdfminer.six
from .base_agent import BaseAgent


class ExtractorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Extractor",
            instructions="""Extract and structure information from resumes.
            Focus on: personal info, work experience, education, skills, and certifications.
            Provide output in a clear, structured format."""
        )

    async def run(self, messages: list) -> Dict[str, Any]:
        """Process the resume and extract information"""
        print("📄 Extractor: Processing resume")

        resume_data = eval(messages[-1]["content"])

        # Extract text from PDF
        if resume_data.get("file_path"):
            raw_text = extract_text(resume_data["file_path"])
        else:
            raw_text = resume_data.get("text", "")

        # Get structured information from Ollama
        extracted_info = self._query_ollama(raw_text)

        return {
            "raw_text": raw_text,
            "structured_data": extracted_info,
            "extraction_status": "completed"
        }

