              # A small conversation




# This program say me Hello! and ask my name.

print('Hello Gentleman / Gentlewoman')
print('What is your name?') # It ask name

my_name = input()

print("\n")
print('oh!')

print('Nice to meet you' , my_name)

print('The length of your name is:')
print(len(my_name))
print("\n")

print("What is you gender?")
my_gender = input()

if my_gender == "male":
    print("How are you, Sir?")# Ask the condition
elif my_gender == "Female":
     print("How are you, mam?")
elif my_gender == "Transgender":
     print("How are you?")
else:
    print("What are typing?, Tell me your gender")
my_condition = input()
if my_condition == "Good":
    print("Nice to hear!")
elif my_condition == "Fine":
    print('I am happy to hear')
elif my_condition == "Happy": 
        print("I am also happy to hear")       
else:
    print("Hope you feel better soon")

print("Okay!")

print('What is your age?') # Ask the namage

my_age = input()
print('very good')
print(' SO, you will be ' + str(int(my_age) +1) +' in your next birthday')
print('nice')

print('What is your occupation?') # Ask the occupation
my_occupation = input()
print('Oh!, So you are a ' + my_occupation + ' now')

print("What is your father's name?") # Ask the father's name
myfathernmae = input()

print('Oh! What does he do?') # Ask father's occupation
father_occupation = input()
print('\n')

print("What is your mother's name?")
mother_name = input()

print("What does she do?")
mother_ocuppation = input()
print('\n')

print("Where do you live?")
I_live = input()
print('\n')

print("What do you want to achieve in your life?")
my_achievement = input()
print('\n')

print("Thank you so much, I am so happy to talk to you", my_name)