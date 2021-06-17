from tkinter import *
import tkinter.messagebox as tmsg
frame1=Tk()
frame1.configure(bg="yellow")
frame1.title("0-X Game")
frame1.geometry("500x400")
# val=Val(frame1,yscrollcommand=Scrollbar.set())
# function to check the game is win or loose or draw
def checkwingame(value):
	arr=[]
	k=0
	# for i in range(9):
	# 	print(value[i].get())
	for i in range(3):
		tempo=[]
		for j in range(3):
			tempo.append(value[k].get())
			k+=1
		arr.append(tempo)
	for i in range(3):
		if arr[i][0]==arr[i][1]==arr[i][2]=='0' or arr[i][0]==arr[i][1]==arr[i][2]=='X':
			return True
		elif arr[0][i]==arr[1][i]==arr[2][i]=='0' or arr[0][i]==arr[1][i]==arr[2][i]=='X':
			return True
	if arr[0][0]==arr[1][1]==arr[2][2]=='0' or arr[0][0]==arr[1][1]==arr[2][2]=='X':
		return True
	elif arr[0][2]==arr[1][1]==arr[2][0]=='0' or arr[0][2]==arr[1][1]==arr[2][0]=='X':
		return True
	for i in range(3):
		for j in range(3):
			if arr[i][j]!='0' and arr[i][j]!='X':
				return False
	else :
		return -1
width=100
height=100
turn="userA"
def click(i,m):
	global turn 
	if player1select.get()=='0':
		h='0'
		k='X'
	else :
		h='1'
		k='X'
	if turn=="userA":
		if visited[m]==False:
			value[m].set(h)
			result=checkwingame(value)
			if result==True:
				tmsg.showinfo("Result",f"{player1.get()} wins the game")
				print('yes this')
				quit()
			elif result==-1:
				tmsg.showinfo("Result","Game draws")
				quit()
			else :
				turn = "userB"
			visited[m]=True
		else :
			tmsg.showinfo("Warning","This is already selected")
	else :
		if visited[m]==False:
			value[m].set(k)
			result=checkwingame(value)
			visited[m]=True
			if result==True:
				tmsg.showinfo("Result",f"{player2.get()} wins the game")
				print('this is done')
				quit()
			elif result==-1:
				tmsg.showinfo("Result","Game draws")
				quit()
			else :
				turn="userA"
		else:
			tmsg.showinfo("Warning","This is already selected")

# Shows the symbol of both player
def player():
	if player1select.get()=='0':
		Label(frame1,text=f"Now symbol of {player1.get()} is 0 ").pack()
		Label(frame1,text=f"Now symbol of {player2.get()} is X ").pack()

	elif player1select.get()=='X':
		Label(frame1,text=f"Now symbol of {player1.get()} is X ").pack()
		Label(frame1,text=f"Now symbol of {player2.get()} is 0 ").pack()
	func()
value=[0]*9
visited=9*[False]
for i in range(9):
	value[i]= StringVar()
	# value[i].set("")
turn='userA'
def func():
	global value
	print("Yes it works")
	count=0
	f1=Frame(frame1,bg="green")
	button=Button(f1,textvariable=value[0],padx=10,pady=10,font="lucida 15 bold",command=lambda:click(value[0].get(),0))
	button.pack(side=LEFT,padx=10,pady=10)

	button=Button(f1,textvariable=value[1],padx=10,pady=10,font="lucida 15 bold",command=lambda:click(value[1].get(),1))
	button.pack(side=LEFT,padx=10,pady=10)

	button=Button(f1,textvariable=value[2],padx=10,pady=10,font="lucida 15 bold",command=lambda:click(value[2].get(),2))
	button.pack(side=LEFT,padx=10,pady=10)
	f1.pack()

	f1=Frame(frame1,bg="green")
	button=Button(f1,textvariable=value[3],padx=10,pady=10,font="lucida 15 bold",command=lambda:click(value[3].get(),3))
	button.pack(side=LEFT,padx=10,pady=10)

	button=Button(f1,textvariable=value[4],padx=10,pady=10,font="lucida 15 bold",command=lambda:click(value[4].get(),4))
	button.pack(side=LEFT,padx=10,pady=10)

	button=Button(f1,textvariable=value[5],padx=10,pady=10,font="lucida 15 bold",command=lambda:click(value[5].get(),5))
	button.pack(side=LEFT,padx=10,pady=10)
	f1.pack()

	f1=Frame(frame1,bg="green")
	button=Button(f1,textvariable=value[6],padx=10,pady=10,font="lucida 15 bold",command=lambda:click(value[6].get(),6))
	button.pack(side=LEFT,padx=10,pady=10)

	button=Button(f1,textvariable=value[7],padx=10,pady=10,font="lucida 15 bold",command=lambda:click(value[7].get(),7))
	button.pack(side=LEFT,padx=10,pady=10)

	button=Button(f1,textvariable=value[8],padx=10,pady=10,font="lucida 15 bold",command=lambda:click(value[8].get(),8))
	button.pack(side=LEFT,padx=10,pady=10)
	count+=1
	f1.pack()
	count=0
Label(frame1,text="Name of player 1",font="Calibari 10 bold").pack(anchor="w")
player1=StringVar()
Entry(frame1,textvariable=player1).pack(anchor="e")
Label(frame1,text="Name of player 2",font="Calibari 10 bold").pack(anchor="w")
player2=StringVar()
Entry(frame1,textvariable=player2).pack(anchor="e")
Label(frame1,text="player 1 Choose your digit from 0 and X").pack()
player1select=StringVar()
player1value=Entry(frame1,textvariable=player1select).pack()
Button(frame1,text="Submit",command=player).pack()
# Scrollbar.config(command=frame1.yview)
frame1.mainloop()