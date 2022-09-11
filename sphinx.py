import json

def read_questions():
    f = open("questions.json","r")
    data = json.load(f)

    for q in data['quiz']:
        print("question")
        print(q['question'])
        i = 1
        for a in q['answers']:
            print('{}: {}'.format(i, a['answer']))
            i+=1

    f.close()

def main():
    read_questions()

if __name__ == "__main__":
    main()
