def findDecision(obj): #obj[0]: type, obj[1]: step_cluster, obj[2]: amount_cluster
	# {"feature": "amount_cluster", "instances": 968264, "metric_value": 2030.9905, "depth": 1}
	if obj[2] == '100k-500k':
		# {"feature": "step_cluster", "instances": 350217, "metric_value": 1201.1383, "depth": 2}
		if obj[1] == '187-372':
			# {"feature": "type", "instances": 149465, "metric_value": 577.1559, "depth": 3}
			if obj[0] == 'CASH_OUT':
				return 'No_Fraud'
			elif obj[0] == 'CASH_IN':
				return 'No_Fraud'
			elif obj[0] == 'TRANSFER':
				return 'Fraud'
			elif obj[0] == 'PAYMENT':
				return 'Fraud'
			elif obj[0] == 'DEBIT':
				return 'No_Fraud'
			else: return 'No_Fraud'
		elif obj[1] == '1-186':
			# {"feature": "type", "instances": 105947, "metric_value": 499.8035, "depth": 3}
			if obj[0] == 'CASH_OUT':
				return 'No_Fraud'
			elif obj[0] == 'CASH_IN':
				return 'No_Fraud'
			elif obj[0] == 'TRANSFER':
				return 'Fraud'
			elif obj[0] == 'PAYMENT':
				return 'Fraud'
			elif obj[0] == 'DEBIT':
				return 'No_Fraud'
			else: return 'No_Fraud'
		elif obj[1] == '373-558':
			return 'No_Fraud'
		elif obj[1] == '559-743':
			return 'No_Fraud'
		else: return 'No_Fraud'
	elif obj[2] == '0-50k':
		# {"feature": "step_cluster", "instances": 320173, "metric_value": 1295.0492, "depth": 2}
		if obj[1] == '187-372':
			# {"feature": "type", "instances": 146515, "metric_value": 815.345, "depth": 3}
			if obj[0] == 'PAYMENT':
				return 'No_Fraud'
			elif obj[0] == 'CASH_OUT':
				return 'No_Fraud'
			elif obj[0] == 'CASH_IN':
				return 'No_Fraud'
			elif obj[0] == 'TRANSFER':
				return 'Fraud'
			elif obj[0] == 'DEBIT':
				return 'No_Fraud'
			else: return 'No_Fraud'
		elif obj[1] == '1-186':
			# {"feature": "type", "instances": 108379, "metric_value": 690.5468, "depth": 3}
			if obj[0] == 'PAYMENT':
				return 'No_Fraud'
			elif obj[0] == 'CASH_OUT':
				return 'No_Fraud'
			elif obj[0] == 'CASH_IN':
				return 'No_Fraud'
			elif obj[0] == 'TRANSFER':
				return 'Fraud'
			elif obj[0] == 'DEBIT':
				return 'No_Fraud'
			else: return 'No_Fraud'
		elif obj[1] == '373-558':
			return 'No_Fraud'
		elif obj[1] == '559-743':
			return 'No_Fraud'
		else: return 'No_Fraud'
	elif obj[2] == '50k-100k':
		# {"feature": "step_cluster", "instances": 100248, "metric_value": 666.2544, "depth": 2}
		if obj[1] == '187-372':
			# {"feature": "type", "instances": 44369, "metric_value": 394.0753, "depth": 3}
			if obj[0] == 'CASH_OUT':
				return 'No_Fraud'
			elif obj[0] == 'CASH_IN':
				return 'No_Fraud'
			elif obj[0] == 'TRANSFER':
				return 'Fraud'
			elif obj[0] == 'PAYMENT':
				return 'No_Fraud'
			elif obj[0] == 'DEBIT':
				return 'No_Fraud'
			else: return 'No_Fraud'
		elif obj[1] == '1-186':
			# {"feature": "type", "instances": 27438, "metric_value": 341.9165, "depth": 3}
			if obj[0] == 'CASH_OUT':
				return 'No_Fraud'
			elif obj[0] == 'CASH_IN':
				return 'No_Fraud'
			elif obj[0] == 'TRANSFER':
				return 'Fraud'
			elif obj[0] == 'PAYMENT':
				return 'No_Fraud'
			elif obj[0] == 'DEBIT':
				return 'No_Fraud'
			else: return 'No_Fraud'
		elif obj[1] == '373-558':
			return 'No_Fraud'
		elif obj[1] == '559-743':
			return 'No_Fraud'
		else: return 'No_Fraud'
	elif obj[2] == '1M-5M':
		# {"feature": "step_cluster", "instances": 85876, "metric_value": 628.6275, "depth": 2}
		if obj[1] == '187-372':
			# {"feature": "type", "instances": 31520, "metric_value": 234.6628, "depth": 3}
			if obj[0] == 'TRANSFER':
				return 'Fraud'
			elif obj[0] == 'CASH_OUT':
				return 'Fraud'
			elif obj[0] == 'CASH_IN':
				return 'No_Fraud'
			else: return 'No_Fraud'
		elif obj[1] == '373-558':
			# {"feature": "type", "instances": 26275, "metric_value": 310.551, "depth": 3}
			if obj[0] == 'TRANSFER':
				return 'No_Fraud'
			elif obj[0] == 'CASH_OUT':
				return 'No_Fraud'
			else: return 'No_Fraud'
		elif obj[1] == '1-186':
			# {"feature": "type", "instances": 16764, "metric_value": 158.0628, "depth": 3}
			if obj[0] == 'TRANSFER':
				return 'Fraud'
			elif obj[0] == 'CASH_OUT':
				return 'Fraud'
			elif obj[0] == 'CASH_IN':
				return 'No_Fraud'
			else: return 'No_Fraud'
		elif obj[1] == '559-743':
			return 'No_Fraud'
		else: return 'No_Fraud'
	elif obj[2] == '500k-1M':
		# {"feature": "step_cluster", "instances": 73518, "metric_value": 438.9878, "depth": 2}
		if obj[1] == '187-372':
			# {"feature": "type", "instances": 26342, "metric_value": 179.9759, "depth": 3}
			if obj[0] == 'TRANSFER':
				return 'Fraud'
			elif obj[0] == 'CASH_OUT':
				return 'Fraud'
			elif obj[0] == 'CASH_IN':
				return 'No_Fraud'
			else: return 'No_Fraud'
		elif obj[1] == '373-558':
			return 'No_Fraud'
		elif obj[1] == '1-186':
			# {"feature": "type", "instances": 16764, "metric_value": 86.1954, "depth": 3}
			if obj[0] == 'TRANSFER':
				return 'Fraud'
			elif obj[0] == 'CASH_OUT':
				return 'Fraud'
			elif obj[0] == 'CASH_IN':
				return 'No_Fraud'
			else: return 'No_Fraud'
		elif obj[1] == '559-743':
			return 'No_Fraud'
		else: return 'No_Fraud'
	elif obj[2] == '5M-10M':
		return 'No_Fraud'
	elif obj[2] == '10M-60M':
		return 'No_Fraud'
	elif obj[2] == '60M-70M':
		return 'No_Fraud'
	else: return 'No_Fraud'
