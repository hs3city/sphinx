import json
import time
import badger2040
import random
badger = badger2040.Badger2040()

FONT_SCALE=0.7


def clear_screen():
    badger.pen(15)
    badger.clear()
    badger.pen(0)

def splash_screen():
    file = 'slide1.bin'
    image = bytearray(int(296 * 128 / 8))
    open("images/{}".format(file), "r").readinto(image)
    badger.image(image)
    badger.update()
    time.sleep(4.0)

def write_text(text, x, y, scale):
    badger.text(text, x, y, scale)
    print(text)

def generate_nickname():
    nickname = ''
    options = ['a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    for n in [1,2,3,4]:
        i = int(random.random() * len(options))
        nickname += options[i]
    return nickname

def read_questions():
    nickname = generate_nickname()

    clear_screen()
    write_text('Hello, your id is {}'.format(nickname), 5, 20, scale=FONT_SCALE)
    write_text('Write it down', 5, 45, scale=FONT_SCALE)
    write_text('Press A to continue', 5, 95, scale=FONT_SCALE)
    badger.update()

    while True:
        if badger.pressed(badger2040.BUTTON_A):
            break
        badger.halt()

    f = open("questions.json","r")
    data = json.load(f)
    points = 0
    q_number = 0

    for q in data['quiz']:
        q_number += 1

        clear_screen()
        write_text(q["question"], 5, 20,scale=FONT_SCALE)

        i = 1
        correct_answer = 0
        for a in q['answers']:
            write_text('{}. {}'.format(chr(i-1+ord('A')), a['answer']), 20, 40+i*20,scale=FONT_SCALE)
            correct_answer = i if a['correct'] else correct_answer
            i+=1
        badger.update()
        #ans = int(input('pick 1, 2 or 3\n'))

        while True:
            if badger.pressed(badger2040.BUTTON_A):
                ans = 1
                break
            if badger.pressed(badger2040.BUTTON_B):
                ans = 2
                break
            if badger.pressed(badger2040.BUTTON_C):
                ans = 3
                break

            badger.halt()
        points = points + 1 if ans == correct_answer else points

    clear_screen()
    write_text('Id: {}'.format(nickname), 5, 20,scale=FONT_SCALE)
    write_text('Points: {}/{}'.format(points, q_number), 5, 40,scale=FONT_SCALE)
    badger.update()
    f.close()

    highscores = open('highscores', 'a')
    highscores.write('Id: {}, Points: {}/{}\n'.format(nickname, points, q_number))
    highscores.close()

    time.sleep(4.0)

def highscores():
    message = 'No highschores yet!'

    try:
        highscores_file = open('highscores', 'r')
        lines = highscores_file.readlines()

        message = ''
        if len(lines) > 0:
            scores = []
            for line in lines:
                [raw_nick, raw_scores] = line.split(',')
                nick = raw_nick[4:]
                [raw_score, raw_total_score] = raw_scores.split('/')
                scores.append({'id': nick, 'score': int(raw_score[9:]), 'total_score': int(raw_total_score.strip()), 'line': line})

            scores = sorted(scores, key=lambda k: k['score'], reverse=True)[0:4]
            for s in scores:
                message += s['line']
    except:
        pass
    finally:
        highscores_file.close()

    clear_screen()

    i = 0
    for line in message.split('\n'):
        write_text(line, 5, 20+i*20,scale=FONT_SCALE)
        i += 1

    write_text('Press A to return to menu', 5, 20+i*20,scale=FONT_SCALE)
    badger.update()

    while True:
        if badger.pressed(badger2040.BUTTON_A):
            main_menu()
            break

        badger.halt()

def main_menu():
    clear_screen()
    write_text('Welcome to SphinxQuiz!', 5, 20, scale=FONT_SCALE)
    write_text('Please pick', 5, 45, scale=FONT_SCALE)
    write_text('A. Start a new game', 5, 70, scale=FONT_SCALE)
    write_text('B. See leaderboards', 5, 90, scale=FONT_SCALE)
    write_text('C. Exit', 5, 110, scale=FONT_SCALE)
    badger.update()
    while True:
        if badger.pressed(badger2040.BUTTON_A):
            read_questions()
            break
        if badger.pressed(badger2040.BUTTON_B):
            highscores()
            break
        if badger.pressed(badger2040.BUTTON_C):
            return False

        badger.halt()
    return True

def main():
    #splash_screen()
    next_round = True
    while next_round:
        next_round = main_menu()

if __name__ == "__main__":
    main()
