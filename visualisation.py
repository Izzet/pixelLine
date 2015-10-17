from tkinter import *
canvas = False
canvas_width = 800
canvas_height = 400

master = Tk()
	
canvas = Canvas(master, 
	width=canvas_width,
	height=canvas_height)
canvas.pack()

def addPointAt(x,y, canvas):
	scale = 2
	y0 = int(canvas_height * 3 / 4)
	x0 = int(canvas_width / 4 )
	canvas.create_rectangle(x+x0,-y+y0,x+x0+scale,-y+y0-scale, fill="black")

mainloop()