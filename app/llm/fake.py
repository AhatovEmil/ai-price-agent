from models import SearchRequest
from llm.base import BaseLLM


class FakeLLM(BaseLLM):
    """
    Фейковая реализация LLM для разработки и тестирования.
    """

    def parse_request(self, text: str) -> SearchRequest:

        return SearchRequest(
            product=text,
            max_price=None,
            shop=None
        )