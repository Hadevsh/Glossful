from app import create_app
from app.utils import get_wiktionary_data

app = create_app()

if __name__ == "__main__":
    word_data = get_wiktionary_data("bear")
    print(word_data)

    app.run(debug=True)