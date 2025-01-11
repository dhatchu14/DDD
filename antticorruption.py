# External System
class ExternalSystem:
    def get_customer_info(self):
        # External system provides customer info
        return {"customer_id": "12345", "external_data": "some data"}

# Anti-Corruption Layer
class CustomerInfoACL:
    def __init__(self, external_system):
        self.external_system = external_system

    def get_customer_info(self):
        # Translate external data to internal format
        external_info = self.external_system.get_customer_info()
        internal_info = {
            "id": external_info["customer_id"],
            "data": external_info["external_data"]
        }
        return internal_info

# Internal Domain
class Customer:
    def __init__(self, customer_info):
        self.id = customer_info["id"]
        self.data = customer_info["data"]

# Example Usage
external_system = ExternalSystem()
acl = CustomerInfoACL(external_system)  # Anti-Corruption Layer
customer_info = acl.get_customer_info()  # Translated data
customer = Customer(customer_info)  # Internal domain working with cleaned data

print(f"Customer ID: {customer.id}, Data: {customer.data}")

# Anti-Corruption Layer (ACL) Explanation:
# The Anti-Corruption Layer pattern is used to prevent external system concepts
# from "corrupting" our domain model. It acts as a translator between two systems
# that speak different languages.

# In this code:
# 1. ExternalSystem represents a legacy/external system with its own data format:
# Returns data in format: {"customer_id": "12345", "external_data": "some data"}

# 2. CustomerInfoACL is the Anti-Corruption Layer:
# Takes external system as dependency
# Translates external format to our internal format
# Maps "customer_id" -> "id" and "external_data" -> "data"
# Protects our domain model from external system changes
#
# 3. Customer is our clean domain model:
# Works only with translated internal format
# Completely unaware of external system details
# Protected from changes in external system



