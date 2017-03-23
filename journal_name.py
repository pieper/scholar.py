import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import json
import pdb
import types

def store(data,file_name):
    with open(file_name, 'w') as json_file:
        json_file.write(json.dumps(data))

        
def get_json():
	jour=0
	conf=0
	list=[]
	diction={}
	number=[]
	name=[]
	bibdic={}
	n=0
	with open('bibtex.json') as json_file:
		data = json.load(json_file) #type of data is list
		for a in data:
			c=a.split("\n")  #type of data is list
			n=n+1
			for mate in c:
				d=mate.split("{")
				if len(d)==2:   #type of d[0] is srtings
					m=str(n)
					d[0]=d[0]+m
					bibdic[d[0]]=d[1]
		store(bibdic,"Bibtex_format.json")
		for a in bibdic:
				if "journal=" in a:
					jour=jour+1
					diction[bibdic[a]]= diction.get(bibdic[a],0)+1
				elif "booktitle=" in a:
					conf= conf+1
					diction[bibdic[a]]= diction.get(bibdic[a],0)+1
				elif "title" in a:
					list.append(bibdic[a]) 
		print ("the number of journal is:",jour)
		print ("the number of conference is:",conf)
		store(list,"title.json")
		for key in diction:
			number.append(diction[key])
			key = key.replace("journal=","")
			key = key.replace("},","")
			name.append(key)
	plt.rcdefaults()
	fig, ax = plt.subplots()

	y_pos = np.arange(len(name))
	ax.barh(y_pos, number,
			color='blue')
	ax.set_yticks(y_pos)
	ax.set_yticklabels(name)
	ax.invert_yaxis()  # labels read top-to-bottom
	ax.set_xlabel('Number')
	ax.set_title('How many times a journal has show up')

	plt.show()
	
	
if __name__=="__main__":
	get_json()
	
            
               
