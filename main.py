from flask import *
import os

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


def create_model():
    model = "model"
    return model


@app.route('/predict', methods=['POST'])
def predict():
    audience = request.form.get('famille') or request.form.get('amis') or request.form.get('collegues')
    if not audience:
        return redirect(url_for('index'))

    if 'file' not in request.files:
        return redirect(url_for('index'))
    file = request.files['file']

    if file:
        file.filename = "user_upload.png"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # mise en place du model
        model = create_model()
        print("Model")

        description = "Generated description by model"
        print(filepath)
    return render_template('result.html', audience=audience, image_path=filepath, description=description)


if __name__ == '__main__':
    # changer à False le debug lorsque le code sera fini
    app.run(debug=True)