from abc import ABC, abstractmethod

from models import SearchRequest


class BaseLLM(ABC):
    """
    Базовый интерфейс для всех языковых моделей.
    """

    @abstractmethod
    def parse_request(self, text: str) -> SearchRequest:
        """
        Преобразовать запрос пользователя
        в объект SearchRequest.
        """
        pass