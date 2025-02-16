import os

def create_text_files():
    num_files = int(input("Enter the number of text files to create: "))
    
    for i in range(num_files):
        filename = input(f"Enter the name for file {i+1} (e.g., file{i+1}.txt): ")
        content = input(f"Enter the content for {filename}: ")
        try: 
            with open(filename, "w") as file:
                file.write(content)
        except PermissionError:
            print(f"Error: Permission denied while accessing '{file}'.")
        except Exception:
            print(f"Error reading {file}")

def get_user_inputs():
    directory = input("Enter the directory path where the text files are located: ")

    #If directory is empty, choose current directory
    if not directory:
        directory = os.getcwd()  #Get current directory

    search_string = input("Enter the search string: ")
    replace_string = input("Enter the replacement string: ")
    return directory, search_string, replace_string


def search(directory, search_string, replace_string):
    search_files = [i for i in os.listdir(directory) if i.endswith(".txt")]
    for file in search_files:
        file_path = os.path.join(directory, file)
        try:
            with open(file_path, "r") as f:
                content = f.read()
            
            occurrences = content.count(search_string)
            
            if occurrences > 0:
                print(f"{search_string} found {occurrences} times in {file}")
                changes = content.replace(search_string,replace_string)

                print(f"Replaced {occurrences} occurrences in {file}.\n")

        except FileNotFoundError:
            print(f"Error: File '{file}' was not found")
        except PermissionError:
            print(f"Error: Permission denied while accessing '{file}'.")
        except Exception:
            print(f"Error reading {file}")


create_text_files()
directory, search_string, replace_string = get_user_inputs()
search(directory, search_string, replace_string)