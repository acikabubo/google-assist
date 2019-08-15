from flask import Flask
from flask_assistant import Assistant, ask, tell

app = Flask(__name__)
assist = Assistant(app, route='/google', project_id='home-59465')


# TODO: go_to_channel

@assist.action('turn-on-off-the-tv')
def turn_on_off_the_tv(tv_on_off):
    print()
    print(f"TURN {tv_on_off.upper()} THE TV")
    print()
    # TODO: send to serial

    if tv_on_off == "on":
        return ask(f"Sure, i'm turning {tv_on_off} your TV. \
            Do you want anything else?")
    else:
        return tell(f"Sure, i'm turning {tv_on_off} your TV")


@assist.action('increase-volume')
def increase_volume(volume):
    volume = int(volume)
    print()
    print(f"INCREASE THE VOLUME BY {volume}")
    print()
    # TODO: maybe need to convert from strint to integer
    # TODO: send to serial
    # return tell(f"Sure, i'm increasing the volume by {volume}")
    return ask(f"Sure, i'm increasing the volume by {volume}. \
        Do you want anything else?")


@assist.action('decrease-volume')
def increase_volume(volume):
    volume = int(volume)
    print()
    print(f"DECREASE THE VOLUME BY {volume}")
    print()
    # TODO: maybe need to convert from strint to integer
    # TODO: send to serial
    return ask(f"Sure, i'm decreasing the volume by {volume}. \
        Do you want anything else?")


@assist.action('greeting')
def greet_and_start():
    speech = "Hey! Are you male or female?"
    return ask(speech)


@assist.action("give-gender")
def ask_for_color(gender):
    print()
    print(f'GENDER: {gender}')
    print()
    if gender == 'male':
        gender_msg = 'Sup bro!'
    else:
        gender_msg = 'Haay gurl!'

    speech = gender_msg + ' What is your favorite color?'
    return ask(speech)


@assist.action('give-color', mapping={'color': 'sys.color'})
def ask_for_season(color):
    speech = 'Ok, {} is an okay color I guess'.format(color)
    return ask(speech)

if __name__ == '__main__':
    app.run(debug=True)
