from flask import *
import os
from openai import OpenAI

# convention à respecter
# images, css, tout mettre dans le répertoire static sinon ça marche pas
# page HTML dans le réperoire templates

# modèle à implémenter

# faire lien API ChatGPT

app = Flask(__name__)

UPLOAD_FOLDER = 'static/images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# key for chatgpt
client = OpenAI(
    api_key="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")


@app.route('/')
def home():
    return render_template('index.html')


def create_model():
    model = "model"
    return model


def chat_with_gpt(content):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": content}
        ]
    )
    description = completion.choices[0].message.content
    return description


@app.route('/predict', methods=['POST'])
def predict():
    audience = request.form.get('audience')
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

        description = chat_with_gpt("Can you write a caption for my instagram post, my audience is my " + audience + ".The photo represents " + model)
        print(filepath)
    return render_template('result.html', audience=audience, image_path=filepath, description=description)


if __name__ == '__main__':
    # changer à False le debug lorsque le code sera fini
    app.run(debug=True)
