from flask import Flask, render_template, request, abort, make_response
from PIL import Image, UnidentifiedImageError
from datetime import datetime
import numpy as np
import io

app = Flask(__name__)

@app.route('/')
def index():
      date = datetime.now().year
      return render_template('index.html', year=date)

@app.route('/results', methods=['GET', 'POST'])
def scan():
    if request.method == 'POST':
        try:
            file = request.files['imageinput']
            filename = file.filename
            img = Image.open(io.BytesIO(file.read()))
            image = np.array(img)
            
            flattened_img_array = image.reshape(-1, 3)
            unique_colors, counts = np.unique(flattened_img_array, axis=0, return_counts=True)
            sorted_indices = np.argsort(counts)[::-1]
            sorted_colors = unique_colors[sorted_indices]
            top_colors = sorted_colors[:10]
            
            response = make_response(render_template("results.html", colors=top_colors))
            response.headers['Content-Type'] = 'text/html'
            return response
      
        except UnidentifiedImageError:
            return abort(415)
        
if __name__ == '__main__':
    app.run()