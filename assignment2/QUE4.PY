A={34,56,78,90}
B={78,45,90,23}

print("set A",A)
print("set B",B)
#i 
union=A.union(B)
print("unique score achived by both teams",union)

#ii
intersection=A.intersection(B)
print("\n common score ",intersection)

#iii
symm_dif=A.symmetric_difference(B)
print("score excluive to each team",symm_dif)

#iv
print("Is A is a subset of B?",A.issubset(B))
print("Is B is a subset of A?",B.issuperset(A))

#v
x=int(input("enter score to remove from set A:"))
if x in A:
    A.remove(x)
    print("score",x,"removed from set A")
    print("updated A ",A)
else :
    print("score ",x,"is not present in set A.")