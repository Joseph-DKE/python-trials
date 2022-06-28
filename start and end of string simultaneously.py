s = " "
s = s.lower()
possibilities = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

length_of_string = len(s)
middle_of_string = int(length_of_string / 2)
last_item_in_string = length_of_string - 1
dict_of_nonalpha_chars = {}
i_check = False
last_check = False
position_i = 0
position_last = 0

if middle_of_string * 2 == length_of_string:
    for i in range(middle_of_string):
        if s[i].isalnum() == False:
            dict_of_nonalpha_chars[s[i]] = True
        if s[last_item_in_string].isalnum() == False:
            dict_of_nonalpha_chars[s[last_item_in_string]] = True
        last_item_in_string -= 1
    for key in dict_of_nonalpha_chars:
        s = s.replace(key, '')
else:
    for i in range(middle_of_string + 1):
        if s[i].isalnum() == False:
            dict_of_nonalpha_chars[s[i]] = True
        if s[last_item_in_string].isalnum() == False and last_item_in_string > middle_of_string:
            dict_of_nonalpha_chars[s[last_item_in_string]] = True
        last_item_in_string -= 1
    for key in dict_of_nonalpha_chars:
        s = s.replace(key, '')
        
reversed_s = s[::-1]
if s == reversed_s:
    print(True)
else:
    print(False)