            # 2nd project

        # Student's report card

print('What is your name and  Roll no.?')
name = input('Name = ')
Roll_no = input('Roll no. = ')
print('\n')

print('English F.M = 100')
while True:
    english_marks = input('Obtained marks = ')
    my_english_marks = int(english_marks)
    if my_english_marks > 100:
        continue
    if my_english_marks <= 100:
        break
    if my_english_marks >= 40:
        print('Pass')
else:
    print('Fail')
print('\n')

print('Hindi F.M = 100')
while True:
    hindi_marks = input('Obtained marks = ')
    my_hindi_marks = int(hindi_marks)
    if my_hindi_marks > 100:
        continue
    if my_hindi_marks <= 100:
        break
    if my_hindi_marks >= 40:
        print('Pass')
    else:
        print('Fail')
print('\n')

print('Math F.M. = 100')
while True:
    math_marks = input('Obtained marks = ')
    my_math_marks = int(math_marks)
    if my_math_marks > 100:
        continue
    if my_math_marks <= 100:
        break
    if my_math_marks >= 40:
        print('Pass')
    else:
        print('Fail')
print('\n')


print('Physics Theory F.M. = 70')
while True:
    physics_theory = input('Obtained marks = ')
    physics_theory_marks = int(physics_theory)
    if physics_theory_marks > 70:
        continue
    if physics_theory_marks <= 70:
        break
print('P_Practical F.M. = 30')
while True:
    p_practical = input('P_Practical marks = ')
    p_practical_marks = int(p_practical)
    if p_practical_marks > 30:
        continue
    if p_practical_marks <= 30:
        break
my_physics_marks = physics_theory_marks + p_practical_marks 
if my_physics_marks >= 40:
    print('Pass')
else:
    print('Fail')
print('\n')

print('Chemistry Theory F.M. = 70')
while True:
    chemistry_theory = input('Obtained marks = ')
    chemistry_theory_marks = int(chemistry_theory)
    if chemistry_theory_marks > 70:
        continue
    if chemistry_theory_marks <= 70:
        break
print('C_parctical F.M. = 30')
while True:
    c_practical = input('C_Practical marks = ')
    c_practical_marks = int(c_practical)
    if c_practical_marks > 30:
        continue
    if c_practical_marks <= 30:
        break
my_chemistry_marks = chemistry_theory_marks + c_practical_marks
if my_chemistry_marks >= 40:
    print('Pass')
else:
    print('Fail')
print('\n')

print('Full marks = 500')
print('Passing marks = 150')
print('\n')

Obtained_marks =  my_english_marks + my_hindi_marks + my_math_marks + my_physics_marks + my_chemistry_marks
print('Total_Obtained_marks =',Obtained_marks)

if Obtained_marks >= (700 <= 300):
    print('1st Division')
elif Obtained_marks == (299 <= 225):
    print('2nd Division')
elif Obtained_marks == (224 <= 150):
    print('3rd Division')
else:
    print('Fail')









