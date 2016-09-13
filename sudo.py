board = input("Enter the board row by row in a single block. Dots (.) as blanks ")
# make parallel lists
r = list()
c = list()
a = list()
digits = "123456789"
for i in range(len(board)):
	#print(board[i])
	if board[i] != ".":
		#print(board[i])
		a.append(board[i])
		r.append(i//9)
		c.append(i%9)
	else:
		a.append(digits)
		r.append(i//9)
		c.append(i%9)

# eliminate
def eliminate(row,col,num):
	# eliminate in the rows
	r = list() # master
	rr = list() # recycled
	for k in range(0,81):
		if (len(num[k]) == 1):
			rr.append(num[k])
		if (k%9 == 8):
			r.append(rr)
			rr = list()
	#print(r)
	for e in range(0,81):
		if (len(num[e]) > 1):
			t = list(num[e])
			t2 = r[e//9]
			for l in t2:
				try:
					t.remove(l)
				except ValueError:
					pass
			num[e] = "".join(t)
	# eliminate in the columns
	c = list() # master
	cc = list() # recycled
	rngc = list(range(0,81,9))+list(range(1,81,9))+list(range(2,81,9))+list(range(3,81,9))+list(range(4,81,9))+list(range(5,81,9))+list(range(6,81,9))+list(range(7,81,9))+list(range(8,81,9))
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
	#print(u)
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
	# pick out numbers that are the only box in the row/col/unit to have that number
	# select in the rows
	r = list() # master
	rr = "" # recycled
	for k in range(0,81):
		if (len(num[k]) > 1):
			rr = rr + num[k]
		if (k%9 == 8):
			r.append([x for x in list(rr) if list(rr).count(x)==1])
			rr = ""
	print(r)
	for rs in range(0:9):											# not done yet!
		for r_sel in range(0:len(r[rs])):
			r[rs][r_sel]

# main			
a_copy = list()
while (a_copy != a):
	while (a_copy != a):
		#print(a)
		#print(a_copy)
		a_copy = a[:]
		eliminate(r,c,a)
	select(r,c,a)
#eliminate(r,c,a)
#while (a_copy != a):
#	print(a)
#	print(a_copy)
#	a_copy = a[:]
#	eliminate(r,c,a)
print(a)