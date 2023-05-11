# שאלון אבטחה לפני כניסה למתקן מאובטח

# חלק ראשון - פרטים אישיים
print("Welcome to the secured facility. Please fill in the following details:")
name = input("Full name: ")
id_number = input("ID number: ")
phone_number = input("Phone number: ")
email = input("Email address: ")
address = input("Home address: ")

print("Thank you, your details have been saved in the system.")

# חלק שני - שמירת סודיות לפי תקן צבאים ישראלי
print("Now, a few short questions about confidentiality according to Israeli army standards:")
answer1 = input("Will you copy confidential information to an unsecured device? (Yes/No) ")
answer2 = input("Will you publish confidential information on social networks? (Yes/No) ")
answer3 = input("Will you give anyone access to your device that contains confidential information? (Yes/No) ")

print("Thank you, your answers have been saved in the system.")

# חלק שלישי - בטיחות במתקן מפעל חומרים מסוכנים
print("Now, a few short questions about safety in a hazardous materials facility:")
answer4 = input("What are the minimum conditions for entering the facility? ")
answer5 = input("What are the guidelines for handling personal equipment in the hazardous materials facility? ")
answer6 = input("What are the guidelines for handling hazardous materials and injuries to the workers in the facility? ")
safety_questions = [answer4, answer5, answer6]
if safety_questions.count("Correct") >= 4:
   print("Thank you for answering the questions about safety in a hazardous materials facility. The data has been saved in the system.")
else:
   print("Unfortunately, you did not pass the required safety check for a hazardous materials facility. Please contact the facility manager for more information.")

# חלק רביעי - שמירת נתונים וסיום השאלון

print("Thank you for completing the questionnaire.")
with open("security_survey.txt", "a") as file:
  file.write(f"Personal information:\n{answer1}\n{answer2}\n{answer3}\n")
  file.write(f"Confidentiality:\n{safety_questions[0]}\n{safety_questions[1]}\n{safety_questions[2]}\n")
  file.write(f"Safety:\n{answer4}\n{answer5}\n{answer6}\n")
  file.write("-------------------------\n")


# The project works well, but I want to improve more in the coming days

