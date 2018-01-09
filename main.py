from spy_details import spy
STATUS_MESSAGE = [' ACADVIEW IS AWESOME', ' EAT, SLEEP, CODE, REPEAT',  'ALWAYS SMILE, IT COSTS NOTHING']

friends = []

print "Let\'s get started"

question = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N)?"
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
    new_friend ={
       'name': '',
       'salutation':'',
       'age':0,
       'rating':0.0
       }
    new_friend['name'] = raw_input('enter your friend\'s name: ')
    new_friend['salutation'] = raw_input('enter his salutation: ')
    new_friend['age'] = input('enter his/her age: ')
    new_friend['rating'] = input('enter his/her rating: ')

    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)
        print "A friend is added."
    else:
        print "Invalid Entry!!"
    return len(friends)

# defining a function for listing friend's details


def select_friend():
    item = 1
    for friend in friends:
        print '%d. %s whose age is %d and whose rating is %.2f is online' % (item, friend['name'], friend['age'], friend['rating'])
        item = item + 1
    return True

# defining a chat function


def start_chat(spy):

    current_status_message = None
    spy['name'] = spy['salutation'] + " " + spy['name']
    if spy['age']> 12 and spy['age'] < 50:

        print "Authentication complete.Welcome " + spy['name'] + " " + 'Your age is: ' + str(spy['age']) + " " + "and rating is:" + " " + str(
            spy['rating']) + " " + ".Proud to have you on board."

        show_menu = True

        while show_menu:

            menu_choices = "What do you wanna do? \n1. Add a status \n2. Add a friend  \n3. Print friend\'s list \n4. Close Application \n"
            menu_choice = input(menu_choices)

            if menu_choice == 1:
                current_status_message = add_status(current_status_message)
            elif menu_choice == 2:
                number_of_friends = add_friend()
                if number_of_friends == 1:
                    print 'you have 1 friend'
                else:
                    print 'You have %d friends' % (number_of_friends)
            elif menu_choice == 3:
                if len(friends) == 0:
                    print 'You don\'t have any friends yet!!!!'
                else:
                    print 'your friend list is: '
                friend_list = select_friend()
            elif menu_choice == 4:
                print 'BYE BYE !!! SEE YOU AGAIN!!!'
                show_menu = False
    else:
        print " You are not of correct age to be a spy. "

# function ends here!!


if existing.upper() == "Y":

    start_chat(spy)
else:
    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }

    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy['name']) > 0:
        spy['salutation'] = raw_input("Should I call you Mr. or Ms.? ")

        spy['age'] = input("What is your age?")

        spy['rating'] = input("What is your spy rating?")

        spy['is_online'] = True

        start_chat(spy)
    else:
        print 'Please add a valid spy name'
