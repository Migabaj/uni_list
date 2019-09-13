def print_out_phrase(uni, phrase):
    i = 0
    one_atatime = []
    
    for e, letter in enumerate(uni):
        if i <= len(phrase) - 1:
            if phrase[i] == letter:
                i += 1
                one_atatime.append(uni[:e] + letter.upper() + uni[e + 1:])
                
    for one in one_atatime:
        for n, letter in enumerate(one):
            if letter != uni[n]:
                uni = uni[:n] + letter.upper() + uni[n + 1:]
    
    return uni

def find_phrase(uni, phrase):
    i = 0
    duplicate = ''
    
    for letter in uni:
        if i <= len(phrase) - 1:
            if phrase[i] not in uni:
                return False
            elif phrase[i] == letter:
                duplicate += letter
                i += 1
    
    if duplicate == phrase:
        return True
    else:
        return False

def main():
    
    print(find_phrase(input(), input()))

if __name__ == '__main__':
    main()