def select_name():

    #from names_ip import b_names as names #sample data
    from names_ip import g_names as names #sample data
    my_string = names()
    
    #my_string = input("enter names: ")
    my_word = input("name 1: ")
    my_word2 = input("name 2: ")
    my_word1 = my_word + my_word2
    my_word2 = my_word2 + my_word

    my_string = my_string.upper()
    my_word1 = my_word1.upper()
    my_word2 = my_word2.upper()
    
    mwi_max = 0
    match_max = 0
    match_word = ""
    delimiter = ","

    for string_word in my_string.split(delimiter):
        match_point1 = 0
        match_point2 = 0
        mwi = 0
        msip = 0
        
        for el1 in my_word1:
            mwi += 1
            msi = 0
            if (mwi_max < mwi):
                mwi_max = mwi
            
            for el2 in string_word:
                msi += 1
                if (el1 == el2 and msip < msi):
                    match_point1 += 1
                    msip = msi

        mwi = 0
        for el1 in my_word2:
            mwi += 1
            msi = 0
            
            for el2 in string_word:
                msi += 1
            
                if (el1 == el2 and msip < msi):
                    match_point2 += 1
                    msip = msi

        if(match_point1 > match_max):
            match_max= match_point1
            match_word = string_word
        elif(match_point2 > match_max):
            match_max= match_point2
            match_word= string_word

        if ((match_point1+(mwi_max/2)) >= mwi_max or (match_point2+(mwi_max/2)) >= mwi_max ):
            print (string_word)

    print(match_word)

