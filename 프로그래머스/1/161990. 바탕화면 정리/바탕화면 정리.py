def solution(wallpaper):
    lux, luy, rdx, rdy = 0, 0, 0, 0
    x, uy, dy = [], [], []
    for i in range(len(wallpaper)):
        l = wallpaper[i]
        if '#' in l:
            x.append(i)
            uy.append(len(list(l.split('#')[0])))
            dy.append(len(l) - len(list(l.split('#')[-1])))
        else:
            uy.append(len(list(l)))
            dy.append(len(l) - len(list(l.split('#')[-1])))
    answer = [min(x), min(uy), max(x)+1, max(dy)]
    return answer