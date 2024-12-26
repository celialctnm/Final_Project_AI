from groq import Groq
import os

# API key configured on your computer
# Can be generated on https://console.groq.com/keys
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def get_adapted_captions(base_caption, tone, audience):
    try:
        # Create a request for LLM model with the parameters
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {
                    "role": "user",
                    "content": "(Generate only each option seperated by a newline character, no other text please) \
                                Create a custom description (you can add hashtag if necessary) for a social media post for this description: " + base_caption + \
                                " using the following tone and mood : " + tone + \
                                " adapted to the audience of type : " + audience

                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )

        # Access and return the generated content
        if completion and completion.choices:
            generated_content = completion.choices[0].message.content
            print("Content generated.\n")
            descriptions = [line.strip() for line in generated_content.split("\n") if line.strip()]
            print("Options for adapted captions:", descriptions)
            return descriptions
        else:
            print("No content generated")
            return base_caption

    except Exception as e:
        print(f"An error occurred: {e}")
        return base_caption