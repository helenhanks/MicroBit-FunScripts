from microbit import *
import random
#
# Initialisation
options = ["images", "compass", "thermometer", "dice", "coin toss",
           "magic 8 ball", "spirit level"]
selector = -1 % len(options)
#
# Start options menu
display.scroll("Choose app", wait=False)
while not button_b.was_pressed():
    if button_a.is_pressed():
        selector = (selector + 1) % len(options)
        display.show(str(selector + 1))
        sleep(500)
        display.scroll(options[selector], loop=False, wait=False)
#
# Images app
if selector + 1 == 1:
    images = [Image.HEART, Image.HEART_SMALL, Image.HAPPY,
              Image.SMILE, Image.SAD, Image.CONFUSED,
              Image.ANGRY, Image.ASLEEP, Image.SURPRISED,
              Image.SILLY, Image.FABULOUS, Image.MEH,
              Image.YES, Image.NO, Image.TRIANGLE,
              Image.TRIANGLE_LEFT, Image.CHESSBOARD,
              Image.DIAMOND, Image.DIAMOND_SMALL,
              Image.SQUARE, Image.SQUARE_SMALL, Image.RABBIT,
              Image.COW, Image.MUSIC_CROTCHET,
              Image.MUSIC_QUAVER, Image.MUSIC_QUAVERS,
              Image.PITCHFORK, Image.XMAS, Image.PACMAN,
              Image.TARGET, Image.TSHIRT, Image.ROLLERSKATE,
              Image.DUCK, Image.HOUSE, Image.TORTOISE,
              Image.BUTTERFLY, Image.STICKFIGURE, Image.GHOST,
              Image.SWORD, Image.GIRAFFE, Image.SKULL,
              Image.UMBRELLA, Image.SNAKE]
    imageindex = 0
    sleep(500)
    while True:
        if button_a.is_pressed():
            imageindex = (imageindex - 1) % len(images)
        elif button_b.is_pressed():
            imageindex = (imageindex + 1) % len(images)
        display.show(images[imageindex])
        sleep(300)
#
# Compass app
elif selector + 1 == 2:
    if not compass.is_calibrated():
        compass.calibrate()
    while True:
        needle = ((15 - compass.heading()) // 30) % 12
        display.show(Image.ALL_CLOCKS[needle])
#
# Thermometer app
elif selector + 1 == 3:
    degrees_c = Image("99000:"
                      "99099:"
                      "00900:"
                      "00900:"
                      "00099")
    degrees_f = Image("99000:"
                      "99999:"
                      "00900:"
                      "00999:"
                      "00900")
    degrees_k = Image("99000:"
                      "99909:"
                      "00990:"
                      "00990:"
                      "00909")
    degrees_r = Image("99000:"
                      "99999:"
                      "00909:"
                      "00990:"
                      "00909")
    scales = [degrees_c, degrees_f, degrees_k, degrees_r]
    scalesindex = 0
    dummy = button_a.was_pressed() and button_b.was_pressed()
    while True:
        temperature_out = [str(temperature()),
                           str(round(temperature() * 1.8 + 32)),
                           str(round(temperature() + 273.15)),
                           str(round(((temperature() + 273.15) * 1.8)))]
        if button_a.was_pressed():
            scalesindex = (scalesindex - 1) % len(scales)
        if button_b.was_pressed():
            scalesindex = (scalesindex + 1) % len(scales)
        display.scroll(temperature_out[scalesindex], wait=True, delay=300)
        display.show(scales[scalesindex])
        sleep(2000)
#
# Dice app
elif selector + 1 == 4:
    dummy = button_a.was_pressed() and button_b.was_pressed()
    display.show(Image.SQUARE)
    while True:
        if accelerometer.was_gesture("shake") \
           or button_a.was_pressed() or button_b.was_pressed():
            display.show(Image.SQUARE_SMALL)
            sleep(500)
            display.show(Image.SQUARE)
            sleep(500)
            display.show(str(random.randint(1, 6)))
#
# Coin Toss app
elif selector + 1 == 5:
    dummy = button_a.was_pressed() and button_b.was_pressed()
    coinchoices = ["H", "T"]
    display.show(Image.DIAMOND)
    while True:
        if accelerometer.was_gesture("shake") \
           or button_a.was_pressed() or button_b.was_pressed():
            display.show(Image.DIAMOND_SMALL)
            sleep(500)
            display.show(Image.DIAMOND)
            sleep(500)
            display.show(str(random.choice(coinchoices)))
#
# Magic 8 Ball app
elif selector + 1 == 6:
    dummy = button_a.was_pressed() and button_b.was_pressed()
    eightballchoices = ["It is certain",
                        "It is decidedly so",
                        "Without a doubt",
                        "Yes, definitely",
                        "You may rely on it",
                        "As I see it, yes",
                        "Most likely",
                        "Outlook good",
                        "Yes",
                        "Signs point to yes",
                        "Reply hazy try again",
                        "Ask again later",
                        "Better not tell you now",
                        "Cannot predict now",
                        "Concentrate and ask again",
                        "Don't count on it",
                        "My reply is no",
                        "My sources say no",
                        "Outlook not so good",
                        "Very doubtful"]
    while True:
        display.show('8')
        if accelerometer.was_gesture("shake") \
           or button_a.was_pressed() or button_b.was_pressed():
            display.clear()
            sleep(1000)
            display.scroll(str(random.choice(eightballchoices)))
            sleep(500)
#
# Spirit Level app
elif selector + 1 == 7:
    while True:
        reading = accelerometer.get_x()
        if reading > 20:
            display.show("R")
        elif reading < -20:
            display.show("L")
        else:
            display.show("-")
