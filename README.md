# Adaptative Post Description Based on Audience

## Overview
This project uses AI to generate personalized social media captions from images or text. Unlike existing tools, our solution adapts content based on audience types, ensuring more relevant and engaging posts. Descriptions can reflect different tones and emotions to match the intended demographic.

## Features
- **Image Captioning** – Upload an image and receive a caption.
- **Audience Adaptation** – Adjust tone and content for different audiences.
- **Emotion Selection** – Tailor captions to reflect specific moods or intentions.

## How It Works
1. **Image Analysis** – Visual features are extracted using Vision Transformer (ViT).
2. **Text Generation** – GPT-2 generates captions in natural language.
3. **Customization** – Audience and emotion parameters refine the final output using a link to the API of the pre-trained large language model **llama3-70b-8192**.

## Setup
### Prerequisites
- Python 3.8+
- PyTorch
- Transformers (Hugging Face)
- PIL (Pillow)
- Flask

### Installation
```bash
# Clone the repository
git clone https://github.com/celialctnm/Final_Project_AI.git
cd Final_Project_AI

# Install required packages
pip install -r requirements.txt
```
- Generate you API key for accessing LLaMA3 model on https://console.groq.com/keys.
- Create an environment variable to your computer named `GROQ_API_KEY` with you API key for the code to access it.

## Usage
### Execute the program
1. Execute the file `main.py` to run the Flask server.
2. Go to the specified link on the web browser. By default, the link is: `127.0.0.1:5000`.

## Model Details
- **Vision Encoder** – ViT extracts visual features from images.
- **Text Decoder** – GPT-2 generates captions from the extracted features.
- **Fine-Tuning** – Models adapt to various audiences and emotional tones by leveraging LLaMA3 for advanced language generation.

## Results
Our model consistently generates audience-specific and emotionally relevant captions, filling a gap left by existing tools. Testing shows increased engagement and better alignment with user expectations.