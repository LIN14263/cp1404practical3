"""
CP1404/CP5632 Practical 04 - Subject Reader
Reads subject data from subject_data.txt
Each line format: subject_code, lecturer_name, number_of_students
"""

FILENAME = "subject_data.txt"

def main():
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)

def load_subjects(filename):
    """Return a list of tuples: (code:str, lecturer:str, students:int)."""
    subjects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            if len(parts) != 3:
                # Skip malformed lines safely
                continue
            code, lecturer, students_text = parts
            try:
                students = int(students_text)
            except ValueError:
                # Skip if student count is not an integer
                continue
            subjects.append((code, lecturer, students))
    return subjects

def display_subjects(subjects):
    for code, lecturer, students in subjects:
        # Example output: CP1401, Lecturer Name, 100 students
        print(f"{code} is taught by {lecturer:12} and has {students:3} students")

if __name__ == "__main__":
    main()
