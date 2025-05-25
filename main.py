import json
from pathlib import Path
from cv_analyzer import CVAnalyzer


class CVAnalyzerRunner:
    def __init__(self):
        self.analyzer = CVAnalyzer()

    def get_output_filename(self, input_path):
        path = Path(input_path)
        return f"{path.stem}-output.json"

    def run(self):
        criteria = self.analyzer.load_criteria()
        input_dir = Path("input")
        output_dir = Path("output")
        output_dir.mkdir(parents=True, exist_ok=True)

        for pdf_file in input_dir.glob("*.pdf"):
            try:
                print(f"\nProcessing: {pdf_file.name}...")
                text = self.analyzer.extract_text_from_pdf(pdf_file)

                print(f"Analyzing: {pdf_file.name}...")
                result = self.analyzer.analyze(text, criteria)

                output_path = output_dir / self.get_output_filename(pdf_file)
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)

                print(f"Results saved to: {output_path}")
            except Exception as e:
                print(f"Failed to analyze {pdf_file.name}: {e}")


if __name__ == "__main__":
    try:
        runner = CVAnalyzerRunner()
        runner.run()
    except Exception as e:
        print(f"\nERROR: {str(e)}")
        print("Please make sure that:")
        print("- You have a valid 'config/config.json' file with evaluation criteria.")
        print("- You have a '.env' file with your OPENAI_API_KEY and prompts defined.")
        print("- Your PDF files are located in the 'input/' folder.")
