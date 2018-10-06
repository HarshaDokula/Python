import csv
from pprint import pprint

"""
Note:This code is not refined to work with holidays and the months with variable amount of days
"""

def wrangle_atten(filename):

	"""
	This function takes the csv file data as imput and returns the presentees 
	for each day as an output in file with name of the format :"filename_presentee.csv"
	"""
	
	li_month=['feb','april','jun','sep','nov']
	m=filename.split('.')[0]

	if m in li_month:
		n=31
	else:
		n=32

	fileout=m+'_presentees.csv'

	with open(filename,'r') as fin, open(fileout,'w') as fout:
		
		list_at = []
		read_atten=csv.DictReader(fin)
		for i in read_atten:
			list_at.append(i)   
		

		headers=read_atten.fieldnames

		lis=[]
		pre={}
		for j in range(1,n):
			for i in list_at:
				if(i[str(j)]=='P:1'):
					#print(i['Regd No #'])
					lis.append(int(i['Regd No #'][8:]))

			if(len(lis)==68):
				pre[j]='All present'
			elif(len(lis)==0):
				pre[j]='All absent or session not updated'
			else:
				pre[j]=str(lis)

			lis.clear()
		out_cols=['date']
		atten_writer = csv.DictWriter(fout, fieldnames=out_cols)
		atten_writer.writeheader()
		for row in pre:
			fout.write("{},{},\n".format(row,pre[row]))



				
"""
The main function starts here. 
First we will be accepting the number of files that we are going to work on, i.e 'n'.
Then we will accept the file names for the user and store them in data files list.
The wrangle_atten(filename) function is called for each of the file, which will generate a file with the presentees numbers.
"""
	
data_files = []

n=int(input('Enter the number of files:'))
print('Please enter the file names with correctly with the extension , (.csv) in our case, it is case sensitive')
for i in range(n):
	data_files.append(input('Enter name of file ' +str(i+1)+':'))

for data_file in data_files:
	wrangle_atten(data_file) 
