from linear_model_generation import *

import matplotlib.pyplot as plt

print("b0 = " + str(learning_regression.intercept_))
for i in range(0, learning_regression.coef_.size - 1):
    print("b" + str(i + 1) + " = " + str(learning_regression.coef_[i]))

for i in range(0, input_data.data.shape[1]):
    data = {'a': input_data.data.iloc[:, i],
            'b': input_data.target,
            'd': 0.05}
    plt.scatter('a', 'b', s='d', data=data)
    plt.xlabel(i)
    plt.ylabel('y')
    plt.savefig("graph.png")
    plt.show()
