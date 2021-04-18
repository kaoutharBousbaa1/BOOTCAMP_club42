from book import Book
from recipe import Recipe
from datetime import datetime

book1 = Book("book1", datetime.now(), datetime.now(), {"starter":[], "lunch":[], "dessert":[]})
recipe1 = Recipe("recipe1", 10, 5, ["sugar"], "", "starter")
recipe2 = Recipe("recipe2", 20, 3, ["watermelon"], "", "lunch")
to_print1 = str(recipe1)
print(to_print1)
to_print2 = str(recipe2)
print(to_print2)
book1.add_recipe(recipe1)
book1.get_recipe_by_name(recipe1)
book1.add_recipe(recipe2)
book1.get_recipes_by_types("lunch")



