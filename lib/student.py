#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name, knowledge=[] ):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge
        # print(type(knowledge))

    def learn(self, a_string):
        self.knowledge.append(a_string)


# schell=Student("Schell", "Mckenzie")
# print(schell.first_name)
# print(schell.last_name)

# schell.learn("History")
# print(schell.knowledge)