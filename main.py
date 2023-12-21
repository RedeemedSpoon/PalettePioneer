from flask import Flask, render_template, request, redirect, flash
from PIL import Image, UnidentifiedImageError
from datetime import datetime
import numpy as np
import io

app = Flask(__name__)
app.secret_key = '5db46df5b1b5n15gs1f56sg1t5665n1f6s2dg5er' # Very insecure and improfessional but idc
@app.route('/')
def index():
      date = datetime.now().year
      return render_template('index.html', year=date)

@app.route('/results', methods=['GET', 'POST'])
def scan():
      if request.method == 'POST':
            try:
                  f = request.files['imageinput']
                  img = Image.open(io.BytesIO(f.read()))
                  img_array = np.array(img)
                  
                  return "Image received and converted to np.array successfully!"
            except UnidentifiedImageError:
                  flash('Error: Please upload a valid image file.')
                  return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)