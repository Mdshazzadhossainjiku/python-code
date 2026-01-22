#You are given the weight of a watermelon, represented by an integer n.
#You need to determine whether it is possible to divide the watermelon into two parts, such that:
#Both parts have even weights, and
#Each part has a positive weight greater than zero.
#Print "YES" if such a division is possible, otherwise print "NO"

w = int(input())

if w > 2 and w % 2 == 0:
    print("YES")
else:
    print("NO")
