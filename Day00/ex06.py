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
#print the keys of the dictionary 
for cle in cookbook.keys():
    print(cle)
#print the values of the dictionary
for valeur in cookbook.values():
    print(valeur)

#print recipe from the cookbook
def print_recipe(recipe):
    for valeur in cookbook.recipe.values():
        print(valeur)
        
#delete a recipe from the dictionary 
def delete_recipe(recipe):
    del placard[recipe]
    
#fucntion to add a new recipe to the cookbook
def add_recipe(recipe, ingredinets, meal, pre_time):
    cookbook.update({recipe: ingredinets, meal, pre_time})

def print_all(cookbook):
    for cle in cookbook.keys():
        print(cle)

print("===============Please select an option by typing the corresponding number:=============")
print("1: Add a recipe\n 2: Delete a recipe\n 3: Print a recipe \n4: Print the cookbook \n 5: Quit")
choice = input()
while choice != NULL:
    switch (choice):
        case 5:
            print("Cookbook closed")
            exit(0)
            break
        case 2:
            recipe = input("Enter please the name of the recipe you want to delete from the cookbook")
            delete_recipe(recipe)
            break
        case 1:
            recipe = input("Enter please the name of the recipe you want to add to the cookbook")
            add_recipe(recipe)
            break
        case 3:
            recipe = input("Enter please the name of the recipe you want to print from the cookbook")
            print_recipe(recipe)
            break
        case 4:
            print_all(cookbook)
            break
        else:
            print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")





