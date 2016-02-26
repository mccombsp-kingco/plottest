import datetime

def cleaner(input_str):
	remove_chars = '$, '
	return input_str.translate(None, remove_chars)

with open("new_sw7.txt", 'r') as new_handle:
	new_rows = new_handle.readlines()

with open("sw7.csv",'a') as sw7_handle:
	sw7_handle.write('\n')
	
	for row in new_rows:
		row_list = row.split('\t')
		row_datetime = datetime.datetime.strptime(row_list[0], '%Y/%m/%d')
		row_list[0] = '{dt.month}/{dt.day}/{dt.year}'.format(dt = row_datetime)
		row_list[2] = cleaner(row_list[2])
		row_pct = row_list[3]
		row_list[3] = str(float(row_pct.strip('%'))/100)
		row_list[4] = cleaner(row_list[4])
		row_list[5] = cleaner(row_list[5])
		row_list[6] = cleaner(row_list[6])

		line_string = ''
		for item in row_list[0:7]:
			line_string = line_string+item+','
		line_string = line_string+row_list[7]
		sw7_handle.write(line_string)



