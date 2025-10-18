import datetime
import re


README_PATH = ".../README.md"

def GenerateAJoke():
    # generate a joke automatically using ai
    # THIS IS WHERE YOU PUT THE AI CODE
    print("HELLO WORLD !")
    return ("famous artist")


def Update_dynamic_section():
    """ Generates a dynamic text for the README file.  """
    
    startMarker = "<!--START_DYNAMIC-->"
    endMarker = "<!--END_DYNAMIC-->"
    current_time = datetime.datetime.now().strftime(f"%d-%m-%Y %H:%M:%S") 

    jokeOfTheDay = GenerateAJoke()
    
   
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    dynamic_content = f"{startMarker}\n{GenerateAJoke()}\n{endMarker}"

    if re.search(f"{startMarker}[\\s\\S]*{endMarker}", readme):
        readme = re.sub(f"{startMarker}[\\s\\S]*{endMarker}", dynamic_content, readme)
    else:
        readme += f"\n\n{dynamic_content}"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme)

    print("✅ README updated successfully!")

    return (
        f"_{jokeOfTheDay}_\n"
        f"### ✨ Auto-updated Info\n"
        f"🕒 Updated on: **{current_time}**  \n"
    )


if __name__ == "__main__":
    Update_dynamic_section()
