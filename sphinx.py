import json
import time
import badger2040
badger = badger2040.Badger2040()

def splash_screen():
    file = 'slide1.bin'
    image = bytearray(int(296 * 128 / 8))
    open("images/{}".format(file), "r").readinto(image)
    badger.image(image)
    badger.update()
    time.sleep(4.0)

def read_questions():
    nickname = "AAC"
    print('Hello, your id is {}'.format(nickname))
    f = open("questions.json","r")
    data = json.load(f)
    points = 0
    q_number = 0

    for q in data['quiz']:
        badger.pen(15)
        q_number += 1
        badger.clear()
        badger.pen(0)
        badger.text("question", 20, 20,scale=0.5)
        badger.text(q["question"], 20, 40,scale=0.5)
        print("question")
        print(q['question'])
        i = 1
        correct_answer = 0
        for a in q['answers']:
            print('{}: {}'.format(i, a['answer']))
            badger.text('{}: {}'.format(chr(i-1+ord('a')), a['answer']), 20, 40+i*20,scale=0.5)
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

            # Halt the Badger to save power, it will wake up if any of the front buttons are pressed
            badger.halt()
        points = points + 1 if ans == correct_answer else points

    badger.pen(15)
    badger.clear()
    badger.pen(0)
    badger.text('Id: {}'.format(nickname), 20, 20,scale=0.5)
    badger.text('Points: {}/{}'.format(points, q_number), 20, 40,scale=0.5)
    badger.update()
    print('\n')
    print('Id: {}'.format(nickname))
    print('Points: {}/{}'.format(points, q_number))
    f.close()

    highscores = open("highscores", "a")
    highscores.write("Id: {}, Points: {}/{}\n".format(nickname, points, q_number))
    highscores.close()

def main():
    splash_screen()
    read_questions()

if __name__ == "__main__":
    main()
