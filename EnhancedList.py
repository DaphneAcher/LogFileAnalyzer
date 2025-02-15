from collections import Counter

def operations():
    try:
        input_numbers = input("Input the list of integers here (comma-separated): ")
        input_numbers = [int(num) for num in input_numbers.split(",")]

        #addition
        addition = sum(input_numbers)
        #product
        product = 1
        for n in input_numbers:
            product *= n
        #median
        median = addition/len(input_numbers)
        #mode
        count = Counter(input_numbers)
        max_freq = max(count.values())
        mode = [num for num, frq in count.items() if frq == max_freq]


        print(f"Sum: {addition}")
        print(f"Product: {product}")
        print(f"Median: {median}")
        print(f"Mode: {mode}")

    except ValueError:
        print(f"Invalid input. Please enter valid list")
        operations() #reprompts user

operations()