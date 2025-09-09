import random
from library import Library
import json

class Member:
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    members = []
    def __init__(self, name):
        self.name = name
        letter = random.choice(Member.letters)
        number = random.randrange(100,999,1)
        self.memberID = f"#{letter}{number}"
        Library.memberList.append(self.memberID)
        Member.members.append(self)

    def to_dict(self):
        return {
            "Name": self.name,
            "Member ID": self.memberID
        }

member1 = Member("Samppa")
member2 = Member("James")
member3 = Member("Nilay")
member4 = Member("Joona")
member5 = Member("Atte")
member6 = Member("Joonatan")
member7 = Member("Erik")
member8 = Member("Jasper")
member9 = Member("Celia")
member10 = Member("Grigory")
member11 = Member("Noah")
member12 = Member("Kamal")


with open("members.json", "w") as outfile:
    json.dump([member.to_dict() for member in Member.members], outfile, indent=2)
