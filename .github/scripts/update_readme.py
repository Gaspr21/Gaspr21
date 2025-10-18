import datetime
import os
import re
import openai

README_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../README.md"))

def fetch_ai_joke() -> str:
    """Fetch a random programmer joke using OpenAI API (v1.0+)."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        # In case these is no api key
        jokes = [
            "Why did the programmer quit his job? Because he didn't get arrays.",
            "Why do Java developers wear glasses? Because they don't C#.",
            "I would tell you a UDP joke, but you might not get it.",
            "Why did the function return early? Because it had too many arguments!"
        ]
        return random.choice(jokes)

    openai.api_key = api_key

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
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
    return f"_{joke}_ \n  ✨ Auto-updated Info\n🕒 Updated on: **{current_time}**  \n💬 Come tomorrow for a new one ☝️"

def update_readme():
    """Updates the README file with the new dynamic section."""
    start_marker = "<!--START_DYNAMIC-->"
    end_marker = "<!--END_DYNAMIC-->"

    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    dynamic_content = f"{start_marker}\n{generate_dynamic_section()}\n{end_marker}"

    if re.search(f"{start_marker}[\\s\\S]*{end_marker}", readme):
        readme = re.sub(f"{start_marker}[\\s\\S]*{end_marker}", dynamic_content, readme)
    else:
        readme += f"\n\n{dynamic_content}"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme)

if __name__ == "__main__":
    import random
    update_readme()
