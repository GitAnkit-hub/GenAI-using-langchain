from flask import Flask, request, jsonify
import Projects.SemanticSimilarityAPI.similarity as similarity
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello, World!<p>"

@app.route('/chat/SemanticSimilarity', methods=['POST'])
# @app.route('/api/CheckSimilarity')
def SemanticSimilarity():
    if not request.is_json:
        return jsonify({
            "status": "error",
            "message": "Request must contain JSON data."
        }), 400

    
    data = request.get_json(silent=True)


    if not isinstance(data, dict):
        return jsonify({
            "status": "error",
            "message": "Invalid JSON request body."
        }), 400

    
    query1 = data.get('input1')
    query2 = data.get('input2')

    # Validate input types
    if not isinstance(query1, str) or not isinstance(query2, str):
        return jsonify({
            "status": "error",
            "message": "Both input1 and input2 must be strings."
        }), 400

    
    # Remove leading and trailing whitespace
    query1 = query1.strip()
    query2 = query2.strip()

    # Check empty inputs
    if not query1 or not query2:
        return jsonify({
            "status": "error",
            "message": "Please provide two non-empty input statements."
        }), 400

    # Check input length
    if len(query1) > 100 or len(query2) > 100:
        return jsonify({
            "status": "error",
            "message": "Each input statement must not exceed 100 characters."
        }), 400

    
    # Calculate semantic similarity
    try:
        response = similarity.SimiarityCheckAPI(query1, query2)

        return jsonify({
            "status": "success",
            "data": response
        }), 200

    except Exception:
        app.logger.exception("Similarity calculation failed")

        return jsonify({
            "status": "error",
            "message": "Unable to calculate similarity at this time."
        }), 500

app.run(debug=True)