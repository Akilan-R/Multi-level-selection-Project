import numpy as np
test_array = np.array([{"C1":5, "C2":10} , {"C1":5, "C2":10}])
zero_array = np.zeros(2)
print(zero_array[1])
print(test_array)

zero_array[1] = [{"C1":5, "C2":10}]


#why even store it, why don't IZ jjst

#
# for i in range(len(zero_array)):
#     zero_array[i] =
#


print(zero_array)

