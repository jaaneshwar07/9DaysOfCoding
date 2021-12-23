from collections import defaultdict

def panf(wrd):
    group=defaultdict(list)

    for w in wrd:
        group ["".join (sorted(w))].append(w)
    for g in group.values():
        print("".join(g))

wrd = ["cat","n","tac", "ggvmhv","act","taaa","1232"]
panf(wrd)
