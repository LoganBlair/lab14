#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in colision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
tx1 = 200
ty1 = 20
tx2 = 280
ty2 = 80
target = drawpad.create_rectangle(tx1,ty1,tx2,ty2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 5
didwehit = True

class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Up", background= "green")
		self.button1.grid(row=1,column=1)					
		# "Bind" an action to the first button												
		self.button1.bind("<Button-1>", self.button1Click)
                
                self.button2 = Button(self.myContainer1)
                self.button2.configure(text="Right", background= "green")
                self.button2.grid(row=2, column=2)
                self.button2.bind("<Button-1>", self.button2Click)
                
                self.button3 = Button(self.myContainer1)
                self.button3.configure(text="Left", background= "green")
                self.button3.grid(row=2, column=0)
                self.button3.bind("<Button-1>", self.button3Click)
                
                self.button4 = Button(self.myContainer1)
                self.button4.configure(text="Down", background= "green")
                self.button4.grid(row=3, column=1)
                self.button4.bind("<Button-1>", self.button4Click)
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()

		
	def button1Click(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                drawpad.move(player,0,-5)
		# Get the coords of our target
                if x1 < 0:
                    drawpad.move(player,-4,0)
        	
	def button2Click(self, event):   
		global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                drawpad.move(player,5,0)     
				
		
	def button3Click(self, event):   
		global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                drawpad.move(player,-5,0)	
		
		
		
	def button4Click(self, event):                  
		global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                drawpad.move(player,0,5)	
	
	
	
	def animate(self):
	    global drawpad
	    global player
	    global target
	    global direction
	    x1, y1, x2, y2 = drawpad.coords(target)
	    if x2 > 480:
                direction = -5
            elif x1 < 0:
                direction = 5
	    drawpad.move(target,direction,0)	    
	    drawpad.after(10, self.animate)	

							
		
		# Ensure that we are doing our collision detection
		# After we move our object!
            didWeHit = self.collisionDetect()
            if didWeHit == False:
                direction = 0
                    # We made contact! Stop our animation!
                print "Do something"
	# Use a function to do our collision detection
	# This way we only have to write it once, and call it from
	# every button click function.
	def collisionDetect(self):
                global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                tx1, ty1, tx2, ty2 = drawpad.coords(target)
                if  x1 > tx1 and x1 < tx2 + 1 and y1 > ty1 and y1 < ty2+1:
                    didwehit = False
                    return False
                else:
                    return True
                # Do your if statement - remember to return True if successful!
                
	    
		
myapp = MyApp(root)

root.mainloop()