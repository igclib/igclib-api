import binascii
from tempfile import NamedTemporaryFile
from base64 import b64decode
from io import StringIO
from os import environ

from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_file
from igclib.core.xc import XC

app = Flask(__name__)
load_dotenv('../.env')


@app.route('/')
def index():
    return send_file('static/index.html')


@app.route('/xc')
def flight():
    airspace = request.args.get('airspace')
    if airspace is None:
        if 'EA_FILE' not in environ:
            return jsonify({'error': 'no airspace file available'})
        airspace = environ.get('EA_FILE')
    print(f'AIRSPACE = {airspace}')

    flight = request.args.get('flight')
    if flight is None:
        return jsonify({'error': 'missing flight argument'})
    try:
        flight = b64decode(flight, validate=True)
    except binascii.Error:
        return jsonify({'error': 'bad base64 encoding'})

    with NamedTemporaryFile() as tf:
        tf.write(flight)
        try:
            xc = XC(tracks=tf.name, airspace=airspace, progress='gui')
        except KeyError:
            return jsonify({'error': 'bad igc file'})
    return jsonify(xc.serialize())


if __name__ == '__main__':
    app.run()
