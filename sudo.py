board = input("Enter the board row by row in a single string. Dots (.) as blanks ")
# make parallel lists
r = list()
c = list()
a = list()
digits = "123456789"
for i in range(len(board)):
	#print(board[i])
	if board[i] != ".": # if given
		#print(board[i])
		a.append(board[i])	# add the number
		r.append(i//9)		# record row
		c.append(i%9)		# record column
	else:
		a.append(digits)	# add all digits, since all are possible at this point
		r.append(i//9)		# record row
		c.append(i%9)		# record column

# eliminate
def eliminate(row,col,num):
	print("Eliminating")
	# eliminate in the rows
	r = list() # master
	rr = list() # recycled
	for k in range(0,81):	 		# for each cell
		if (len(num[k]) == 1):		# if the cell is already decided on add that to the list
			rr.append(num[k])
		if (k%9 == 8):				# at the end of the row, add to master list and recycle
			r.append(rr)
			rr = list()
	#print(r)
	for e in range(0,81):			# for each cell
		if (len(num[e]) > 1):		# if the cell isnt decided on
			t = list(num[e])		# make a list of the possible numbers
			t2 = r[e//9]			# get list of numbers that cant be there because they are spoken for in other cells in that row
			for l in t2:
				try:
					t.remove(l)		# remove them
				except ValueError:
					pass
			num[e] = "".join(t)		# reassign the possible numbers
	# eliminate in the columns      # comments similar to above, the code is very similar.
	c = list() # master
	cc = list() # recycled
	rngc = list(range(0,81,9))+list(range(1,81,9))+list(range(2,81,9))+list(range(3,81,9))+list(range(4,81,9))+list(range(5,81,9))+list(range(6,81,9))+list(range(7,81,9))+list(range(8,81,9)) # specific numbers so loop runs the rows
	for k2 in rngc:
		if (len(num[k2]) == 1):
			cc.append(num[k2])
		if (rngc.index(k2)%9 == 8):
			c.append(cc)
			cc = list()
	#print(c)
	for e2 in rngc:
		if (len(num[e2]) > 1):
			t = list(num[e2])
			t2 = c[e2%9]
			for l in t2:
				try:
					t.remove(l)
				except ValueError:
					pass
			num[e2] = "".join(t)
	# eliminate in the units
	# below are the 9 lists of values to to help with iteration over them
	u1 = sorted(list(range(0,81,9))+list(range(1,81,9))+list(range(2,81,9)))[0:9]
	u2 = sorted(list(range(3,81,9))+list(range(4,81,9))+list(range(5,81,9)))[0:9]
	u3 = sorted(list(range(6,81,9))+list(range(7,81,9))+list(range(8,81,9)))[0:9]
	u4 = sorted(list(range(0,81,9))+list(range(1,81,9))+list(range(2,81,9)))[9:18]
	u5 = sorted(list(range(3,81,9))+list(range(4,81,9))+list(range(5,81,9)))[9:18]
	u6 = sorted(list(range(6,81,9))+list(range(7,81,9))+list(range(8,81,9)))[9:18]
	u7 = sorted(list(range(0,81,9))+list(range(1,81,9))+list(range(2,81,9)))[18:27]
	u8 = sorted(list(range(3,81,9))+list(range(4,81,9))+list(range(5,81,9)))[18:27]
	u9 = sorted(list(range(6,81,9))+list(range(7,81,9))+list(range(8,81,9)))[18:27]
	u = [u1,u2,u3,u4,u5,u6,u7,u8,u9]
	# similar comments to above, very similar code
	it = list()
	itt = list()
	for u_s in u:
		for us2 in u_s:
			if (len(num[us2]) == 1):
				itt.append(num[us2])
		it.append(itt)
		itt = list()
	#print(it)
	unum = u1+u2+u3+u4+u5+u6+u7+u8+u9
	for u2 in unum:
		if (len(num[u2]) > 1):
			t = list(num[u2])
			t2 = it[unum.index(u2)//9]
			for l in t2:
				try:
					t.remove(l)
				except ValueError:
					pass
			num[u2] = "".join(t)	
			
def select(row,col,num):
	print("Selecting")
	# pick out numbers that are the only cell in the row/col/unit to have that number
	# select in the rows
	r = list() # master
	rr = "" # recycled
	for k in range(0,81):												# for all cells
		if (len(num[k]) > 1):											# if the cell isnt called for
			rr = rr + num[k]											# add its possibilities to the string
		if (k%9 == 8):													# at the end of the row
			r.append([x for x in list(rr) if list(rr).count(x)==1])		# parse the string to pick out numbers that only occured once
			rr = ""														# recycle
	for rs in range(0,9):												# for each row
		for r_sel in r[rs]:												# for each selected number
			for sqr in range((rs*9),(rs*9+9)):							# for each square in that row
				if r_sel in num[sqr]:									# if the cell contains the selected number
					num[sqr] = r_sel									# assign that number to the cell
					break												# break the loop cause the search is over

	# select in the columns												# similar comments as above, very similar code
	c = list() # master
	cc = "" # recycled
	rngc = list(range(0,81,9))+list(range(1,81,9))+list(range(2,81,9))+list(range(3,81,9))+list(range(4,81,9))+list(range(5,81,9))+list(range(6,81,9))+list(range(7,81,9))+list(range(8,81,9))
	for k2 in rngc:
		if (len(num[k2]) > 1):
			cc = cc + num[k2]
		if (rngc.index(k2)%9 == 8):
			c.append([x2 for x2 in list(cc) if list(cc).count(x2)==1])
			cc = ""
	for cs in range(0,9):											
		for c_sel in c[cs]:
			for sqr in rngc[(cs*9):(cs*9+9)]:
				if c_sel in num[sqr]:
					num[sqr] = c_sel
					break
					
	# selection in the units, still buggy								# similar commets as above, very similar code
	U = list()
	uu = ""
	u1 = sorted(list(range(0,81,9))+list(range(1,81,9))+list(range(2,81,9)))[0:9]
	u2 = sorted(list(range(3,81,9))+list(range(4,81,9))+list(range(5,81,9)))[0:9]
	u3 = sorted(list(range(6,81,9))+list(range(7,81,9))+list(range(8,81,9)))[0:9]
	u4 = sorted(list(range(0,81,9))+list(range(1,81,9))+list(range(2,81,9)))[9:18]
	u5 = sorted(list(range(3,81,9))+list(range(4,81,9))+list(range(5,81,9)))[9:18]
	u6 = sorted(list(range(6,81,9))+list(range(7,81,9))+list(range(8,81,9)))[9:18]
	u7 = sorted(list(range(0,81,9))+list(range(1,81,9))+list(range(2,81,9)))[18:27]
	u8 = sorted(list(range(3,81,9))+list(range(4,81,9))+list(range(5,81,9)))[18:27]
	u9 = sorted(list(range(6,81,9))+list(range(7,81,9))+list(range(8,81,9)))[18:27]
	u = [u1,u2,u3,u4,u5,u6,u7,u8,u9]
	for u_s in u:
		for us2 in u_s:
			if (len(num[us2]) > 1):
				uu = uu + num[us2]
		U.append([x3 for x3 in list(uu) if list(uu).count(x3)==1])
		uu = ""
	for us in range(0,9):											
		for u_sel in U[us]:
			for sqr in u[us]:
				if u_sel in num[sqr]:
					num[sqr] = u_sel
					break
# main			
a_copy = list()						# make space for a reference copy of a
while (a_copy != a):				# while the refence isnt equal to the current best guess
	while (a_copy != a):			# still, while the refence isnt equal to the current best guess
		a_copy = a[:]				# assign the new reference
		eliminate(r,c,a)			# eliminate
	#print(a)
	if len("".join(a)) > 81:		# if solved skip selection
		select(r,c,a)				# if not solved, go into selection

# write a display function
print(a)