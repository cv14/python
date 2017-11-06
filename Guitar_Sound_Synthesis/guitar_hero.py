import guitar_string
import stdaudio
import stddraw
import time
import stdarray
import math


# Draw a 24-by-170 black key whose lower left corner is at (x, y), and
# color it red if is_pressed is True.
def black_key(x, y, is_pressed):
    if is_pressed:
        stddraw.setPenColor(stddraw.RED)
    else:
        stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledRectangle(x, y, 24, 170)


# Draw a 48-by-300 white key whose lower left corner is at (x, y), and
# color it red if is_pressed is True.
def white_key(x, y, is_pressed):
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.rectangle(x, y, 48, 300)
    if is_pressed:
        stddraw.setPenColor(stddraw.RED)
    else:
        stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(x, y, 48, 300)


# Draw keyboard, with the pressed key in red.
def draw_keyboard(pressed):
    stddraw.clear()
    white_key(0, 0, pressed == 0)
    white_key(48, 0, pressed == 2)
    black_key(36, 130, pressed == 1)
    white_key(96, 0, pressed == 3)
    white_key(144, 0, pressed == 5)
    black_key(132, 130, pressed == 4)
    white_key(192, 0, pressed == 7)
    black_key(180, 130, pressed == 6)
    white_key(240, 0, pressed == 8)
    white_key(288, 0, pressed == 10)
    black_key(276, 130, pressed == 9)
    white_key(336, 0, pressed == 12)
    black_key(324, 130, pressed == 11)
    white_key(384, 0, pressed == 14)
    black_key(372, 130, pressed == 13)
    white_key(432, 0, pressed == 15)
    white_key(480, 0, pressed == 17)
    black_key(468, 130, pressed == 16)
    white_key(528, 0, pressed == 19)
    black_key(516, 130, pressed == 18)
    white_key(576, 0, pressed == 20)
    white_key(624, 0, pressed == 22)
    black_key(612, 130, pressed == 21)
    white_key(672, 0, pressed == 24)
    black_key(660, 130, pressed == 23)
    white_key(720, 0, pressed == 26)
    black_key(708, 130, pressed == 25)
    white_key(768, 0, pressed == 27)
    white_key(816, 0, pressed == 29)
    black_key(804, 130, pressed == 28)
    white_key(864, 0, pressed == 31)
    black_key(852, 130, pressed == 30)
    white_key(912, 0, pressed == 32)
    white_key(960, 0, pressed == 34)
    black_key(948, 130, pressed == 33)
    white_key(1008, 0, pressed == 36)
    black_key(996, 130, pressed == 35)

# Return the starting index of key in keyboard, or -1.


def index(keyboard, key):
    for i, v in enumerate(keyboard):
        if v == key:
            return i
    return -1


# A guitar_string client that plays the guitar in real-time, using the
# keyboard to input notes. The program also displays a keyboard and highlights
# the pressed key in red.
def main():
    # Refresh rate (in seconds) for the keyboard.
    KEYBOARD_REFRESH_DELAY = 0.01

    # Specifies superposition window size.
    SUPERPOSITION_RANGE = 2

    # Setup the canvas and scale for the keyboard.
    stddraw.setCanvasSize(1056, 300)
    stddraw.setXscale(0, 1056)
    stddraw.setYscale(0, 300)

    # Create guitar strings for notes corresponding to the keys in keyboard.
    keyboard = 'q2we4r5ty7u8i9op-[=zxdcfvgbnjmk,.;/\' '
    key_notes = stdarray.create1D(len(keyboard), 0.0)
    for i in range(len(keyboard)):
        key_notes[i] = guitar_string.create(440 * math.pow(2, (i-24)/12))

    pressed = -1          # index of the pressed key
    start = time.clock()  # for refreshing the keyboard
    while True:
        # Check if the user has typed a key; if so, process it, ie, pluck
        # the corresponding string.
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key in keyboard:
                pressed = index(keyboard, key)
                guitar_string.pluck(key_notes[pressed])

        if pressed != -1:
            # Compute the superposition of samples.
            sample = guitar_string.sample(key_notes[index(keyboard, key)])

            if pressed == 0:
                sample += guitar_string.sample(key_notes[pressed + 1])
                sample += guitar_string.sample(key_notes[pressed + 2])
            elif pressed == 36:
                sample += guitar_string.sample(key_notes[pressed - 1])
                sample += guitar_string.sample(key_notes[pressed - 2])
            else:
                sample += guitar_string.sample(key_notes[pressed + 1])
                sample += guitar_string.sample(key_notes[pressed - 1])
                sample += guitar_string.sample(key_notes[pressed + 2])
                sample += guitar_string.sample(key_notes[pressed - 2])

            # Advance the simulation of each guitar string by one step.
            guitar_string.tic(key_notes[pressed])
            if pressed == 0:
                guitar_string.tic(key_notes[pressed])
                guitar_string.tic(key_notes[pressed + 1])
                guitar_string.tic(key_notes[pressed + 2])
            elif pressed == 36:
                guitar_string.tic(key_notes[pressed])
                guitar_string.tic(key_notes[pressed - 1])
                guitar_string.tic(key_notes[pressed - 2])
            else:
                guitar_string.tic(key_notes[pressed])
                guitar_string.tic(key_notes[pressed + 1])
                guitar_string.tic(key_notes[pressed - 1])
                guitar_string.tic(key_notes[pressed - 2])
                guitar_string.tic(key_notes[pressed + 2])

            # Play the sample on standard audio.
            stdaudio.playSample(sample)

        # Display the keyboard with the pressed key in red, every
        # KEYBOARD_REFRESH_DELAY seconds.
        if time.clock() - start > KEYBOARD_REFRESH_DELAY:
            start = time.clock()
            draw_keyboard(pressed)
            stddraw.show(0.0)


if __name__ == '__main__':
    main()
