import openai
import json 
import os 
from collections import defaultdict
import requests
import time

# load market place listings simulated data for getting corresponding images
f = open(r'/Users/ketakikolhatkar/Documents/Projects/RAG/data/maketplace_listings.json', 'r')
data = json.load(f)

# output dir 
output_dir = 'data/images'
os.makedirs(output_dir, exist_ok=True)

# track index per category
category_counter = defaultdict(int)

def safe_prompt(item):
    """
    Generate a safe prompt for the item.
    """
    title = item.get('title', '').strip()[:50].replace(" ", "").replace("'", "").replace(",", "")
    condition = item.get("condition", "used").lower()
    category = item.get("category", "general").lower()
    description = item.get('description', '').strip()[:50].replace(" ", "").replace("'", "").replace(",", "")
    return f"Generate a high-quality product photo of a {condition} {category} item that someone might be selling on a marketplace."

# Generate an image using OpenAI's DALL-E
openai.api_key = "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"


for item in data[468:]:
    category = item['category'].lower().replace(" ", "_")
    index = category_counter[category]
    id = item['id']
    condition = item['condition'].lower()
    title = item['title']
    description = item['description']

    # Generate DALL-E image 
    prompt = safe_prompt(item)
    response = openai.images.generate(
        model='dall-e-3',
        prompt=prompt,
        n=1,
        size="1024x1024",
        quality='standard'
    )

    image_url = response.data[0].url

    # download the image
    filename = f'{category}_{id}.jpg'
    image_path = os.path.join(output_dir, filename)
    img_data = requests.get(image_url).content
    with open(image_path, 'wb') as image_file:
        image_file.write(img_data)

    item['image_path'] = image_path
    # increment the counter for the category
    category_counter[category] += 1
    print(f'Saved image: {image_path}')
    time.sleep(10)


# save updated json
with  open(r'/data/maketplace_listings_with_images.json', 'w') as f:
    json.dump(data, f, indent=4)
