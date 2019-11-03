import json
import sys

try:
    with open('votes.json', 'r') as json_file:
        fruits = json.load(json_file)
except FileNotFoundError:
    fruits = {
        'apple': 0,
        'banana': 0,
        'orange': 0
    }

vote = input("What is your favourite fruit: apple, banana or orange?")
if vote == "banana":
    fruits['banana'] +=1
elif vote == "apple":
    fruits['apple'] +=1
elif vote == "orange":
    fruits['orange'] +=1
else:
    print("You fruit cant be found.")
    sys.exit()

with open('votes.json', 'w') as json_file:
    json.dump(fruits, json_file)

print("Results:" + "banana = " + str(fruits['banana']),
      "apple = " + str(fruits['apple']),
      "orange = " + str(fruits['orange']))