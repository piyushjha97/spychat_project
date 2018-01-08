from spy_details import spy_name, spy_salutation, spy_age, spy_rating, spy_is_online

STATUS_MESSAGE = ['my name is Bond,James Bond', 'Happy New Year',  'Always Smile,It costs nothing']

friend_name = []
friend_age = []
friend_rating = []
friend_is_online = []

print "Let\'s get started"

question = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N)?"
existing = raw_input(question)

# defining status function


def add_status(current_status_message):
    updated_status_message = None

    if current_status_message != None:

        print "Your current status is  %s \n" % current_status_message
    else:
        print "You don\'t have any status. \n"

    default = raw_input("Do you want to print from older status(y/n)??")

    if default.upper() == "N":
        new_status_message = raw_input("What status do you wanna set?")

        if len(new_status_message) > 0:
            STATUS_MESSAGE.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == "Y":

        # Use of for loop for choosing and updating status message

        position = 1

        for message in STATUS_MESSAGE:

            print "%d. %s" % (position, message)
            position = position + 1

        message_selection = input("\n Choose from above messages.")

        if len(STATUS_MESSAGE) >= message_selection:
            updated_status_message = STATUS_MESSAGE[message_selection-1]

    else:
        print " You chose an invalid option!!!!Press either y or n."

    if updated_status_message:
        print 'Your updated status message is: %s' % updated_status_message
    else:
        print 'You did not update your status message'

    return updated_status_message


# defining another function for adding friend:


def add_friend():

    new_name = raw_input("what \'s your friend\'s name?")

    new_age = raw_input("what\'s is age?")

    new_rating = raw_input("what is his/her rating")

    if len(new_name) > 0 and new_age > 15 and new_rating >= spy_rating:

        friend_name.append(new_name)
        friend_age.append(new_age)
        friend_rating.append(new_rating)
        friend_is_online.append(True)

        print "A friend is added."

    else:
        print "Invalid Entry!!"

    return len(friend_name)

# defining a chat function


def start_chat(spy_name, spy_age, spy_rating):

    current_status_message = None
    spy_name = spy_salutation + " " + spy_name
    if spy_age > 12 and spy_age < 50:

        print "Authentication complete.Welcome " + spy_name + " " + str(spy_age) + " " + "and rating of: " + " " + str(
            spy_rating) + " " + "Proud to have you on board."

        show_menu = True

        while show_menu:

            menu_choices = "What do you wanna do? \n1. Add a status \n2. Add a friend \n3. Close Application \n"
            menu_choice = input(menu_choices)

            if menu_choice == 1:
                current_status_message = add_status(current_status_message)
            elif menu_choice == 2:
                number_of_friends = add_friend()
                print 'You have %d friends' % (number_of_friends)
            elif menu_choice == 3:
                show_menu = False
    else:
        print " You are not of correct age to be a spy. "

# function ends here!!


if existing.upper() == "Y":

    start_chat(spy_name, spy_age, spy_rating)
else:
    spy_salutation = ""

    spy_name = ""

    spy_age = 0

    spy_rating = 0.0

    spy_is_online = False

    spy_name = raw_input("what is your name?")

    if len(spy_name) > 0:

        spy_salutation = raw_input("would you like to be called Mr. or Ms. ?")

        spy_age = input("Please enter your age")

        spy_rating = input("what is your rating?")

        spy_is_online = True

        start_chat(spy_name, spy_age, spy_rating)
    else:
        print "A spy needs to have a valid name so please input the spy name"
