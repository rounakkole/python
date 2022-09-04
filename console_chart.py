def print_chart(data_list):

    print("\n")
    j = 1
    list_len = len(data_list)

    while (j <= 10 and list_len > 1):

        for pre_num in range(0, list_len):
            tenR = (data_list[pre_num][1] - data_list[pre_num][2]) / 10

            if (data_list[pre_num][0] > data_list[pre_num][3]):
                if (j > (data_list[pre_num][1] - data_list[pre_num][0]) / tenR
                        and j <
                    (data_list[pre_num][1] - data_list[pre_num][3]) / tenR):
                    print(" ██dn", end="    ")
                else:
                    print("  |  ", end="    ")
            else:
                if (j < (data_list[pre_num][1] - data_list[pre_num][0]) / tenR
                        and j >
                    (data_list[pre_num][1] - data_list[pre_num][3]) / tenR):
                    print(" ██up", end="    ")
                else:
                    print("  |  ", end="    ")
        j = j + 1
        print(end="\n")
    print("\n")


    #from console_chart import print_chart
    #data_list = {}
    #data_list [0]= open, high, low, close
    #print_chart(#data_list)

    #not to scale
