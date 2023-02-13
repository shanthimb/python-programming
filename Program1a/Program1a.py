if __name__ == "__main__":
    # Input the marks for three test marks
    marks1 = int(input("Enter test-1 marks: "))
    marks2 = int(input("Enter test-2 marks:"))
    marks3 = int(input("Enter test-3 marks: "))

    # Find the minimum among three
    minimum = min(marks1, marks2, marks3)
    sum_of_best_two = marks1 + marks2 + marks3 - minimum
    avg_best_two = sum_of_best_two / 2
    print("The average of best two tests:  ", avg_best_two)
