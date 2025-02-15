def average(student_scores):
    average_list = []

    for student in student_scores:
        try: 
            name = student[0]
            age = student[1]
            scores = student[2]

            if not isinstance(scores, list) or not scores:
                print("Missing scores")
                exit(1)
            else:
                avg_score = sum(scores) / len(scores)

            average_list.append((name, age, avg_score))

        except Exception as e:
            print(f"Error: {e}") 

    sorted_list = sorted(average_list, key=lambda x: x[2], reverse=True)

    print("Top Student:", sorted_list[0])

student_scores = (
    ["Alice", 20, [85, 90, 78]],
    ["Bob", 22, [88, 76, 91]],
    ["Charlie", 19, [92, 85, 87]], 
    ["David", 21, [79, 83, 88]],
    ["Eve", 20, [90, 89, 84]]
)

average(student_scores)
