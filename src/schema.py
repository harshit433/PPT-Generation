from pydantic import BaseModel, Field
from typing import List, Literal, Union

# Define constraints for each slide type
class WelcomeSlideContent(BaseModel):
    title: str = Field(..., max_length=120, description="Title with a maximum of 12 words.")
    subtitle: str = Field(..., max_length=200, description="Subtitle with a maximum of 20 words.")

class SimpleContentSlideContent(BaseModel):
    heading: str = Field(..., max_length=80, description="Heading with a maximum of 8 words.")
    text_content: str = Field(..., max_length=500, description="Content with a maximum of 50 words.")

class ThreeTextContentSlideContent(BaseModel):
    heading: str = Field(..., max_length=80, description="Heading with a maximum of 8 words.")
    text_content_1: str = Field(..., max_length=400, description="First text content with a maximum of 40 words.")
    text_content_2: str = Field(..., max_length=400, description="Second text content with a maximum of 40 words.")

class FourTextContentSlideContent(BaseModel):
    heading: str = Field(..., max_length=80, description="Heading with a maximum of 8 words.")
    text_content_1: str = Field(..., max_length=300, description="First text content with a maximum of 30 words.")
    text_content_2: str = Field(..., max_length=300, description="Second text content with a maximum of 30 words.")
    text_content_3: str = Field(..., max_length=300, description="Third text content with a maximum of 30 words.")

class ThankYouSlideContent(BaseModel):
    thank_you_text: str = Field(..., max_length=100, description="Text with a maximum of 10 words.")

# Union of all content types
SlideContent = Union[
    WelcomeSlideContent,
    SimpleContentSlideContent,
    ThreeTextContentSlideContent,
    FourTextContentSlideContent,
    ThankYouSlideContent
]

# Define the structure of a slide
class Slide(BaseModel):
    layout_id: Literal[1, 2, 3, 4, 5] = Field(
        ...,
        description="The layout ID corresponding to the slide type (1-5)."
    )
    content: SlideContent = Field(..., description="Content specific to the chosen layout.")

# Define the LLM response model
class LLMResponse(BaseModel):
    slides: List[Slide] = Field(
        ...,
        description="A list of slides in the presentation."
    )
