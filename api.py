from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from curl_cffi import requests as curl_requests
import re
import json

app = Flask(__name__)
CORS(app)

BASE_URLS = {
    "fr": "https://www.lacentrale.fr/le-rachat-express/mon-rendez-vous/description-voiture",
}

@app.route("/car/<country>", methods=["GET"])
def car(country):
    if country not in BASE_URLS:
        return jsonify({"success": False, "error": "Unsupported country"}), 400
    
    plate = request.args.get("plate")
    if not plate:
        return jsonify({"success": False, "error": "Missing 'plate' parameter"}), 400
    
    url = f"{BASE_URLS[country]}?registration={plate}"
    try:
        response = curl_requests.get(url, impersonate="chrome")
        response.raise_for_status()
        
        match = re.search(r'var FunnelProps = (\{.*?\});', response.text)
        if match:
            funnel_data = json.loads(match.group(1))
            vehicle_data = funnel_data.get("matching", {}).get("vehicle", {})
            return jsonify({"success": True, "data": vehicle_data})
        
        return jsonify({"success": False, "error": "Vehicle data not found"}), 404
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
