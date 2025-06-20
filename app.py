import streamlit as st
import json
import os
from main import TechBlogGenerator
from config import API_KEY

st.set_page_config(page_title="AI Tech Blog Generator", layout="wide")
st.title("🤖 AI Tech Blog Generator")

default_prompt = (
    "Write a tech blog explaining BERT model in simple terms. "
    "Give me:\n"
    "1. Trending Instagram hashtags\n"
    "2. Medium-worthy full blog\n"
    "3. Instagram caption (2–3 witty lines)\n"
    "4. 3-5 short Canva infographic texts.\n"
    "Separate each section with '==='"
)

user_prompt = st.text_area("✍️ Enter your blog prompt:", value=default_prompt, height=200)

if st.button("🚀 Generate"):
    with st.spinner("Generating..."):
        generator = TechBlogGenerator(API_KEY)
        json_filename = "blog_output.json"
        generator.generate_tech_blog(user_prompt, save_to_json=True, filename=json_filename)

        # Check if JSON file exists
        if os.path.exists(json_filename):
            with open(json_filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Combine everything into one formatted text
            combined_output = f"""📘 **Full Blog**:
{data.get("full_blog", "")}

📱 **Instagram Caption**:
{data.get("instagram_caption", "")}

🏷 **Hashtags**:
{" ".join(data.get("hashtags", []))}

📊 **Canva Infographic Texts**:
{"\n".join(f"- {text}" for text in data.get("canva_texts", []))}
"""

            st.subheader("📝 Complete Blog Output")
            st.text_area("Blog Content", value=combined_output, height=600)

        else:
            st.error("❌ Failed to load blog output JSON file.")
