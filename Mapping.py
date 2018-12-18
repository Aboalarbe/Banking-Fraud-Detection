def transform_type(val):
	if val == 'payment':
		return 3
	elif val == 'transfer':
		return 4
	elif val == 'cash_out':
		return 1
	elif val == 'cash_in':
		return 0
	elif val == 'debit':
		return 2
	else:
		return 0
def transform_nameDest(val):
	dest = val[0]
	if dest == 'M':
		return 1
	elif dest == 'C':
		return 0
	else:
		return 0