from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def generate_partitions(n, max_part=None):
    if max_part is None or max_part > n:
        max_part = n
    if n == 0:
        yield []
    else:
        for first in range(max_part, 0, -1):
            for rest in generate_partitions(n-first, first):
                yield [first] + rest

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/partitions", methods=["GET"])
def api_partitions():
    try:
        n = int(request.args.get("n", ""))
        if n < 0:
            raise ValueError
    except ValueError:
        return jsonify({"error": "n must be a non-negative integer"}), 400

    parts = ["+".join(map(str, p)) for p in generate_partitions(n)]
    return jsonify({
        "n": n,
        "count": len(parts),
        "partitions": parts
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)