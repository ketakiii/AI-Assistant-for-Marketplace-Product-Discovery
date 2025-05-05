# import necessary libraries
import random 
import json 
import os
from faker import Faker 

'''
This script generates a list of fake marketplace data for a product listing application.
The data includes product details such as title, description, price, category, location, condition
'''
class simulate_data:

    # initialize the class with some default values
    def __init__(self):
        self.categories = ['Electronics', 'Furniture', 'Clothing', 'Books', 'Sports']
        self.conditions = ['New', 'Like New', 'Used', 'Refurbished']
        self.locations = ['New York', 'Boston', 'Los Angeles', 'Chicago', 'Miami']
        self.products = []
        self.fake = Faker()

    # generate fake data for marketplace listings
    def generate_marketplace_data(self):
        # generate 500 products with random attributes
        for i in range(500):
            category = random.choice(self.categories)
            title = self.fake.sentence(nb_words=4)
            description = self.fake.paragraph(nb_sentences=2)
            price = round(random.uniform(5, 1000), 2)
            location = random.choice(self.locations)
            condition = random.choice(self.conditions)
            seller_name = self.fake.name()
            seller_rating = round(random.uniform(1, 5), 1)

            self.products.append({
                'id':f'prod_{i+1:04}',
                'title': title,
                'description': description,
                'price': price,
                'category': category,
                'location': location,
                'condition': condition,
                'seller_name': seller_name,
                'seller_rating': seller_rating,
                'created_at': self.fake.date_time_this_year().isoformat(),
                'updated_at': self.fake.date_time_this_year().isoformat(),
                'is_sold': random.choice([True, False]),
                'is_featured': random.choice([True, False]),
                'is_verified': random.choice([True, False]),
                'is_on_sale': random.choice([True, False]),
                'is_bargain': random.choice([True, False]),
                'is_wishlist': random.choice([True, False]),
                'is_favorite': random.choice([True, False]),
            })
        return self.products

    # save the generated data to a JSON file
    def generate_json_file(self, products):
        os.makedirs('data', exist_ok=True)
        with open('data/maketplace_listings.json', 'w') as f:
            json.dump(products, f, indent=4)


# main function to run the script
if __name__ == "__main__":
    # create an instance of the simulate_data class
    data_generator = simulate_data()
    # generate marketplace data
    products = data_generator.generate_marketplace_data()
    # save the generated data to a JSON file
    data_generator.generate_json_file(products)
    print("Marketplace data generated and saved to 'data/maketplace_listings.json'")
