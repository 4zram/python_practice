def solv(s):
    b = s.split()
    for l in b:
        lis = l.capitalize() + " "
    return lis

if __name__ == '__main__':
    fptr = open("test.txt", 'a')
    s = input()
    result = solv(s)
    fptr.write(result + '\n')
    fptr.close()