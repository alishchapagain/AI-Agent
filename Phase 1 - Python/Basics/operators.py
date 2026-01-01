'''
Types of operators in python:
> Arithmetic
> Assignment
> Comparison
> Logical
> Membership
> Identity
> Bitwise
'''

age = 18
has_id = True
score = 75

# Arithmetic operators
total_score = score + 5
average_score = total_score / 2

# Comparison operators
is_adult = age >= 18
is_pass = score >= 40

# Logical operators
eligible_for_exam = is_adult and has_id and is_pass

# Membership operator
allowed_scores = [40, 50, 60, 70, 80, 90]
score_valid = score in allowed_scores

# Identity operator
x = None
y = None
same_reference = x is y

print("Total Score:", total_score)
print("Average Score:", average_score)
print("Is Adult:", is_adult)
print("Eligible for Exam:", eligible_for_exam)
print("Score is valid:", score_valid)
print("x and y refer to same object:", same_reference)
