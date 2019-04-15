def convert_string_to_1letter_number(entered_string, vietnam_number_letter):
    flag = False
    if entered_string in vietnam_number_letter:
        flag = True
        return vietnam_number_letter.get(entered_string)
    else:
        return flag

def convert_string_to_2letters_number(entered_string, vietnam_number_letter):
    chuc = 0
    don_vi = 0
    chuc_string = None
    don_vi_string = None
    flag = True
    if(len(entered_string.split()) == 2):
        chuc_string = entered_string.split()[0]
        don_vi_string = entered_string.split()[1]
    elif (len(entered_string.split()) == 3):
        chuc_string = entered_string.split()[0]
        don_vi_string = entered_string.split()[2]
        flag = False if entered_string.split()[1] != 'mươi' else True
        # for example: hai hai hai

    if flag == True:
        if chuc_string in vietnam_number_letter and chuc_string == 'mười':
            chuc = 1
            #for example: mười lăm
            if don_vi_string == 'lăm':
                don_vi = 5
                flag = True
            elif don_vi_string in vietnam_number_letter and don_vi_string != 'năm' and don_vi_string != 'mười':
                don_vi = vietnam_number_letter.get(don_vi_string)
                flag = True
                #for example: mười năm, mười mười, mười
            else:
                flag = False
                #for example: abc lăm, 678 một
        elif chuc_string in vietnam_number_letter and chuc_string != 'mười' and chuc_string != 'không' and chuc_string != 'một':
            #for example : hai mươi, hai mươi mốt, hai mươi tư, hai mươi lăm
            chuc = vietnam_number_letter.get(chuc_string)
            if don_vi_string == 'lăm':
                don_vi = 5
                flag = True
            elif don_vi_string == 'mốt':
                don_vi = 1
                flag = True
            elif don_vi_string == 'tư':
                don_vi = 4
                flag = True
            elif don_vi_string == 'năm' or don_vi_string == 'bốn' or don_vi_string == 'một' or don_vi_string == 'mười' or don_vi_string == 'không':
                flag = False
                #for example: hai mươi năm, hai mươi bốn, ba mươi một, một mươi hai
            elif don_vi_string in vietnam_number_letter and flag == True:
                don_vi = vietnam_number_letter.get(don_vi_string)
                flag = True
        else:
            flag = False
            #for example: 678 mười, ...

    if flag == True:
        return chuc * 10 + don_vi
    else:
        return flag

def convert_string_to_3letters_number(entered_string, vietnam_number_letter):
    tram_string, chuc_string, don_vi_string = None, None, None
    tram, chuc, don_vi, result_of_2letters_number = 0, 0, 0, 0
    flag = True
    # for example: một trăm, hai trăm, mười trăm
    if len(entered_string.split()) == 2:
        tram_string = entered_string.split()[0]
        chuc_string = entered_string.split()[1]
        if tram_string != 'mười' and tram_string != 'không' and tram_string in vietnam_number_letter:
            tram = vietnam_number_letter.get(tram_string)
            if chuc_string == 'trăm':
                return tram*100
            else:
                flag = False
                return flag
        else:
            flag = False
            #for example: trăm trăm, chin trăm, jfhs trăm
    if (len(entered_string.split()) == 3):
        #for example: một trăm mười, bảy trăm mười
        tram_string = entered_string.split()[0]
        chuc_string = entered_string.split()[2]
        if tram_string != 'mười' and entered_string.split()[1] == 'trăm' and chuc_string == 'mười'\
                and tram_string in vietnam_number_letter and chuc_string in vietnam_number_letter:
            tram = vietnam_number_letter.get(tram_string)
            chuc = 10
            return tram*100 + chuc
        else: flag = False
        flag = False if entered_string.split()[1] != 'trăm' else True
        #for example: hai năm trăm, hai năm năm
        return flag
    if (len(entered_string.split()) == 4):
        #for example: một trăm hai ba
        tram_string = entered_string.split()[0]
        chuc_string = entered_string.split()[2]
        don_vi_string = entered_string.split()[3]
        flag = False if entered_string.split()[1] != 'trăm' else True
    elif (len(entered_string.split()) == 5):
        # for example: một trăm hai mươi ba
        tram_string = entered_string.split()[0]
        chuc_string = entered_string.split()[2]
        don_vi_string = entered_string.split()[4]
        flag = False if entered_string.split()[1] != 'trăm' else True
        flag = False if entered_string.split()[3] != 'mươi' else True
    else: flag = False

    if flag == True:
        if tram_string in vietnam_number_letter and tram_string != 'mười':
            tram = vietnam_number_letter.get(tram_string)
            if chuc_string == 'linh':
                # for example: một trăm linh lăm, một trăm linh bốn
                chuc = 0
                if don_vi_string == 'lăm':
                    don_vi = 5
                    flag = True
                elif don_vi_string == 'tư':
                    don_vi = 4
                    flag = True
                elif don_vi_string == 'năm' or don_vi_string == 'bốn' or don_vi_string == 'mười' or don_vi_string == 'không':
                    flag = False
                elif don_vi_string in vietnam_number_letter and flag == True:
                    don_vi = vietnam_number_letter.get(don_vi_string)
                else: flag = False
                result_of_2letters_number = chuc*10 + don_vi
            if chuc_string == 'lẻ':
                # for example: một trăm lẻ bốn, một trăm lẻ lăm
                chuc = 0
                if don_vi_string == 'lăm':
                    don_vi = 5
                    flag = True
                elif don_vi_string == 'năm' or don_vi_string == 'mười' or don_vi_string == 'không':
                    flag = False
                elif don_vi_string in vietnam_number_letter and flag == True:
                    don_vi = vietnam_number_letter.get(don_vi_string)
                else: flag = False
                result_of_2letters_number = chuc*10 + don_vi
            elif chuc_string in vietnam_number_letter:
                start_split_string = len(tram_string) + len('trăm') + 2
                letters_number_string = entered_string[start_split_string:]
                if convert_string_to_2letters_number(letters_number_string, vietnam_number_letter) == False:
                    flag = False
                else:
                    result_of_2letters_number = convert_string_to_2letters_number(letters_number_string, vietnam_number_letter)
                    flag = True
            elif chuc_string in vietnam_number_letter == False and chuc_string != 'linh' and chuc_string != 'lẻ':
                flag = False
        elif tram_string == 'mười':
            flag = False
    if flag == True:
        return tram*100 + result_of_2letters_number
    else: return flag


loop_quantity = eval(input("Enter the quantity of tested number: "))
index = 0
while index < loop_quantity:
    entered_string = input("Enter number in letter format: ")
    split_entered_string = entered_string.split()
    vietnam_number_letter={'không':0, 'một':1, 'hai':2, 'ba':3, 'bốn':4, 'năm':5, 'sáu':6, 'bảy':7,
                           'tám':8, 'chín':9, 'mười':10}

    if len(split_entered_string) == 1:
        if convert_string_to_1letter_number(entered_string, vietnam_number_letter) == False:
            print('None exist number')
        else: print(convert_string_to_1letter_number(entered_string, vietnam_number_letter))
    elif (len(split_entered_string) == 3 or len(split_entered_string) == 2) and ('trăm' in split_entered_string) == False:
        if convert_string_to_2letters_number(entered_string, vietnam_number_letter) == False:
            print('None exist number')
        else:
            print(convert_string_to_2letters_number(entered_string, vietnam_number_letter))
    else:
        if convert_string_to_3letters_number(entered_string, vietnam_number_letter) == False:
            print('None exist number')
        else:
            print(convert_string_to_3letters_number(entered_string, vietnam_number_letter))
    index+=1