a={1,2,3,4,5}
b={4,5,6,7,8}
a.union(b)# gives union of 2 sets but no change in set to change use update
a.update(b)
a.intersection(b)
a.intersection_update(b)
a.symmetric_difference(b)#gives unique values
a.symmetric_difference_update(b)
a.difference(b)#a-b
a.difference_update(b)
a.isdisjoint(b)#there is no duplicates
a.issubset(b)
b.issuperset(a)
a.add(12)
a.remove(12)#error if not present
a.discard(12)#no error
a.pop()#random delete
del a
b.clear()