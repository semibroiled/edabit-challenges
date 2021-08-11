user_input = input('Type in here a sequence of numbers: ')
lst = list(user_input)
print(lst)

def count_boomerangs(lst):
    boomerCount = 0 #empty var tracker 
    indexCounter = 0
    for i,value in enumerate(lst):
        while int(i) < len(lst)-2:
            if lst[int(i)] == lst[int(i)+2] and lst[int(i)] != lst[int(i)+1]:
                 boomerCount += 1
    return boomerCount


#doesnt Work!!! But why.... 
#The task was to read how many boomerangs ie 656 767 there are in a list
#heres a version that works 


def count_boomerangsWorks(lst):
    boomerCount = 0
    countChocula = 0
    for i in lst: 
        if countChocula == len(lst)-2 : 
            return boomerCount
        elif lst[countChocula] == lst[countChocula+2] and lst[countChocula] != lst[countChocula +1]:
            boomerCount += 1
        countChocula += 1
    return boomerCount

print(count_boomerangsWorks(lst))