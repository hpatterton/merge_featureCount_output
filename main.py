def Merge_Lists(list_1, list_2, column_to_add):
	result_list = []
	for index in range(len(list_1)):
		entry = []
		query = list_1[index][0]
		entry.append(query)
		#print(list_1[index][column_to_add])
		sum = int(list_1[index][column_to_add])

		# see if the entry is in list_2
		for index2 in range(len(list_2)):
			if query == list_2[index2][0]:
				sum += int(list_2[index2][column_to_add])
				list_2[index2][0] = '0'
		entry.append(str(sum))
		result_list.append(entry)
		#now test to see if any list_2 entries that are not in list2 remain and add them

	for index3 in range(len(list_2)):
		if list_2[index3][0] != '0':
			result_list.append(list_2[index3])

	return result_list


# read file of filename
# supply filepath

header = True
column_to_add = 1
file_of_filenames = 'C:\\Users\\hpatterton\\Downloads\\446_ featureCounts on collection 377_ Counts_H9\\featureCounts on collection 377_ Counts\\filename.txt'


point = file_of_filenames.rfind('.')
outfilename = file_of_filenames[:point]
outfile = outfilename + '_merged.txt'
file_handle = open(file_of_filenames,'r')
list_of_files = []
for line in file_handle:
	list_of_files.append(line.rstrip('\n'))
# read in the data of each file
list_of_lists = []
for filepath in list_of_files:
	list = []
	file_handle = open(filepath,'r')
	for index,entry in enumerate(file_handle):
		if (header == True):
			if (index > 0):
				line2 = entry.rstrip('\n')
				line3 = line2.split('\t')
				list.append(line3)
		else:
			line2 = entry.rstrip('\n')
			line3= line2.split('\t')
			list.append(line3)
	list_of_lists.append(list)

number_of_files = len(list_of_lists)
if number_of_files < 3:
	print('Need 2 or more files to merge!')
	exit(0)

# call the merge_data function for for the combined (file 1 when you start)
# and the next file, until you have merged all files

result_list = Merge_Lists(list_of_lists[0], list_of_lists[1], column_to_add)
for file_number in range(2, number_of_files):
	result_list = Merge_Lists(result_list, list_of_lists[file_number], column_to_add)

print(list_of_lists[0], list_of_lists[1], list_of_lists[2], result_list)
outhandle = open(outfile,'w')
for entry in result_list:
	outhandle.write(entry[0]+'\t'+entry[1]+'\n')
print('Written',str(len(result_list)),'entries to',outfile)

