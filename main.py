from flask import *
import os

from models.image_model import get_image_caption
from models.text_model import get_adapted_captions

app = Flask(__name__)

UPLOAD_FOLDER = 'static/images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def homePage():
    return render_template('home.html')

@app.route('/how')
def how():
    return render_template('how.html')

@app.route('/ourTeam')
def team():
    return render_template('ourTeam.html')

@app.route('/predict', methods=['POST'])
def predict():
    audience = request.form.get('audience')

    tone = request.form.get('tone')
    print("Tone:", tone)

    if not audience:
        return redirect(url_for('home'))

    if 'file' not in request.files:
        return redirect(url_for('home'))
    file = request.files['file']

    if file:
        file.filename = "user_upload.png"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        print(filepath)

        base_description = get_image_caption(filepath)
        description = get_adapted_captions(base_description, tone, audience)[0]

    return render_template('result.html', audience=audience, tone=tone, image_path=filepath, description=description)


if __name__ == '__main__':
    app.run(debug=True)