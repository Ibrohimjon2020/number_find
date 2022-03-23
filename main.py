import random
def son_top_pc(x):

    print(f"\n Keling men \n 1 da {x} gacha son o'ylayman siz topishga harakat qiling")
    kom_oylagan_son = random.randint(1,x)
    taxminlar_sum = 0
    while True:
        taxminlar_sum +=1
        taxmin = int(input(">>> "))
        if taxmin > kom_oylagan_son:
            print("katta son o'yladiz")        
        elif taxmin < kom_oylagan_son:
            print("kichkina son o'yladiz")
        else:
            break
    print(f"Tabriklayman topdingiz men {kom_oylagan_son} o'ylagan edim \n Siz {taxminlar_sum} ta taxmin bilan topdingiz")
    return taxminlar_sum

def son_top(x):
    input(f"1 dan {x} gacha son o'ylang men topaman. O'yini boshlash uchun istalgan tugmani bosing")
    quyi = 1
    yuqori = x
    choice = 0
    while True:
        choice +=1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = yuqori
        javob = input(f"siz o'ylagan son {taxmin} mi ? Agar topgan bolsam (t) harifini bosing agar son kichkina bolsa (-) bosing agar katta bo'lsa (+)\n >>>")

        if javob == "+":
            quyi = taxmin + 1
        elif javob == "-":
            yuqori = taxmin - 1
        else:
            break
    print(f"{choice} ta taxmin bilan topdim")
    return choice
play = True
while play:
    taxminlar_user = son_top(10)
    taxminlar_pc = son_top_pc(10)

    if taxminlar_pc > taxminlar_user:
        print("Men yutdim")
    elif taxminlar_user > taxminlar_pc:
        print("Siz yutdingiz")
    else:
        print("Durang")
    play = int(input("\n Yana o'ynaysizmi Ha (1) / Yo'q (0) >> "))
