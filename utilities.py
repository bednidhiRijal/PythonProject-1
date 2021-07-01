#import module
import turtle;
import math;
import random;

#global variable declaration and initalize them with turtle inital positition
turtle_x = turtle.xcor();
turtle_y = turtle.ycor();
turtle_pen_color = turtle.pencolor();
turtle_fill_color = turtle.fillcolor();


#This module draw a triangle with the help of center, widht and height. The coordinate of trinagle is calculated with
#the help of center, height, and width. we can get the left bottom coordinate of triangle by moving width/2 in negative 
#x direction from center i.e x = center_x-width/2 similarly we get the y coordinate by moving hight/2 in negative y direction
#from the center i.e. y=center_y-height/2. Using the same principle i calculated all other two cooridante and draw a triangle
def draw_triangle(centre_x, centre_y, width, height, pen_color, fill_color):    #draw trinagle
    save_state();
    
    turtle.penup();                    #turtle pen is disable
    turtle.setpos(centre_x-width/2,centre_y-height/2);      #compute first coordinate of triangle
    turtle.pendown();                                        #turtle pen is enable
    turtle.pencolor(pen_color);             #define turtle pen color
    turtle.fillcolor(fill_color);           #define color to be filled inside an object
    turtle.begin_fill();                    #start color filling
    turtle.goto(centre_x, centre_y+height/2);           #turtle move from first coordinate to second coordinate of triangle
    turtle.goto(centre_x+width/2,centre_y-height/2);    #turtle moove from second coordinate to third coordinate of triangle
    turtle.goto(centre_x-width/2,centre_y-height/2);    #turtle move from third coordinate to first coordinate of triangle
    turtle.end_fill();                  #complete color filling inside an object
    
    restore_state();


#This module draw a reactangel with the help of centre, height and widht. The bottom left coordinate can be calculated by moving 
# width/2 distance in negative x direction and height/2 in negative y-direction from the center of rectangle. 
# ie. the bottom left coordinate is (centre_x-width/2, center_y-height/2). Using the same principle, i calculate other three point
# of rectangle and draw the rectangle    
def draw_rectangle(centre_x, centre_y, width, height, pen_color, fill_color):   #draw rectangle    
    save_state();
    
    turtle.penup();         #turtle pen is disable
    turtle.setpos(centre_x-width/2,centre_y-height/2);  #compute first coordinate of rectangle
    turtle.pendown();   #turtle pen is enable
    turtle.pencolor(pen_color);     #define turtle pen color
    turtle.fillcolor(fill_color);    #define color to be filled inside rectangle
    turtle.begin_fill();            #start filling color inside rectangle
    turtle.goto(centre_x-width/2,centre_y+height/2);        #Turtle move from first coordinate to second coordinate of rectangle
    turtle.goto(centre_x+width/2,centre_y+height/2);        #Turtle move from second coordinate to third coordinate of rectangle
    turtle.goto(centre_x+width/2,centre_y-height/2);        #Turtle move from third coordinate to fourt coordinate of rectangle
    turtle.goto(centre_x-width/2,centre_y-height/2);        #Turtle move from fourt coordinate to first coordinate of rectangle
    turtle.end_fill();          #complete color filling inside an object
    
    
    restore_state();
    

#this module draw a circle with (centre_x, centre_y) and radius and fill inside with color fill_color. For drawing circle turtle circle
# funtion is used and this turtle.circle() starts drawing circle from the current crusor position. However, we need to draw the circle
# with centre_x and centre_y, therefore, i calculate one coordinate that lies on the boundary of circle and start drawing the circle 
# from that boundary coordiante. Boundary coordiante is claculated by moving distance equivalent to radius in negative y-direction
# so that boundary point of circle is calculated as (centre_x, centre_y-radius)
def draw_circle(centre_x, centre_y, radius, pen_color, fill_color): # draw circle; used to create radio button that is used to select tree and bird mode
    save_state();
    
    turtle.hideturtle();        #hide turtle
    turtle.penup();             #disable turtle pen
    turtle.setpos(centre_x,centre_y-radius);    #compute a point that lies on the boundary of a circle
    turtle.pendown();       #enable turtle pen
    turtle.pensize(1);      #define turtle pensize to 1px
    turtle.pencolor(pen_color);     #define turtle pen color
    turtle.fillcolor(fill_color);   #define color to be filled inside an object
    turtle.begin_fill();        #start filling color inside an object
    turtle.circle(radius);      #draw a circle centre at centre_x and centre_y
    turtle.end_fill();          #complete color filling inside a circle
        
    restore_state();
        


#This module is used to copy the bird, from a fixed location i.e. just outside the upper left corner of rectangle, inside 
# rectangle. after stamping the turtle, it returns back to its orginal position that is just outside the upper left corner of rectangle
def stamp_turtle(centre_x, centre_y, color):        #copy turtle in the particular position of window where user clicked
    save_state();

    turtle.penup();         #disable turtle pen
    id = turtle.stamp();    #copy the stamp of the turtle shape
    turtle.setpos(centre_x,centre_y);   #copy the stamp of the turtle shape in coordinate(centre_x,centre_y) of window
    turtle.color(color);        #turtle color
    turtle.clearstamp(id);      #delete the original turtle whose stampId is id
    turtle.stamp();

    restore_state();


def save_state():       #It save the turtle parameters like position, fill color, pen color in global variable
    global turtle_x, turtle_y, turtle_fill_color, turtle_pen_color;
    turtle_x = turtle.xcor();
    turtle_y = turtle.ycor();
    turtle_fill_color = turtle.fillcolor();
    turtle_pen_color = turtle.pencolor();

#This moduel restore the previous state ie. the state before the turtle starts drawing in global vairable 
def restore_state():
    turtle.penup();
    turtle.goto(turtle_x,turtle_y);
    turtle.fillcolor(turtle_fill_color);
    turtle.pencolor(turtle_pen_color);
    turtle.pendown();


def display_text_tree_bird(init_x,init_y,mode_name):        #write the user selection mode in text
    turtle.hideturtle();    #hide default turtle
    turtle.penup();         #disable turtle pen
    turtle.setpos(init_x,init_y-10);    #define starting position of text i.e. Tree or Bird
    turtle.pendown();           #enable turtle pen
    turtle.pensize(1);          #define turtle pen size
    turtle.write(mode_name, font=("Arial",12,"normal"));        #write text and set the font size of text to 12px

    
def distance(x1, y1, x2, y2):       #compute absolute distance between two point
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2);
    return dist;
    

#this module compute the scaled coordinate of triangle, rectangle and call draw_triangle and draw_rectangle module 
# to draw a tree. It receives user clicked coordiante and this point always lies in the middle of the top boundary line of rectangle
# and in the middle of the bottom boundary line of triangle. therefore, i need to move down by rectangle_height/2, which i called
# stem offset in the program, to get the center of rectangle and pass this center value, scaled height and width
# to the draw_rectangle module to draw stem of tree. similarly i move up by traingle_height/2, which i called triangle
# offset, to get the center of traingle. once i find the center of one triangle, i shifted the same center up by 60% of height to find
# the center of another traingle so that these two triangle overlap by 40%, similarly i get the coordiante of last traingle and call
# draw_triangle module passing the center, scaled height and widht of each  triangle respectively to draw branch and leaves. 

def draw_tree(centre_x,centre_y):           #draw a tree that consist three overlapping triangle and one rectangle
    scale_factor = random.uniform(0.7,1.3);     #generate a random scaling factor in the range 0.7 to 1.3
    stem_width = 15*scale_factor;               #scaling reference stem width
    stem_height = 80*scale_factor;              #scaling reference stem height       
    leaf_height = 50*scale_factor;              #scaling reference leaf width
    leaf_width = 100*scale_factor;              #scaling reference leaf height
    leaf_overlap = leaf_height*0.6;             #compute overlapping distance in y direction
    stem_offset = stem_height/2;  #compute stem offset. Tells turtle how much it needs to move down to get the center of the stem 
    leaf_offset = leaf_height/2;    #compute leaf offset. Tells turtle how much it needs to move up to get the center of the single leaf
    draw_rectangle(centre_x,centre_y-stem_offset,stem_width, stem_height,'red','red');    #draw stem of a tree
    #draw branches and leaves by overlapping 3 triangle
    draw_triangle(centre_x,centre_y+leaf_offset,leaf_width,leaf_height,'green','green');
    draw_triangle(centre_x,centre_y+leaf_offset + leaf_overlap,leaf_width,leaf_height,'green','green');
    draw_triangle(centre_x,centre_y+leaf_offset*2+leaf_overlap,leaf_width,leaf_height,'green','green');
