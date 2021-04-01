import time
import random

name = ""
answer1 = ""
answer2 = ""
answer3 = ""
answer4 = ""
answer5 = ""
answer6 = ""
last_randoms = []
last_verbs = []

random_words = ["flying", "running", "leaving", "yawning", "joking", "smiling", "watering", "fighting", "eating", "hammering", "paying", "intervening", "scoring", "submitting", "freezing", "following", "singing", "publishing", "meeting", "celebrating", "breathing"]
random_verbs = ["wish", "reach", "mix", "reinforce", "talk","insert", "invest", "establish", "check", "deprive"]
random_nouns1 = ["library", "literature", "medicine", "audience", "gate"]
random_nouns2 = ["disaster", "nature", "vehicle", "theory", "inflation"]
sentence_list1 = ["{0} began their {1} day.", "Wowee, {0} is {1} this morning!", "{0} cannot wait to start this {1} day."]
sentence_list2 = ["{0} woke up to the {1} {2}.", "{0} opened up Instagram to a {1} {2}.", "{0} couldn’t believe that they saw a {1} {2}."]
sentence3 = "Since it was Sunday morning, {0} decided to {1} their favorite breakfast: {2}."
sentence_list4 = ["{0} poured themselves a warm cup of {1} and they ate their food while {2} a {3}.", "{0} enjoyed a bowl of {1} and they ate their food and {2} a {3}.", "{0} threw out a barrel of {1}, then casually {2} a {3}."]
sentence_list5 = ["After breakfast, {0} met up with a {1} for an all-day {2}.", "Following the delicious breakfast, {0} saw a {1} talking about {2}.", "Having had an amazing breakfast, {0} turned on the {1} to enjoy the sound of {2}."]

time.sleep(.5)
name = input("Hello, what is your name? ")
first_name = name.capitalize()
time.sleep(.5)
print("Hello, " + first_name)
time.sleep(1)
answer1 = input("What is one adjective to describe the beach? ")
time.sleep(.5)
print("Great!")
time.sleep(1)
answer2 = input("What is something found at grocery store? ")
time.sleep(.5)
print("Got it.")
time.sleep(1)
answer3 = input("What is your favorite food? ")
time.sleep(.5)
print("Yum!")
time.sleep(1)
answer4 = input("What is a liquid found at restaurant? ")
time.sleep(.5)
print("Love it.")
time.sleep(1)
answer5 = input("What is something that can be read? ")
time.sleep(.5)
print("Gotcha!")
time.sleep(1)
answer6 = input("What is an animal found at the zoo? ")
time.sleep(.5)
print("Aw, cute!")
time.sleep(1)
print(" ")
print("Okay... now, I'm compiling your answers and generating a story for you.")
time.sleep(.5)
print(".")
time.sleep(.5)
print(".")
time.sleep(.5)
print(".")
time.sleep(.5)
print("Oh, I think you are going to love this one...")
time.sleep(.5)
print("------------------------------------------------------------")
print(" ")

def random_word (words):
    global last_randoms
    word = random.choice(random_words)
    while word in last_randoms:
      word = random.choice(random_words)
    last_randoms.append(word)
    return word


# def random_nouns1 (nouns):
#     global last_nouns1
#     noun = random.choice(random_nouns1)
#     while noun in last_nouns1:
#       noun = random.choice(random_nouns1)
#     last_nouns1.append(noun)
#     return noun

# def random_nouns2 (nouns):
#     global last_nouns2
#     noun = random.choice(random_nouns2)
#     while noun in last_nouns2:
#       noun = random.choice(random_nouns2)
#     last_nouns2.append(noun)
#     return noun

def random_verb (verbs):
    global last_verbs
    verb = random.choice(random_verbs)
    while verb in last_verbs:
      verb = random.choice(random_verbs)
    last_verbs.append(verb)
    return verb

if len(name) >= 5:
  random_noun = random_nouns2
elif len(name) < 5:
  random_noun = random_nouns1

sentence1 = random.choice(sentence_list1).format(first_name, answer1)
sentence2 = random.choice(sentence_list2).format(first_name, answer2, random.choice(random_words))
sentence4 = random.choice(sentence_list4).format(first_name, answer4, random.choice(random_words), answer5)
sentence5 = random.choice(sentence_list5).format(first_name, answer6, random.choice(random_noun))


print(sentence1, sentence2)
print(sentence3.format(first_name, random.choice(random_verbs),answer3))
print(sentence4)
print(sentence5)
print(" ")
print("I hope you enjoyed the story, " + first_name +"!")
print(" ")
