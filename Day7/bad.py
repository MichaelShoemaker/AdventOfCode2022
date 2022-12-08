import re

class directory:
    def __init__(self, level, letter):
        self.level = level
        self.letter = letter
        self.size = 0

def get_dirs(file:str):
    f = open(file).read().splitlines()
    in_progress = []
    done = []
    for line in f:
        level = len(line.split('-')[0])
        for i, n in enumerate(in_progress):
            if n.level >= level:
                done.append(in_progress.pop(i))


        if 'dir' in line:
            in_progress.append(directory(len(line.split('-')[0]),line.split('-')[1][:2].strip()))
        
        val = re.findall(r'\d+', line)
        if len(val) > 0:
            for n in in_progress:
                n.size += int(val[0])
    return in_progress + done

if __name__=='__main__':
    f = get_dirs('test')
    result = 0
    for i in f:
        if i.size < 100000:
            result += i.size
    print(result)