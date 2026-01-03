from openai import OpenAI
from openai.types.chat import ChatCompletion
from openai.types.chat.chat_completion import ChatCompletionMessage

from utils.config import OPENAI_API_KEY

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def initial_completion(
        self,
        messages: list[ChatCompletionMessage],
        history: list[ChatCompletionMessage] | None = None,
        model: str = "gpt-5",
        temperature: float = 1,
        json_mode: bool = False
    ) -> ChatCompletion:
        """
        Create a chat completion using OpenAI's API.
        
        Args:
            messages: List of chat messages
            model: The model to use (default: "gpt-4")
            stream: Whether to stream the response (default: False)
            temorature: Sampling temperature (default: 1)
            json_mode: Whether to return response in JSON format (default: False)
            
        Returns:
            Either a ChatCompletion or an AsyncIterable of ChatCompletionChunk if streaming
        """
        try:
            response_format = {"type": "json_object"} if json_mode else {"type": "text"}
            
            chat_completion =self.client.chat.completions.create(
                messages=messages,
                model=model,
                temperature=temperature,
                response_format=response_format
            )
            
            return chat_completion
            
        except Exception as error:
            print(f"Error in OpenAI completion: {error}")
            raise 