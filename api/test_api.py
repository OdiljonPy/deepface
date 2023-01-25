from flask import Flask, jsonify, request, make_response
from deepface.DeepFace import verify
import argparse
import time

app = Flask(__name__)


@app.route('/verify', methods=['POST', 'GET'])
def demo():
    files = request.files
    data = request.form
    print(data)
    if request.method == 'GET':
        return 'ok'
    model_name = data.get('model')
    if model_name is None:
        model_name = "Facenet512"
    metric = data.get('metric')
    if metric is None:
        metric = "euclidean_l2"
    img1_name = f"img1-{time.time()}"
    img2_name = f"img2-{time.time()}"
    result = verify(files['img1'], files['img2'], model_name=model_name, distance_metric=metric)
    return jsonify(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--port',
        type=int,
        default=5000,
        help='Port of serving api')
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port, debug=True)
