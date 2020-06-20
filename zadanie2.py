def max(tab:list)->int:
    m = 0
    for i in tab:
        if i>m:
            m = i
    return m

def indexMax(tab:list)->int:
    for i in range(len(tab)):
        if tab[i] == max(tab):
            return i

