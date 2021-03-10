import sklearn.datasets as sl
import sklearn.linear_model as lm

input_data = sl.fetch_california_housing(as_frame=True)

learning_regression = lm.LinearRegression()
learning_regression.fit(input_data.data, input_data.target)

