import json
import uuid

def read_questions():
    nickname = str(uuid.uuid4())[0:6]
    print('Hello, your id is {}'.format(nickname))
    f = open("questions.json","r")
    data = json.load(f)
    points = 0
    q_number = 0

    for q in data['quiz']:
        q_number += 1
        print("question")
        print(q['question'])
        i = 1
        correct_answer = 0
        for a in q['answers']:
            print('{}: {}'.format(i, a['answer']))
            correct_answer = i if a['correct'] else correct_answer
            i+=1
        ans = int(input('pick 1, 2 or 3\n'))
        points = points + 1 if ans == correct_answer else points


    print('\n')
    print('Id: {}'.format(nickname))
    print('Points: {}/{}'.format(points, q_number))
    f.close()

    highscores = open("highscores", "a")
    highscores.write("Id: {}, Points: {}/{}\n".format(nickname, points, q_number))
    highscores.close()

def main():
    read_questions()

if __name__ == "__main__":
    main()
