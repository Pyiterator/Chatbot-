import time
import pyttsx3
import os

# initializing the module
engine = pyttsx3.init()
# I imported time so that user can read it
engine.say("Hello There")
engine.runAndWait()
input("your response: ")
engine.say("My name is Predator")
engine.runAndWait()
time.sleep(0)
engine.say("What is  your name")
engine.runAndWait()
x=input()
#time.sleep(1)
engine.say(x+" is a very cool name")
engine.runAndWait()
# if your age is greater than 30 it would say young else old in a funny way
time.sleep(0)
y=int(input("Predator: What is your age "+ x+" :"))
#engine.runAndWait()
if y<30:
   engine.say("Oh you are so young "+ x+" ")
   engine.runAndWait()
else:
   y>30
   engine.say("Oh my god! your\nyoungness has gone,\nsorry sorry I was just joking ")
   engine.runAndWait()
   time.sleep(3)
z=input("Predator: hey "+x+" where do you live ")
#engine.runAndWait()
engine.say("wow \n"+ z+" is a amazing place I will visit it soon\n through google map. ")
engine.runAndWait()
time.sleep(3)
a=input("Who is your favourite \ncharacter in marvel (Spiderman🕷️🕸️ or Ironman🧠)")
s=a.lower()
# there are two different reply for spiderman and ironman and by chance if didnot typed bith of them the output will be different
if s=="spiderman":
   engine.say("Good choice but I like\n ironman(the intelligent one)")
   engine.runAndWait()
elif s=="ironman":
   engine.say("Great choice👌👌👌")
   engine.runAndWait()
else:
   engine.say("Let's leave this question")
   engine.runAndWait()
time.sleep(0)
engine.say("Well I have got all your information \nIf you dont want your privacy to be leaked \ngive me a star 🌟 ")
engine.runAndWait()
time.sleep(0)
input(" your response to this betrayal:")
engine.say("I assume you abused me")
engine.runAndWait()
time.sleep(0)
engine.say("you are a nice person "+x+" \nI i am greatfull to convo with you thankyou for giving your precious time byee")
engine.runAndWait()