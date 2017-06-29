#!/usr/bin/python3

"""
Execute N commands given in N lines.
"""


def execute(s, num_commands, commands):
    """ Executes N commands """
    for i in range(num_commands):
        if len(commands[i]) == 1:
            s.pop()
        else:
            if commands[i][0] == 'remove':
                s.remove(int(commands[i][1]))
            elif commands[i][0] == 'discard':
                s.discard(int(commands[i][1]))

    print(sum(s))


if __name__ == '__main__':
    N = int(input())
    S = set(map(int, input().split()))
    NUM_COMMANDS = int(input())
    COMMANDS = [input().split() for n in range(NUM_COMMANDS)]
    execute(S, NUM_COMMANDS, COMMANDS)
