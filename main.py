shopping_list = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]

}
amount = 0
for shop, products in shopping_list.items():
    
    shop_title = shop.title()
    products_title = [product.title() for product in products]

    print(f"Idę do {shop_title} i kupuję tam {products_title}.") 
    
    amount = amount + len(products)

print(f"W sumie kupuję {amount} produktów")

