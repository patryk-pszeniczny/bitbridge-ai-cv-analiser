import os
import json
import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


class CVAnalyzer:
    """A class to analyze CVs using OpenAI API based on user-defined criteria."""

    def __init__(self, api_key=None):
        """
        Initializes the CVAnalyzer with an OpenAI API key.

        Args:
            api_key (str, optional): OpenAI API key. If not provided, it will be loaded from .env file.
        """
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("API key not found. Provide it in the .env file as OPENAI_API_KEY.")
        self.client = OpenAI(api_key=self.api_key)
        self.api_model = os.getenv("OPENAI_API_MODEL", "gpt-4")

    def load_config(self, config_path="config/config.json"):
        """
        Loads evaluation criteria from a JSON config file.

        Args:
            config_path (str): Path to the JSON configuration file.

        Returns:
            dict: Parsed criteria dictionary.
        """
        try:
            with open(config_path, encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"Error loading config.json: {str(e)}")

    def extract_text_from_pdf(self, pdf_path):
        """
        Extracts text content from a PDF file.

        Args:
            pdf_path (str): Path to the PDF file.

        Returns:
            str: Extracted text content from the PDF.
        """
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

    def analyze_with_openai(self, text, criteria):
        """
        Sends CV text and evaluation criteria to OpenAI API for analysis.

        Args:
            text (str): Text content of the CV.
            criteria (dict): Dictionary of evaluation criteria.

        Returns:
            dict: OpenAI response with evaluation details.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.api_model,
                messages=[
                    {"role": "system", "content": "You are a professional CV reviewer. Analyze the candidate based on the provided criteria."},
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
                temperature=0.3
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")


def get_output_filename(input_path):
    """
    Generates the output file name based on the input PDF path.

    Args:
        input_path (str): Path to the input PDF.

    Returns:
        str: Output filename with .json extension.
    """
    path = Path(input_path)
    return f"{path.stem}-output.json"


if __name__ == "__main__":
    try:
        analyzer = CVAnalyzer()
        criteria = analyzer.load_config()

        for pdf_file in Path('input/').glob('*.pdf'):
            print(f"\nProcessing: {pdf_file.name}...")
            text = analyzer.extract_text_from_pdf(pdf_file)

            print(f"Analyzing: {pdf_file.name}...")
            result = analyzer.analyze_with_openai(text, criteria)

            output_path = Path("output") / f"{pdf_file.stem}-output.json"
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

            print(f"Results saved to: {output_path}")

    except Exception as e:
        print(f"\nERROR: {str(e)}")
        print("Please make sure that:")
        print("- You have a valid 'config/config.json' file with evaluation criteria.")
        print("- You have a '.env' file with your OPENAI_API_KEY defined.")
        print("- Your PDF files are located in the 'input/' folder.")
