"""
grade_checker.py

practicing functions + if/elif/else from module 2.
takes a score and tells you the letter grade.

now actually asks for input instead of just using
a hardcoded list, so you can actually try it
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


# my actual quiz scores from the course, just kept this in
# cause i thought it was a funny way to test the function
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

print("--- my actual course quiz grades ---")
for quiz_name in my_quiz_scores:
    score = my_quiz_scores[quiz_name]
    grade = get_letter_grade(score)
    print(quiz_name + ": " + str(score) + "% (" + grade + ")")

print("")

# now let the user try their own score
user_input = input("Enter a score (0-100) to check your own grade: ")
score = int(user_input)
grade = get_letter_grade(score)
print("Your score: " + str(score) + " -> Grade: " + grade)
