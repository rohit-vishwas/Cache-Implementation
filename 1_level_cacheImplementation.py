'''
Name:- Rohit Kumar Vishwas
Roll no.- 2019269
Project type:- Cache Implementation by various mapping
'''


def initial_work(dict, minbit):
    print("Enter 0: for Read")
    print("Enter 1: for Write")
    choice = int(input())
    check = True
    while check == True:
        print("Enter the address")
        first = input()
        if len(first) > minbit and first.count("0") + first.count("1") == len(first):
            check = False
        else:
            print("Enter word's bit is not appropriate take another chance")
    print("Enter data corresponding to the address")
    firstdata = input()
    dict[first] = firstdata
    if choice == 1:
        print("Cachemiss")
    work = True
    print("Do you want more operation.")
    print("Enter 0: for YES")
    print("Enter 1: for NO")
    furchoice = int(input())
    if furchoice == 1:
        work = False
    return first, work


def middle_work(dict, bit):
    print("Enter 0: for Read")
    print("Enter 1: for Write")
    choice = int(input())
    check = True
    while check == True:
        print("Enter the address")
        word = input()
        if len(word) == bit and word.count("0") + word.count("1") == len(word):
            check = False
        else:
            print("Enter word's bit is not appropriate take another chance")
    if word not in dict:
        print("Please enter data store at this address")
        worddata = input()
        dict[word] = worddata
    return word, choice


def last_work():
    work = True
    print("Do you want more operation.")
    print("Enter 0: for YES")
    print("Enter 1: for NO")
    furchoice = int(input())
    if furchoice == 1:
        work = False
    return work


def Direct_mapping(cache_size, line, blocksize, cachelist):
    dict = {}
    first, work = initial_work(dict, line + blocksize)
    bit = len(first)
    cachelist[int(first[(bit-line - blocksize):(bit - blocksize)], 2)
              ] = first[: (bit-line - blocksize)]
    while work == True:
        word, choice = middle_work(dict, bit)
        if cachelist[int(word[(bit-line - blocksize):(bit - blocksize)], 2)] != word[: (bit-line - blocksize)]:
            cachelist[int(word[(bit-line - blocksize):(bit - blocksize)], 2)
                      ] = word[: (bit-line - blocksize)]
            if choice == 1:
                print("Cachemiss")
        else:
            if choice == 1:
                print("Cachehit")
                print("Data corresponding to the address is :", dict[word])
        # print(cachelist)
        work = last_work()


def Associative_mapping(cache_size, line, blocksize, cachelist):
    dict = {}
    first, work = initial_work(dict, line + blocksize)
    bit = len(first)
    cachelist[0] = first[: bit - blocksize]
    while work == True:
        word, choice = middle_work(dict, bit)
        tag = word[: bit - blocksize]
        for t in range(2 ** line):
            if t == len(cachelist) - 1 and cachelist[t] != tag and cachelist[t] != "Null":
                cachelist.pop(0)
                cachelist.append(tag)
                if choice == 1:
                    print("Cachemiss")
            else:
                if cachelist[t] == tag:
                    if choice == 1:
                        print("Cachehit")
                        print("Data corresponding to the address is :",
                              dict[word])
                    break
                if cachelist[t] == "Null":
                    if choice == 1:
                        print("Cachemiss")
                    cachelist[t] = tag
                    break
        # print(cachelist)
        work = last_work()


def nway_set_associative(cache_size, line, blocksize, cachelist):
    dict = {}
    check3 = True
    while check3 == True:
        print("Enter the number you want split your set where number is in terms of log(n)")
        n = int(input())
        if line > n:
            check3 = False
        else:
            print(
                "Enter number is greater than the given cache line is not allowed. Do it again")
    cachelist = []
    cache_length = (2 ** line) // (2 ** n)
    # print(cache_length)
    for k in range(cache_length):
        cachelist1 = []
        for k in range(2 ** n):
            cachelist1.append("Null")
        cachelist.append(cachelist1)
    first, work = initial_work(dict, line + blocksize)
    bit = len(first)
    cachelist[int(first[: bit - blocksize], 2) %
              (2 ** n)][0] = first[: bit - blocksize]
    print(cachelist)
    while work == True:
        word, choice = middle_work(dict, bit)
        tag = word[: bit - blocksize]
        middle = int(word[: bit - blocksize], 2) % (cache_length)
        for t in range(2 ** n):
            if t == len(cachelist[middle]) - 1 and cachelist[middle][t] != tag and cachelist[middle][t] != "Null":
                cachelist[middle].pop(0)
                cachelist[middle].append(tag)
                if choice == 1:
                    print("Cachemiss")
            else:
                if cachelist[middle][t] == tag:
                    if choice == 1:
                        print("Cachehit")
                        print("Data corresponding to the address is :",
                              dict[word])
                    break
                if cachelist[middle][t] == "Null":
                    if choice == 1:
                        print("Cachemiss")
                    cachelist[middle][t] = tag
                    break
        print(cachelist)
        work = last_work()


check1 = True
while check1 == True:
    print("Enter Cache size in terms of bit")
    cache_size = int(input())
    print("Enter length of Cache in terms of bit ")
    line = int(input())
    print("Enter block size in terms of bit")
    blocksize = int(input())
    if cache_size > line:
        check1 = False
    else:
        print("You enter data is not appropriate. Do again")
cachelist = []
for k in range(2 ** line):
    cachelist.append("Null")
print("Choose one of the number from below type of mapping")
print("Enter : 1 for Direct Mapping")
print("Enter : 2 for Associative memory")
print("Enter : 3 for n-way set associative memory")
maping = int(input())
if maping == 1:
    Direct_mapping(cache_size, line, blocksize, cachelist)
elif maping == 2:
    Associative_mapping(cache_size, line, blocksize, cachelist)
else:
    nway_set_associative(cache_size, line, blocksize, cachelist)
