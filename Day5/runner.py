import re

def clean_chars(x: str):
    stacks = []
    instructions = []
    f = open(x).read().splitlines()
    flag = 0
    ins_flag = 0
    for i in f:
        if flag == 0:
            for s in range(len(i)):
                stacks.append([])
            flag = 1

        if i == '':
            ins_flag = 1
            continue

        if ins_flag == 0:
            for l,c in enumerate(i):
                if c.isalpha():
                    stacks[l].insert(0, c)

        elif ins_flag == 1:
            instructions.append(i.split(' '))
    return [s for s in stacks if s], instructions


def move_crates(stacks: list, instructions: list, part):
    for i in instructions:
        crates = stacks[int(i[3])-1][-int(i[1]):]
        if part == 1:
            for c in reversed(crates):
                stacks[int(i[5])-1].append(c)
            stacks[int(i[3])-1] = stacks[int(i[3])-1][:-int(i[1])]
        elif part == 2:
            for c in crates:
                stacks[int(i[5])-1].append(c)
            stacks[int(i[3])-1] = stacks[int(i[3])-1][:-int(i[1])]

    ans = ''
    for i in stacks:
        ans += i[-1]
    return ans


if __name__ == '__main__':
    print(move_crates(clean_chars('prod')[0], clean_chars('prod')[1],part = 2))