pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

food_list = [pasta, apple_pie, ratatouille, chocolate_cake, omelette]
food_list_name = ["pasta", "apple pie", "ratatouille", "chocolate cake", "omelette"]

item = input()
'''
for i in range(len(food_list)):
    if item in food_list[i]:
        print(food_list_name[i] + " time!")
'''
for i in food_list:
    if item in i:
        print(food_list_name[food_list.index(i)] + " time!")

# Dictionary Solution
'''
pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingredient = input()

cook_book = {"pasta": pasta,
             "apple pie": apple_pie,
             "ratatouille": ratatouille,
             "chocolate cake": chocolate_cake,
             "omelette": omelette}

for name, recipe in cook_book.items():
    if ingredient in recipe:
        print("You can make %s" % name)
'''
