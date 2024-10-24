import pygame as pyg

# ---------------- CONSTANTS
X = 0
Y = 1

class Shapes:
  SQUARE = "s"
  RHOMBUS = "r"
  PARRALELLOGRAM = "p"
  CIRCLE = "c"
  OVAL = "o"

class Defaults:
  DIAMETER = 100
  POSITION = (640, 360)
  COLOR = "black"
  TEXT = ""
  
  def rectPoints(pos):
    Xoffset = 60
    Yoffset = 35
    
    top_left = (pos[X]-Xoffset, pos[Y]+Yoffset)
    top_right = (pos[X]+Xoffset, pos[Y]+Yoffset)
    
    bottom_right = (pos[X]+Xoffset, pos[Y]-Yoffset)
    bottom_left = (pos[X]-Xoffset, pos[Y]-Yoffset)
    
    return (top_left, top_right, bottom_right, bottom_left)
  
  def rhombusPoints(pos):
    offset = 50
    
    top = (pos[X], pos[Y]+offset)
    left = (pos[X]-offset, pos[Y])
    bottom = (pos[X], pos[Y]-offset)
    right = (pos[X]+offset, pos[Y])
    
    return (top, left, bottom, right)

  def ovalPoints(pos):
    Xoffset = 60
    Yoffset = 40

    top_left = (pos[X]-Xoffset, pos[Y]+Yoffset)
    top_right = (pos[X]+Xoffset, pos[Y]+Yoffset)
    
    bottom_right = (pos[X]+Xoffset, pos[Y]-Yoffset)
    bottom_left = (pos[X]-Xoffset, pos[Y]-Yoffset)
    
    return (top_left, top_right, bottom_right, bottom_left)

    

# ----------------- PYGAME VARS

pyg.init()
screen = pyg.display.set_mode((1280, 720))
clock = pyg.time.Clock()
dt = 0
running = True

# ----------------- OBJECT VARS
nextId = 0

class Quad:
  def __init__(self, points):
    self.points = points

class Ellipse:
  def __init__(self, points):
    self.points = points

class Square(Quad):
  TOPLEFT = 0
  TOPRIGHT = 1
  BOTTOMRIGHT = 2
  BOTTOMLEFT = 3
  
class Rectangle(Quad):
  TOPLEFT = 0
  TOPRIGHT = 1
  BOTTOMRIGHT = 2
  BOTTOMLEFT = 3
  

class Rhombus(Quad):
  TOP = 0
  LEFT = 1
  BOTTOM = 2
  RIGHT = 3
    

class Oval(Ellipse):
  x_dia = 0
  y_dia = 1
  
class Circle(Ellipse):
  pass;
    
    
# -----------------------------

# ------------- GLOBAL FUNCTIONS

def get_next_id():
    global nextId
    nextId+=1
    return nextId

def get_arrow_lines(startObj, endObj):
  pass 

def check_if_pos_empty(pos):
    pass

def draw_obj(obj):
  
  match obj.shape:
    case Rhombus() | Rectangle():
      pyg.draw.polygon(screen, obj.color, obj.shape.points)
    
    case Oval():
      width = obj.shape.points[1][X] - obj.shape.points[0][X]
      height = obj.shape.points[0][Y] - obj.shape.points[3][Y]

      pyg.draw.ellipse(screen, obj.color, pyg.Rect(*obj.shape.points[3], width, height))
    

# ----------------------------

objects = []

class Object:
    def __init__(self, *args, **kwargs):
      # Get Pos
        try:
            self.pos = kwargs["pos"]
        except KeyError:
            self.pos = Defaults.POSITION

        # Get Text
        try:
            self.text = kwargs["text"]
        except KeyError:
            self.text = Defaults.TEXT

        # Get Color
        try: 
          self.color = kwargs["color"]
        except KeyError:
          self.color = Defaults.COLOR
        
          
        self.id = get_next_id()
        
        self.connections = {}
        
        
        
    def getPos(self):
      return pyg.Vector2(*self.pos)
    
    def addNewConnection(self, id):
      objToConnect = objects[id]
      self.connections[id] = { } # TODO: Make this have a point on the base object AND the object it's connected to
      
class Action(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        try:
          self.shape = kwargs["shape"]
        except KeyError:
          self.shape = Rectangle(Defaults.rectPoints(self.pos))

class Condition(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        try: 
          self.shape = kwargs["shape"]
        except KeyError:
          self.shape = Rhombus(Defaults.rhombusPoints(self.pos))

class StartStop(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            self.shape = kwargs["shape"]
        except KeyError:
            self.shape = Oval(Defaults.ovalPoints(self.pos))

objects.extend([
    Condition(pos=(500, 500)),
    Action(pos=(400,400)),
    StartStop(),
])

# -------------------------------- GAME LOOP
while running:

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    screen.fill('white')
    #--------------------- DISPLAY

    for obj in objects:
        draw_obj(obj)


    #---------------------------
    pyg.display.flip()
    dt = clock.tick(60) / 1000
pyg.quit()


