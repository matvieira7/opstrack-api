from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "OpsTrack API",
        "status": "online"
    })

#teste do diff
if __name__ == "__main__":
    app.run(debug=True)