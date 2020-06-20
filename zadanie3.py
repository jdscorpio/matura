def numEqualWord(num:int, txt:str)->bool:
    if int(num)==len(txt):
        return True
    else:
        return False

def por(num1:int, txt1:str, num2:int, txt2:str):
    if num1<num2:
        return num1,txt1
    elif num2<num1:
        return num2,txt2
    else:
        if txt1==txt2:
            return num1,txt1
        elif txt1<txt2:
            return num1,txt1
        else:
            return num2,txt2

