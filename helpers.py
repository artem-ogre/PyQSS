'''
 Copyright Artem Amirkhanov 2014
 Distributed under the MIT Software License (See accompanying file LICENSE.txt)
 Contact the author: artem.ogre@gmail.com
'''

#======================================================
# Helper functions and classes
# Provides useful classes and methods for working with QSS
#======================================================

from copy import copy

def inverse(val):
    "Returns an inverse value of a color component"
    return 255-val

class Rgba():
    """Class representing color in rgba.
    Has some auxiliary functions and basic overriden operators"""
    def __init__(self, a_rgba) :
        def crop(e) :
            "Perform [0, 255] boundary check"
            if e>255 :
                e = 255
            elif e<0:
                e = 0
            return e
        self.rgba = list(map(crop, a_rgba))
    def invCol(self):
        "Inverse the color (not opacity), modify self"
        res = [255 - e for e in self.rgba[:3]] + self.rgba[3:]
        self.rgba = res
    def inverse(self):
        "Inverse the color (not opacity), ruturn new Rgba"
        return Rgba([255 - e for e in self.rgba[:3]] + self.rgba[3:])
    def __add__(self, other) :
        if(type(other) == int) :
            return Rgba( [i + other for i in self.rgba[:3]] + self.rgba[3:] )
        else:
            return Rgba( [i + j for i,j in zip(self.rgba[:3],other.rgba[:3])] )
    def __sub__(self, other) :
        if(type(other) == int) :
            return Rgba( [i - other for i in self.rgba[:3]] + self.rgba[3:] )
        else:
            return Rgba( [i - j for i,j in zip(self.rgba,other.rgba)] )
    def __mul__(self, other) :
        if(type(other) == int or type(other) == float) :
            return Rgba( [int(i * other) for i in self.rgba] )
        else:
            return Rgba([i*j for i,j in zip(self.rgba,other.rgba)])
    def __str__(self) :
        res = "rgba(" + str(self.rgba[0])
        for e in self.rgba[1:] :
            res = res + ", " + str(e)
        res+= ")"
        return res

def rgb(r, g, b) :
    """Create Rgba instance with a==255, based on r,g,b values"""
    return Rgba( [r, g, b, 255] )

def rgba(r, g, b, a = 255) :
    """Create Rgba instance based on r,g,b,a values"""
    return Rgba( [r, g, b, a] )

def gray(gr) :
    """Create Rgba instance for gray color with intensity == gr"""
    return Rgba( [gr, gr, gr, 255] )

def interpolate(col1, col2, t) :
    """Interpolate between col1 and col2 based on t[0,1].
    t == 0 corresponds to col1"""
    l = [int(i + (j-i)*t) for i,j in zip(col1.rgba[:3], col2.rgba[:3])]
    l.append(255)
    return Rgba(l)

def gradientWithBreak(pt1, pt2, t, col1, col2, step = 0) :
    """Generates a gradient where color brakes at t=[0,1].
    The break magnitude is step. Returns a proper QSS gradient description."""
    intCol = interpolate(col1, col2, t)
    res_str  = "background: qlineargradient(spread:pad, \n\t\t";
    res_str += "x1:" + str( pt1[0] ) + ", y1:" + str( pt1[1] ) + ", \n\t\t"
    res_str += "x2:" + str( pt2[0] ) + ", y2:" + str( pt2[1] ) + ", \n\t\t"
    res_str += "stop:0 " + str(col1) + ", \n\t\t"
    res_str += "stop:" + str(t - 0.001) + " " + str(intCol + step) + ", \n\t\t"
    res_str += "stop:" + str(t) + " " + str(intCol - step) + ", \n\t\t"
    res_str += "stop:1 " + str(col2) + ");"
    return res_str
