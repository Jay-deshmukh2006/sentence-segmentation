from flask import Flask, render_template, request
import nltk
from nltk.tokenize import sent_tokenize

# Download required NLTK data
nltk.download("punkt_tab")

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    sentences = []
    text = ""
    word_count = 0
    character_count = 0

    if request.method == "POST":

        text = request.form.get("text", "")

        if text.strip():

            # Sentence Segmentation
            sentences = sent_tokenize(text)

            # Word Count
            word_count = len(text.split())

            # Character Count
            character_count = len(text)

    return render_template(
        "index.html",
        sentences=sentences,
        text=text,
        word_count=word_count,
        character_count=character_count
    )


if __name__ == "__main__":
    app.run(debug=True)