#To ask for age and print if they can drive/not drive or need physical presence to decide.

print("What is your age?")
var = int(input())

if 18<var<100:
    print("You can drive")
elif var==18:
    print("Your physical presence is required for us to decide if you can drive or not")
elif 18>var>0:
    print("Sorry kid, you can not drive")
else:
    print("Please enter propper age limit")