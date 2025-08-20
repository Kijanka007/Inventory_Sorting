from File_Handling.util import write_file


# Function: displays whole inventory
def display_whole_inventory(inventory):
    # Runs through the whole inventory and prints every available product
    for ind, val in enumerate(inventory):
        print(val)

# Function: displays a item by name from the input of the user
def display_item_by_name(item_to_display, inventory):
    found = False
    found_item = ""

    # Looks for the item in the inventory
    for ind, item in enumerate(inventory):
        if item["name"] == item_to_display:
            found = True
            found_item = item
            break

    # If found returns the contact. else returns "name not found"
    if found == True:
        print(found_item)
    else:
        print("Item not found.")


# Function: updates an item in the inventory
def update_item(item_to_update, inventory, price_or_stock):

    # Loops through each item in inventory
    for ind, item in enumerate(inventory):

        # Checks if the current item's name matches the one the user wants to update
        if item["name"].lower() == item_to_update:

            # Checks if the user chose to edit the "price"
            if price_or_stock == "price":
                price_to_edit = input("Please enter a new price: ")
                item["price"] = price_to_edit
                print(f"New price: {price_to_edit} successfully edited")

            # Checks if the user chose to edit the "stock"
            elif price_or_stock == "stock":
                stock_to_edit = int(input("Please enter a new value: "))
                item["stock"] = stock_to_edit
                print(f"New number of stock: {stock_to_edit} successfully edited")



            # If the option is neither "price" nor "stock"
            else:
                print("Invalid price or number of stock")
            break
        else:
            print("Name not found.")

    write_file(file_name="inventory_sorting.json", data=inventory)



# Function: checks for an existing item
def check_already_exist(item_to_add, inventory):
    for item in inventory:
        if str(item["name"]) == str(item_to_add):
            return True
    return False


def add_item(item_to_add, price_to_add, stock_to_add, inventory):
    if not check_already_exist(item_to_add, inventory):

        # Assign ID based on current length of inventory (so index = id)
        inventory.append({
            "id": len(inventory) + 1,
            "name": item_to_add,
            "price": price_to_add,
            "stock": stock_to_add
        })

        print(f"Added new item: {item_to_add}, with price: {price_to_add}, stock: {stock_to_add}")
        write_file(file_name="inventory_sorting.json", data=inventory)

    else:
        print("Item already exists.")


# Function: deletes an item
def delete_item(item_to_delete, inventory):

    # Creates a new list
    new_inventory = []
    found = False

    # Searches for the "name" provided by the user, if it is not the name provided by the user it adds it to the new_inventory
    for item in inventory:
        if item["name"] != item_to_delete:
            new_inventory.append(item)
        else:
            found = True
            print(f"Contact deleted: {item_to_delete}")

    if found == False:
        print("Name not found.")

    # Returns the updated data with the removed "name"
    return new_inventory

def update_id_index(inventory):
    for ind, item in enumerate(inventory):
        item["id"] = ind + 1

    write_file(file_name="inventory_sorting.json", data=inventory)
