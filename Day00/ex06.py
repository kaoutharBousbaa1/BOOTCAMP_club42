cookbook= {
    "sandwich":{'ingredients': ['ham', 'bread', 'cheese' ,'tomatoes'],
                'meal': 'lunch',
                'prep_time': '10 min'
                },
    "cake":{'ingredients':['flour', 'sugar' , 'eggs'],
            'meal': 'desert',
            'prep_time':'60 min'
            },
    "salad":{'ingredients': ['avocado', 'arugula', ' tomatoes' ,'spinach'],
            'meal':'lunch',
            'prep_time':'15 min'
            }
    }
for cle in cookbook.keys():
    print(cle)
for valeur in cookbook.values():
    print(valeur)
def print_recipe(recipe):
    for valeur in cookbook.recipe.values():
        print(valeur)

def delete_recipe(recipe):
    del placard[recipe]

def add_recipe(recipe, ingredinets, meal, pre_time):
    cookbook.update({recipe: ingredinets, meal, pre_time})

def print_all(cookbook):
    for cle in cookbook.keys():
        print(cle)

print("===============Please select an option by typing the corresponding number:=============")
print("1: Add a recipe\n 2: Delete a recipe\n 3: Print a recipe \n4: Print the cookbook \n 5: Quit")

while True:
    choice = input()
    if choice == 5:
        print("Cookbook closed")
        exit(0)
    if choice == 2:
        recipe = input("Enter please the name of the recipe you want to delete from the cookbook")
        delete_recipe(recipe)
    if choice == 1:
        recipe = input("Enter please the name of the recipe you want to add to the cookbook")
        add_recipe(recipe)
    if choice == 3:
        recipe = input("Enter please the name of the recipe you want to print from the cookbook")
        print_recipe(recipe)
    if choice == 4:
        print_all(cookbook)
    else:
        print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")





