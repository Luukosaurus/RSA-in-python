import math
characters = {"a": "01","b": "02","c": "03","d": "04","e": "05","f": "06","g": "07","h": "08","i": "09","j": "10","k": "11","l": "12","m": "13","n": "14","o": "15","p": "16","q": "17","r": "18","s": "19","t": "20","u": "21","v": "22","w": "23","x": "24","y": "25","z": "26"," ": "27",".": "28",}
todo = input("Wat wil je doen 'versturen', 'ontvangen' of sleutel 'aanmaken' \n")
def isprime(number):
    top = math.ceil(math.sqrt(number))
    for i in range(2,top+1):
        if number%i == 0:
            return False
    return True
def isrelprime(k,pn):
    for j in range(2,k):
        if k%j == 0 and pn%j == 0:
            return False
    else:
        return True
def getrelprime(pn):
    for k in range(1,pn):
        if pn%k != 0:
            if isrelprime(k,pn):
                return k
def getjfast(k,pn):
    for i in range(100):
        if (1+i*pn)%k == 0:
            j = (1+i*pn)//k
            return j
def convert(tekst):
    messagelist = []
    for letter in tekst:
        numberstring = characters[letter]
        messagelist.append(numberstring)
    print(messagelist)
    convertedtekst = ''.join(messagelist)
    return convertedtekst
def revert(convertedtekst):
    messagelist = []
    if len(convertedtekst)%2 != 0:
        convertedtekst = "0"+convertedtekst
    x=2
    res=[convertedtekst[y-x:y] for y in range(x, len(convertedtekst)+x,x)]
    for i in res:
        messagelist.append(list(characters.keys())[list(characters.values()).index(i)])
    message = ''.join(messagelist)
    return message
def decriptfaster(b,e,m):
    if m == 1:
        return 0
    else:
        r = 1
        b = b % m
        while e > 0:
            if e % 2 == 1:
                r = (r*b) % m
            b = (b*b) % m
            e = e >> 1
    return r
if todo in "versturen":
    n = int(input("Wat is de eerste waarde van de publieke sleutel? "))
    k = int(input("Wat is de tweede waarde van de publieke sleutel? "))
    m = int(convert(input("Wat wil je versturen?\n")))
    while m >= n:
        print("Je bericht getal mag niet groter zijn dan de n waarde")
        m = int(convert(input("Wat wil je versturen?\n")))
    r = m**k+n
    print(f"Je versleutelde bericht is:\n{r}")
if todo in "ontvangen":
    p = int(input("Wat is de eerste waarde van je prive sleutel? "))
    q = int(input("Wat is de tweede waarde van je prive sleutel? "))
    r = int(input("Wat is het bericht dat je wilt ontvangen? \n"))
    pn = (p-1)*(q-1)
    n = p*q
    k = getrelprime(pn)
    j = getjfast(k,pn)
    m = decriptfaster(r,j,n)
    message = revert(str(m))
    print(f"Het ontvangen bericht is: {message}.")
if todo in "aanmaken":
    p = int(input("Wat is de eerste waarde van je prive sleutel? "))
    while isprime(p) == False:
        print("Je eerste waarde moet een priem getal zijn")
        p = int(input("Wat is de eerste waarde van je prive sleutel? "))
    q = int(input("Wat is de tweede waarde van je prive sleutel? "))
    while isprime(q) == False or p == q:
        print("Je tweede waarde moet een uniek priem getal zijn")
        q = int(input("Wat is de tweede waarde van je prive sleutel? "))
    n = p*q
    pn = (p-1)*(q-1)
    k = getrelprime(pn)
    print(f"Je publieke sleutel is({n},{k})")