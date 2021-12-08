# Store the value of famous person in variable for reference in the string in the next section
famous_person = 'Monkey D. Luffy'
# Created message variable and the in its value I reference the previous variable using f-strings f-strings allows
# placing variables within strings and the interpreter will replace those variables with its values. For f-strings to
# work, you need to add "f" (without quotes) before entering your string, In curly braces within your string that's
# where you place your variable and the interpreter will place the value of your variable within your string
message = f"{famous_person}, \"If you don’t take risks, you can’t create a future.\""
# Prints message using the print function and within the parenthesis add the variable.
print(message)
