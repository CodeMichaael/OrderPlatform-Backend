# OrderPlatform-Backend
Sneak peek of the backend for OrderPlatform 

# Examples

**1. Creating an Organization:**
```python
create_organization("MyOrg", "org123", 456)
# Output: [Order|Platform] | Success: Created organization, MyOrg.
```

**2. Removing an Organization:**
```python
remove_organization("MyOrg", "org123", 456)
# Output: [Order|Platform] | Success: Removing organization, MyOrg.
# Note: Make sure to use the correct ID and passcode for the organization.
```

**3. Setting Contents for an Organization:**
```python
contents_to_set = ["item1", "item2", "item3"]
set_contents("MyOrg", "org123", 456, contents_to_set)
# Output: [Order|Platform] | Success: Contents added to organization, MyOrg.
# Note: Ensure the organization credentials are correct.
```

**4. Searching for an Organization:**
```python
organization_exists = search_bool({"organization": "MyOrg", "id": "org123"})
if organization_exists:
    print("Organization exists.")
else:
    print("Organization not found.")
# Output: Organization exists.
```

**5. Retrieving Contents of an Organization:**
```python
org_contents = search_value({"organization": "MyOrg", "id": "org123"}, "contents")
if org_contents:
    print("Contents:", org_contents)
else:
    print("Organization not found.")
# Output: Contents: ['item1', 'item2', 'item3']
# Note: Ensure the organization credentials are correct.
```

**6. Deleting a Record (Organization):**
```python
delete_value({"organization": "MyOrg"})
# This deletes the organization record with the specified name.
```
