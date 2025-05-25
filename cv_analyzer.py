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
                    {"role": "system",
                     "content": "You are a professional CV reviewer. Analyze the candidate based on the provided criteria."},
                    {"role": "user", "content": f"""
                CV Text:
                {text}

                Evaluation Criteria:
                {json.dumps(criteria, indent=2)}

                Return the result as a JSON object with the following fields:
                - 'overall_score' (0-100): overall fit score
                - 'matches': list of satisfied criteria
                - 'missing': list of missing or unsatisfied criteria
                - 'summary': brief textual summary in English
                """}
                ],
                temperature=self.api_temperature
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
