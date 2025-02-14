from collections import defaultdict

input_file = "error.txt"

error_dict = defaultdict(int)

try:
    input_file = open(input_file, 'r')
    for line in input_file:
                if "ERROR " in line:
                    error_message = line.split("ERROR ", 1)[1].strip()
                    error_dict[error_message] += 1
                    
    def get_count(item):
        return item[1]

    sorted_errors = sorted(error_dict.items(), key=get_count, reverse=True)

    print("\nTop 3 most frequent error messages:")
    for i in range(min(3, len(sorted_errors))):
        message, count = sorted_errors[i]
        print(f"{i+1}. {message} - {count} occurrences")

except FileNotFoundError:
    print("This files doesn't exist")


input_file.close()