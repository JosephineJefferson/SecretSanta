import random

names = []
with open("names.txt") as namefile:
    names = namefile.read().splitlines()
    print("Generating random Santa assignments for:\n",names)
num_santas = len(names)
receive = []

while True:
    giftees = list(range(0,num_santas))
    doubleup = False
    for n in range(0,num_santas):
        #print("Santa: ", names[n])
        giftee_idx = random.randint(0,len(giftees)-1)
        giftee = giftees[giftee_idx]
        if n==giftee:
            doubleup = True
        #print("To: ", names[giftee], "\n")
        receive.append(names[giftee])
        giftees.pop(giftee_idx)
    if doubleup:
        receive = []
        print("\nDOUBLE UP - retrying\n")
        doubleup = False
    else:
        print("Done. No peeking! Always remember that real Santa sees you when you are sleeping.")
        break

fpath = "results/"
for idx in range(0,num_santas):
    with open(fpath+names[idx]+".txt", "w") as thefile:
        thefile.write(receive[idx])