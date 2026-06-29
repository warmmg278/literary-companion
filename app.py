from flask import Flask, render_template, request, jsonify

import asyncio

from ai_agents import (
    run_image_agent,
    run_feedback_agent
)


app = Flask(__name__)


@app.route("/")
def home():

    return render_template(
        "index.html",
        image_result="",
        feedback_result=""
    )

@app.route("/image", methods=["POST"])
def image():

    emotion = request.form["emotion"]

    scene = request.form["scene"]

    print(emotion)

    print(scene)

    result = asyncio.run(
        run_image_agent(
            emotion,
            scene
        )
    )

    return jsonify({"result": result})


@app.route("/feedback", methods=["POST"])
def feedback():

    writing = request.form["writing"]

    result = asyncio.run(
        run_feedback_agent(
            writing
        )
    )

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)