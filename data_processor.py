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


print(get_max_value(contributions))
print(get_max_value(predictions))
print(get_max_value(rates))
print()
print(get_min_value(contributions))
print(get_min_value(predictions))
print(get_min_value(rates))