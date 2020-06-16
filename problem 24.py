import itertools
#Generate perms
perms = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))
perms.sort()
#Pick the millionth
print(perms[999999])
