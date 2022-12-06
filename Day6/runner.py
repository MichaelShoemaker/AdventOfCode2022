def get_counts(file):
    f = open(file).readline()
    for line in f:
        for i in range(0,len(line)-3):
            if len(set(line[i:i+3])) == 3:
                return i+3    



if __name__=='__main__':
    a = 
    get_counts('file')