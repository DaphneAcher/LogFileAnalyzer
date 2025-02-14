def merge_and_sort_files(file1, file2, output_file):
    try:
        f1 = open(file1, 'r')
        f2 = open(file2, 'r')

        numbers = []
        for line in f1:
            numbers.append(int(line.strip()))
        for line in f2:
            numbers.append(int(line.strip()))

        f1.close()
        f2.close()

        numbers.sort()

        f_out = open(output_file, 'w')
        for num in numbers:
            f_out.write(f"{num}\n")
        f_out.close()

    except FileNotFoundError:
        print("One or both input files do not exist.")
    except ValueError:
        print("Ensure all lines in the input files contain valid integers.")

input_file1 = "file1.txt"
input_file2 = "file2.txt"
output_file = "merged_sorted.txt"

merge_and_sort_files(input_file1, input_file2, output_file)