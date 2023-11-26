from flask import Flask, request, jsonify
from flask_cors import CORS
from colorthief import ColorThief
import io

app = Flask(__name__)
CORS(app)

@app.route('/get-colors', methods=['POST'])
def get_colors():
    if 'image' in request.files:
        image = request.files['image']
        color_thief = ColorThief(io.BytesIO(image.read()))
        palette = color_thief.get_palette(color_count=6)
        return jsonify(palette)
    return 'No image provided', 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')