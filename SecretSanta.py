import random

def get_names(filename = "names.txt"):
    names = []
    with open(filename) as namefile:
        names = namefile.read().splitlines()
        print("Generating random Santa assignments for:\n",names)
    return names

def assign_santas(names):
    num_santas = len(names)
    receivers = []

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
            receivers.append(names[giftee])
            giftees.pop(giftee_idx)
        if doubleup:
            receivers = []
            print("\nDOUBLE UP - retrying\n")
            doubleup = False
        else:
            print("Done. No peeking! Always remember that real Santa sees you when you are sleeping.")
            break
    return names, receivers

def make_files(names, receivers):
    fpath = "results/"
    for idx in range(0,len(names)):
        with open(fpath+names[idx]+".txt", "w") as thefile:
            thefile.write(receivers[idx])

def merry_xmas():
    names=get_names()
    both_lists = assign_santas(names)
    make_files(both_lists[0], both_lists[1])



if __name__ == "__main__":
    merry_xmas()