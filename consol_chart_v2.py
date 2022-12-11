def console_chart_v2(data_list):

    print("\n")
    j = 1
    list_len = len(data_list)
    lowest = data_list[1][1]
    highest = 0

    for pre_num in range(0, list_len):
        if (data_list[pre_num][2] < lowest):
            lowest = data_list[pre_num][2]
        if (data_list[pre_num][1] > highest):
            highest = data_list[pre_num][1]
    tenR = (highest - lowest) / 20

    while (j <= 20 and list_len > 1):

        for pre_num in range(0, list_len):

            if (data_list[pre_num][0] > data_list[pre_num][3]):

                if ((((data_list[pre_num][2]) - lowest) / tenR) + j > 20
                        or ((highest) - data_list[pre_num][1]) / tenR >= j):
                    print(end="         ")

                elif (j > (highest - data_list[pre_num][0]) / tenR and j <=
                      (highest - data_list[pre_num][3]) / tenR):
                    print(" ██dn", end="    ")

                else:
                    print("  |  ", end="    ")
            else:

                if ((((data_list[pre_num][2]) - lowest) / tenR) + j > 20
                        or ((highest) - data_list[pre_num][1]) / tenR >= j):
                    print(end="         ")

                elif (j <= (highest - data_list[pre_num][0]) / tenR and j >
                      (highest - data_list[pre_num][3]) / tenR):
                    print(" ██up", end="    ")
                else:
                    print("  |  ", end="    ")
        j = j + 1
        print(end="\n")
    print("\n")


#data_list[0] = [open, high, low, close]

#data_list = {}
#data_list[0] = 20, 40, 10, 30
#data_list[1] = 30, 50, 20, 40
#data_list[2] = 50, 60, 30, 40
#data_list[3] = 30, 40, 10, 20
#console_chart_v2(data_list)

