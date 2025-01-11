# Production Bounded Context

# Recipe Model
class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

# Batch Model
class Batch:
    def __init__(self, batch_id, recipe, produced_date):
        self.batch_id = batch_id  # Identity
        self.recipe = recipe
        self.produced_date = produced_date

# Example Usage
chocolate_recipe = Recipe("Milk Chocolate", ["milk", "sugar", "cocoa"])
chocolate_batch = Batch(1, chocolate_recipe, "2025-01-10")

print(f"Batch ID: {chocolate_batch.batch_id}, Produced Date: {chocolate_batch.produced_date}, Recipe: {chocolate_batch.recipe.name}")

# Bounded Context Explanation:
# The Production Bounded Context represents the manufacturing domain of chocolate production.
# It contains models that are specifically focused on the production process:

# 1. Recipe Model:
# Represents the formula/instructions for making a specific type of chocolate
# Contains name and ingredients list
# Relevant only in the production context, may differ from recipes in other contexts
# (e.g. Marketing context might have different recipe details)

# 2. Batch Model:
#  Represents a single production run of chocolate
#  Has unique identity (batch_id)
#  Contains reference to the recipe used
#  Tracks production date
#  Only concerned with production-specific attributes
#  Does not contain irrelevant details from other contexts


# This bounded context:
# Maintains clear boundaries around production domain concepts
# Uses ubiquitous language specific to production ("batch", "recipe", "ingredients")
# Isolates production logic from other business concerns
# Ensures models only contain attributes relevant to production
# Prevents concept bleeding from other contexts (like sales or inventory)
