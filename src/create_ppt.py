import time
import win32com.client
import os
from .modify_ppt import modify_ppt

def generate_ppt_from_template(dest_ppt_content, template_path="template.pptx", output_path="result.pptx"):
    """
    Generates a PowerPoint presentation based on the provided content and a template.

    Args:
        dest_ppt_content (dict): The content dictionary containing slide data and layout IDs.
        template_path (str): Path to the PowerPoint template file.
        output_path (str): Path to save the generated PowerPoint file.

    Returns:
        None
    """
    # Define a mapping of custom keys to slide numbers
    slide_key_mapping = {
        1: 1,   # Slide 1 saved as key 1
        2: 2,   # Slide 2 saved as key 2
        3: 3,   # Slide 3 saved as key 3
        4: 5,   # Slide 5 saved as key 4
        5: 10   # Slide 10 saved as key 5
    }

    # Extract slide numbers based on the provided layout IDs
    slides_list = []
    for slide in dest_ppt_content['slides']:
        slides_list.append(slide_key_mapping[slide['layout_id']])

    # Open PowerPoint application
    ppt_app = win32com.client.Dispatch("PowerPoint.Application")

    try:
        # Open the source presentation
        source_ppt = ppt_app.Presentations.Open(os.path.abspath(template_path), True, False, False)

        # Create a new presentation
        new_ppt = ppt_app.Presentations.Add()

        # Copy specified slides to the new presentation
        for slide_number in slides_list:
            slide = source_ppt.Slides(slide_number)
            slide.Copy()  # Copy the slide to the clipboard
            time.sleep(3)
            new_ppt.Slides.Paste()  # Paste the slide into the new presentation

        # Save the new presentation
        new_ppt.SaveAs(os.path.abspath(output_path))

        # Modify the presentation content using the `modify_ppt` function
        modify_ppt(dest_ppt_content, output_path)

    finally:
        # Close presentations and quit PowerPoint
        source_ppt.Close()
        new_ppt.Close()
        ppt_app.Quit()
