import os

def create_text_files():
    num_files = int(input("Enter the number of text files to create: "))
    
    for i in range(num_files):
        filename = input(f"Enter the name for file {i+1} (e.g., file{i+1}.txt): ")
        content = input(f"Enter the content for {filename}: ")

        with open(filename, "w") as file:
            file.write(content)
        print(f"{filename} created successfully!")

create_text_files()

def get_user_inputs():
    directory = input("Enter the directory path where the text files are located: ")
    search_string = input("Enter the search string: ")
    return directory, search_string

directory, search_string = get_user_inputs()
print(f"Searching for '{search_string}' in directory: {directory}")
