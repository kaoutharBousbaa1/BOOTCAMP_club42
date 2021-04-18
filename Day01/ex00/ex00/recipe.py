
class Recipe:
    def __init__(self, name, cooking_time, cooking_lvl, ingredients, description, recipe_type):
        if type(name) != str or name == "":
            print("Invalid name")
            exit(1)
        if cooking_time < 0 or type(cooking_time) != int:
            print("Invalid cooking_time")
            exit(1)
        if type(cooking_lvl) != int or cooking_lvl not in range (1, 6):
            print("Invalid cooking_lvl")
            exit(1)
        if len(ingredients) == 0 or type(elem) != str for elem in ingredients:
            print("Ingredients list is not valid")
            exit(1)
        if type(description) != str:
            print("Description is not valid")
            exit(1)
        if type(recipe_type != str) or recipe_type not in ["starter", "lunch", "dessert"]
            print("Invalid recipe_type")
            exit(1)
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = reccipe_type
    def __str__(self):
        txt = "Recipe_name:" + self.name + "cooking_time: " + str(self.cooking_time) + "cooking_lvl :" + str(self.cooking_lvl) + "ingredients: " + str(self.ingredients) + "Description :" + self.description + "Recipe_type :" + self.recipe_type
        return txt