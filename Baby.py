# ================= Compulsory Task ==================
# Create a Python file called “baby.py” in this folder.
# This program will be used to test if the user is over 18 and allowed entry into a party. 
# Ask the user to enter the year they were born and calculate if they are older than 18.
# If they are older then display a message saying “Congrats you are old enough”

age = int(input("Please enter the year you were born: "))
if age <= 2000:
    print ("Congrats you are old enough.")

else:
    print ("Unfortunately you are not old enough!")
