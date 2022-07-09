def newFunction(option):
    # notice I am passing something and reading whats returned. This can be
    # useful for putting different chapters of your story in modules and having
    # them keep track of how your story is progressing

    # Expand with all types of options here, be creative! pay attention to how
    # different the code looks vs what you see in the terminal. The person you
    # share your game with will not see your code when interacting with it.

    # you can ask things like math questions and make choices on if the user gets
    # it right or not.
    #userInput= input("The user input:")
    #if (userInput == "Y"):
        #print(userInput)

#localUserInput = input("please enter something new")

# add this so it can began the back story
    #print("___" , option)
    localuserInput = input("Are you sure? y/n? ")
    if localuserInput == "y":
            print("""You are a theif and have a skill for pickpoketing.
        This was all until you decided to pickpoket one of the royal princes of ___.
        The prince and the guards caught you and you dragged away to their dungon ...""")

            print(""" This dungon is being at the top of the castle. You weren't chained to the wall like you heard in the rumors or in other countries (kinda dumb if you ask me. I'm just saying.).
        They just threw you in a enclosed room surrounded with nothing but old bricks that had been dying for years and a thick rusty metal bar that has a small vertical opening for the guards to slide mush food
        that had been out for weeks.
        (personally i wouldn't touch that only eat food from my mom <3 and Gordan Ramsay but that's just me).
        All until you saw something in the food that you where able to use to pick the lock (You welcome). You took your oportunity and escaped while they weren't looking...

                Now you are a lone theif in the night sneaking around the castle looking for an escape...


            Dont Get Caught.
            Get as many gems and Jewls as you can.
            But what ever you do don't die.
            .......

            Good luck, See you on the other side!


            """ )

    elif localuserInput == "n":
        print("ok...")


    return localuserInput

#import random
# this is so you can roll the dice 1-20 sided and get the chocies

    #print(")
