print("We are going to find the thief inside this program\n")

def find_thief():
    """ 
    a1 = "من و ج پیش از امروز بارها با هم ملاقات کرده ایم"
    a2 = "ب مجرم است"
    a3 = "دزد نمی دانست ماشین مال کاراگاه است"

    b1 = "د این کار را نکرده است"
    b2 = "حرف سوم د دروغ است"
    b3 = "من بی تقصیرم"

    c1 = "من قبل از این اصلا الف را ندیده بودم"
    c2 = "ب گناهکار نیست"
    c3 = "د رانندگی بلد است"

    d1 = "حرف اول ب دروغ است"
    d2 = "من اصلا رانندگی بلد نیستم"
    d3 = "ای این کار را کرده است"
    """
    a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3 =  True, True, True, True, True, True, True, True, True, True, True, True

    # rabete mostaghim (a1 <-> c1),(a2 <-> c2 -> b3),(b1 <-> d1),(b2 <-> d3)
        # ,(c3 <-> d2),(a3 -> True)

    true = 0
    false = 0
    if a1 == True:
        c1 = False
    if b1 == True:
        d1 = False
    if b2 == True:
        d3 = False
    if c3 == True:
        d2 = False
        # baray inke true == false tebgh shart c2 <-> a2 <-> b3:
    if a2 == True:
        c2 = False
        b3 = False
    thief_list = [a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3]
    for item in thief_list:
        if item == True:
            true += 1
        else:
            false += 1
    if true == false:
        print("in this case, number of lies and truths is equal(lies == truths)")
    
    print("so following people are not thieves")
    
    print("a because a2 is always truth")
    
    print("c because c2 is always lie")
    
    print("d because b3 is always lie")
    
    print("so b is a thief \n\ngood luck! ")

find_thief()

