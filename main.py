#parse the string for brackets 
#implement stack in list
#append for open parenthesis
#pop for close parenthesis
#check if they form a pair




def parenthesis_validator(input_string):
    brackets=[]
    bracket_map={'{':'}','(':')','[':']'}
    for char in input_string:
        if char in ['(','{','[']:
            brackets.append(char)
        elif char in [')','}',']']:
            try: 
                last_element=brackets.pop() #(, char=)
                if bracket_map.get(last_element) == char:
                    continue
                else :
                    return False
            except IndexError:
                return False
    if brackets:       
        return False # if everything is validated
    else:
        return True

input_string=input()
print(parenthesis_validator(input_string))






