def splitster(my_str):
    my_str = list(my_str)
    dex = int(len(my_str)/2)
    return set(my_str[:dex]).intersection(set(my_str[dex:]))

def make_let(x):
    if x.isupper():
        val = ord(x) - 38
    else:
        val = ord(x) - 96
    return val


def solve_part1(file):
    total = 0
    f = open(file,'r').read().splitlines()
    for line in f:       
        total += make_let(list(splitster(line))[0])
    return total

def solve_part2(file):
    x = 0
    y = 1
    z = 2
    ans = 0

    f = open(file,'r').read().splitlines()
    chunks=int(len(f)/3)
    while chunks != 0:
        ans += make_let(list(set(f[x]) & set(f[y]) & set(f[z]))[0])
        chunks -= 1
        x += 3
        y += 3
        z += 3
    return ans



if __name__ == '__main__':
    # print(solve_part1('prod'))
    print(solve_part2('prod'))

