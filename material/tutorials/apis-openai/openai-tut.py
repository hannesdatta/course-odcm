# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # APIs Advanced (OpenAI)

# %% [markdown]
# ## 1. Introduction
#
# Welcome to the **API Advanced Tutorial**, introducing you to an advanced API for using AI.
#
# In this session, we'll start with a brief introduction to APIs and go over some essential programming tools. We'll use a simple analogy to help explain how different models in the OpenAI API work, and we'll carry that analogy throughout the workshop.
#
# You'll learn the building blocks for using generative AI in research. We'll also cover important topics like data privacy and security when working with AI tools.
#
# ### Learning Goals
#
# - Create an OpenAI account and set up your API key
# - Understand how to send and receive requests using the OpenAI API
# - Use different models such as text generation-, speech-, and embeddings models
# - Be aware of costs, limitations, and ethical considerations
#

# %% [markdown]
# ## 1. Getting Started
#
# ### Prerequisites
#
#
# Before joining the workshop, make sure you have the following ready:
#
# - An [OpenAI account](https://platform.openai.com/signup)
#   - Note that during class, you will be provided with an API key.
#   - Outside of the class, you need your own (paid) API key.
# - A code editor installed on your computer
#   - e.g., Visual Studio Code (VS Code) ([Install guide via Tilburg Science Hub](https://tilburgsciencehub.com/topics/Computer-Setup/software-installation/IDE/vscode/))
#

# %% [markdown]
# ### What were API calls again?
#
# We'll start with the most basic way to make an API call to OpenAI's GPT model.
#
# **Restaurant analogy**:
# - **You (Customer):** The person making the request  
# - **OpenAI API (Waiter):** The messenger that takes your request to the AI  
# - **GPT Model (Chef):** The system that processes your request and creates the response

# %% [markdown]
# ### Setting Up Your API Key
#
# Before making your first API call, follow these steps:
#
# 1. Get your API key at [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
# 2. Store it securely in an `.env` file
#    
#    `OPENAI_API_KEY="sk-..."` 
#    
# 3. In Python, you’ll access it using...
#

# %%
from dotenv import find_dotenv, load_dotenv
import os

found = find_dotenv(usecwd=True)
print("Found .env at:", found)
load_dotenv(found, override=True)
api_key = os.getenv("OPENAI_API_KEY")
print(f"OPENAI_API_KEY = {api_key}")


# %% [markdown]
# ### Exercise 1
#
# - Please create a `.env` file in your project directory and try running the code snippet in the cell above. Does it display the correct API key, as shared with you during the class?

# %% [markdown]
# ### Let's run our first API call to OpenAI

# %% [markdown]
# ### Exercise 2
#
# - Run the cell below - do you get the output (let's compare it with other students)
# - Change the *temperature parameter* (e.g., to 1, 2, etc.) - compare the output again. What does *temperature* in the context of AI mean?
#

# %%
import os
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv

# Load environment variables from .env
found = find_dotenv(usecwd=True)
load_dotenv(found, override=True)
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

prompt = "Why do you think it is a good idea to study in Tilburg?"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=1
)

print("🧠 Response from the AI (Chef):\n")
print(response.choices[0].message.content)

# %% [markdown]
# ## 2. Applying Basic Programming Principles to OpenAI's API
#
# ### Looping — “Ordering Again and Again”
#

# %%
import pandas as pd

reviews = pd.DataFrame({
    "review": [
        "The pasta was perfectly al dente, but the service felt rushed.",
        "A cozy spot with incredible sushi and a relaxed atmosphere.",
        "Overpriced for the portion size, though the flavors were outstanding.",
        "The waiter remembered our names and made the evening feel special.",
        "The burger was juicy, but the fries were soggy and cold."
    ]
})

for i, r in enumerate(reviews["review"], 1):
    print(f"Pretend we're asking the AI to text-analyze review {i}: {r}\n")

# %% [markdown]
# ### Looping the OpenAI API

# %%
import time

reviews["emotional_score_gpt"] = None
prompt_template = (
    "Read the following restaurant review and rate the overall emotional tone "
    "on a scale from 1 (very negative) to 5 (very positive). Return only the number.\nReview: {}"
)

for i, review_text in enumerate(reviews["review"], 1):
    print(f"Iteration {i}...")
    review_prompt = prompt_template.format(review_text)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": review_prompt}],
        temperature=0
    )
    reviews.loc[i - 1, "emotional_score_gpt"] = response.choices[0].message.content
    time.sleep(0.5)

reviews

# %% [markdown]
# ### API “Memory” Demonstration

# %%
response1 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "My favorite color is blue."}],
    temperature=0
)
print("First response:\n", response1.choices[0].message.content, "\n")

response2 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What is my favorite color?"}],
    temperature=0
)
print("Second response (no memory):\n", response2.choices[0].message.content, "\n")

# %% [markdown]
# ## 3. Meet Some of OpenAI's Endpoints — “Different Sections of the Menu”

# %%
import requests
import base64

api_key = os.getenv("OPENAI_API_KEY")
output_dir = "product_images"
os.makedirs(output_dir, exist_ok=True)

base_prompt = (
    "A studio photo of a can of sparkling water, on a minimalist background, "
    "professional lighting, high-quality product photography, marketing style"
)

prompts = [
    f"{base_prompt} — blue packaging with silver logo",
    f"{base_prompt} — green packaging with a lemon slice",
    f"{base_prompt} — pink packaging with a berry illustration"
]

for i, prompt in enumerate(prompts, 1):
    print(f"\n🪄 Generating variant {i}...")
    resp = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={"model": "gpt-image-1", "prompt": prompt, "size": "1024x1024", "n": 1}
    )
    res = resp.json()
    img_data = res["data"][0]["b64_json"]
    image_file = f"{output_dir}/product_variant_{i}.png"
    with open(image_file, "wb") as f:
        f.write(base64.b64decode(img_data))
    print(f"✅ Saved generated image: {image_file}")

# %% [markdown]
# ### Speech Endpoint — Text to Audio

# %%
voices = ["echo", "nova", "shimmer"]
input_text = (
    "Today, we are testing the OpenAI API. "
    "At the moment, we are testing the audio API."
)
audio_dir = "audio"
os.makedirs(audio_dir, exist_ok=True)

for voice in voices:
    speech_file = f"{audio_dir}/speech_{voice}.mp3"
    resp = requests.post(
        "https://api.openai.com/v1/audio/speech",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={"model": "gpt-4o-mini-tts", "voice": voice, "input": input_text}
    )
    with open(speech_file, "wb") as f:
        f.write(resp.content)
    print("Saved speech to:", speech_file)

# %% [markdown]
# ### Transcription Endpoint — Speech to Text

# %%
audio_file_path = f"{audio_dir}/speech_echo.mp3"
with open(audio_file_path, "rb") as f:
    resp = requests.post(
        "https://api.openai.com/v1/audio/transcriptions",
        headers={"Authorization": f"Bearer {api_key}"},
        files={"file": (audio_file_path, f, "audio/mpeg")},
        data={"model": "whisper-1"}
    )
print("Transcript:\n", resp.json().get("text"))

# %% [markdown]
# ### Embeddings Endpoint

# %%
text = "The food was delicious and the waiter..."
resp = requests.post(
    "https://api.openai.com/v1/embeddings",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={"model": "text-embedding-3-small", "input": text}
)
embedding = resp.json()["data"][0]["embedding"]
print("🔢 First 50 values of embedding:\n", embedding[:50])
print("\nThe embedding is a list of", len(embedding), "floats")

# %% [markdown]
# ## Tokens — “How Much You’re Saying”

# %%
prompt = "Explain API calls in simple terms, using the customer - waiter - chef metaphor."

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7
)

output = response.choices[0].message.content
print("Output:\n", output, "\n")

usage = response.usage
print("Token usage:")
print("Input tokens:", usage.prompt_tokens)
print("Output tokens:", usage.completion_tokens)
print("Total tokens:", usage.total_tokens)

cost = (
    (usage.prompt_tokens / 1_000_000) * 2
    + (usage.completion_tokens / 1_000_000) * 8
)
print("\nEstimated cost ($):", round(cost, 6))

# %% [markdown]
# ## Wrapping Up
#
# In this workshop, we covered:
# - Using your OpenAI API key securely
# - Making your first API call
# - Looping over multiple prompts
# - Using different endpoints (text, image, audio, embeddings)
# - Understanding tokens and cost
