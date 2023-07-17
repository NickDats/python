a1 = "WorldChanges"
a2 = "WorldChanges"
a3 = "WorldChanges"

print('a1:', a1, ' type:', str(type(a1)), ' id:', str(id(a1)))
print('a2:', a2, ' type:', str(type(a2)), ' id:', str(id(a2)))
print('a3:', a3, ' type:', str(type(a3)), ' id:', str(id(a3)))

a1 = list(a1)
a2 = list(a2)
a3 = list(a3)
print('a1:', a1, ' type:', str(type(a1)), ' id:', str(id(a1)))
print('a2:', a2, ' type:', str(type(a2)), ' id:', str(id(a2)))
print('a3:', a3, ' type:', str(type(a3)), ' id:', str(id(a3)))

b1 = ['e', 2]
b2 = ['e', 2]
print('b1:', b1, ' type:', str(type(b1)), ' id:', str(id(b1)))
print('b2:', b2, ' type:', str(type(b2)), ' id:', str(id(b2)))

b1 = bool(b1)
b2 = bool(b2)
print('b1:', b1, ' type:', str(type(b1)), ' id:', str(id(b1)))
print('b2:', b2, ' type:', str(type(b2)), ' id:', str(id(b2)))
