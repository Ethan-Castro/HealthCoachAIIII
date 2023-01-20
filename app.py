import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


response = openai.Completion.create(
  model="text-davinci-003",
  prompt="",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
      
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Q: What is a schedule for me\nA: Wakeup at a reasonable time for your circadian rhythm, which usually falls in line with sunrise.\nGo to work and stuff\nGo home and sleep boy",",
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
)
      
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


