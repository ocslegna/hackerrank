#!/usr/bin/python3

""" Nested lists. """

if __name__ == '__main__':
    L = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        L.append([name, score])

    SCORES = [student[1] for student in L]
    MINSCORE = min(SCORES)
    SECMINSCORE = min(score for score in SCORES if score != MINSCORE)

    RESULTS = sorted([student[0] for student in L if student[1] == SECMINSCORE], key=lambda results: RESULTS[0])
    for student in RESULTS:
        print(student)
