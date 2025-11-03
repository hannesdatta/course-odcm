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
# # API Advanced using OpenAI's API 
#
# In this tutorial, we’ll gradually explore how to use **OpenAI’s API** in Python.
# Each section builds on the previous one:
#
# 1. Getting started – setting up and sending your first message  
# 2. Basic uses of chat completions  
# 3. Additional endpoints (images, audio, speech-to-text)  
# 4. Embeddings and semantic similarity
#
# Every section ends with a short **exercise** so that you can experiment with
# your own prompts and parameters.

# %% [markdown]
# # 1. Getting Started
#
# Let’s begin by setting up access to the API and making our very first request.
# Think of this as opening a conversation with the “AI waiter” for the first time.

# %% [markdown]
# ## 1.1 Loading your API key
#
# The API key is your personal password for talking to OpenAI’s servers.
# To keep it safe, we store it in a hidden file called `.env` in the same folder as this notebook.
#
# Example of what that file should contain:
#
# ```
# OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXX
# ```
#
# The code below loads the key from `.env` and prints only the beginning.

# %%
from dotenv import find_dotenv, load_dotenv
import os

found = find_dotenv(usecwd=True)
load_dotenv(found, override=True)
api_key = os.getenv("OPENAI_API_KEY")

print("Found .env at:", found)
print("Loaded key starts with:", api_key[:8], "...")

# %% [markdown]
# ### 🧩 Exercise 1 — Checking your setup
#
# - Verify that the path printed above actually points to your own project folder.  
# - If it shows a different directory (e.g. your user home), move your `.env` file here.  
# - Try intentionally changing the key to an invalid one and watch the API return an authentication error.  
# - Then fix it again!

# %% [markdown]
# ## 1.2 Your first chat with the model
#
# With the key loaded, we can finally “say hello” to the model.
# The OpenAI client handles the communication for us.

# %%
from openai import OpenAI
import json

client = OpenAI(api_key=api_key)

prompt = "Why might studying in Tilburg be a good idea?"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7
)

print(json.dumps(response.model_dump(), indent=2)[:500], "...\n")
print("🧠 Response:\n")
print(response.choices[0].message.content)

# %% [markdown]
# ### 🧩 Exercise 2 — Your first modification
#
# - Replace the prompt with your own question (for example *“What makes a good research question?”*).  
# - Change the `temperature` value (try `0`, `1`, and `1.5`) and observe how the creativity of the response changes.  
# - Reflect: what does “temperature” mean for text generation?

# %% [markdown]
# # 2. Basic Uses of Chat Completions
#
# Once you can send a single message, the next step is learning how to
# *structure a conversation* or repeat a task for many inputs.
# We’ll start with a small dataset of restaurant reviews.

# %%
reviews = [
    {"review": "The pasta was perfectly al dente, but the service felt rushed."},
    {"review": "A cozy spot with incredible sushi and a relaxed atmosphere."},
    {"review": "Overpriced for the portion size, though the flavors were outstanding."},
    {"review": "The waiter remembered our names and made the evening feel special."},
    {"review": "The burger was juicy, but the fries were soggy and cold."}
]

for i, item in enumerate(reviews, 1):
    print(f"{i}. {item['review']}")

# %% [markdown]
# - Each element here is a small dictionary (key → value pair).  
# - This mirrors the structure of JSON data returned by APIs — which is why
# we practice reading and writing lists of dictionaries instead of spreadsheets.

# %% [markdown]
# ## 2.1 Asking the model to analyse many texts
#
# We’ll now send each review to the API and ask for a quick sentiment score
# between 1 (very negative) and 5 (very positive).

# %%
import time

prompt_template = (
    "Rate the emotional tone of this restaurant review from 1 (very negative) "
    "to 5 (very positive). Return only the number.\nReview: {}"
)

for i, item in enumerate(reviews, 1):
    question = prompt_template.format(item['review'])
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}],
        temperature=0
    )
    item["score"] = response.choices[0].message.content.strip()
    print(f"{i}. {item['score']}")
    time.sleep(0.5)

# %% [markdown]
# ### 🧩 Exercise 3 — Experimenting with prompts
#
# - Change the question so that the model returns both a **score and one-sentence explanation**.  
# - What happens if you set `temperature=1`?  
# - Try writing a version that asks the model to output `"positive"`, `"neutral"`, or `"negative"` instead of numbers.

# %% [markdown]
# ## 2.2 Does the model remember?
#
# Each API call is independent — the model does *not* remember previous messages unless you send them again.
# Let’s see that in action.

# %%
r1 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "My favourite colour is blue."}],
    temperature=0
)
print("First answer:", r1.choices[0].message.content, "\n")

r2 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What is my favourite colour?"}],
    temperature=0
)
print("Second answer:", r2.choices[0].message.content)

# %% [markdown]
# ### 🧩 Exercise 4 — Building a short conversation
#
# - Modify the code so that the **second request includes both messages** in its `messages` list.  
# - Observe how the answer changes when the model has access to the conversation history.

# %% [markdown]
# # 3. Additional Endpoints — “Different Sections of the Menu”
#
# The Chat Completion endpoint is just one of several that OpenAI provides.
# Others let you generate images, convert text → speech, or speech → text.
# Think of these as talking to different *departments* of the same restaurant:
# the kitchen, the bar, and the cashier.

# %% [markdown]
# ## 3.1 Generating an image
#
# Here we create simple product images by sending text descriptions to the image endpoint.

# %%
import requests, base64

headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
output_dir = "product_images"
os.makedirs(output_dir, exist_ok=True)

prompts = [
    "A studio photo of a can of sparkling water — blue packaging with silver logo",
    "A studio photo of a can of sparkling water — green packaging with lemon slice"
]

for i, p in enumerate(prompts, 1):
    print(f"Creating image {i} ...")
    data = {"model": "gpt-image-1", "prompt": p, "size": "512x512", "n": 1}
    r = requests.post("https://api.openai.com/v1/images/generations", headers=headers, json=data)
    img_b64 = r.json()["data"][0]["b64_json"]
    file = f"{output_dir}/variant_{i}.png"
    with open(file, "wb") as f:
        f.write(base64.b64decode(img_b64))
    print("Saved:", file)

# %% [markdown]
# ### 🧩 Exercise 5 — Your own product idea
#
# - Replace one of the prompts with a description of your favourite drink or snack.  
# - Change the `size` from `"512x512"` to `"1024x1024"`.  
# - Observe how changing the text description changes the generated image.

# %% [markdown]
# ## 3.2 Text-to-Speech and Transcription
#
# Let’s make the model speak, then turn the audio back into text.

# %%
voices = ["nova", "shimmer"]
text_input = "This is a demonstration of OpenAI's text-to-speech model."
audio_dir = "audio"
os.makedirs(audio_dir, exist_ok=True)

for v in voices:
    filename = f"{audio_dir}/speech_{v}.mp3"
    resp = requests.post(
        "https://api.openai.com/v1/audio/speech",
        headers=headers,
        json={"model": "gpt-4o-mini-tts", "voice": v, "input": text_input}
    )
    with open(filename, "wb") as f:
        f.write(resp.content)
    print("Saved voice:", filename)

# %% [markdown]
# Now we transcribe one of those files back into text.

# %%
audio_file = f"{audio_dir}/speech_nova.mp3"
with open(audio_file, "rb") as f:
    r = requests.post(
        "https://api.openai.com/v1/audio/transcriptions",
        headers={"Authorization": f"Bearer {api_key}"},
        files={"file": (audio_file, f, "audio/mpeg")},
        data={"model": "whisper-1"}
    )
print("Transcript:\n", r.json().get("text"))

# %% [markdown]
# ### 🧩 Exercise 6 — Make it your own
#
# - Change `text_input` to a sentence of your choice (for instance a Dutch phrase).  
# - Try another `voice` name.  
# - Then transcribe it back — does the model handle the language correctly?

# %% [markdown]
# # 4. Embeddings — Understanding Similarity
#
# While chat and image endpoints produce *content*, embeddings represent *meaning* as numbers.
# They allow us to measure how similar two pieces of text are, even if they use different words.
# This section shows two simple applications.

# %%
def get_embedding(text):
    r = requests.post(
        "https://api.openai.com/v1/embeddings",
        headers=headers,
        json={"model": "text-embedding-3-small", "input": text}
    )
    return r.json()["data"][0]["embedding"]

def cosine(a, b):
    dot = sum(x*y for x, y in zip(a, b))
    mag = (sum(x*x for x in a)**0.5) * (sum(y*y for y in b)**0.5)
    return dot / mag

# %% [markdown]
# ## 4.1 Application 1 – Semantic Search
#
# Suppose we have a few product descriptions and a user query.
# We’ll embed both and sort by similarity.

# %%
products = [
    {"desc": "Crispy organic chips with sea salt"},
    {"desc": "High-protein energy bar"},
    {"desc": "Low-fat yogurt with real fruit"}
]

for p in products:
    p["embedding"] = get_embedding(p["desc"])

query = "healthy breakfast snack"
query_emb = get_embedding(query)

for p in products:
    p["similarity"] = cosine(p["embedding"], query_emb)

products.sort(key=lambda x: x["similarity"], reverse=True)
for p in products:
    print(p["desc"], "→", round(p["similarity"], 3))

# %% [markdown]
# ### 🧩 Exercise 7 — New products
#
# - Add one more description to the `products` list.  
# - Try a new `query` such as *“sweet dessert”* or *“post-workout snack”*.  
# - Which description is most similar?  
# - Reflect on how embeddings capture *meaning*, not exact wording.

# %% [markdown]
# ## 4.2 Application 2 – Automatic Coding of Survey Responses
#
# Instead of hand-coding open answers, we can embed both responses and category descriptions and match them by similarity.

# %%
responses = [
    {"text": "I love how convenient the app is."},
    {"text": "It’s too expensive for what you get."},
    {"text": "Customer service was very friendly."}
]

themes = [
    {"theme": "Convenience", "desc": "Ease and simplicity of using the product."},
    {"theme": "Price", "desc": "Affordability and value for money."},
    {"theme": "Service", "desc": "Friendliness and helpfulness of staff."}
]

for r in responses:
    r["embedding"] = get_embedding(r["text"])
for t in themes:
    t["embedding"] = get_embedding(t["desc"])

for r in responses:
    best = max(themes, key=lambda t: cosine(r["embedding"], t["embedding"]))
    r["best_theme"] = best["theme"]
    print(r["text"], "→", r["best_theme"])

# %% [markdown]
# ### 🧩 Exercise 8 — Expanding categories
#
# - Add a new theme such as `"Speed"` or `"Design"`.  
# - Try new responses in different wording.  
# - Observe whether the model still assigns them to the correct theme.

# %% [markdown]
# # 5. Wrapping Up
#
# In this tutorial we:
#
# - Set up API access with OpenAI
# - Sent and modified chat prompts  
# - Used loops to analyse multiple texts  
# - Generated images and speech  
# - Created embeddings to measure meaning
#
# You now know how to combine these building blocks for your own projects:
# from chat assistants to recommender systems and data analysis pipelines.
