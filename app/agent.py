from llm.gemini import GeminiLLM


class PriceAgent:

    def __init__(self):
        self.llm = GeminiLLM()

    def greet(self) -> str:
        return "👋 AI Price Agent"

    def process_request(self, text: str):
        return self.llm.parse_request(text)