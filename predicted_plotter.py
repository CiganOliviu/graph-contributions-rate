from plotter import plot_based_on_data
import matplotlib.pyplot as plt

plt.style.use('ggplot')

indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

predictions = [3005.2395209580836, 2996.041666666667, 3027.9881656804732, 3018.187134502924, 3032.4709302325577,
          	   3061.35838150289, 3040.9714285714285, 3345.142045454545, 3358.8202247191007, 3537.8491620111736,
               3568.888888888889]

plt.plot(indexes, predictions)

plt.show()
