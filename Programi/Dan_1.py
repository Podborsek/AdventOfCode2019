dat = open("D1N1.txt", "r")
sez = dat.read().split("\n")
enostavna = 0
for x in sez:
    x = int(x)
    enostavna += (x // 3) - 2
print(enostavna)

def gorivo(n):
    return ((n // 3) - 2)


neki = 4442231
tezja = 0
for x in sez:
    x = int(x)
    t = gorivo(x)
    n = t
    while 0 < gorivo(n):
        n = gorivo(n)
        t += n
    tezja += t

print(tezja)


