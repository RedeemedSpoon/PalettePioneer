from flask import Flask, render_template, request, abort, make_response
from PIL import Image, UnidentifiedImageError
from sklearn.cluster import KMeans
from datetime import datetime
import numpy as np
import io, base64

app = Flask(__name__)

@app.route('/')
def index():
    # Get the current year
    date = datetime.now().year
    return render_template('index.html', year=date)

@app.route('/results', methods=['GET', 'POST'])
def scan():
    if request.method == 'POST':
        try:
            file = request.files['imageinput']
            img = Image.open(io.BytesIO(file.read()))
            image = np.array(img)
            filename = file.filename
            resolution = f"{image.shape[0]}x{image.shape[1]}"
        
            flattened_img_array = image.reshape(-1, 3)
            unique_colors, counts = np.unique(flattened_img_array, axis=0, return_counts=True)

            num_clusters = min(10, len(unique_colors)) 
            kmeans = KMeans(n_clusters=num_clusters, random_state=42).fit(unique_colors)
            cluster_centers = kmeans.cluster_centers_
            cluster_centers_int = cluster_centers.astype(int)
            colors = ['#' + ''.join(format(c, '02x') for c in color) for color in cluster_centers_int]
            
            buffer = io.BytesIO()
            Image.fromarray(image.astype('uint8')).save(buffer, format="PNG")
            img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
            response = make_response(render_template("results.html", colors=colors, filename=filename, resolution=resolution, image=img_str))
            response.headers['Content-Type'] = 'text/html'
            return response
      
        except UnidentifiedImageError:
            return abort(415)

if __name__ == '__main__':
    app.run(debug=True)