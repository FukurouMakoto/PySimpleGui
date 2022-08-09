def km_to_mile(x):
	def result(x):
		return int(x) * 0.621371 
	return f'{x} kilometers is equal to {result(x):.2f} miles.'

def mile_to_km(x):
	def result(x):
		return int(x) / 0.621371
	return f'{x} miles is equal to {result(x):.2f} kilometers.'

def sec_to_min(x):
	def result(x):
		return int(x) / 60
	return f'{x} seconds is equal to {result(x):.2f} minutes.'

def min_to_sec(x):
	def result(x):
		return int(x) * 60
	return f'{x} minutes is equal to {result(x):.2f} seconds.'

def min_to_hrs(x):
	def result(x):
		return int(x) / 60
	return f'{x} minutes is equal to {result(x):.2f} hours.'

def meter_to_ft(x):
	def result(x):
		return int(x) * 3.281
	return f'{x} meters is equal to {result(x):.2f} feet.'

def ft_to_meter(x):
	def result(x):
		return int(x) / 3.281
	return f'{x} feet is equal to {result(x):.2f} meters.'
if __name__ == "__main__":
	main()

