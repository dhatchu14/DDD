# Value Object: ProducedDate
class ProducedDate:
    def __init__(self, date):
        self.date = date

    def __eq__(self, other):
        return isinstance(other, ProducedDate) and self.date == other.date

# Entity: Batch
class Batch:
    def __init__(self, batch_id, recipe, produced_date):
        self.batch_id = batch_id  # Entity ID
        self.recipe = recipe
        self.produced_date = produced_date  # Value Object
        self.quality_checks = []

    def add_quality_check(self, issue):
        self.quality_checks.append(issue)

# Example Usage
chocolate_recipe = "Milk Chocolate"  # Simple recipe for example
produced_date = ProducedDate("2025-01-10")  # Value Object
chocolate_batch = Batch(1, chocolate_recipe, produced_date)

chocolate_batch.add_quality_check("Batch too soft")

# Outputs
print(f"Batch ID: {chocolate_batch.batch_id}")
print(f"Produced Date: {chocolate_batch.produced_date.date}")
print(f"Quality Checks: {chocolate_batch.quality_checks}")
