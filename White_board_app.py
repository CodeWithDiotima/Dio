'''White Board App
Author: Diotima Nag
Date: 16/09/2021'''

from tkinter import *       #necessary packages
from datetime import date

def write(event,colour):    #write on board with fixed marker
    x1,y1,x2,y2=(event.x-3),(event.y-3),(event.x+3),(event.y+3)
    board.create_line(x1,y1,x2,y2,fill=colour,width=5)
    
def change_colour(col):     #change marker
    global colour
    colour=col
    
def clear_all(canvas):      #clean board
    canvas.delete('all')
    
colour="black"              #default colour of marker is black
bg="white"

root=Tk()                   #creating window
root.title("White Board")
default=StringVar(root,"black")
board=Canvas(root,width=1200,height=600,bg=bg)  #create board
board.grid(column=0,row=2,columnspan=7)

board.bind("<B1-Motion>",lambda event:write(event,colour))      #write when mouse clicked

l=Label(root,text="Choose Colour from Palette",font=('arial',10))
l.grid(column=2,row=0,columnspan=3)

today = date.today()
# dd/mm/YY
d=today.strftime("%d/%m/%Y")            #insert date on top of board
board.create_text(1150,30,text=d,font=('arial',12))

#design colour palette
b1=Radiobutton(root,text="Red",variable=default,value="red",fg="red",command=lambda:change_colour('red'))
b2=Radiobutton(root,text="Black",variable=default,value="black",fg="black",command=lambda:change_colour('black'))
b3=Radiobutton(root,text="Green",variable=default,value="green",fg="green",command=lambda:change_colour('green'))
b4=Radiobutton(root,text="Magenta",variable=default,value="magenta",fg="magenta",command=lambda:change_colour('magenta'))
b5=Radiobutton(root,text="Brown",variable=default,value="brown",fg="brown",command=lambda:change_colour('brown'))

#option to erase particular text on board
b6=Button(text="Clear",foreground="black",command=lambda:change_colour('white'))

#option to clear the board
b7=Button(text="Clear All",foreground="black",command=lambda:clear_all(board))

#make position of the buttons on window
b1.grid(column=0,row=1,columnspan=2)
b2.grid(column=1,row=1,columnspan=2)
b3.grid(column=2,row=1,columnspan=2)
b4.grid(column=3,row=1,columnspan=2)
b5.grid(column=4,row=1,columnspan=2)
b6.grid(column=5,row=1,columnspan=2)
b7.grid(column=6,row=1,columnspan=2)

#main loop
root.mainloop()

