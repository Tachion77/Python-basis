integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
binary_dict = dict(zip(integer, binary))
print(binary_dict)
additive_inverse = [-1*i for i in integer]
print(additive_inverse)
integer2 = [1, -1, 2, -2, 3, -3]
sq_set = {i*i for i in integer2}
print(sq_set)