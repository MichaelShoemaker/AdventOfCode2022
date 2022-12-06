def get_counts(line: str, mark: int) -> int:
    for i in range(0,len(line)):
        if len(set(line[i:i+mark])) == mark:
            return i+mark    

def gen_lines(file: str) -> str:
    with open(file,'r') as infile:
        for line in infile:
            yield(line.replace('\n',''))

if __name__=='__main__':
    count = 0
    for i in gen_lines('prod'):
        print(f"Part1 : {get_counts(i, 4)}")
        print(f"Part2 : {get_counts(i, 14)}")