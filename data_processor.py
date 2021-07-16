import sys
from data_source import contributions
from data_source import predictions
from data_source import rates


def get_max_value(data):

	result = 0

	for item in data:
		if result < item:
			result = item

	return result


def get_min_value(data):

	result = sys.maxsize 

	for item in data:
		if result > item:
			result = item

	return result


def get_rates_difference(data):

	return get_max_value(data) - get_min_value(data)


def get_last_week_data(data):

	return data[-7:]


def get_last_month_data(data):

	return data[-30:]


def list_info():
	print("Max value for contributions " + str(get_max_value(contributions)))
	print("Max value for predictions " + str(get_max_value(predictions)))
	print("Max value for rates " + str(get_max_value(rates)))
	print()
	print("Min value for contributions " + str(get_min_value(contributions)))
	print("Min value for predictions " + str(get_min_value(predictions)))
	print("Min value for rates " + str(get_min_value(rates)))
	print()
	print("Rates difference " + str(get_rates_difference(rates)))
	print()
	print(contributions[-7:])
	print(predictions[-7:])
	print(rates[-7:])

if __name__ == '__main__':
	list_info()