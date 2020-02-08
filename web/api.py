from tempfile import NamedTemporaryFile
from os import environ

from flask import Flask, jsonify, request, send_file, redirect
from igclib.core.xc import XC

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
@app.route('/api')
def index():
    return send_file('static/index.html')


@app.route('/api/xc', methods=['GET', 'POST'])
def xc():
    if request.method == 'GET':
        return send_file('static/airspace_validation.html')

    if 'flight' not in request.files:
        return redirect(request.url)

    flight = request.files['flight']
    tf_flight = NamedTemporaryFile(suffix=flight.filename)
    flight.save(tf_flight.name)

    tf_airspace = None
    if 'airspace' not in request.files:
        if 'AIRSPACE_FILE' not in environ:
            airspace = None
        else:
            airspace = environ['AIRSPACE_FILE']
    else:
        tf_airspace = NamedTemporaryFile()
        airspace = request.files['airspace']
        airspace.save(tf_airspace.name)

    try:
        airspace = tf_airspace.name if tf_airspace is not None else airspace
        xc = XC(tracks=tf_flight.name, airspace=airspace, progress='silent')
        return jsonify(xc.serialize())
    except ValueError:
        return jsonify({'error': 'bad igc file'})
    finally:
        tf_flight.close()
        if tf_airspace is not None:
            tf_airspace.close()


if __name__ == '__main__':
    app.run(debug=False)
