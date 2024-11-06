#this is a word guessing game project
# randomly choose a word
#greet user
#let him know he has limited attempts

#create a varlist with random objects
import random

attempt=1
wordlist=['hello','world','goat','snake','grass','glass','book','toddler']
guess_word=random.choice(wordlist)
guess_word_length=len(guess_word)

#interact with user
print("Welcome to the guessing game")
print("you have 7  attempts")

user_display="-"*guess_word_length
print(user_display)

while attempt<=7:
 attempt = attempt + 1
 user_input=input("enter your guess letter").lower()

 first_index=guess_word.find(user_input)
 occurances=guess_word.count(user_input)
 temp_list = list(user_display)

 if(first_index>=0):
     if(occurances>1):
        for i in range(0,guess_word_length):
             if guess_word[i] ==user_input:
                 temp_list[i]=user_input
        user_display="".join(temp_list)

     else:
        #temp_index = guess_word.index(user_input)
        temp_list[first_index]=user_input
        user_display="".join(temp_list)
 else:
     print('letter does not exist, try again')
 print(user_display)

 if(guess_word==user_display):
  print("you won")
  attempt=10

if(guess_word!=user_display):

    print(f"Your Attempts are over ,the guess word is {guess_word}, Game Over ")


