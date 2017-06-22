#!/usr/bin/python3


if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])

    scores = [student[1] for student in l]
    minscore = min(scores)
    secminscore = min(score for score in scores if score != minscore)

    results = sorted([student[0] for student in l if student[1] == secminscore], key=lambda results: results[0])
    for student in results:
        print(student)
