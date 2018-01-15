import datetime


class Spy:


    def __init__(self,name,salutation,age,rating):
          self.name = name
          self.salutation = salutation
          self.age = age
          self.rating = rating
          self.is_online = True
          self.chat = []
          self.current_status_message = None


spy = Spy('Bond','Mr.',34,4.5)
friend_one = Spy('Avhishek', 'Mr.', 27, 4.9)
friend_two = Spy('Pooja', 'Ms.', 21, 4.39)
friend_three = Spy('Narendra', 'Dr.', 37, 4.95)
friends = [friend_one, friend_two, friend_three]


class ChatMessage :
    def __init__(self,message, sent_by_me):

        self.message = message

        self.sent_by_me = sent_by_me


