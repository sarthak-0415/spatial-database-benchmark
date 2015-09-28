import sys
import math

print "INSERT INTO lineLayer VALUES"

#no_records=10

no_records = int(sys.argv[1])
y=1.0
arr=[]
while(y<=no_records):
	
	if(y%2 == 0):
		x=0.001
	else:
		x=0.002
		
	diff = math.ceil(y/2)
	while(x +  math.ceil(diff)<=no_records):
		arr.append(''' ('Linestring','LINESTRING(''' + str(x) +' '+str(y) +','+ str(x+diff) +' '+str(y)+ ''')'),''')
		x = x + math.ceil(diff*2)	
	y = y+0.001


## code to delete comma and insert semicolon at the end of the file
size = len(arr)
length = len(arr[size-1])

temp_list = list(arr[size-1])
temp_list[length-1] = ";"

arr[size-1] = "".join(temp_list)

#code to print to output in a sql file
for line in arr:
	print line

#print 'select * from lineLayer;'