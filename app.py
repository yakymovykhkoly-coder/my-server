from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api")
def api():
    return jsonify({"message": "Привіт! Це відповідь з Python 🚀"})

if __name__ == "__main__":
    app.run(debug=True)
