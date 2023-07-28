from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS, cross_origin
import readCSVChatGPT
import readCSVLev
import os

app = Flask(__name__, static_folder="static")
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/uploadGPT", methods=["POST"])
def uploadDoc():
    csvFile = request.files['file']

    # create output.csv
    readCSVChatGPT.detectDuplicates(csvFile.read())
    #Do     readCSVLev.detectDuplicates(csvFile.read()) when requested
    uploads = os.path.join(app.root_path, "output")
    return send_from_directory(uploads, "output.csv")

   
@app.route("/uploadLev", methods=["POST"])
def uploadLev():
    csvFile = request.files['file']

    # create output.csv
    # readCSVChatGPT.detectDuplicates(csvFile.read())
    readCSVLev.detectDuplicatesLev(csvFile.read())
    uploads = os.path.join(app.root_path, "output")
    return send_from_directory(uploads, "output.csv")



app.run(debug=True, port=3500, host="0.0.0.0")