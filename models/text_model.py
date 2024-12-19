from groq import Groq
import os

# Configurez votre clé API
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

try:
    # Créez une requête pour obtenir une description Instagram personnalisée
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": "Create a custom description for Instagram for a mountain image please."
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    # Accéder et afficher le contenu généré
    if completion and completion.choices:
        generated_content = completion.choices[0].message.content
        print("Generated Content:\n")
        print(generated_content)
    else:
        print("No content generated")

except Exception as e:
    print(f"An error occurred: {e}")