def bubbleSort(arrays: list) -> None:
    for i in range(len(arrays)):
        for j in range(0, len(arrays) - i - 1):
            if arrays[j] > arrays[j + 1]:
                arrays[j], arrays[j + 1] = arrays[j + 1], arrays[j]

def main():
    marks = []
    n = int(input("Enter the number of students: "))
    for i in range(n):
        marks.append(int(input("Enter the marks of student {}: ".format(i+1))))
    
    bubbleSort(marks)
    print(marks)

main()