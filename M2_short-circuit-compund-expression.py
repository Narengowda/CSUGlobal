"""
Short circuiting is a tricky way of evaluating logical operations involving "and" & "or",
where evaluation stops as soon as the result is determined.
This is very useful in compound conditional expressions, where unnecessary evaluations can
be reduced, increasing the efficiency.
Incase of the and operator, if the first operand is False, Python does not evaluate the
further operands with "and" because the whole expression cannot be True.
simillarly, for the or operator, if the first operand is True, it skips the second and any
other operands with "or" operand because the whole expression is already True.

Here is the example:
a = 1
b = 2
c = 3

result = a < b and a > c and a < d
Here, while evaluating a>c since a is not greater than c, python skips the remaining evaluation
hence "result" will will be false


a = 1
b = 2
c = 3
d = 4

result = a > b or a < c or a > d
 Here, while evaluating a < c since a is less than c, python skips the remaining evaluation
 hence "result" will be true
"""

# Real world example to decide Student's result, when minimum passing marks is 35 out of 100

# scores
physics = 28
Chemistry = 59
history = 100
mathematics = 100
astronomy = 100

is_student_pass = physics>35 and Chemistry > 35 and history >35 and mathematics>35 and astronomy>35
print("is_student_pass = ", is_student_pass) # since student failed in physis there is no point in continuing evaluation

is_sudent_failed = physics<35 or Chemistry < 35 or history < 35 or mathematics < 35 or astronomy < 35
print("is_sudent_failed = ", is_sudent_failed) # since student failed in Physis there is no point in continuing evaluation




