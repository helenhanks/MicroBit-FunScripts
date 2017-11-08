from microbit import *
import random
import speech
dummy = button_a.was_pressed() and button_b.was_pressed()
eightballchoices = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes, definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
speech.say("Ask me a question!")
while True:
    display.show('8')
    if accelerometer.was_gesture("shake") \
    or button_a.was_pressed() or button_b.was_pressed():
        display.clear()
        sleep(1000)
        reply = str(random.choice(eightballchoices))
        speech.say(reply)
        #display.scroll(reply)
        sleep(500)
        speech.say("Ask me another question!")