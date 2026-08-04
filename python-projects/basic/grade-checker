"""
grade_checker.py

practicing functions + if/elif/else from module 2.
takes a score and returns a letter grade.

nothing fancy, just wanted to actually write a function
that does something instead of the copy-paste exercises
"""

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# quick test with a few scores
test_scores = [95, 82, 71, 55, 60]

for score in test_scores:
    grade = get_letter_grade(score)
    print(f"Score: {score} -> Grade: {grade}")


# messing around with my own quiz scores from the course lol
my_quiz_scores = {
    "expressions_and_variables": 80,
    "functions": 80,
    "conditionals": 100,
    "while_loops": 80,
    "for_loops": 100,
    "strings": 100,
    "lists": 83,
    "dictionaries": 100
}

print("\n--- my actual course quiz grades ---")
for quiz_name, score in my_quiz_scores.items():
    grade = get_letter_grade(score)
    print(f"{quiz_name}: {score}% ({grade})")
