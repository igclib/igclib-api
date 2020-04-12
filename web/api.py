from subprocess import check_output, CalledProcessError
import os
from tempfile import NamedTemporaryFile
import json
from flask import Flask, jsonify, redirect, request, send_file

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.config["JSON_AS_ASCII"] = False
app.config["DEBUG"] = False

IGCLIB_BIN = f'{os.environ["HOME"]}/igclib/build/src/igclib'
HSPOINTS_BIN = f'{os.environ["HOME"]}/usr/local/bin/xc_optimizer'


@app.route("/")
@app.route("/api")
def index():
    return send_file("static/index.html")


@app.route("/api/xc", methods=["GET", "POST"])
def xc():
    if request.method == "GET":
        return send_file("static/airspace_validation.html")

    if "flight" not in request.files:
        return redirect(request.url)

    flight = request.files["flight"]
    tf_flight = NamedTemporaryFile(suffix=flight.filename)
    flight.save(tf_flight.name)

    tf_airspace = None
    if "airspace" not in request.files or not request.files["airspace"].filename:
        airspace_name = os.environ.get("DEFAULT_AIRSPACE", "")
    else:
        tf_airspace = NamedTemporaryFile()
        airspace = request.files["airspace"]
        airspace.save(tf_airspace.name)
        airspace_name = tf_airspace.name

    try:
        airspace_result = check_output(
            [IGCLIB_BIN, "xc", "--flight", tf_flight.name, "--airspace", airspace_name,]
        )
        airspace_result = json.loads(airspace_result)

        xc_result = check_output([HSPOINTS_BIN, tf_flight.name, "-", "XC",])
        xc_result = json.loads(xc_result)

        airspace_result["xc_info"] = xc_result
        return jsonify(airspace_result)
    except CalledProcessError:
        return jsonify({"error": "bad igc file"})
    finally:
        tf_flight.close()
        if tf_airspace is not None:
            tf_airspace.close()


if __name__ == "__main__":
    app.run()
