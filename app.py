import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        translate = request.form["translate"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """
                    You are a helpful Japanese teacher. You will
                        1. Correct any grammar mistake that I make in my prompt and also give explanation.
                """},
                {"role": "user", "content": generate_prompt(translate)}
            ]
        )
        return redirect(url_for("index", result=response.choices[0].message.content))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(translate):
    return translate
