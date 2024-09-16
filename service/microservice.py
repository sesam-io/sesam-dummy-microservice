from flask import Flask, request, Response
from logger import Logger
from json import dumps


app = Flask(__name__)
logger = Logger("url-post-rest-service")


@app.route("/dms", methods=["POST"])
def sesam_data():
    data = request.json[0]
    data["from_microservice"] = True

    return Response(dumps(data))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
