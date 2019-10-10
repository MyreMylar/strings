# ---------------------------------------------------------------------------------------
# What is a string?
# -----------------
#
# It is a type of data in programming that
# stores a sequence of letters, numbers and symbols. They are usually used
# for putting words, sentences and blocks of text on the screen.
#
# Why is it called a string?
# ---------------------------
# Probably because in the old days of printing presses they used to charge by the letter
# printed and they would add the letters to be printed to an actual string so they could
# quickly estimate the cost and easily transport the letters.
# ---------------------------------------------------------------------------------------

my_string = "hey, I'm a string. a bunch of numbers: 12345 and some symbols: &%()!?[]:   "
print(my_string)

# --------------------------------------------------------------------------------
# Below I demonstrate some of the string functions available in python
# There are many more that you can find by adding a '.' after any string and
# scrolling through the auto complete options that come up
#
# --------------------------------------------------------------------------------
# Have a look at the code below and the output in the console when the code is run.
# When you've done that, scroll down to line 57 for challenge 1!
# --------------------------------------------------------------------------------


if 'hey' in my_string:
    print("found hey in my_string!")

number_of_as = my_string.count('a')
print("number of 'a's: " + str(number_of_as))

my_string = my_string.capitalize()
print(my_string)

my_string = my_string.upper()
print(my_string)

my_string = my_string.lower()
print(my_string)

position_of_bunch = my_string.find('bunch')
print("position of bunch in my_string: " + str(position_of_bunch))

digit_string = "5678"
is_digit = digit_string.isdigit()
print("does digit_string contain only numbers: " + str(is_digit))

text_to_centre = "centered text"
text_to_centre = text_to_centre.center(32, '.')
print(text_to_centre + "\n\n")

# ---------------------------------------------------------------------------------
# CHALLENGE 1
# ------------
#
# Add the text "- defeated!" onto the end of the challenge_string variable below
# without editing the original text and then print it a second time to the console.
#
# -----------------------------
# Challenge 2 is on line 70!
# ---------------------------------------------------------------------------------
challenge_string = "Challenge 1"
print(challenge_string)


# ---------------------------------------------------------------------------------
# CHALLENGE 2
# ------------
#
# A) Replace the text 'UNRESOLVED' in the challenge_string_2 with RESOLVED without
# changing the original string, then print it a second time to the console.
#
# B) Convert the whole string to lower case then print it a third time to the console.
#
# C) Use a for loop to print each letter of the string to the console one at a time.
#
# Tips
# -----
#
# - strings have a default replace function.
# - you can mostly treat strings just like python lists.
# ----------------------------
# Challenge 3 is on line 94
# ---------------------------------------------------------------------------------
challenge_string_2 = "STATUS: UNRESOLVED - CHALLENGE 2"
print(challenge_string_2)


# ---------------------------------------------------------------------------------
# CHALLENGE 3
# ------------
#
# Split challenge_string_3 into a list of words. Loop through the word list and
# convert each word to lower case, add an exclamation mark '!' to the end of the
# word. Finally create a new empty string variable with just a space in it and use
# the join function to add all the words in the word list to it. Print the resulting
# string to the console.
#
# Tips
# -----
#
# - strings have a default split method. You need to specify what character to split
#   the string up with. a space ' ' counts as a character.
# - the join function uses the contents of the initial string as the 'separator'
#   between the things in the list to be joined. If we started with a comma instead
#   of a space all the words would have a comma between them.
# ---------------------------------------------------------------------------------
challenge_string_3 = "Challenge Three dog CAT owl"
print(challenge_string_3)
