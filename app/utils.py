import requests
import wikitextparser as wtp

def get_wiktionary_data(word, language='English'):
    url = f"https://en.wiktionary.org/w/index.php?title={word}&action=raw"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Failed to fetch data for '{word}'"

    parsed = wtp.parse(response.text)
    sections = parsed.sections

    for section in sections:
        if section.title and language in section.title:
            result = {}

            # Szukanie sekcji Pronunciation
            pronunciation = "Not found"
            for subsec in section.get_sections(level=3):
                if "Pronunciation" in (subsec.title or ""):
                    lines = subsec.string.splitlines()
                    for line in lines:
                        if line.startswith("*") and '/' in line:
                            pronunciation = line.strip()
                            break

            result['pronunciation'] = pronunciation

            # Szukanie typu słowa (np. Verb, Noun)
            pos_sections = section.get_sections(level=3)
            for pos_sec in pos_sections:
                pos_title = pos_sec.title or ""
                if pos_title.lower() in ["noun", "verb", "adjective", "adverb", "pronoun", "conjunction"]:
                    result['type'] = pos_title.strip()

                    # Definicja
                    definitions = pos_sec.get_lists()
                    if definitions:
                        result['definition'] = definitions[0].items[0].strip()
                    else:
                        result['definition'] = "Not found"

                    # Przykładowe zdanie
                    example_lines = [line for line in pos_sec.string.splitlines() if line.strip().startswith("#*")]
                    if example_lines:
                        result['example_sentence'] = example_lines[0].replace("#*", "").strip()
                    else:
                        result['example_sentence'] = "Not found"

                    return result

    return f"No {language} section found for '{word}'"