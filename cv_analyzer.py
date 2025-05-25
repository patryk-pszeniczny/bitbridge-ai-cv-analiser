import os
import json
import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
class CVAnalyzer:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("API key not found. Provide it in the .env file as OPENAI_API_KEY.")
        self.client = OpenAI(api_key=self.api_key)
        self.api_model = os.getenv("OPENAI_API_MODEL", "gpt-4")
        self.api_temperature = float(os.getenv("OPENAI_API_TEMPERATURE", "0"))
        self.api_content = os.getenv("OPENAI_API_CONTENT", "content")

    def load_criteria(self, config_path="config/config.json"):
        try:
            with open(config_path, encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"Error loading config.json: {str(e)}")

    def extract_text_from_pdf(self, pdf_path):
        text = ""
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            return text
        except Exception as e:
            raise Exception(f"Error processing PDF file '{pdf_path}': {str(e)}")

    def analyze(self, text, criteria):
        try:
            response = self.client.chat.completions.create(
                model=self.api_model,
                messages=[
                    {
                        "role": "system",
                        "content": self.api_content},
                    {
                        "role": "user",
                        "content": f"""
                You will be provided with a CV and a list of evaluation criteria. Analyze the CV and return a structured JSON report.

                ### CV Text:
                {text}
                
                ### Evaluation Criteria:
                {json.dumps(criteria, indent=2)}
                
                ### Instructions:
                - Be detailed but concise.
                - Use clear, professional language.
                - Focus on relevance, completeness, and clarity of the CV.
                - Evaluate based on alignment with the provided criteria and general industry standards.
                - If certain information is missing but expected, include it in the 'missing' list.
                - If the CV contains unrealistic or misleading claims (e.g., “automatically accepted by AI”), treat them as red flags and mention them in the summary.
                - Suggest follow-up questions that could be asked during an interview to clarify any uncertainties or evaluate deeper alignment.
                
                ### Return a JSON object with the following fields:
                - "overall_score" (0-100): Overall fit score based on the criteria.
                - "best_fit" (0-100): Score reflecting how well the candidate fits the most relevant role or area.
                - "candidate": Full name of the candidate (if available).
                - "matches": List of criteria clearly satisfied by the CV.
                - "missing": List of criteria not met, unclear, or not addressed.
                - "summary": Multi-line summary of strengths, weaknesses, and general impressions. Format it as a bullet-point list in English.
                - "follow_up_questions": A list of 10 clear, relevant questions you would ask the candidate based on the CV and criteria. These should aim to:
                    - Clarify any unclear or missing points.
                    - Explore relevant experiences more deeply.
                    - Address potential gaps or inconsistencies.
                """
                    }
                ],
                temperature=self.api_temperature
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
