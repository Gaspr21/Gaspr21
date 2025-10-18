import datetime
import os
import re
import openai

README_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../README.md"))

def fetch_ai_joke() -> str:
    """Fetch a random joke from OpenAI."""
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a witty joke-telling assistant."},
            {"role": "user", "content": "Tell me a short, funny programmer joke."}
        ],
        max_tokens=50
    )
    joke = response.choices[0].message.content.strip()
    return joke

def generate_dynamic_section() -> str:
    """Generate the dynamic section with current time and joke."""
    current_time = datetime.datetime.now().strftime(f"%d-%m-%Y %H:%M:%S") 
    joke = fetch_ai_joke()
    return f"###Joke of the day: _{joke}_\n  ✨ Auto-updated Info\n🕒 Updated on: **{current_time}**  \n💬 Come tomorrow for a new one ☝️"

def update_readme():
    start_marker = "<!--START_DYNAMIC-->"
    end_marker = "<!--END_DYNAMIC-->"

    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    dynamic_content = f"{start_marker}\n{generate_dynamic_section()}\n{end_marker}"

    if re.search(f"{start_marker}[\\s\\S]*{end_marker}", readmefile):
        readmefile = re.sub(f"{start_marker}[\\s\\S]*{end_marker}", dynamic_content, readmefile)
    else:
        readmefile += f"\n\n{dynamic_content}"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readmefile)

if __name__ == "__main__":
    update_readme()
