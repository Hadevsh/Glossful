import requests
import wikitextparser as wtp
import datetime, calendar

def get_wiktionary_data(word, language='English'):
    url = f"https://en.wiktionary.org/w/index.php?title={word}&action=raw"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": f"Failed to fetch data for '{word}'"}

    parsed = wtp.parse(response.text)
    sections = parsed.sections

    for section in sections:
        if section.title and language in section.title:
            result = {}

            # Sarching for sections (which can be at level 3 or 4)
            pos_sections = section.get_sections(level=3) + section.get_sections(level=4)

            # Searching for the Pronunciation section
            pronunciation = "Not found"
            for subsec in pos_sections:
                if "Pronunciation" in (subsec.title or ""):
                    lines = subsec.string.splitlines()
                    for line in lines:
                        if line.startswith("*") and '/' in line:
                            pronunciation = line.strip()
                            break
            result['pronunciation'] = pronunciation

            # Searching for type, definition and examples sections
            for pos_sec in pos_sections:
                pos_title = pos_sec.title or ""
                if pos_title.lower() in ["noun", "verb", "adjective", "adverb", "pronoun", "conjunction"]:
                    result['type'] = pos_title.strip()

                    # Definition
                    definitions = pos_sec.get_lists()
                    if definitions:
                        result['definition'] = definitions[0].items[0].strip()
                    else:
                        result['definition'] = "Not found"

                    # Example sentence
                    example_lines = [line for line in pos_sec.string.splitlines() if line.strip().startswith("#*")]
                    if example_lines:
                        result['example_sentence'] = example_lines[0].replace("#*", "").strip()
                    else:
                        result['example_sentence'] = "Not found"

                    return result

    return {"error": f"No {language} section found for '{word}'"}

def get_random_word(language='en'):
    url = f"https://{language}.wiktionary.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnnamespace": 0,  # Namespace 0 contains main content (words)
        "rnlimit": 1
    }
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        return {"error": f"Failed to fetch a random word from {language} Wiktionary"}
    
    data = response.json()
    random_entries = data.get("query", {}).get("random", [])
    
    if random_entries:
        return random_entries[0].get("title", "No title found")
    else:
        return {"error": "No random word found in the response"}
    
def get_day_word():
    # Returns a dictionary with an English word and a foreign language word of the day
    date = datetime.datetime.now()
    year = date.year
    month = calendar.month_name[date.month]
    day = date.day

    url = f"https://en.wiktionary.org/wiki/Wiktionary:Word_of_the_day/{year}/{month}_{day}?&action=raw"
    print(url)

get_day_word()