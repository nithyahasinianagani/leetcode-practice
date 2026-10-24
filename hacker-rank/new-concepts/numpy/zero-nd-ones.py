
#zeros and ones default type is float but ques is asked in int



import numpy as np

shape = tuple(map(int, input().split()))

print(np.zeros(shape, dtype=int))
print(np.ones(shape, dtype=int))
