# Recipe Subdomain
class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

#Recipe Entity:Represents a unique recipe used to create chocolate batches.
# Unlike Value Objects, Recipe can have a unique identity if needed.
# Contains attributes:
# name: Name of the recipe (e.g., "Milk Chocolate").
# ingredients: List of ingredients used in the recipe.

# Batch Subdomain
class Batch:
    def __init__(self, batch_id, recipe, produced_date):
        self.id = batch_id  # Identity
        self.recipe = recipe
        self.produced_date = produced_date
        self.quality_checks = []

    def add_quality_check(self, issue):
        self.quality_checks.append(issue)

#Batch Entity:Represents a unique batch of chocolate production.
#Has its own identity (batch_id) that distinguishes it from other batches.
#Contains attributes:
#id: Unique identifier for the batch (batch_id).
#recipe: The recipe associated with the batch (e.g., Milk Chocolate).
#produced_date: The date when the batch was produced.
#quality_checks: A list of quality issues related to that batch.

# Example usage:
chocolate_recipe = Recipe("Milk Chocolate", ["milk", "sugar", "cocoa"])
chocolate_batch = Batch(1, chocolate_recipe, "2025-01-10")
chocolate_batch.add_quality_check("Batch too soft")

dark_chocolate_recipe = Recipe("Dark Chocolate", ["cocoa", "sugar"])
dark_chocolate_batch = Batch(2, dark_chocolate_recipe, "2025-01-11") 
dark_chocolate_batch.add_quality_check("Texture too grainy")

print(f"Batch ID: {chocolate_batch.id}")
print(f"Quality checks for batch {chocolate_batch.id}: {chocolate_batch.quality_checks}")
