'''
Name:- Rohit Kumar Vishwas
Roll no.- 2019269
Project type:- 2 level Cache Implementation by various mapping
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


def Direct_mapping(cache_size, line, blocksize, cachelist1, cachelist2):
    dict = {}
    first, work = initial_work(dict, line + blocksize)
    bit = len(first)
    cachelist1[int(first[(bit-(line // 2) - blocksize)
                   :(bit - blocksize)], 2)] = first[: (bit - blocksize)]
    while work == True:
        word, choice = middle_work(dict, bit)
        bool1 = False
        bool2 = False
        if cachelist1[int(word[(bit-(line // 2) - blocksize):(bit - blocksize)], 2)] == word[: (bit - blocksize)]:
            bool1 = True
        if cachelist2[int(word[(bit - line - blocksize):(bit - blocksize)], 2)] == word[: (bit - blocksize)]:
            cachelist2[int(word[(bit - line - blocksize)
                           :(bit - blocksize)], 2)] = "Null"
            bool2 = True
        if bool1 == True:
            if choice == 1:
                print("Cachehit")
                print("Data corresponding to the address is :", dict[word])
        elif bool2 == True:
            store1 = word[: (bit - blocksize)]
            store2 = cachelist1[int(
                word[(bit-(line // 2) - blocksize):(bit - blocksize)], 2)]
            cachelist1[int(word[(bit-(line // 2) - blocksize)
                           :(bit - blocksize)], 2)] = store1
            cachelist2[int(store2[bit - line - blocksize], 2)] = store2
            if choice == 1:
                print("Cachehit")
                print("Data corresponding to the address is :", dict[word])
        else:
            store1 = word[: (bit - blocksize)]
            if cachelist1[int(word[(bit-(line // 2) - blocksize):(bit - blocksize)], 2)] == "Null":
                cachelist1[int(word[(bit-(line // 2) - blocksize)
                               :(bit - blocksize)], 2)] = store1
            else:
                store2 = cachelist1[int(
                    word[(bit-(line // 2) - blocksize):(bit - blocksize)], 2)]
                cachelist1[int(word[(bit-(line // 2) - blocksize)
                               :(bit - blocksize)], 2)] = store1
                cachelist2[int(
                    store2[bit - line - blocksize: bit - blocksize], 2)] = store2
            if choice == 1:
                print("Cachemiss")
        print(cachelist1)
        print("-----------###############----------------")
        print(cachelist2)
        work = last_work()


def Associative_mapping(cache_size, line, blocksize, cachelist1, cachelist2):
    dict = {}
    minbit = line + blocksize
    first, work = initial_work(dict, minbit)
    bit = len(first)
    cachelist1[0] = first[: (bit - blocksize)]
    while work == True:
        word, choice = middle_work(dict)
        bool1 = False
        bool2 = False
        for t in range((2 ** line) // 2):
            if cachelist1[t] == word[: (bit - blocksize)]:
                bool1 = True
            if cachelist1[t] == "Null":
                break
        for t in range(2 ** line):
            if cachelist2[t] == word[: (bit - blocksize)]:
                bool2 = True
                cachelist2.pop(t)
                cachelist2.append("Null")
            if cachelist2[t] == "Null":
                break
        if bool1 == True:
            if choice == 1:
                print("Cachehit")
                print("Data corresponding to the address is :", dict[word])
        elif bool2 == True:
            if choice == 1:
                print("Cachehit")
                print("Data corresponding to the address is :", dict[word])
            store1 = cachelist1.pop(0)
            cachelist1.append(word[: (bit - blocksize)])
            cachelist2[cachelist2.index("Null")] = store1

        else:
            if choice == 1:
                print("Cachemiss")
            if cachelist2.count("Null") == len(cachelist2):
                if cachelist1.count("Null") > 0:
                    cachelist1[cachelist1.index(
                        "Null")] = word[: (bit - blocksize)]
                else:
                    cachelist2[0] = cachelist1.pop(0)
                    cachelist1.append(word[: (bit - blocksize)])
            elif cachelist2.count("Null") > 0:
                cachelist2[cachelist2.index("Null")] == cachelist1.pop(0)
                cachelist1.append(word[: (bit - blocksize)])
            else:
                cashelist2.pop(0)
                cashelist2.append(cachelist1.pop(0))
                cachelist1.append(word[: (bit - blocksize)])
        print(cachelist1)
        print("-----------###############----------------")
        print(cachelist2)
        work = last_work()


def nway_set_associative(cache_size, line, blocksize, cachelist1, cachelist2):
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
    cachelist1 = []
    cachelist2 = []
    cache_length1 = ((2 ** line) // 2) // (2 ** n)
    cache_length2 = (2 ** line) // (2 ** n)
    #print(cache_length1, cache_length2)
    for k in range(cache_length1):
        cachelist3 = []
        for k in range(2 ** n):
            cachelist3.append("Null")
        cachelist1.append(cachelist3)
    for j in range(cache_length2):
        cachelist4 = []
        for k in range(2 ** n):
            cachelist4.append("Null")
        cachelist2.append(cachelist4)
    print(cachelist1, cachelist2)
    first, work = initial_work(dict, line + blocksize)
    bit = len(first)
    cachelist1[int(first[: bit - blocksize], 2) %
               (2 ** n)][0] = first[: bit - blocksize]
    while work == True:
        word, choice = middle_work(dict, bit)
        tag = word[: bit - blocksize]
        middle1 = int(word[: bit - blocksize], 2) % (cache_length1)
        middle2 = int(word[: bit - blocksize], 2) % (cache_length2)
        bool1 = False
        bool2 = False
        for t in range(2 ** n):
            if cachelist1[middle1][t] == tag:
                bool1 = True
        for t in range(2 ** n):
            if cachelist2[middle2][t] == tag:
                bool2 = True
                cachelist2[middle2].pop(t)
                cachelist2[middle2].append("Null")
        if bool1 == True:
            if choice == 1:
                print("Cachehit")
                print("Data corresponding to the address is :", dict[word])
        elif bool2 == True:
            if choice == 1:
                print("Cachehit")
                print("Data corresponding to the address is :", dict[word])
            store1 = cachelist1[middle1].pop(0)
            cachelist1[middle1].append(tag)
            middle4 = int(store1[: bit - blocksize], 2) % (cache_length2)
            if cachelist2[middle4]. count("Null") > 0:
                cachelist2[middle4][cachelist2[middle4].index("Null")] = store1
            else:
                cachelist2[middle4].pop(0)
                cachelist2[middle4].append(store1)

        else:
            if choice == 1:
                print("Cachemiss")
            if cachelist1[middle1].count("Null") > 0:
                cachelist1[middle1][cachelist1[middle1].index("Null")] = tag
            else:
                store1 = cachelist1[middle1].pop(0)
                cachelist1[middle1].append(tag)
                middle4 = int(store1[: bit - blocksize], 2) % (cache_length2)
                if cachelist2[middle4]. count("Null") > 0:
                    cachelist2[middle4][cachelist2[middle4].index(
                        "Null")] = store1
                else:
                    cachelist2[middle4].pop(0)
                    cachelist2[middle4].append(store1)
        print(cachelist1)
        print("-----------###############----------------")
        print(cachelist2)
        work = last_work()


check1 = True
while check1 == True:
    print("Enter Cache size in terms of bit")
    cache_size = int(input())
    print("Enter length of Cache in terms of bit ")
    line = int(input())
    print("Enter block size in terms of bit")
    blocksize = int(input())
    if cache_size > line + blocksize:
        check1 = False
    else:
        print("You enter data is not appropriate. Do again")
cachelist1 = []
cachelist2 = []
for k in range((2 ** line) // 2):
    cachelist1.append("Null")
for k in range(2 ** line):
    cachelist2.append("Null")
print("Choose one of the number from below type of mapping")
print("Enter : 1 for Direct Mapping")
print("Enter : 2 for Associative memory")
print("Enter : 3 for n-way set associative memory")
maping = int(input())
if maping == 1:
    Direct_mapping(cache_size, line, blocksize, cachelist1, cachelist2)
elif maping == 2:
    Associative_mapping(cache_size, line, blocksize, cachelist1, cachelist2)
else:
    nway_set_associative(cache_size, line, blocksize, cachelist1, cachelist2)
