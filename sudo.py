board = input("Enter the board row by row in a single string. Dots (.) as blanks ")
# ranges for iterating through rows cols and units
r1 = list(range(0,9))
r2= list(range(9,18))
r3= list(range(18,27))
r4= list(range(27,36))
r5= list(range(36,45))
r6= list(range(45,54))
r7= list(range(54,63))
r8= list(range(63,72))
r9= list(range(72,81))
global row_ranges 
row_ranges = [r1,r2,r3,r4,r5,r6,r7,r8,r9]

c1 = list(range(0,81,9))
c2 = list(range(1,81,9))
c3 = list(range(2,81,9))
c4 = list(range(3,81,9))
c5 = list(range(4,81,9))
c6 = list(range(5,81,9))
c7 = list(range(6,81,9))
c8 = list(range(7,81,9))
c9 = list(range(8,81,9))
global rngc
rngc = c1+c2+c3+c4+c5+c6+c7+c8+c9
global col_ranges
col_ranges = [c1,c2,c3,c4,c5,c6,c7,c8,c9]


u1 = sorted(list(range(0,81,9))+list(range(1,81,9))+list(range(2,81,9)))[0:9]
u2 = sorted(list(range(3,81,9))+list(range(4,81,9))+list(range(5,81,9)))[0:9]
u3 = sorted(list(range(6,81,9))+list(range(7,81,9))+list(range(8,81,9)))[0:9]
u4 = sorted(list(range(0,81,9))+list(range(1,81,9))+list(range(2,81,9)))[9:18]
u5 = sorted(list(range(3,81,9))+list(range(4,81,9))+list(range(5,81,9)))[9:18]
u6 = sorted(list(range(6,81,9))+list(range(7,81,9))+list(range(8,81,9)))[9:18]
u7 = sorted(list(range(0,81,9))+list(range(1,81,9))+list(range(2,81,9)))[18:27]
u8 = sorted(list(range(3,81,9))+list(range(4,81,9))+list(range(5,81,9)))[18:27]
u9 = sorted(list(range(6,81,9))+list(range(7,81,9))+list(range(8,81,9)))[18:27]
global u
u = [u1,u2,u3,u4,u5,u6,u7,u8,u9]

# make parallel lists
r = list()
c = list()
uu = list()
a = list()
digits = "123456789"
for i in range(len(board)):
	if board[i] != ".": # if given
		a.append(board[i])	# add the number
		r.append(i//9)		# record row
		c.append(i%9)		# record column
		uu.append(sum(u,[]).index(i)//9) # record unit
	else:
		a.append(digits)	# add all digits, since all are possible at this point
		r.append(i//9)		# record row
		c.append(i%9)		# record column
		uu.append(sum(u,[]).index(i)//9) # record unit

# eliminate
def eliminate(row,col,unit,num):
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
	# specific numbers so loop runs the rows
	for k2 in rngc:
		if (len(num[k2]) == 1):
			cc.append(num[k2])
		if (rngc.index(k2)%9 == 8):
			c.append(cc)
			cc = list()
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
	# similar comments to above, very similar code
	it = list()
	itt = list()
	for u_s in u:
		for us2 in u_s:
			if (len(num[us2]) == 1):
				itt.append(num[us2])
		it.append(itt)
		itt = list()
	for u_list in range(0,9):
		for u2 in u[u_list]:
			if (len(num[u2]) > 1):
				t = list(num[u2])
				t2 = it[u_list]
				for l in t2:
					try:
						t.remove(l)
					except ValueError:
						pass
				num[u2] = "".join(t)
	#print(num)
			
def select(row,col,unit,num):
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
		for r_sel in r[rs]:				# add a aspecial elim in for col and unit								# for each selected number
			for sqr in range((rs*9),(rs*9+9)):							# for each square in that row
				if r_sel in num[sqr]:									# if the cell contains the selected number
					num[sqr] = r_sel									# assign that number to the cell
					c_elim = col[sqr]
					u_elim = unit[sqr]
					for itr in range(0,81):
						if ((col[itr] == c_elim or unit[itr] == u_elim) and len(num[itr]) > 1):
							tt = list(num[itr])
							try:
								tt.remove(r_sel)
							except ValueError:
								pass
							num[itr] = "".join(tt)
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
					num[sqr] = c_sel									# assign that number to the cell
					r_elim = row[sqr]
					u_elim = unit[sqr]
					for itr2 in range(0,81):
						if ((row[itr2] == r_elim or unit[itr2] == u_elim)and len(num[itr2]) > 1):
							tt = list(num[itr2])
							try:
								tt.remove(c_sel)
							except ValueError:
								pass
							num[itr2] = "".join(tt)
					break
					
	# selection in the units,								# similar commets as above, very similar code
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
					num[sqr] = u_sel			# assign that number to the cell	
					r_elim = row[sqr]
					c_elim = col[sqr]
					for itr3 in range(0,81):
						if ((row[itr3] == r_elim or col[itr3] == c_elim)and len(num[itr3]) > 1):
							tt = list(num[itr3])
							try:
								tt.remove(u_sel)
							except ValueError:
								pass
							num[itr3] = "".join(tt)
					break
	#print(num)
	
	
def channel(row,col,unit,num):
	#within a unit, look in th rows and find sets of 2 or 3 of a single number in only 1 row of the unit. save them and elimminate that number form that row in all units that share that row.
	# channeling within the rows
	print("Channeling")
	save_r = []
	for unt in u:
		temp_save = [""]*3 # one for each of the 3 rows in the unit
		word_lst = ["","",""]
		for cell in unt:
			if len(num[cell])>1:
				word_lst[row[cell]%3] = word_lst[row[cell]%3]+num[cell]
		seen1 = set()
		seen1_add = seen1.add
		listed1 = word_lst[0]
		u_listed1 = [x for x in listed1 if not (x in seen1 or seen1_add(x))]
		seen2 = set()
		seen2_add = seen2.add
		listed2 = word_lst[1]
		u_listed2 = [x for x in listed2 if not (x in seen2 or seen2_add(x))]
		seen3 = set()
		seen3_add = seen3.add
		listed3 = word_lst[2]
		u_listed3 = [x for x in listed3 if not (x in seen3 or seen3_add(x))]
		for i in range(1,10):
			if (u_listed1+u_listed2+u_listed3).count(str(i)) == 1:
				if str(i) in u_listed1:
					temp_save[0] = temp_save[0] + str(i)
				elif str(i) in u_listed2:
					temp_save[1] = temp_save[1] + str(i)
				else:
					temp_save[2] = temp_save[2] + str(i)
		save_r.append(temp_save[0])
		save_r.append(temp_save[1])
		save_r.append(temp_save[2])
	
	# channeling in the columns
	u_by_col1 = list(range(0,81,9))[0:3]+list(range(1,81,9))[0:3]+list(range(2,81,9))[0:3]
	u_by_col2 = list(range(3,81,9))[0:3]+list(range(4,81,9))[0:3]+list(range(5,81,9))[0:3]
	u_by_col3 = list(range(6,81,9))[0:3]+list(range(7,81,9))[0:3]+list(range(8,81,9))[0:3]
	u_by_col4 = list(range(0,81,9))[3:6]+list(range(1,81,9))[3:6]+list(range(2,81,9))[3:6]
	u_by_col5 = list(range(3,81,9))[3:6]+list(range(4,81,9))[3:6]+list(range(5,81,9))[3:6]
	u_by_col6 = list(range(6,81,9))[3:6]+list(range(7,81,9))[3:6]+list(range(8,81,9))[3:6]
	u_by_col7 = list(range(0,81,9))[6:9]+list(range(1,81,9))[6:9]+list(range(2,81,9))[6:9]
	u_by_col8 = list(range(3,81,9))[6:9]+list(range(4,81,9))[6:9]+list(range(5,81,9))[6:9]
	u_by_col9 = list(range(6,81,9))[6:9]+list(range(7,81,9))[6:9]+list(range(8,81,9))[6:9]
	
	u_by_col = [u_by_col1,u_by_col2,u_by_col3,u_by_col4,u_by_col5,u_by_col6,u_by_col7,u_by_col8,u_by_col9]
	save_c = []
	for unt in u_by_col:
		temp_save = [""]*3 # one for each of the 3 cols in the unit
		word_lst = ["","",""]
		for cell in unt:
			if len(num[cell])>1:
				word_lst[col[cell]%3] = word_lst[col[cell]%3]+num[cell]
		seen4 = set()
		seen4_add = seen4.add
		listed4 = word_lst[0]
		u_listed4 = [x for x in listed4 if not (x in seen4 or seen4_add(x))]
		seen5 = set()
		seen5_add = seen5.add
		listed5 = word_lst[1]
		u_listed5 = [x for x in listed5 if not (x in seen5 or seen5_add(x))]
		seen6 = set()
		seen6_add = seen6.add
		listed6 = word_lst[2]
		u_listed6 = [x for x in listed6 if not (x in seen6 or seen6_add(x))]

		for i in range(1,10):
			if (u_listed4+u_listed5+u_listed6).count(str(i)) == 1:
				if str(i) in u_listed4:
					temp_save[0] = temp_save[0] + str(i)
				elif str(i) in u_listed5:
					temp_save[1] = temp_save[1] + str(i)
				else:
					temp_save[2] = temp_save[2] + str(i)
		save_c.append(temp_save[0])
		save_c.append(temp_save[1])
		save_c.append(temp_save[2])

	# eliminating the channels from the rows
	for chan in range(27):
		if save_r[chan] != "":
			unt = chan//3
			if chan < 9:
				rw = chan%3
			elif chan < 18:
				rw = (chan-9)%3 + 3
			else:
				rw = (chan-18)%3 + 6
			if unt < 3:
				unt_not = [0,1,2]
				unt_not.remove(unt)
			elif unt < 6:
				unt_not = [3,4,5,]
				unt_not.remove(unt)
			else:
				unt_not = [6,7,8]
				unt_not.remove(unt)
			for x in range(0,81):
				if (row[x] == rw and (unit[x] == unt_not[0] or unit[x] == unt_not[1]) and len(num[x]) > 1):
					tt = list(num[x])
					if len(save_r[chan]) > 1:
						for k in save_r[chan]:
							try:
								tt.remove(k)
							except ValueError:
								pass
					else:
						try:
							tt.remove(save_r[chan])
						except ValueError:
							pass
					num[x] = "".join(tt)
					
	# eliminating the channels from the columns
	for chan in range(27):
		if save_c[chan] != "":
			unt = chan//3
			cl = chan%9
			if unt == 0 or unt == 3 or unt == 6: 
				unt_not = [0,3,6]
				unt_not.remove(unt)
			elif unt == 1 or unt == 4 or unt == 7: 
				unt_not = [1,4,7,]
				unt_not.remove(unt)
			else: 
				unt_not = [2,5,8]
				unt_not.remove(unt)
			for x in range(0,81):
				if (col[x] == cl and (unit[x] == unt_not[0] or unit[x] == unt_not[1]) and len(num[x]) > 1):
					tt = list(num[x])
					if len(save_c[chan]) > 1:
						for k in save_c[chan]:
							try:
								tt.remove(k)
							except ValueError:
								pass
					else:
						try:
							tt.remove(save_c[chan])
						except ValueError:
							pass
					num[x] = "".join(tt)
	
#def omission() # see http://www.learn-sudoku.com/omission.html 	
#def hidden_pair() # see http://www.sudokuessentials.com/sudoku_tips.html	
		
# main			
a_copy = list()						# make space for a reference copy of a
while (a_copy != a):				# while the refence isnt equal to the current best guess
	while (a_copy != a):			# still, while the refence isnt equal to the current best guess
		a_copy = a[:]				# assign the new reference
		eliminate(r,c,uu,a)			# eliminate
	if len("".join(a)) > 81:		# if solved skip selection
		select(r,c,uu,a)			# if not solved, go into selection
		if len("".join(a)) > 81 and a == a_copy:	# if still not solved and selection did nothing
			channel(r,c,uu,a)

# a pretty display

if len("".join(a)) == 81: # if solved
	for i in range(0,81,3):
		if i%27 == 0 and i != 0 :
			print("-----------------")
		if (i+3)%9 == 0:
			print("%s %s %s" %("".join(a[i]),"".join(a[i+1]),"".join(a[i+2])))
		else:
			print("%s %s %s" %("".join(a[i]),"".join(a[i+1]),"".join(a[i+2])),end = "|")
else:
	print(a)

#print(a)