# Core Domain: Chocolate Production
#ubiquitous language are batch_id,recipe,produced-date,ingreduents

# Recipe:subdomain
class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

# Batch:subdomain
class Batch:
    def __init__(self, batch_id, recipe, produced_date):
        self.batch_id = batch_id
        self.recipe = recipe
        self.produced_date = produced_date
        self.quality_checks = []

    def add_quality_check(self, issue):
        self.quality_checks.append(issue)

# Quality Control:subdomain
class QualityControl:
    def __init__(self, batch):
        self.batch = batch
        self.checks = []

    def add_check(self, issue):
        self.checks.append(issue)

# Generic Domain: Authentication
class Authentication:
    def __init__(self, user):
        self.user = user
        self.is_authenticated = False

    def login(self):
        # Logic for user authentication
        self.is_authenticated = True

# Generic Domain: Logging
class Logging:
    def __init__(self):
        self.logs = []

    def add_log(self, message):
        self.logs.append(message)

# Example Usage
chocolate_recipe = Recipe("Milk Chocolate", ["milk", "sugar", "cocoa"])
chocolate_batch = Batch(1, chocolate_recipe, "2025-01-10")
quality_control = QualityControl(chocolate_batch)
quality_control.add_check("Batch too soft")

authentication = Authentication("User123")
authentication.login()

logger = Logging()
logger.add_log("Batch 1 produced successfully")

print(f"Quality checks for batch {chocolate_batch.batch_id}: {quality_control.checks}")
print(f"Authentication status: {authentication.is_authenticated}")
print(f"Logs: {logger.logs}")
