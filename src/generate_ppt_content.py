from groq import Groq
import instructor
from .schema import LLMResponse

client = Groq(api_key='you_api_key_here')

client = instructor.from_groq(client)

system_prompt = """You are an assistant that designs PowerPoint presentations based on the provided research text. The presentation must adhere to the following layouts and their content restrictions:

Layouts:
Welcome Slide (Layout ID: 1)
Fields:
Title 
Subtitle

Simple Content Slide (Layout ID: 2)
Fields:
Heading 
Text Content 

Three-Text Content Slide (Layout ID: 3)
Fields:
Heading 
Text Content 1 
Text Content 2 

Four-Text Content Slide (Layout ID: 4)
Fields:
Heading 
Text Content 1 
Text Content 2 
Text Content 3

Thank You Slide (Layout ID: 5)
Fields:
Thank You Text

Guidelines:
Analyze the provided text and divide the content into logical slides.
Choose an appropriate layout for each slide based on the content's structure and length.
Fields should be filled with relevant information from the text and all field in a layout should be used. Otherwise choose a different layout.
Ensure no field exceeds the specified content limits like title and headings should be less than 4 words and text content should be less than 40 words.
Make sure to create a very very detailed and informative presentation that covers all key points. I want each section to be explained in detail.
Number of slides should be atleast 10. It is a very serious requirement and should be followed strictly.

Adhere to the above guidelines at any cost to create a comprehensive and informative presentation.
"""


def generate_content(content : str):
    response = client.chat.completions.create(
        model = "mixtral-8x7b-32768",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"The research is {content}"}
        ],
        response_model= LLMResponse
    )
    return response
