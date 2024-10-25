#1. Create a dictionary of 8 foods and their recipes.
dict = {
"Easy Fish Tacos": "3 cups green cabbage (300 g) shredded",
"Asparagus-Stuffed Chicken Breast": "3 boneless, skinless chicken breasts",
"Garlic Broccoli Shrimp Stir Fry": "1 lb large shrimp (455 g), peeled and deveined",
"One-Pot Creamy Tuscan Pasta": "2 tablespoons unsalted butter",
"Honey Soy-Glazed Salmon": "12 oz skinless salmon (340 g)",
"Fajita Parchment-Baked Chicken": "parchment paper, or aluminium foil, 12x18 inches",
"Slow Cooker Pot Roast": "3 lb chuck roast (1.5 kg)",
"Veggie Garlic Noodles": "2 tablespoons vegetable oil (30 mL)",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the recipe of the 5th food.
print("The recipe of the 5th food is: ", dict["Honey Soy-Glazed Salmon"])

#4. Update the recipe of the 3rd food.
dict["Garlic Broccoli Shrimp Stir Fry"] = "Shrimps"
print(dict)

#5. Delete the 7th food from the dictionary.
del dict["Slow Cooker Pot Roast"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last kay-value is: ", last_key, ":", last_value)