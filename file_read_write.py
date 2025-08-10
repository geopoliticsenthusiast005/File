# file_read_write.py

def read_and_modify_file():
    # Ask user for the file name
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # Modify the content (Example: convert to uppercase)
        modified_content = content.upper()

        # Create a new file to store modified content
        new_filename = "modified_" + filename
        with open(new_filename, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        print(f"File successfully modified and saved as '{new_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_modify_file()
