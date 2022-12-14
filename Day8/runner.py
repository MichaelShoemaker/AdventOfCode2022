from time import sleep

def check_heights(s: list, i: int, t: int) -> bool:
    for l in s:
        if int(l[i]) >= t:
            return False
    return True


def make_grid(file:str):
    f =open(file).read().splitlines()
    grid = [list(x) for x in f]
    visible = 0

    height = len(grid)
    width = len(grid[0])
    #print(grid)
    visible += (height * 2) + (width * 2) - 4
    for h in range(1,len(grid)-1):
        for w in range(1,len(grid[0])-1):
            if h == 97 and w > 94:
                print(grid[h][w])
            tree = int(grid[h][w])
            if all(int(x) < tree for x in grid[h][:w]):
                if h == 97 and w > 94:
                    print(h,w, grid[h][w],'a')
                visible += 1
                continue
            if all(int(x) < tree for x in grid[h][w+1:]):
                if h == 97 and w > 94:
                    print(h,w, grid[h][w],'b')
                visible += 1
                continue
            if check_heights(grid[:h], w, tree):
                # print(check_heights(grid[:h], w, tree))
                if h == 97 and w > 94:
                    print(h,w, grid[h][w],'c')
                visible +=1 
                continue
            if check_heights(grid[h+1:], w, tree):
                if h == 97 and w > 94:
                    print(h,w, grid[h+1:][0][95:],'d')
                visible +=1
                continue

    return visible



if __name__=='__main__':
    print(make_grid('prod'))
