import os
import connectToGcloud as gcp
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    first5 = gcp.getData()
    print(first5)
    return "Hello {}! Just Making sure it is working twice".format(first5)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

