# from flask import Flask, jsonify, request
# from utils.github_client import fetch_repo_data, fetch_pull_requests

# app = Flask(__name__)

# @app.route('/health', methods=['GET'])
# def health_check():
#     return jsonify(status='ok'), 200

# @app.route('/repos/<owner>/<repo>', methods=['GET'])
# def get_repo(owner, repo):
#     try:
#         data = fetch_repo_data(owner, repo)
#         return jsonify(data), 200
#     except Exception as e:
#         return jsonify(error=str(e)), 503

# @app.route('/repos/<owner>/<repo>/pulls', methods=['GET'])
# def get_pull_requests(owner, repo):
#     try:
#         pulls = fetch_pull_requests(owner, repo)
#         return jsonify(pulls), 200
#     except Exception as e:
#         return jsonify(error=str(e)), 503

# @app.route('/repos/<owner>/<repo>/webhooks', methods=['POST'])
# def create_webhook(owner, repo):
#     # Simulate webhook creation
#     payload = request.json
#     return jsonify(message="Webhook creation simulated.", payload=payload), 201

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status='ok'), 200

@app.route('/repo/<string:repo_id>', methods=['GET'])
def get_repo(repo_id):
    # Simulated call to GitHub API - replace with real logic
    try:
        data = {"id": repo_id, "name": "Example Repo"}
        return jsonify(data), 200
    except Exception:
        return jsonify(error="Failed to fetch repo data"), 503

if __name__ == '__main__':
    app.run(debug=True)
