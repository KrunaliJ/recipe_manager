# recipe_manager using dictionaries

recipe_book = {...}
Create an initial dictionary called recipe_book.

Each key is a recipe name ("Tea").
Each value is another nested dictionary containing:
ingredients → List of ingredients
time → Cooking time
steps → Instructions
nutrition → Another dictionary with calories and caffeine

def display_menu():
Function to print the main menu options for the user.

Inside display_menu():
print("\n Recipe Manager Menu:")
print("1. View All Recipes")
...
Print all the user actions they can choose: view, add, update, delete, search, backup, exit.

def view_all():
Function to show all recipes from recipe_book.

Inside view_all():
if not recipe_book:
    print("No recipes available.")
    return
If the dictionary is empty, tell the user there are no recipes and return early.

for name, details in recipe_book.items():
    print(f"\n{name}")
    for key, value in details.items():
        print(f"  {key.capitalize()}: {value}")
Loop through each recipe and print all details neatly.

def add_recipe():
Function to add a new recipe into the recipe_book.

Inside add_recipe():

name = input("Recipe name: ").title()
if name in recipe_book:
    print("Recipe already exists!")
    return
Get recipe name.

Check if it already exists to avoid duplicates.

ingredients = input("Ingredients (comma-separated): ").split(",")
ingredients = [i.strip().title() for i in ingredients]
Take ingredients separated by commas and clean extra spaces.

time = int(input("Cooking time (in minutes): "))
steps = input("Steps: ")
calories = input("Calories: ")
caffeine = input("Caffeine (or N/A): ")
Input other required data.

recipe_book[name] = {
    "ingredients": ingredients,
    "time": time,
    "steps": steps,
    "nutrition": {
        "calories": calories,
        "caffeine": caffeine
    }
}
Store everything in the dictionary under the new recipe name.

def update_recipe():
Function to edit an existing recipe.

Inside update_recipe():
name = input("Recipe name to update: ").title()
if name not in recipe_book:
    print("Recipe not found.")
    return
Check if the recipe exists.

print("What do you want to update?")
print("1. Ingredients\n2. Time\n3. Steps\n4. Nutrition")
choice = input("Enter option (1-4): ")
Ask the user what they want to update.

if choice == "1":
    ingredients = input("New ingredients (comma-separated): ").split(",")
    recipe_book[name]["ingredients"] = [i.strip().title() for i in ingredients]
Update ingredients.

elif choice == "2":
    recipe_book[name]["time"] = int(input("New cooking time: "))
Update cooking time.

elif choice == "3":
    recipe_book[name]["steps"] = input("New steps: ")
Update steps.

elif choice == "4":
    recipe_book[name]["nutrition"]["calories"] = input("New calories: ")
    recipe_book[name]["nutrition"]["caffeine"] = input("New caffeine: ")
Update nutrition info (nested dictionary update).

def delete_recipe():
Function to remove a recipe.

Inside delete_recipe():
name = input("Recipe name to delete: ").title()
if name in recipe_book:
    del recipe_book[name]
    print(f"'{name}' removed.")
else:
    print("Recipe not found.")
Use del to delete a key-value pair from dictionary.

def search_recipe():
Function to search for a recipe by name.

Inside search_recipe():
name = input("Enter recipe to search: ").title()
if name in recipe_book:
    print(f"\n{name}")
    for key, value in recipe_book[name].items():
        print(f"  {key.capitalize()}: {value}")
else:
    print("Recipe not found.")
If recipe exists, display its details nicely.

def backup():
Function to make a backup copy of the recipe book.

Inside backup():
backup_copy = recipe_book.copy()
print("\n Backup created successfully!")
print(f"Backup data:\n{backup_copy}")
.copy() method creates a shallow copy of the dictionary.

Show the backup copy.

Main Program Loop:
while True:
    display_menu()
    choice = input("Choose an option (1-7): ")
Always show the menu and ask for the user’s choice.

if choice == "1":
    view_all()
elif choice == "2":
    add_recipe()
...
Based on the choice, call the corresponding function.

elif choice == "7":
    print("Exiting Recipe Manager. Bye!")
    break
Exit the program when the user chooses option 7.

else:
    print("Invalid choice. Try again.")
If invalid input, ask again.
