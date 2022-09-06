from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import socket
import requests

def f1():
	adst.deiconify()
	root.withdraw()
def f2():
	root.deiconify()
	adst.withdraw()

def f3():
	vist.deiconify()
	root.withdraw()
	vist_stdata.delete(1.0,END)
	con = None
	try:
		con = connect("aditya_desale.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		msg = ""
		for d in data:
			msg = msg + "rno : " + str(d[0]) + "    name: " + str(d[1]) + "  marks:" + str(d[2]) + "\n"
		vist_stdata.insert(INSERT,msg)
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()
def f4():
	root.deiconify()
	vist.withdraw()
def f5():
	con = None
	try:
		con = connect("aditya_desale.db")
		cursor = con.cursor()
		sql = "insert into student values('%d', '%s' ,'%s')"
		rno = int(adst_entrno.get())
		name = adst_entname.get()
		marks = int(adst_entmarks.get())
		cursor.execute(sql % (rno,name,marks))
		
		
		if rno < 1:
			showerror("issue","id cannot be zero or less than zero")

	
		elif (not name.isalpha()) or (len(name) < 2):
			showerror("issue","name should be alpha of min length 2")

	
		elif (marks < 0 or marks > 100):
			 showerror("issue","marks should be in range of 0 to 100")
		else:
			con.commit()
			showinfo("sucess","record added")
		
	except Exception as e:
		con.rollback()
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()
		adst_entrno.delete(0,END)
		adst_entname.delete(0,END)
		adst_entmarks.delete(0,END)
		adst_entrno.focus()
def f6():
	upst.deiconify()
	root.withdraw()

def f7():
	root.deiconify()
	upst.withdraw()

def f8():
	dest.deiconify()
	root.withdraw()

def f9():
	root.deiconify()
	dest.withdraw()
def f10():
	con = None
	try:
		con = connect("aditya_desale.db")
		cursor = con.cursor()
		sql = "delete from student where rno='%d'"
		rno = int(dest_entrno.get())
		
		cursor.execute(sql % (rno))
		if cursor.rowcount > 0 :
			con.commit()
			showinfo("success","record deleted")
		else:
			showinfo("issue","record does not exists")
	except Exception as e:
		con.rollback()
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()
		dest_entrno.delete(0,END)
		
		
		dest_entrno.focus()
def f11():
	con = None
	try:
		con = connect("aditya_desale.db")
		cursor = con.cursor()
		sql = "update student SET name='%s',marks='%d' where rno='%d'"
		rno = int(upst_entrno.get())
		name = upst_entname.get()
		marks = int(upst_entmarks.get())
		cursor.execute(sql % (name,marks,rno))
		if (not name.isalpha()) or (len(name) < 2):
			showerror("issue","name should be alpha of min length 2")

	
		elif (marks < 0 or marks > 100):
			 showerror("issue","marks should be in range of 0 to 100")
		elif cursor.rowcount > 0 :
			con.commit()
			showinfo("success","record updated")
		
		else:
			showinfo("issue","record does not exists")
	except Exception as e:
		con.rollback()
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()
		upst_entrno.delete(0,END)
		upst_entname.delete(0,END)
		upst_entmarks.delete(0,END)
		upst_entrno.focus()
def f12():
	import matplotlib.pyplot as plt
	import pandas as pd
	import sqlite3

	con=None
	try:
		con=sqlite3.connect("aditya_desale.db")
		#print("Connected")
		sql="select name,marks from student order by rno asc limit 5;"
		data=pd.read_sql_query(sql,con)
		#print(data)

		name=data['name'].tolist()
		marks=data['marks'].tolist()

		plt.bar(name,marks,color='r')
	
		plt.title("Batch information")
		plt.xlabel("Name")
		plt.ylabel("Marks")
		plt.show()

	except Exception as e:
		print("issue",e)
	finally:
		if con is not None:
			con.close()
			print("Disconnected")
def f13():
	import socket
	import requests
	try:
	
		socket.create_connection( ("www.google.com", 80))
		api_address= "http://api.openweathermap.org/data/2.5/weather?units=metric&q=mumbai&appid=c6e315d09197cec231495138183954bd" 		
		res = requests.get(api_address)
		#print(res)
	
		data=res.json()
		#print(data)

		Location=data['name']
		main=data['main']
		temp1=main['temp']
		showinfo("location&temperature",Location+str( temp1))
        #label=Label(root,text=Location+str( temp1))
        #label.grid(row=8,column=1)
    
	except OSError as e:
		print("issue ", e)
	except KeyError as e1:
		print("check city name",e1)

def f14():
	import socket
	import requests
	import bs4


	try:
		socket.create_connection(("www.google.com",80))
		#print("YOU are connected")

		res=requests.get("http://www.brainyquote.com/quote_of_the_day")
		#print(res)

		soup=bs4.BeautifulSoup(res.text,"lxml")
		#print(soup)

		data=soup.find("img",{"class":"p-qotd"})
		#print(data)

		motd=data['alt']
		#showinfo("motd",motd)

		image_url="http://www.brainyquote.com"+data['data-img-url']
		import datetime
		dt=datetime.datetime.now().date()
		image_name=str(dt)+".jpg"
        
		#with open(image_name,"wb") as f:
			#r1=requests.get(image_url)
			#f.write(r1.content)
	except Exception as e:
		print("issue",e)



root = Tk()
root.title("S.M.S.")
root.geometry("640x600+400+150")
main_lbl=Label(root, text = "\n STUDENT MANAGEMENT SYSTEM \n BY ADITYA DESALE", font=('Calibri', 30, 'bold'), foreground="red")
main_lbl.config(anchor=CENTER)
main_lbl.pack()

btnadd = Button(root,text="Add",width=10,font=("arial",18,"bold"),command=f1)
btnview = Button(root,text="View",width=10,font=("arial",18,"bold"),command=f3)
btnupdate = Button(root,text="Update",width=10,font=("arial",18,"bold"),command=f6)
btndelete = Button(root,text="Delete",width=10,font=("arial",18,"bold"),command=f8)
btnchart = btnchart = Button(root,text="chart",width=10,font=("arial",18,"bold"),command=f12)
#lblcity = Label(root,text="Location:",font=("arial",18,"bold"))
#entcity = Entry(root,bd=5,font=("arial",18,"bold"))
#lbltemp = Label(root,text="Temp:",font=("arial",18,"bold"))

#lblqt = Label(root,text="QOTD:",font=("arial",18,"bold"))

btnadd.pack(pady=15)
btnview.pack(pady=15)
btnupdate.pack(pady=15)
btndelete.pack(pady=15)
btnchart.pack(pady=15)
#lblcity.place(x=10,y=420)
#lbltemp.place(x=300,y=420)
#lblqt.place(x=10,y=520)

adst = Toplevel(root)
adst.title("Add st.")
adst.geometry("600x700+400+50")

adst_lblrno = Label(adst,text="enter rno",font=("arial",18,"bold"))
adst_entrno = Entry(adst,bd=5,font=("arial",18,"bold"))
adst_lblname = Label(adst,text="enter name",font=("arial",18,"bold"))
adst_entname = Entry(adst,bd=5,font=("arial",18,"bold"))
adst_lblmarks = Label(adst,text="enter marks",font=("arial",18,"bold"))
adst_entmarks = Entry(adst,bd=5,font=("arial",18,"bold"))
adst_btnsave = Button(adst,text="save",width=5,font=("arial",18,"bold"),command=f5)
adst_btnback = Button(adst,text="back",width=5,font=("arial",18,"bold"),command=f2)


adst_lblrno.pack(pady=15)
adst_entrno.pack(pady=15)
adst_lblname.pack(pady=15)
adst_entname.pack(pady=15)
adst_lblmarks.pack(pady=15)
adst_entmarks.pack(pady=15)
adst_btnsave.pack(pady=15)
adst_btnback.pack(pady=15)
adst.withdraw()

vist = Toplevel(root)
vist.title("view st.")
vist.geometry("700x600+400+100")

vist_stdata = ScrolledText(vist,width=30,height=10,font=("arial",18,"bold"))
vist_btnback = Button(vist,text="back",font=("arial",18,"bold"),command=f4)

vist_stdata.pack(pady=15)
vist_btnback.pack(pady=15)
vist.withdraw()

upst = Toplevel(root)
upst.title("update st.")
upst.geometry("600x700+400+50")

upst_lblrno = Label(upst,text="enter rno:",font=("arial",18,"bold"))
upst_entrno = Entry(upst,bd=5,font=("arial",18,"bold"))
upst_lblname = Label(upst,text="enter name:",font=("arial",18,"bold"))
upst_entname = Entry(upst,bd=5,font=("arial",18,"bold"))
upst_lblmarks = Label(upst,text="enter marks:",font=("arial",18,"bold"))
upst_entmarks = Entry(upst,bd=5,font=("arial",18,"bold"))
upst_btnsave = Button(upst,text="Save",font=("arial",18,"bold"),command=f11)
upst_btnback =Button(upst,text="Back",font=("arial",18,"bold"),command=f7)

upst_lblrno.pack(pady=15)
upst_entrno.pack(pady=15)
upst_lblname.pack(pady=15)
upst_entname.pack(pady=15)
upst_lblmarks.pack(pady=15)
upst_entmarks.pack(pady=15)
upst_btnsave.pack(pady=15)
upst_btnback.pack(pady=15)
upst.withdraw()


dest = Toplevel(root)
dest.title("Delete st.")
dest.geometry("500x400+400+100")

dest_lblrno = Label(dest,text="enter rno:",font=("arial",18,"bold"))
dest_entrno = Entry(dest,bd=5,font=("arial",18,"bold"))
dest_btnsave = Button(dest,text="Save",font=("arial",18,"bold"),command=f10)
dest_btnback =Button(dest,text="Back",font=("arial",18,"bold"),command=f9)

dest_lblrno.pack(pady=15)
dest_entrno.pack(pady=15)
dest_btnsave.pack(pady=15)
dest_btnback.pack(pady=15)
dest.withdraw()


import socket
import requests

try:	
	socket.create_connection( ("www.google.com", 80))
	api_address= "http://api.openweathermap.org/data/2.5/weather?units=metric&q=mumbai&appid=c6e315d09197cec231495138183954bd" 		
	res = requests.get(api_address)
		#print(res)
	
	data=res.json()
		#print(data)

	Location=data['name']
	main=data['main']
	temp1=main['temp']
#showinfo("location&temperature",Location+str( temp1))
except Exception as e:
	print("issue",e)
lblcity=Label(root,text="Location:"+Location+"                              Temperature:"+str( temp1),font=("aerial",18,"bold"))
lblcity.pack(pady=15)
#blank5.grid(row=11,column=0+1)
#label=Label(root,text="Temperature:"+str( temp1),font=("aerial",14,"bold"))
#label.grid(row=10,column=2)

import socket
import requests
import bs4


try:	
	socket.create_connection(("www.google.com",80))
	print("YOU are connected")

	res=requests.get("https://www.brainyquote.com/quote_of_the_day")
	print(res)

	soup=bs4.BeautifulSoup(res.text,"lxml")
		#print(soup)

	data=soup.find("img",{"class":"p-qotd"})
		#print(data)

	motd=data['alt']
		#showinfo("motd",motd)

	image_url="http://www.brainyquote.com"+data['data-img-url']
	import datetime
	dt=datetime.datetime.now().date()
	image_name=str(dt)+".jpg"
        
		#with open(image_name,"wb") as f:
			#r1=requests.get(image_url)
			#f.write(r1.content)
except Exception as e:
	print("issue",e)

#lblqt=Label(root,text="QOTD: "+motd,font=("aerial",8,"bold"))
#lblqt.place(x=10,y=520)
#blank6.grid(row=13,column=0+1)	





root.mainloop()
