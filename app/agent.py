from llm.gemini import GeminiLLM
from services.search_service import SearchService


class PriceAgent:

    def __init__(self):

        self.llm = GeminiLLM()
        self.search_service = SearchService()

    def greet(self) -> str:
        return "👋 AI Price Agent"

    def process_request(self, text: str):

        request = self.llm.parse_request(text)

        products = self.search_service.search(request)

        return products