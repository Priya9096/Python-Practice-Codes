def count_substring(main_str, sub_str):
    count = 0
    n = len(main_str)-len(sub_str)+1
    for i in range(n):
        if(sub_str == main_str[i:i+len(sub_str)]):
            count+=1
    return count
