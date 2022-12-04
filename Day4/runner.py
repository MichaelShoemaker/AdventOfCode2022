def make_range(x:str)->list:
    l = [str(y) for y in range(int(x.split('-')[0]), int(x.split('-')[1])+1)]
    return l


def check_lists(x:list,y:list,part:int) -> bool:
    if part == 1:
        if all(elem in x  for elem in y) or all(elem in y  for elem in x):
            return True
        return False
    elif part == 2:
        if any(elem in x  for elem in y) or any(elem in y  for elem in x):
            return True
        return False


def read_file(file:str)->int:
    count = 0
    with open(file,'r') as infile:
        for line in infile:
            x, y = line.replace('\n','').split(',')
            if check_lists(make_range(x),make_range(y),part=2):
                count += 1
        return count


if __name__=='__main__':
    print(read_file('prod'))