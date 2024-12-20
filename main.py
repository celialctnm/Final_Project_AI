from flask import *
import os

from models.image_model import get_image_caption
from models.text_model import get_adapted_captions

# convention à respecter
# images, css, tout mettre dans le répertoire static sinon ça marche pas
# page HTML dans le réperoire templates

# modèle à implémenter

# faire lien API ChatGPT

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
        # TODO: adapter si on veut afficher toutes les options des descriptions générées (il faut adapter le result.html pour prendre une liste de string)
        description = get_adapted_captions(base_description, "funny", audience)[0]

    return render_template('result.html', audience=audience, image_path=filepath, description=description)


if __name__ == '__main__':
    # changer à False le debug lorsque le code sera fini
    app.run(debug=True)