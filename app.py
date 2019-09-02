import serial
from flask import Flask
from flask_assistant import Assistant, ask, tell

app = Flask(__name__)
assist = Assistant(app, route='/google', project_id='home-59465')

# Open serial porn
arduino = serial.Serial('/dev/ttyUSB0', 9600)

# Define constants for arduino functions
TURN_ON_OFF = b"1"
MUTE_VOLUME = b"2"
INCREASE_VOLUME = "3"
DECREASE_VOLUME = "4"
GO_TO_CHANNEL = "5"
BACK_TO_PREVIOUS_CHANNEL = b"6"


last_channel = None


def make_code(code, value):
    val = str(value)
    c = code + "0" * (4 - len(val)) + val
    return c.encode()


@assist.action('turn-on-off-the-tv')
def turn_on_off_the_tv(tv_on_off):
    print()
    print(f"TURN {tv_on_off.upper()} THE TV")
    print()

    # Send code for turn on or off
    arduino.write(TURN_ON_OFF)
    
    if tv_on_off == "on":
        return ask(f"Sure, i'm turning {tv_on_off} your TV. \
            Do you want anything else?")
    else:
        return tell(f"Sure, i'm turning {tv_on_off} your TV")


@assist.action('mute-unmute-volume')
def mute_unmute(mute_unmute):
    print()
    print(f"{mute_unmute.upper()} VOLUME")
    print()

    # Send code for mute or unmute volume
    arduino.write(MUTE_VOLUME)
    
    return ask(f"Sure, i'm will {mute_unmute.lower()} the volume. \
        Do you want anything else?")


@assist.action('show-volume')
def show_volume():
    pass


@assist.action('increase-volume')
def increase_volume(volume):
    volume = int(volume)
    print()
    print(f"INCREASE THE VOLUME BY {volume}")
    print()
    
    code = make_code(INCREASE_VOLUME, volume)
    print(f"CODE: {code}")
    print()
    arduino.write(code)
    
    return ask(f"Sure, i'm increasing the volume by {volume}. \
        Do you want anything else?")


@assist.action('decrease-volume')
def decrease(volume):
    volume = int(volume)
    print()
    print(f"DECREASE THE VOLUME BY {volume}")
    print()

    code = make_code(DECREASE_VOLUME, volume)
    print(f"CODE: {code}")
    print()
    arduino.write(code)
    
    return ask(f"Sure, i'm decreasing the volume by {volume}. \
        Do you want anything else?")


@assist.action('goto-channel')
def goto_channel(channel, prev_next_channel):
    print()
    print(f"GO TO CHANNEL {channel}")
    print()
    global last_channel
    channel = int(channel) if channel else None
    
    def req_resp(channel):
        arduino.write(make_code(GO_TO_CHANNEL, channel))
        return ask(f"Sure, go to channel {channel}. \
            Do you want anything else?")

    if channel:
        last_channel = channel
        return req_resp(last_channel)
    
    elif prev_next_channel and last_channel:
        if prev_next_channel == 'previous':
            last_channel -= 1
        else:
            last_channel += 1

        return req_resp(last_channel)

    return ask(f"Sorry I don't know which channel is {prev_next_channel}. \
        Do you want anything else?")
    

@assist.action('goto-previous-channel')
def goto_previous_channel():
    print()
    print(f"GO TO PREVIOUS CHANNEL")
    print()

    # Send code for turn on or off
    arduino.write(BACK_TO_PREVIOUS_CHANNEL)
     
    return ask("Sure, go to previous channel. \
        Do you want anything else?")


if __name__ == '__main__':
    app.run(debug=True)
