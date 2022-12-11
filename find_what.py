
def find_what():

    my_string = find_from() #sample function
    #my_string = input("find from: ")
    my_word = input("find what: ")
    my_string = my_string.upper()
    my_word = my_word.upper()
    match_max = 0
    match_word = ""
    mwi_max = 0
    delimiter = " "

    for string_word in my_string.split(delimiter):
        match_point = 0
        mwi = 0
        msip = 0
        
        if ((match_max/3) >= mwi_max and match_max != 0):
            break
    
        for el1 in my_word:
            mwi += 1
            msi = 0
            if (mwi_max < mwi):
                mwi_max = mwi
            
            for el2 in string_word:
                msi += 1
            
                if (el1 == el2 and msip < msi):
                   match_point += 3
                   msip = msi
                   break

                elif(match_point != 0 and msip < msi):
                    match_point -= 1
                    
        if(match_max < match_point and match_point != 0):
            match_max = match_point
            match_word = string_word

    print (match_word)
    #print (match_max)


    
def find_from():
    my_string = "the at there some my of be use her than and this an would first a have each make water to from which like been in or she him call is one do into who you had how time oil that by their has its it word if look now he but will two find was not up more long for what other write down on all about go day are were out see did as we many number get with when then no come his your them way made they can these could may I said so people part"
    return my_string