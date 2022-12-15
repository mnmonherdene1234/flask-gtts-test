from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from gtts import gTTS

app = Flask(__name__)


@app.route("/text-to-voice/<text>", methods=["GET", "POST"])
async def text_to_voice(text: str):
    tts = gTTS(text)
    filename = "voices/" + secure_filename(text + ".mp3")
    tts.save(filename)
    return send_file(filename)
