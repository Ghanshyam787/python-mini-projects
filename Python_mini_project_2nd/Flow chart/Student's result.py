            # 2nd project

        # Student's report card

print('What is your name and  Roll no.?')
name = input('Name = ')
Roll_no = input('Roll no. = ')
    
print('\n')

print('English F.M = 100')
while True:

    English_marks = int(input('Obtained marks = '))
    if 0 <= English_marks <= 100:
        break       
    else:
        print("Invalid marks! Enter again.")

if English_marks >= 40:
        print('English Pass')
else:
        print('English Fail')
print('\n')

print('Hindi F.M = 100')
while True:
    Hindi_marks = int(input('Obtained marks = '))
    if 0 <= Hindi_marks <= 100:
        break
    else:
        print("Invalid marks!, Enter again")
   
if Hindi_marks >= 40:
        print('Pass')
else:
        print('Fail')
print('\n')

print('Math F.M. = 100')
while True:
    Math_marks = int(input('Obtained marks = '))
    if 0 <= Math_marks <= 100:
        break
    else:
        print("Invalid marks!, Enter again")
   
if Math_marks >= 40:
        print('Pass')
else:
        print('Fail')
print('\n')


print('Physics Theory F.M. = 70')
while True:
    Physics_theory = int(input('Obtained marks = '))
    if 0 <= Physics_theory <= 70:
        break
    else:
        print("Invalid marks!, Enter again")
print('P_Practical F.M. = 30')
while True:
    P_Practical = int(input('P_Practical marks = '))
    if 0 <= P_Practical <= 30:
        break
    else:
        print("Invalid marks!, Enter again")
Physics_marks = Physics_theory + P_Practical
if Physics_marks >= 40:
    print('Pass')
else:
    print('Fail')
print('\n')

print('Chemistry Theory F.M. = 70')
while True:
    Chemistry_Theory = int(input("Chemistry Theory = "))
    if 0 <= Chemistry_Theory <= 70:
        break
    else:
        print("Invalid marks!, Enter again")
print('C_Practical F.M. = 30')
while True:
    C_Practical = int(input('C_Practical = '))
    if 0 <= C_Practical <= 30:
        break
    else:
        print("Invalid marks!, Enter again")
Chemistry_marks = Chemistry_Theory + C_Practical
if Chemistry_marks >= 40:
    print('Pass')
else:
    print('Fail')
print('\n')

print('Full marks = 500')
print('Passing marks = 150')
print('\n')
Full_marks = 500
Obtained_marks =  English_marks + Hindi_marks + Math_marks + Physics_marks + Chemistry_marks
print('Total_Obtained_marks =',Obtained_marks)
Percentage = (Obtained_marks / Full_marks) * 100
print("Percentage =", Percentage, "%")
print('\n')
if 300 <=Obtained_marks <= 700:
    print('1st Division')
elif 225<= Obtained_marks <= 299:
    print('2nd Division')
elif 150<= Obtained_marks <= 224:
    print('3rd Division')
else:
    print('Fail')
