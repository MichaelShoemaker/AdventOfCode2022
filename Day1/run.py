def find_heaviest(file, part = 1):
    elves = {}
    elf = 1
    with open(file,'r') as infile:
        for line in infile:
            if len(line.strip()) == 0:
                elf += 1
                continue
            else:
                if elf in elves:
                    elves[elf] += int(line)
                else:
                    elves[elf] = int(line)

    if part == 1:
        return elves[max(elves, key=elves.get)]
    top_three = sorted(elves, key=elves.get, reverse=True)[:3]
    return elves[top_three[0]]+elves[top_three[1]]+elves[top_three[2]]

if __name__ == '__main__':
    print(find_heaviest('./Day1/prod', 2))