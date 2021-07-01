
# Name: Bednidhi Rijal (Ben)
# Date: 01-05-2020
# Time:2:22 am

###Program Description#####
#This user interactive program. This program has two basic mode: tree and bird, in both mode this program respond on mouse right click
#however in bird mode it support left and right arrow key to change the orientation of bird. user can select either bird or tree mode
#in tree mode, if user clicks inside the inner ractangle, enclosed by black boundary, tree is rendered in the clicked position
#in bird mode, the bird is displayed in the upper left corner of the window, this bird is copied in the user clicked points inside 
# the inner rectangle in a case if user hit clicks inside rectangle. user also can change the orientation in counter clockwise and
# clockwise using right and left key respectively. This program allows user to swithc between the mode as many times they want and 
# can draw tree or bird based on selection mode.


#import module
import utilities;
import turtle;

#global variable declaration
mode_selection = False;     #default for tree selection 
turtle_rotation = 0;        #define turtle rotation in degree


#This module create inner rectange of size 700 X 700. 
def inner_rectangle(width,height):      #create a inner rectangle in a window where we are going to draw tree and bird
    turtle.hideturtle();            #hide turtle
    turtle.penup();         #disable turtle pen
    turtle.setpos(-width/2,height/2);         #compute first coordinate of rectangle
    turtle.pendown();   #enable turtle pen
    turtle.pensize(5);      #define turtle pensize 5px
    for i in (range(4)):    #create rectange
        turtle.forward(700);        #move turtle 700px in specified direction
        turtle.right(90);       #turn turtle right by 90degree
        

#detect left key if the user is in bird mode, and allows user to change the bird orientation with left key in keyboard
def left_keypress():        #rotate turtle clockwise direction when user click left arrow
    global turtle_rotation;
    turtle_rotation +=5;    #define size of turtle rotation
    if mode_selection == True:  #only if user select bird mode
        turtle.tiltangle(turtle_rotation);  #rotate turtle in clockwise direction
    if turtle_rotation == 360:      #reset turtle_rotation to initial position i.e. 0 once it reach 360deg or one complete rotation
        turtle_rotation = 0;


#detect right key if the user is in bird mod,e and allows user to change the bird orientation with right key in keyboard
def right_keypress():           #rotate turtle anit-clockwise direction when user click right arrow
    global turtle_rotation;
    turtle_rotation -=5;        #define size of turtle rotation
    if mode_selection == True:      #only if user select bird mode
        turtle.tiltangle(turtle_rotation);  #rotate turtle in anti-clockwise direction
    if turtle_rotation == -360:     #reset turtle rotation to initial posistion i.e. 0 once it reach 360deg or one complete rotation
        turtle_rotation = 0;


#The module "handle_click" finds where the user clicks by checking the boundary condition. If user clicks, then the clicks location
# is checked with the boudary condition of two small circle to determine whehter user wants to change the tree-bird mode.
# If this condition fails, it checks with the boundary condition of rectange to find whether it lies inside and if this check pass the boundary
# condition, it is confirmed that the user click point is inside the rectange, otherwise outside the reactangle and this module do not 
# respond the click. once it confirmed that the click is  the rectange, it checks current mode and if it is tree, it calls
# tree function to draw tree inside the window, however if the mode is bird, it calls birds drawing moudle to draw birds in the working
# window.
def handle_click(x,y):          #give position to draw tree and bird
    global mode_selection;      #global variable that store mode slection i.e. Tree mode or Bird mode
    
    if(utilities.distance(0,370,x,y) < 10):       #check whehter user select tree mode
        utilities.draw_circle(0,370,10,'black','green');        #Highlight Tree mode selection
        utilities.draw_circle(100,370,10,'black','lightyellow');    #disable Bird mode selection
        turtle.hideturtle();            #hide turtle i.e. make it invisible
        mode_selection = False;     #Tree mode selection
    
    elif (utilities.distance(100,370,x,y) < 10):        #check whehter user select bird
        utilities.draw_circle(0,370,10,'black','lightyellow');          #Disable Tree mode selection
        utilities.draw_circle(100,370,10,'black','green');              #Highlight Bird selection
        #set turtle position in the upper left corner of the window
        turtle.penup();           
        turtle.setpos(-340,370);
        turtle.showturtle();
        turtle.color('purple');
        mode_selection = True;              #Bird mode selection
    
    elif ((int(x) > -350) and (int(x) < 350) and (int(y) > -350) and (int(y) < 350)):      #check whehter user click inside inner rectangle
        if mode_selection == True:          #Check whther selected mode is Bird
            utilities.stamp_turtle(x,y,'purple');       #stamp a copy of turtle where user clicks in drasing area
            
        else:                               #Tree selected mode
            utilities.draw_tree(x,y);
        
    else:           #outside inner rectangle, do nothing here
        print("");
        

#define main method from where program start execution

def main():

    turtle.tracer(1,0);     #turtle animation is disabled. so that turtle moves instantly
    turtle.update();
    #turtle.setup(800,800);
    turtle.screensize(800,800);     #window size setup of size 800* 800
    turtle.bgcolor("lightyellow");  #Window background color setup
    inner_rectangle(700,700);       #Create inner rectangle of size 700 * 700
    utilities.draw_circle(0,370,10,'black','green');  #Create a circle at the top just outside the inner rectangle
    utilities.display_text_tree_bird(15,370,'Tree');    #write the name of first choice
    utilities.draw_circle(100,370,10,'black','lightyellow');        #Create a circle at the top just outside the inner rectangle
    utilities.display_text_tree_bird(115,370,'Bird');   #write the name of second choice
    
   
    turtle.register_shape('bird', ((-22,-39),(-20,-7),(-7,3),(-11,7),(-12,9),(-11,10),(-9,10),(-3,7),
    (10,24),(30,16),(13,18),(4,0),(14,-6),(6,-13),(0,-4),(-14,-13),(-22,-39))); #define the shape of turtle
    turtle.shape('bird');   #display turtle
    
    
    turtle.listen();    #Define event listener
    turtle.onscreenclick(handle_click);     #called handle_click method when user press mouse left key button
    turtle.onkey(left_keypress,'Left');     #called left_keypress method when user prsee left arrow
    turtle.onkey(right_keypress,'Right');   #called left_keypress method when user prsee left arrow
    
    turtle.done();      #program complete


main();    #call main method