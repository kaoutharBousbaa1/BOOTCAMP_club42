from book import Book
from recipe import Recipe

class Book:
    def __init__(self):
        self.name = ""
        self.last_update = 0
        self.creation_date = 0
        self.recipes_list = {"starter" : , "lunch" : , "dessert" : }
    def get_recipe_by_name(self, name):

        pass
    def get_recipes_by_types(self, recipe_type):

        pass
    def add_recipe(self, recipe):

        pass
class Recipe:
    def __init__(self):
        self.name = " "
        self.cooking_lvl = range(1,5) 
        self.cooking_time = 0
        self.ingredients = []
        self.description = " "
        self.recipe_type = {1: "starter", 2: "lunch", 3:"dessert"}
    def __str__(self):

        txt = ""

        return txt

recipe = Recipe()

