from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "AI Video Clipper API is running"}

@app.route("/clip", methods=["POST"])
def clip_video():
    data = request.json
    video_url = data.get("video_url")

    # Placeholder (later we add AI)
    return jsonify({
        "status": "processing",
        "message": f"Your video {video_url} will be clipped soon!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
