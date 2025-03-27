
from typing import List
import re

class TextProcessor:
    def __init__(self, max_chars_per_slide: int = 500):
        """
        Initialize the text processor with configurable limits.
        
        Args:
            max_chars_per_slide: Maximum number of characters per slide
        """
        self.max_chars_per_slide = max_chars_per_slide

    def split_into_chunks(self, text: str) -> List[str]:
        """
        Split text into chunks that will fit on individual slides.
        
        Args:
            text: The input text to split
            
        Returns:
            List of text chunks, each appropriate for a single slide
        """
        # First split by paragraphs
        paragraphs = text.split('\n')
        chunks = []
        current_chunk = []
        current_length = 0
        
        for paragraph in paragraphs:
            # Skip empty paragraphs
            if not paragraph.strip():
                continue
                
            # If adding this paragraph would exceed the limit
            if current_length + len(paragraph) > self.max_chars_per_slide:
                # If the current chunk has content, save it
                if current_chunk:
                    chunks.append('\n'.join(current_chunk))
                    current_chunk = []
                    current_length = 0
                
                # If the paragraph itself is too long, split it
                if len(paragraph) > self.max_chars_per_slide:
                    # Split into sentences
                    sentences = re.split(r'(?<=[.!?])\s+', paragraph)
                    temp_chunk = []
                    temp_length = 0
                    
                    for sentence in sentences:
                        if temp_length + len(sentence) > self.max_chars_per_slide:
                            if temp_chunk:
                                chunks.append(' '.join(temp_chunk))
                                temp_chunk = []
                                temp_length = 0
                            # If a single sentence is too long, split by words
                            if len(sentence) > self.max_chars_per_slide:
                                words = sentence.split()
                                word_chunk = []
                                word_length = 0
                                for word in words:
                                    if word_length + len(word) + 1 > self.max_chars_per_slide:
                                        chunks.append(' '.join(word_chunk))
                                        word_chunk = [word]
                                        word_length = len(word)
                                    else:
                                        word_chunk.append(word)
                                        word_length += len(word) + 1
                                if word_chunk:
                                    chunks.append(' '.join(word_chunk))
                            else:
                                chunks.append(sentence)
                        else:
                            temp_chunk.append(sentence)
                            temp_length += len(sentence) + 1
                    if temp_chunk:
                        chunks.append(' '.join(temp_chunk))
                else:
                    current_chunk.append(paragraph)
                    current_length = len(paragraph)
            else:
                current_chunk.append(paragraph)
                current_length += len(paragraph) + 1  # +1 for newline
        
        # Add any remaining content
        if current_chunk:
            chunks.append('\n'.join(current_chunk))
            
        return chunks

    def format_chunk_for_slide(self, chunk: str) -> str:
        """
        Format a text chunk for optimal presentation on a slide.
        
        Args:
            chunk: Text chunk to format
            
        Returns:
            Formatted text ready for slide insertion
        """
        # Remove excessive whitespace
        chunk = ' '.join(chunk.split())
        
        # Add bullet points for lines that look like list items
        lines = chunk.split('\n')
        formatted_lines = []
        
        for line in lines:
            # If line starts with a number or bullet-like character
            if re.match(r'^\d+[\.\)]|^[-\*\•]', line.strip()):
                formatted_lines.append('• ' + line.strip())
            else:
                formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)
