from tkinter import *
import os
# Create object
app = Tk()
app.title("Pacman Search Algorithms AI320")
# Adjust size
app.geometry( "300x450" )

# Start Pacman Search
def start():
    if (mazeSizeChoice.get()=="big"):
        string = "python pacman.py -l" +  mazeSizeChoice.get() + "Maze -z .5 -p SearchAgent -a fn=" + algorithmChoice.get()+ ",heuristic=" + heuristicChoice.get()+ "Heuristic"
    else:
        string = "python pacman.py -l" +  mazeSizeChoice.get() + "Maze -p SearchAgent -a fn=" + algorithmChoice.get()+ ",heuristic=" + heuristicChoice.get()+ "Heuristic"
    os.system(string)


# Dropdown menus options
sizeOptions = [
    "tiny",
    "medium",
    "big",
]
algorithmOptions = [
    "dfs",
    "bfs",
    "ucs",
    "astar",
    "gbfs",
]
heuristicOptions = [
    "manhattan",
    "euclidean",
]

###########################
#     Select Maze Size    #
###########################
mazeSizeLabelText = StringVar()
mazeSizeLabelText.set("Maze Size ")
mazeSizeLabel = Label( app, textvariable=mazeSizeLabelText, relief=FLAT, font=('Arial',12,'bold') )
mazeSizeLabel.grid(column=0, row = 1, padx=(15,0), pady=(40, 0))

# datatype of menu text
mazeSizeChoice = StringVar()

# initial menu text
mazeSizeChoice.set( "medium" )

# Create Dropdown menu
mazeSizeDrop = OptionMenu( app , mazeSizeChoice , *sizeOptions )
mazeSizeDrop.config(width=20)
mazeSizeDrop.grid(column=1, row = 1, pady=(40, 0) )

###########################
#     Select Algorithm    #
###########################
algorithmLabelText = StringVar()
algorithmLabelText.set("Algorithm")
algorithmLabel = Label( app, textvariable=algorithmLabelText, relief=FLAT, font=('Arial',12,'bold') )
algorithmLabel.grid(column=0, row = 2, pady=(40, 0))
 
# datatype of menu text
algorithmChoice = StringVar()
  
# initial menu text
algorithmChoice.set( "dfs" )
  
# Create Dropdown menu
algorithmDrop = OptionMenu( app , algorithmChoice , *algorithmOptions )
algorithmDrop.config(width=20)
algorithmDrop.grid(column=1, row = 2, pady=(40, 0)) 


###########################
#     Select Heuristic    #
###########################
heuristicLabelText = StringVar()
heuristicLabelText.set("Heuristic")
heuristicLabel = Label( app, textvariable=heuristicLabelText, relief=FLAT, font=('Arial',12,'bold') )
heuristicLabel.grid(column=0, row = 3, pady=(40, 0))
 
# datatype of menu text
heuristicChoice = StringVar()
# initial menu text
heuristicChoice.set( "manhattan" )
# Create Dropdown menu
heuristicDrop = OptionMenu( app , heuristicChoice , *heuristicOptions )
heuristicDrop.config(width=20)
heuristicDrop.grid(column=1, row = 3, pady=(40, 0)) 


# Start Button
button = Button( app , text = "Start!" , width=15, height= 2, command = start ).grid(row = 4, pady=(50, 0), columnspan=3)


###########################
#         Credits         #
###########################

createdLabelText = StringVar()
createdLabelText.set("Created by:")
creditsLabel = Label( app, textvariable=createdLabelText, relief=FLAT, font=('Arial',8,'bold'))
creditsLabel.grid(column=0, row = 5, pady=(50, 0), columnspan=3)


name1LabelText = StringVar()
name1LabelText.set("Steven Albert")
name1Label = Label( app, textvariable=name1LabelText, relief=FLAT, font=('Arial',8))
name1Label.grid(column=0, row = 6, padx=(30, 0))

name2LabelText = StringVar()
name2LabelText.set("Judy Wagdy")
name2Label = Label( app, textvariable=name2LabelText, relief=FLAT, font=('Arial',8))
name2Label.grid(column=1, row = 6, padx=(30, 0))

ID1LabelText = StringVar()
ID1LabelText.set("2019/01611")
ID1Label = Label( app, textvariable=ID1LabelText, relief=FLAT, font=('Arial',8))
ID1Label.grid(column=0, row = 7, padx=(30, 0))

ID2LabelText = StringVar()
ID2LabelText.set("2019/02181")
ID2Label = Label( app, textvariable=ID2LabelText, relief=FLAT, font=('Arial',8))
ID2Label.grid(column=1, row = 7, padx=(30, 0))

# Execute tkinter
app.mainloop()