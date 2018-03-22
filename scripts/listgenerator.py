#!usr/bin/python
print """
Welcome to kwnos100 Wordlist Generator!
"""
text = """
Dialekste...:

1. NumList Generator
2. WordList Generator
"""
wait_text = " H diadikasia vrisketai se ekseliksi..."
mode = raw_input(text)
if mode == "1":
	text = "Dwste ton arithmo twn xaraktirwn tis NumList(max. 10)"
	max_chars = raw_input(text)
	check = 1
	if max_chars == "1":
		nums = 10
	elif max_chars == "2":
		nums = 100
	elif max_chars == "3":
		nums = 1000
	elif max_chars == "4":
		nums = 10000
	elif max_chars == "5":
		nums = 100000
	elif max_chars == "6":
		nums = 1000000
	elif max_chars == "7":
		nums = 10000000
	elif max_chars == "8":
		nums = 100000000
	elif max_chars == "9":
		nums = 1000000000
	elif max_chars == "10":
		nums = 10000000000
	else:
		print "\nMi-eguri apantisi!\n"
		check = 0
	if check != 0:
		name_text = "\nDwste to onoma pou thelete na exei to arxeio pou tha dimiourgithei(xwris to extension): "
		file_name = raw_input(name_text)
		type_text = "\n Gia na apothikeutei se morfi .txt grapste 1\n Gia na apothikeutei se morfi .lst grapste 2 "
		type = raw_input(type_text)
		if type == "1":
			file_name = file_name + ".txt"
		elif type == "2":
			file_name = file_name + ".lst"
		file = open(file_name, "w")
		print wait_text
		for count in range(1, nums):
			count2 = str(count)
			file.write(count2 + "\n")
		file.close()
elif mode == "2":
	print "\n Gia...\n"
	type_text = """ Lista me peza grammata grapste 1
 Lista me kefalaia grammata grapste 2
 Lista me peza grammata kai arithmous grapste 3
 Lista me kefalaia grammata kai arithmous grapste 4
 Lista me mono sumvola grapste 5
 Lista me peza grammata kai sunmvola grapste 6
 Lista me kefalaia grammata kai sumvola grapste 7
 Lista me arithmous kai sumvola grapste 8
 Lista me peza kai kefalaia grapste 9
 Lista me peza, kefalaia kai arithmous grapste 10
 Lista me peza, kefalaia, arithmous kai sumvola grapste 11 """
	type = raw_input(type_text)
	check = 1
	if type == "1":
		list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', \
		'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	elif type == "2":
		list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', \
		'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	elif type == "3":
		list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', \
		'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	elif type == "4":
		list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', \
		'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	elif type == "5":
		list = [',', '<', '>', '.', '/','?', '\'', '"', ';', ':', ']', '}', '[', '{', '\\', '|',\
		'=', '+', '-', '_', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ' ']
	elif type == "6":
		list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', \
		'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',', '<', '>', '.', '/',\
		'?', '\'', '"', ';', ':', ']', '}', '[', '{', '\\', '|', '=', '+', '-', '_', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ' ']
	elif type == "7":
		list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', \
		'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ',', '<', '>', '.', '/',\
		'?', '\'', '"', ';', ':', ']', '}', '[', '{', '\\', '|', '=', '+', '-', '_', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ' ']
	elif type == "8":
		list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ',', '<', '>', '.', '/','?', '\'', '"', ';', ':', ']', '}', '[', '{', '\\', '|',\
		'=', '+', '-', '_', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ' ']
	elif type == "9":
		list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', \
		'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', \
		'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	elif type == "10":
		list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', \
		'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', \
		'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	elif type == "11":
		list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', \
		'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', \
		'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ',', '<', '>', '.', '/','?', '\'',\
		 '"', ';', ':', ']', '}', '[', '{', '\\', '|', '=', '+', '-', '_', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ' ']
	else:
		print "\n Mi eguri apantisi!\n"
		check = 0
	if check != 0:
		chars_text = "\n Dwste ton arithmo twn xaraktirwn tis WordList(max. 10): "
		type = raw_input(chars_text)
		name_text = "\nDwste to onoma pou thelete na exei to arxeio pou tha dimiourgithei(xwris to extension): "
		file_name = raw_input(name_text)
		type_text = "\n Gia na apothikeutei se morfi .txt grapste 1\n Gia na apothikeutei se morfi .lst grapste 2 "
		save_type = raw_input(type_text)
		if save_type == "1":
			file_name = file_name + ".txt"
		elif save_type == "2":
			file_name = file_name + ".lst"
		file = open(file_name, "w")
		if type == "1":
			print wait_text
			for c1 in list:
				c_1 = str(c1)
				file.write(c_1 + "\n")
		elif type == "2":
			print wait_text
			for c1 in list:
				c_1 = str(c1)
				for c2 in list:
					c_2 = str(c2)
					file.write(c_1 + c_2 + "\n")
		elif type == "3":
			print wait_text
			for c1 in list:
				c_1 = str(c1)
				for c2 in list:
					c_2 = str(c2)
					for c3 in list:
						c_3 = str(c3)
						file.write(c_1 + c_2 + c_3 + "\n")
		elif type == "4":
			print wait_text
			for c1 in list:
				c_1 = str(c1)
				for c2 in list:
					c_2 = str(c2)
					for c3 in list:
						c_3 = str(c3)
						for c4 in list:
							c_4 = str(c4)
							file.write(c_1 + c_2 + c_3 + c_4 + "\n")
		elif type == "5":
			print wait_text
			for c1 in list:
				c_1 = str(c1)
				for c2 in list:
					c_2 = str(c2)
					for c3 in list:
						c_3 = str(c3)
						for c4 in list:
							c_4 = str(c4)
							for c5 in list:
								c_5 = str(c5)
								file.write(c_1 + c_2 + c_3 + c_4 + c_5 + "\n")
		elif type == "6":
			print wait_text
			for c1 in list:
				c_1 = str(c1)
				for c2 in list:
					c_2 = str(c2)
					for c3 in list:
						c_3 = str(c3)
						for c4 in list:
							c_4 = str(c4)
							for c5 in list:
								c_5 = str(c5)
								for c6 in list:
									c_6 = str(c6)
									file.write(c_1 + c_2 + c_3 + c_4 + c_5 + c_6 + "\n")
		elif type == "7":
			print wait_text
			for c1 in list:
				c_1 = str(c1)
				for c2 in list:
					c_2 = str(c2)
					for c3 in list:
						c_3 = str(c3)
						for c4 in list:
							c_4 = str(c4)
							for c5 in list:
								c_5 = str(c5)
								for c6 in list:
									c_6 = str(c6)
									for c7 in list:
										c_7 = str(c7)
										file.write(c_1 + c_2 + c_3 + c_4 + c_5 + c_6 + c_7 + "\n")
		elif type == "8":
			print wait_text
			for c1 in list:
				c_1 = str(c1)
				for c2 in list:
					c_2 = str(c2)
					for c3 in list:
						c_3 = str(c3)
						for c4 in list:
							c_4 = str(c4)
							for c5 in list:
								c_5 = str(c5)
								for c6 in list:
									c_6 = str(c6)
									for c7 in list:
										c_7 = str(c7)
										for c8 in list:
											c_8 = str(c8)
											file.write(c_1 + c_2 + c_3 + c_4 + c_5 + c_6 + c_7 + c_8 + "\n")
		elif type == "9":
			print wait_text
			for c1 in list:
				c_1 = str(c1)
				for c2 in list:
					c_2 = str(c2)
					for c3 in list:
						c_3 = str(c3)
						for c4 in list:
							c_4 = str(c4)
							for c5 in list:
								c_5 = str(c5)
								for c6 in list:
									c_6 = str(c6)
									for c7 in list:
										c_7 = str(c7)
										for c8 in list:
											c_8 = str(c8)
											for c9 in list:
												c_9 = str(c9)
												file.write(c_1 + c_2 + c_3 + c_4 + c_5 +\
												c_6 + c_7 + c_8 + c_9 + "\n")
		elif type == "10":
			print wait_text
			for c1 in list:
				c_1 = str(c1)
				for c2 in list:
					c_2 = str(c2)
					for c3 in list:
						c_3 = str(c3)
						for c4 in list:
							c_4 = str(c4)
							for c5 in list:
								c_5 = str(c5)
								for c6 in list:
									c_6 = str(c6)
									for c7 in list:
										c_7 = str(c7)
										for c8 in list:
											c_8 = str(c8)
											for c9 in list:
												c_9 = str(c9)
												for c10 in list:
													c_10 = str(c10)	
													file.write(c_1 + c_2 + c_3 + c_4 + c_5 +\
													c_6 + c_7 + c_8 + c_9 + c_10 + "\n")
		file.close()
else:
	print """
Mi-eguri apantisi!
"""
raw_input(" H diadikasia teliwse!\n H wordlist apothikeutike me to onoma: " + file_name)
