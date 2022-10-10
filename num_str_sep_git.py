def num_str_sep_git(string, result=[]):
    n = "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
    i = 0
    while i < len(string):
        if string[i] in n:
            level = string[i]
            i+=1
            if i < len(string):
                while string[i] in n:
                    level = level+string[i]
                    i+=1
                    if i == len(string):
                        break
                result.append(level)
            else:
                result.append(level)
                break
        if i < len(string):
            if string[i] not in n:
                level = string[i]
                result.append(level)
            i+=1
    result = ",".join(result)
    return result


a = input("Enter the string : ")
print(num_str_sep_git(a))
