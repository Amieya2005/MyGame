# This is a starter for a text based game in python.
# fill it in and tell a story that would be fun to play

from intro_start import *
from low_rank_monsters import *
# I use multiple modules as an example for you to try and replicate to keep your
# story neat and get used to using them

# Basic control flow is what this file mostly deals with and the end goal is
# to let others use it. Try to make your code so it doesn’t break easily.


def main():
   # end story is the variable I will use to end the program.
   endStory = 2
   # The while loop will keep repeating until the break of set by endStory is
   # triggered
   while(endStory > 1):
       # terminal prints can be over multiple lines using """ print """ format,
       # instead of the regular  "print" give it a try
       print("this is the start of a story, your story. This time you are the one taking control...")
       # this is how your story can take input and read it back out
       userInput = input("What is your name?: ")
       print("Nice to meet you" + userInput + """My name is ___. This may be the first and last time may ever hear from me...
       Or I may be of guidence
       or my not.
       The choice is yours...""")
       # notice input can output to terminal. Look up the input function for python
       # to see why.
       userInput = input("""Now choose from the choices below:
                 option 1: enter a F to end
                 option 2: enter a C to continue
                  """)
       # there are many ways to break this and you should try to write code that
       # catches common cases and check the user for options other than what
       # asked for.
       #EndStory > 1

        # print("Are you Sure?")
         #userInput = input(""" y/n?   """)
     # if (userInput == "y"):
       if userInput :="C" or userInput == "c":
           print("You are a brave one. Well please follow me then ...")
           moduleReturns = newFunction(userInput)
           #moduleReturns = NewFunction(mMonsters)
          # print(moduleReturns)
           print("This is just a demo, thanks you for playing. Goodbye  :)")
           #print("goodbye, rerun python main.py to play")
# This ends the story
           endStory = 0
       elif (userInput := "F" or userInput == "f"):
           print("Goodbye")
         #if (userInput == "n"):
             #print("That is okay, Goodbye...")
# This also ends the story
           #endStory = 0

      #print("the option was case sensitive or you didn't selected from per-determined options")
# Remove this and try to run your code to try and understand what it does so
# if you write a main module and its not working you can tell why.
if __name__ == '__main__':
    main()
