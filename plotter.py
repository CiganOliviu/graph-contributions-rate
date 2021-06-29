import matplotlib.pyplot as plt

plt.style.use('ggplot')

def plot_based_on_indexes_and_data(indexes, data_set_one):

	plt.plot(indexes, data_set_one)

	plt.show()


def plot_based_on_data_and_indexes(data_set_one, indexes):

	plt.plot(data_set_one, indexes)

	plt.show()