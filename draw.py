from display import *
from matrix import *
import math

def add_box( points, x, y, z, width, height, depth ):
    #front bottom
    add_edge(edges, x,y,z, x + width, y, z)
    #front leftside
    add_edge(edges, x,y,z, x, y+ height, z)
    #front rightside
    add_edge(edges, x + width,y, z, x, y + height, z)
    #front top
    add_edge(edges, x,y + height,z, x + width, y + height, z)
    #back bottom
    add_edge(edges, x,y,z - depth, x + width, y, z- depth)
    #back leftside
    add_edge(edges, x, y, z - depth, x, y + height, z - depth)
    #back rightside
    add_edge(edges, x + width,y, z - depth, x + width, y + height, z- depth)
    #back top
    add_edge(edges, x,y + height,z - depth, x + width, y + height, z - depth)
    #center upperleft
    add_edge(edges, x,y + height,z, x, y + height, z - depth)
    #center upperright
    add_edge(edges, x + width,y + height,z, x + width, y + height, z - depth)
    #center bottomleft
    add_edge(edges, x,y,z, x, y, z - depth)
    #center bottomright
    add_edge(edges, x + width,y,z, x + width, y, z - depth)

def add_sphere( points, cx, cy, cz, r, step ):
    #adds the sphere edges (not connecting points to each other, but rather to another point 1 unit away)
    sphere = generate_sphere(points, cx, cy, cz, r, step)

def generate_sphere( points, cx, cy, cz, r, step ):
    #return a matrix of points

def add_torus( points, cx, cy, cz, r0, r1, step ):
    tor = generate_torus(points, cx, cy, cz, r0, r1, step)

def generate_torus( points, cx, cy, cz, r0, r1, step ):
    #returns a matrix of points

def add_circle( points, cx, cy, cz, r, step ):
    #print 'add_circle'
    i = 0
    lastx = cx + r
    lasty = cy
    #for now, we're using float iteration. This might cause some things to be broken in the future, but we'll see.
    while i < (2 * math.pi):
        currx = (r * math.cos(2 * math.pi * i) + cx)
        curry = (r * math.sin(2 * math.pi * i) + cy)
        add_edge(points, lastx, lasty, cz, currx, curry, cz)
        lastx = currx
        lasty = curry
        i += step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    #print 'add_curve'
    xcoef = generate_curve_coefs(x0, x1, x2, x3, curve_type)
    ycoef = generate_curve_coefs(y0, y1, y2, y3, curve_type)
    i = 0.0
    lastx = x0
    lasty = y0
    #for now, we're using float iteration. This might cause some things to be broken in the future, but we'll see.
    while i < 1.0:
        currx = 0
        curry = 0
        for cnt in range(4):
            currx += xcoef[0][cnt] * (i ** (3 - cnt))
            curry += ycoef[0][cnt] * (i ** (3 - cnt))
        add_edge(points, lastx, lasty, 0, currx, curry, 0)
        lastx = currx
        lasty = curry
        i += step




def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )




def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
