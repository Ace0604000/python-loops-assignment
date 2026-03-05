# Name: Harish R
# Assignment: Python Functions & Modularity

# Task 1 — Process Scores
def process_scores(students):
    averages = {}

    for name, scores in students.items():
        total = 0
        count = 0

        for s in scores:
            total += s
            count += 1

        avg = round(total / count, 2)
        averages[name] = avg

    return averages


# Task 2 — Classify Grades
def classify_grades(averages):

    A_grade = 90
    B_grade = 75
    C_grade = 60

    classified = {}

    for name, avg in averages.items():

        if avg >= A_grade:
            grade = "A"
        elif avg >= B_grade:
            grade = "B"
        elif avg >= C_grade:
            grade = "C"
        else:
            grade = "F"

        classified[name] = (avg, grade)

    return classified


# Task 3 — Generate Report
def generate_report(classified, passing_avg=70):

    print("===== Student Grade Report =====")

    passed = 0
    failed = 0

    for name, data in classified.items():

        avg, grade = data

        if avg >= passing_avg:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"
            failed += 1

        print(f"{name:<10} | Avg: {avg:.2f} | Grade: {grade} | Status: {status}")

    print("================================")
    print("Total Students :", len(classified))
    print("Passed         :", passed)
    print("Failed         :", failed)

    return passed


# Main Program
if __name__ == "__main__":

    students = {
        "Alice": [85, 90, 84],
        "Bob": [60, 65, 62],
        "Clara": [95, 97, 97]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)