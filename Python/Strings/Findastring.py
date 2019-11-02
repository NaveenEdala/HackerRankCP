def count_substring(string, sub_string):
    lol = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            lol+=1
    return lol

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
