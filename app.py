from flask import Flask, json, Response, request, jsonify
import os

app = Flask(__name__)


@app.route("/checkStatus", methods=["GET"])
def getPartnerDetail():

    resp = {"status": "OK"}
    return app.response_class(
        response=json.dumps(resp), status=200, mimetype="application/json"
    )




if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0") 
