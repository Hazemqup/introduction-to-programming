def main():
    input_file = C:\Users\hhhaz\Documents
    output_file = C:\Users\hhhaz\Documents

    student = {}

    with open(input_file, 'r') as file:
        for line in file:
            name, unit, mark, weight = line.strip().split(',')
            mark, weight = float(mark), float(weight)
            if name not in student:
                student[name].append(mark, weight))

    with open(output_file, 'w') as file:
        for name, marks_weights in student.items():
            total_marks = sum(mark * (weight / 100) for mark,weight in marks_weight)
            if total_marks >=70:
                grade = "Distinction"
            elif total_marks >= 60:
                grade = "Merit"
            elif total_marks >= 50:
                grade = "Pass"
            else:
                grade = "Fail"
            file.write(f"{name}, {total_mark:.1f}, {grade}\n")


    __name__=="__main__":
        main()
