
# Real-World Recipe Manager App

# Initial recipe book (Nested Dictionary)
recipe_book = {
    "Tea": {
        "ingredients": ["Water", "Tea Leaves", "Sugar", "Milk"],
        "time": 10,
        "steps": "Boil water, add tea leaves, sugar, milk. Simmer and serve.",
        "nutrition": {
            "calories": 40,
            "caffeine": "25mg"
        }
    }
}

def display_menu():
    print("\n Recipe Manager Menu:")
    print("1. View All Recipes")
    print("2. Add New Recipe")
    print("3. Update Recipe")
    print("4. Delete Recipe")
    print("5. Search Recipe")
    print("6. Backup Recipe Book")
    print("7. Exit")

def view_all():
    if not recipe_book:
        print(" No recipes available.")
        return
    for name, details in recipe_book.items():
        print(f"\n {name}")
        for key, value in details.items():
            print(f"  {key.capitalize()}: {value}")

def add_recipe():
    name = input(" Recipe name: ").title()
    if name in recipe_book:
        print(" Recipe already exists!")
        return
    ingredients = input(" Ingredients (comma-separated): ").split(",")
    ingredients = [i.strip().title() for i in ingredients]
    time = int(input(" Cooking time (in minutes): "))
    steps = input(" Steps: ")
    calories = input(" Calories: ")
    caffeine = input(" Caffeine (or N/A): ")

    recipe_book[name] = {
        "ingredients": ingredients,
        "time": time,
        "steps": steps,
        "nutrition": {
            "calories": calories,
            "caffeine": caffeine
        }
    }
    print(f" '{name}' added successfully!")

def update_recipe():
    name = input("✏️ Recipe name to update: ").title()
    if name not in recipe_book:
        print("  Recipe not found.")
        return
    print(" What do you want to update?")
    print("1. Ingredients\n2. Time\n3. Steps\n4. Nutrition")
    choice = input("Enter option (1-4): ")

    if choice == "1":
        ingredients = input("New ingredients (comma-separated): ").split(",")
        recipe_book[name]["ingredients"] = [i.strip().title() for i in ingredients]
    elif choice == "2":
        recipe_book[name]["time"] = int(input("New cooking time: "))
    elif choice == "3":
        recipe_book[name]["steps"] = input("New steps: ")
    elif choice == "4":
        recipe_book[name]["nutrition"]["calories"] = input("New calories: ")
        recipe_book[name]["nutrition"]["caffeine"] = input("New caffeine: ")
    else:
        print(" Invalid option.")
        return

    print(f" '{name}' updated!")

def delete_recipe():
    name = input(" Recipe name to delete: ").title()
    if name in recipe_book:
        del recipe_book[name]
        print(f" '{name}' removed.")
    else:
        print("  Recipe not found.")

def search_recipe():
    name = input(" Enter recipe to search: ").title()
    if name in recipe_book:
        print(f"\n {name}")
        for key, value in recipe_book[name].items():
            print(f"  {key.capitalize()}: {value}")
    else:
        print("  Recipe not found.")

def backup():
    backup_copy = recipe_book.copy()
    print("\n Backup created successfully!")
    print(f"Backup data:\n{backup_copy}")

#  Main loop
while True:
    display_menu()
    choice = input("Choose an option (1-7): ")

    if choice == "1":
        view_all()
    elif choice == "2":
        add_recipe()
    elif choice == "3":
        update_recipe()
    elif choice == "4":
        delete_recipe()
    elif choice == "5":
        search_recipe()
    elif choice == "6":
        backup()
    elif choice == "7":
        print(" Exiting Recipe Manager. Bye!")
        break
    else:
        print("  Invalid choice. Try again.")
