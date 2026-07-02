from google import genai
from google.genai import types

from config import GEMINI_API_KEY
from llm.base import BaseLLM
from models import SearchRequest
from prompts import PARSE_REQUEST_PROMPT


class GeminiLLM(BaseLLM):

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def parse_request(self, text: str) -> SearchRequest:

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=PARSE_REQUEST_PROMPT.format(
                request=text
            ),
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=SearchRequest
            )
        )

        return response.parsed