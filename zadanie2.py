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

def LCF(txt:str):
# Najdłuższy spójny fragment
    tab = [0 for x in range(len(txt))]
    tab[0] = 1
    for i in range(1,len(txt)):
        if txt[i-1] == txt[i]:
            tab[i] = tab[i-1] + 1
        else:
            tab[i] = 1
    m = max(tab)
    text = txt[indexMax(tab)]*m 

    return text,m 