from pydantic import BaseModel

class PromptQuery(BaseModel):
    prompt: str