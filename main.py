import matplotlib.pyplot as plt
import sklearn.datasets as sl
import sklearn.linear_model as lm

input_data = sl.fetch_california_housing(as_frame=True)

learning_regression = lm.LinearRegression()
learning_regression.fit(input_data.data, input_data.target)

print("b0 = " + str(learning_regression.intercept_))
for i in range(0, learning_regression.coef_.size):
    print("b" + str(i + 1) + " = " + str(learning_regression.coef_[i]))

for i in range(0, input_data.data.shape[1]):
    data = {'a': input_data.data.iloc[:, i],
            'b': input_data.target,
            'd': 0.05}
    plt.scatter('a', 'b', s='d', data=data)
    plt.xlabel("x" + str(i + 1))
    plt.ylabel('y')
    plt.savefig("graph.png")
    plt.show()
