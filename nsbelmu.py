"""
NSBELMU AI.
"""
import google.generativeai as genai
import webbrowser
from apikeys import GEMINI_API_KEY
from constants import MESSAGES

genai.configure(api_key=GEMINI_API_KEY)

class NSBEAI:
    def __init__(self):
        safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        ]
        self.model = genai.GenerativeModel(
            model_name="gemini-pro",
            safety_settings=safety_settings
        )

    def generate_newsletter(self, meeting, date):
        """
        Generate a newsletter for LMU NSBE announcing the next chapter meeting.

        Args:
        - meeting: The type of the next chapter meeting.
        - date: The date of the next chapter meeting.

        Returns:
        - response: The generated newsletter.
        """
        prompt = "generate a newsletter for lmu nsbe announcing the next chapter meeting. try to be in a similar format to your previous responses."
        messages = MESSAGES
        messages.append({
            'role': 'user',
            'parts': [prompt,
                      "next meeting: " + meeting,
                      "date: " + date]
        })
        response = self.model.generate_content(messages)
        text = response.text
        mailto = f'mailto:?subject=🦁 NSBE Newsletter - {date}&body={text}'
        webbrowser.open(mailto)
        return text