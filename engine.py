import requests
from config import API_URL, HEADERS
from system import SystemInstruction
from structure import BlogResponse, StructuredBlogOutput

class OpenRouterAPI:
    def __init__(self, api_key, temperature=0.8):
        self.api_key = api_key
        self.headers = HEADERS
        self.api_url = API_URL
        self.temperature = temperature

    def generate_blog(self, user_prompt):
        system_instruction = SystemInstruction()
        data = system_instruction.get_data_payload(user_prompt)

        try:
            response = requests.post(self.api_url, json=data, headers=self.headers)

            if response.status_code == 200:
                raw = response.json()
                blog_response = self.clean_response(raw)

                return self.structure_output(blog_response)

            else:
                print(f"Failed to fetch data from API. Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

    def clean_response(self, response_json) -> BlogResponse:
        try:
            content = response_json['choices'][0]['message']['content'].strip()
            return BlogResponse(
                model=response_json['model'],
                generated_text=content,
                usage=response_json['usage']
            )
        except KeyError as e:
            raise ValueError(f"Missing key in response: {e}")

    def structure_output(self, blog_response: BlogResponse) -> StructuredBlogOutput:
        # Dummy parsing logic – replace with smarter extraction later
        content = blog_response.generated_text

        # Simulated delimiter format (use real ones based on how your model responds)
        sections = content.split("===")

        return StructuredBlogOutput(
            hashtags=[tag.strip() for tag in sections[0].split(",") if tag.strip()],
            full_blog=sections[1].strip(),
            instagram_caption=sections[2].strip(),
            canva_texts=[line.strip() for line in sections[3].split("\n") if line.strip()]
        )
