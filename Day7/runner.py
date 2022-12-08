def make_dirs(file: str):
    f = open(file).read().splitlines()
    for i in f:
        print(i)






if __name__ == '__main__':
    make_dirs('test')