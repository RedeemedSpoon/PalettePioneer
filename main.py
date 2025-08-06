from flask import Flask, render_template, request, abort, make_response
from PIL import Image, UnidentifiedImageError
from sklearn.cluster import MiniBatchKMeans
from datetime import datetime
import numpy as np
import io, base64

app = Flask(__name__)
date = datetime.now().year


@app.route("/")
def index():
    return render_template("index.html", year=date)


@app.route("/results", methods=["GET", "POST"])
def scan():
    if request.method == "POST":
        try:
            file = request.files["imageinput"]
            filename = file.filename
            img = Image.open(io.BytesIO(file.read()))

            image = np.array(img)
            resolution = f"{image.shape[0]}x{image.shape[1]}"

            if image.shape[2] == 4:
                image = image[:, :, :3]

            pixels = image.reshape(-1, 3)
            num_clusters = 10
            sample_size = 100000

            replace = pixels.shape[0] < sample_size
            sample = pixels[np.random.choice(pixels.shape[0], sample_size, replace=replace)]

            kmeans = MiniBatchKMeans(n_clusters=num_clusters, random_state=42).fit(sample)
            cluster_centers_int = kmeans.cluster_centers_.astype(int)

            colors = [
                "#" + "".join(format(c, "02x") for c in color)
                for color in cluster_centers_int
            ]
            
            buffer = io.BytesIO()
            Image.fromarray(image.astype("uint8")).save(buffer, format="PNG")
            img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")

            response = make_response(
                render_template(
                    "results.html",
                    colors=colors,
                    filename=filename,
                    resolution=resolution,
                    image=img_str,
                    year=date,
                )
            )
            response.headers["Content-Type"] = "text/html"
            return response

        except UnidentifiedImageError:
            return abort(415)


if __name__ == "__main__":
    app.run()
