from flask import Flask
from flask_assistant import Assistant, ask, tell

app = Flask(__name__)
assist = Assistant(app, route='/google', project_id='home-59465')


@assist.action('member-count')
def google_member_count():
    print()
    print('GOOGLE MEMBER COUNT')
    print()
    return tell('Hello there')


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
