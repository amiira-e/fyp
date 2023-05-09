def findDecision(obj): #obj[0]: type, obj[1]: amount_category
	# {"feature": "type", "instances": 50, "metric_value": 0.0, "depth": 1}
	if obj[0] == 'PAYMENT':
		return '0'
	elif obj[0] == 'CASH_OUT':
		return '0'
	elif obj[0] == 'CASH_IN':
		return '0'
	elif obj[0] == 'TRANSFER':
		return '0'
	else: return '0'
