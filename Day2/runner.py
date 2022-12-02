def play(n, m):
    score = 0
    if m == 'X':
        score += 1
    elif m == 'Y':
        score += 2
    else:
        score += 3
    if n == 'A':
        if m == 'X':
            score += 3
        elif m == 'Y':
            score += 6
    elif n == 'B':
        if m == 'Y':
            score += 3
        elif m == 'Z':
            score += 6
    elif n == 'C':
        if m == 'X':
            score += 6
        elif m == 'Z':
            score += 3
    return score

def play_second(n, m):

    o = {'A':1,'B':2,'C':3}
    if m == 'X':
        if n == 'A':
            return 3
        elif n == 'B':
            return 1
        else: 
            return 2
    elif m == 'Y':
        return o[n] +3
    else:
        if n == 'A':
            return 8
        elif n == 'B':
            return 9
        else:
            return 7

if __name__=='__main__':
    f = 0
    with open('input','r') as infile:
        round = 0
        for line in infile:
            i = (line.replace('\n','').split(' '))
            f += play_second(i[0],i[1])
            round +=1
            # print(f"Round {round} score is {f}")
    print(f)