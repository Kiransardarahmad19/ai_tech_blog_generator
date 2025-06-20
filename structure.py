from pydantic import BaseModel
from typing import List, Optional

class BlogResponse(BaseModel):
    model: str
    generated_text: str
    usage: dict

class StructuredBlogOutput(BaseModel):
    hashtags: List[str]
    full_blog: str
    instagram_caption: str
    canva_texts: List[str]

class BlogOutputWithRaw(BaseModel):
    raw_text: str
    structured: Optional[StructuredBlogOutput]
