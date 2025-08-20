from CRUD_Functions.util import display_whole_inventory, display_item_by_name, update_item, add_item, delete_item, update_id_index
from File_Handling.util import write_file, read_file

inventory = read_file(file_name="inventory_sorting.json")
write_file(file_name="inventory_sorting.json", data=inventory)

if __name__ == "__main__":

    print("Welcome to Inventory Sorting")
# Loop is used in order for the program to not close, unless the user wants to
    while True:
        print("What would you like to do: ")
        choice_lst = [
            "1. Dispaly full inventory",
            "2. Search for items in inventory by name",
            "3. Update product",
            "4. Add new product",
            "5. Del product",
            "6. Exit application"
        ]

        # Loops through the option and prints them in line
        for ind, val in enumerate(choice_lst):
            print(val)
        number_choice = int(input("Please enter a number for what you would like to do: "))
        print("\n")

        # Displays whole inventory
        if number_choice == 1:

            display_whole_inventory(inventory)

            # Asks the user if he would like to continue using the app
            inp_do_something_else = input(
                "Would you like to do something else: yes/no: "
            ).lower()
            print("\n")

            # If the user says "no" the app closes automatically
            if inp_do_something_else == "no":
                break

            # Checks whether the input is in the desired value "Yes / No", if not then closes automatically
            elif inp_do_something_else != "yes" and inp_do_something_else != "no":
                print("Invalid input. App will close automatically.")
                break

        # Searches the inventory by name
        elif number_choice == 2:

            item_to_display = input(
                "Enter the name of the contact you would like to display: "
            ).lower()

            display_item_by_name(item_to_display, inventory)

            # Asks the user if he would like to continue using the app
            inp_do_something_else = input(
                "Would you like to do something else: yes/no: "
            ).lower()
            print("\n")

            # If the user says "no" the app closes automatically
            if inp_do_something_else == "no":
                break

            # Checks whether the input is in the desired value "Yes / No", if not then closes automatically
            elif inp_do_something_else != "yes" and inp_do_something_else != "no":
                print("Invalid input. App will close automatically.")
                break

        # Updates existing item
        elif number_choice == 3:

            item_to_update = input(
                "Enter the name of the item you would like to edit: "
            ).lower()

            price_or_stock = input(
                "Would you like to change the price or the stock: "
            ).lower()

            update_item(item_to_update, inventory, price_or_stock)

            # Asks the user if he would like to continue using the app
            inp_do_something_else = input(
                "Would you like to do something else: yes/no: "
            ).lower()
            print("\n")

            # If the user says "no" the app closes automatically
            if inp_do_something_else == "no":
                break
            # Checks whether the input is in the desired value "Yes / No", if not then closes automatically
            elif inp_do_something_else != "yes" and inp_do_something_else != "no":
                print("Invalid input. App will close automatically.")
                break


        # Adds a new product
        elif number_choice == 4:
            item_to_add = input("Enter a name: ").lower()
            price_to_add = input("Enter a price: ")
            stock_to_add = input("Enter a value: ")

            add_item(item_to_add, price_to_add, stock_to_add, inventory)

            # Asks the user if he would like to continue using the app
            inp_do_something_else = input(
                "Would you like to do something else: yes/no: "
            ).lower()
            print("\n")

            # If the user says "no" the app closes automatically
            if inp_do_something_else == "no":
                break
            # Checks whether the input is in the desired value "Yes / No", if not then closes automatically
            elif inp_do_something_else != "yes" and inp_do_something_else != "no":
                print("Invalid input. App will close automatically.")
                break



        # Deletes an item
        elif number_choice == 5:
            item_to_delete = input("Enter the name of the item you want to delete: ")

            inventory = delete_item(item_to_delete, inventory)
            write_file(file_name="inventory_sorting.json", data=inventory)
            update_id_index(inventory)

            # Asks the user if he would like to continue using the app
            inp_do_something_else = input(
                "Would you like to do something else: yes/no: "
            ).lower()
            print("\n")

            # If the user says "no" the app closes automatically
            if inp_do_something_else == "no":
                break
            # Checks whether the input is in the desired value "Yes / No", if not then closes automatically
            elif inp_do_something_else != "yes" and inp_do_something_else != "no":
                print("Invalid input. App will close automatically.")
                break


        elif number_choice == 6:
            break
