from recipe import Recipe
import datetime

class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        if type(name) != str:
            print("It must be a string name")
            exit(1)
        if type(last_update) != datetime.datetime:
            print("Input is not valid.")
            exit(1)
        if type(creation_date) != datetime.datetime:
            print("Invalid input.")
            exit(1)
        if type(recipes_list) != dict:
            print("Invalid input.")
            exit(1)
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        for key in self.recipes_list.keys():
            for elem in self.recipes_list[key]:
                self.recipes_list[key].__str__()
        pass
    def get_recipes_by_types(self, recipe_type):
        recipes_name = []
        for key in self.recipe_list.keys():
            if key == recipe_type:
                for elem in self.recipe_list[key]:
                    recipes_names.append(elem.name)
        return recipes_name
        pass
    def add_recipe(self, recipe):
        self.recipes_list[recipe.recipe_type].append(recipe)
        pass