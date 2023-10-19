from pymongo import MongoClient

# Function to browse records
def browse_records(collection):
    for game in collection.find():
        print(game)

# Function to add a new record
def add_record(collection):
    new_game = {
        "Platform": input("Enter Platform: "),
        "Title": input("Enter Title: "),
        "Genre": input("Enter Genre: "),
        "Release Year": input("Enter Release Year: ")
    }
    collection.insert_one(new_game)
    print("Record added successfully!")

# Function to remove a record
def remove_record(collection):
    title_to_remove = input("Enter the Title of the game to remove: ")
    filter_criteria = {"Title": title_to_remove}
    result = collection.delete_one(filter_criteria)
    if result.deleted_count > 0:
        print(f"Record '{title_to_remove}' removed successfully!")
    else:
        print(f"No record found with the title '{title_to_remove}'.")

# Main function
def main():
    client = MongoClient('localhost', 27017)
    db = client['PS3Games']
    collection = db['Games']

    while True:
        print("\nMenu:")
        print("1. Browse Records")
        print("2. Add Record")
        print("3. Remove Record")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            browse_records(collection)
        elif choice == "2":
            add_record(collection)
        elif choice == "3":
            remove_record(collection)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

    client.close()

if __name__ == "__main__":
    main()
