import binascii
from tempfile import NamedTemporaryFile
from base64 import b64decode
from io import StringIO
from os import environ

from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_file
from igclib.core.xc import XC

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
load_dotenv('../.env')


@app.route('/')
def index():
    return send_file('static/index.html')


@app.route('/xc', methods=['GET', 'POST'])
def xc():
    if request.method == 'GET':
        return send_file('static/airspace_validation.html')

    if 'flight' not in request.files:
        return redirect(request.url)

    flight = request.files['flight']
    tf_flight = NamedTemporaryFile()
    flight.save(tf_flight)

    tf_airspace = None
    if 'airspace' not in request.files:
        if 'AIRSPACE_FILE' not in environ:
            airspace = None
        else:
            airspace = environ['AIRSPACE_FILE']
    else:
        tf_airspace = NamedTemporaryFile()
        airspace = request.files['airspace']
        airspace.save(tf_airspace)

    try:
        airspace = tf_airspace.name if tf_airspace is not None else airspace
        xc = XC(tracks=tf_flight.name, airspace=airspace, progress='gui')
    except KeyError:
        return jsonify({'error': 'bad igc file'})
    finally:
        tf_flight.close()
        if tf_airspace is not None:
            tf_airspace.close()

        return jsonify(xc.serialize())


if __name__ == '__main__':
    app.run(debug=True)
