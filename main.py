import json
from engine import OpenRouterAPI
from config import API_KEY
from structure import StructuredBlogOutput

class TechBlogGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_client = OpenRouterAPI(self.api_key)

    def generate_tech_blog(self, prompt, save_to_json=False, filename="blog_output.json"):
        response: StructuredBlogOutput = self.api_client.generate_blog(prompt)

        # Optional: keep printing to terminal if you want
        print("\n📘 Full Blog:\n", response.full_blog)
        print("\n📱 Instagram Caption:\n", response.instagram_caption)
        print("\n🏷 Hashtags:\n", ", ".join(response.hashtags))
        print("\n📊 Canva Infographic Texts:\n", "\n".join(response.canva_texts))

        # ✅ Save to JSON file
        if save_to_json:
            blog_data = {
                "full_blog": response.full_blog,
                "instagram_caption": response.instagram_caption,
                "hashtags": response.hashtags,
                "canva_texts": response.canva_texts,
            }
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(blog_data, f, ensure_ascii=False, indent=2)
            print(f"\n💾 Blog saved as JSON in '{filename}'")

        return response  # ✅ This is necessary for Streamlit to use it

# Optional CLI test (does not affect Streamlit)
if __name__ == "__main__":
    tech_blog_generator = TechBlogGenerator(API_KEY)
    user_prompt = (
        "Write a tech blog explaining Train, Validation, Test: The Cousins You Can’t Mix in machine learning , AI and etc"
        "Give me:\n"
        "1. Trending Instagram hashtags\n"
        "2. Medium-worthy full blog\n"
        "3. Instagram caption (2–3 witty lines)\n"
        "4. 3-5 short Canva infographic texts.\n"
        "Separate each section with '==='"
    )
    tech_blog_generator.generate_tech_blog(user_prompt, save_to_json=True)
