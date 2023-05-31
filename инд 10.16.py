import random
def QuickSort(a):
    if len(a) <= 1:
        return a
    else:
        q = random.choice(a)
        l = []
        m = []
        r = []
        for elem in a:
            if elem < q:
                l.append(elem) 
            elif elem > q: 
                r.append(elem) 
            else: 
                m.append(elem)
        return QuickSort(l) + m + QuickSort(r)
a = [random.randint(1, 50) for i in range(15)]
print(a)
print(QuickSort(a))