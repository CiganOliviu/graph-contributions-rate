contributions = [919, 921, 935, 964, 973, 1000, 1012, 1014, 1023, 1076,
		  1090, 1130, 1145, 1155, 1167, 1194, 1237, 1278, 1302, 1320,
		  1330, 1341, 1350, 1357, 1365, 1375, 1383, 1402, 1414, 1429,
		  1451, 1458, 1613, 1638, 1735, 1760, 1783, 1806, 1830, 1840,
		  1862, 1875, 1887, 1897, 1912, 1941, 1967, 1975, 1995, 2048,
		  2098, 2135, 2146, 2186, 2221, 2236, 2257, 2269, 2278, 2334,
		  2362, 2376, 2426, 2446, 2478, 2480, 2510, 2552, 2564, 2627,
		  2656, 2711, 2733, 2772, 2817, 2833, 2874, 2906, 2946, 2952]

contributions_indexes = [i for i in range(len(contributions))]

# ====================================================================

predictions = [3005.2395209580836, 2996.041666666667, 3027.9881656804732, 3018.187134502924, 3032.4709302325577,
          	   3061.35838150289, 3040.9714285714285, 3345.142045454545, 3358.8202247191007, 3537.8491620111736,
               3568.888888888889, 3595.5524861878453, 3621.923076923077, 3630.1630434782605, 3630.27027027027,
               3653.924731182796, 3659.7593582887703, 3663.5904255319147, 3663.5185185185182, 3673.052631578947,
               3709.240837696335, 3739.348958333333, 3715.8505154639174, 3734.230769230769, 3813.8775510204077,
               3887.1573604060914, 3935.732323232323, 3936.1306532663316, 3989.45, 4033.1592039801, 4040.29702970297,
               4058.152709359606, 4059.7303921568628, 4055.9512195121947, 4135.485436893204, 4164.879227053139,
               4169.423076923077, 4236.794258373206, 4251.380952380952, 4266.367924528302, 4249.765258215963,
			   4281.07476635514, 4312.407407407408, 4332.685185185185, 4418.6866359447, 4446.97247706422,
			   4518.333333333334, 4534.295454545454, 4578.190045248869, 4631.554054054054, 4636.973094170404,
			   4683.080357142857, 4714.177777777778, 4757.9203539823, 4746.607929515419]

predictions_indexes = [i for i in range(len(predictions))]

# ====================================================================

rates =   [8.014705882352942, 8.18840579710145, 8.184397163120567, 8.21830985915493, 8.284722222222221,
		   8.53103448275862, 8.635135135135135, 8.68, 8.68421052631579, 8.525641025641026, 8.433962264150944,
		   8.231707317073171, 8.218181818181819, 8.22289156626506, 8.233532934131736, 8.208333333333334,
		   8.29585798816568, 8.269005847953217, 8.30813953488372, 8.38728323699422, 8.331428571428571,
		   9.164772727272727, 9.202247191011235, 9.692737430167599, 9.777777777777779, 9.850828729281767,
		   9.923076923076923, 9.945652173913043, 9.945945945945946, 10.010752688172044, 10.026737967914439,
		   10.037234042553191, 10.037037037037036, 10.063157894736841, 10.162303664921465, 10.244791666666666,
		   10.18041237113402, 10.23076923076923, 10.448979591836734, 10.649746192893401, 10.782828282828282,
		   10.78391959798995, 10.93, 11.049751243781095, 11.069306930693068, 11.118226600985222, 11.122549019607844,
		   11.112195121951219, 11.330097087378642, 11.41062801932367, 11.423076923076923, 11.607655502392344,
		   11.647619047619047, 11.68867924528302, 11.64319248826291, 11.728971962616823, 11.814814814814815,
		   11.87037037037037, 12.105990783410139, 12.18348623853211, 12.378995433789955, 12.422727272727272,
		   12.542986425339366, 12.68918918918919, 12.704035874439462, 12.830357142857142, 12.915555555555555,
		   13.035398230088495, 13.004405286343612]

rates_indexes = [i for i in range(len(rates))]

# ====================================================================

contributions_last_month = contributions[-30:]

contributions_indexes_last_month = [i for i in range(len(contributions_last_month))]

# ====================================================================

predictions_last_month = predictions[-30:]

predictions_indexes_last_month = [i for i in range(len(predictions_last_month))]

# ====================================================================

rates_last_month = rates[-30:]

rate_indexes_last_month = [i for i in range(len(rates_last_month))]

# ====================================================================

contributions_last_week = contributions[-7:]

contributions_indexes_last_week = [i for i in range(len(contributions_last_week))]

# ====================================================================

predictions_last_week = predictions[-7:]

predictions_indexes_last_week = [i for i in range(len(predictions_last_week))]

# ====================================================================

rates_last_week = rates[-7:]

rate_indexes_last_week = [i for i in range(len(rates_last_week))]

# ====================================================================
