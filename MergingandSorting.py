def merge_and_sort_files(file1, file2, output_file):
    try:
        # Open input files
        f1 = open(file1, 'r')
        f2 = open(file2, 'r')

        # Read numbers and convert them to integers
        numbers = []
        for line in f1:
            numbers.append(int(line.strip()))
        for line in f2:
            numbers.append(int(line.strip()))

        # Close input files
        f1.close()
        f2.close()

        # Sort the numbers
        numbers.sort()

        # Open output file and write sorted numbers
        f_out = open(output_file, 'w')
        for num in numbers:
            f_out.write(f"{num}\n")
        f_out.close()

        print(f"Sorted numbers saved to {output_file}")

    except FileNotFoundError:
        print("One or both input files do not exist.")
    except ValueError:
        print("Ensure all lines in the input files contain valid integers.")
    finally:
        # Ensure files are closed even if an error occurs
        try:
            f1.close()
            f2.close()
            f_out.close()
        except NameError:
            pass  # Ignore if files were never opened

# File names
input_file1 = "file1.txt"
input_file2 = "file2.txt"
output_file = "merged_sorted.txt"

# Call the function
merge_and_sort_files(input_file1, input_file2, output_file)