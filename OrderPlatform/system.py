# Import necessary modules
from typing import Optional, List
from colorama import Fore
import pymongo

# Set up console text color codes
r = Fore.RED,
b = Fore.BLUE,
y = Fore.YELLOW,
c = Fore.CYAN,
g = Fore.GREEN,
bl = Fore.BLACK

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['OrderPlatform']
collection = db.order_platform
content_manager = db.platform_manager

# Define a prefix for console output
prefix = f"{bl}[{b}Order{c}Platform{bl}] {b}|{c}"

# Function to search for a record in the database based on a query
def search_bool(query: dict, value: Optional[str] = False, contentmanager: Optional[bool] = False):
    if not value and not contentmanager:
        filter = query
        result = collection.find_one(filter)
        if result:
            return True

    elif value != False and not contentmanager:
        filter = query
        result = collection.find_one(filter[value])
        if result:
            return True

    elif contentmanager:
        filter = query
        result = content_manager.find_one(filter[value])
        if result:
            return True

# Function to search for and retrieve a record's value from the database based on a query
def search_value(query: dict, value: Optional[str] = False, contentmanager: Optional[bool] = False):
    if not value and not contentmanager:
        filter = query
        result = collection.find_one(filter)
        if result:
            return result

    elif value != False and not contentmanager:
        filter = query
        result = collection.find_one(filter[value])
        if result:
            return result[value]

    elif contentmanager:
        filter = query
        result = content_manager.find_one(filter[value])
        if result:
            return result[value]


# Function to delete a record from the database based on a query
def delete_value(query: dict, value: Optional[str] = False):
    if not value:
        filter = query
        result = collection.delete_one(filter)

    if value != False:
        filter = query
        result = collection.delete_one(filter[value])

# Function to update a specific value in a record in the database
def update_value(query: dict, value: str, new_value: str or list, contentmanager: Optional[bool] = False):
    if not contentmanager:
        filter = query
        update = {"$push": {value: new_value}}
        result = collection.update_one(filter, update)

    elif contentmanager:
        filter = query
        update = {"$push": {value: new_value}}
        result = content_manager.update_one(filter, update)


# Function to create a new organization record in the database
def create_organization(name: str, id: str, id_code: int):
    result = search_bool({"organization": name, "id": id})
    if result:
        print(f"{prefix} {r}Error: ID already exists in database.")
    else:
        collection.insert_one({"organization": name, "id": id, "passcode": id_code, "contents": []})
        print(f"{prefix} {g}Success: Created organization, {name}.")

# Function to remove an organization record from the database
def remove_organization(name: str, id: str, id_code: int):
    result1 = search_value({"organization": name, "id": id})
    result2 = search_value({"organization": name, "passcode": id_code})

    if id == result1 and id_code == result2:
        delete_value({"organization": name})
        print(f"{prefix} {g}Success: Removing organization, {name}.")

    else:
        print(f"{prefix} {r}Error: Incorrect values.")

# Function to set the contents of an organization's record in the database
def set_contents(name: str, organization_id: str, organization_passcode: int, contents: List[any]):
    result1 = search_value({"organization": name, "id": organization_id})
    result2 = search_value({"organization": name, "passcode": organization_passcode})

    if organization_id == result1 and organization_passcode == result2:
        # Update the organization's contents directly, not through content_manager
        update_value({"organization": name, "id": organization_id}, "contents", contents)
        print(f"{prefix} {g}Success: Contents added to organization, {name}.")
    else:
        print(f"{prefix} {r}Error: Incorrect organization credentials.")
