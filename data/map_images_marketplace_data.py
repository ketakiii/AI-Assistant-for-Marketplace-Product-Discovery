import json 
import os 

jsonfile = r'/Users/ketakikolhatkar/Documents/Projects/RAG/data/marketplace-data/maketplace_listings.json'
jsonimagefile = r'/Users/ketakikolhatkar/Documents/Projects/RAG/data/marketplace-data/maketplace_listings_w_images.json'
with open(jsonfile, 'r') as f:
    data = json.load(f)

imagedir = r'/Users/ketakikolhatkar/Documents/Projects/RAG/data/images'

for item in data:
    prod_id = item['id']
    for dir in os.listdir(imagedir):
        if str(prod_id) in dir:
            item['image_path'] = os.path.join(imagedir, dir)
            break

# Save updated JSON
with open(jsonimagefile, "w") as file:
    json.dump(data, file, indent=4)
