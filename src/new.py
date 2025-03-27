import win32com.client
import os

# Open PowerPoint application
ppt_app = win32com.client.Dispatch("PowerPoint.Application")

# Open the source presentation
source_ppt = ppt_app.Presentations.Open(os.path.abspath("D:/Harshit/Ibind Systems/PPT generation/trial1.pptx"), True,False, False)  # Replace with your source file path

# Create a new presentation
new_ppt = ppt_app.Presentations.Add()

# Specify slide numbers to copy (e.g., 1, 2, 4 from the source)
slides_to_copy = [1,2,3,4,5,6,7,8,9,10]

# Copy specified slides to the new presentation
for slide_number in slides_to_copy:
    slide = source_ppt.Slides(slide_number)
    slide.Copy()  # Copy the slide to the clipboard
    new_ppt.Slides.Paste()  # Paste the slide into the new presentation

# Save the new presentation
new_ppt.SaveAs(os.path.abspath("D:/Harshit/Ibind Systems/PPT generation/trial_modified_again.pptx"))  # Replace with your desired file path

# Close presentations and quit PowerPoint
source_ppt.Close()
new_ppt.Close()
ppt_app.Quit()
