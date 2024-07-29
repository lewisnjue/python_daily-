import math 

print(math.pi)
""" 
WE ARE NOT GOING HERE TO LEARN ANYTHING NEW 
TO USE PI IN PYTHON YOU CAN DO THE FOLLOWING 
import math 
print(math.pi)
HERE WE ARE GOING TO SEE 3 FASCINATING WAYS TO APPROXIMATE PI 
IN PYTHON 
1 - 1/3 + 1/5 - 1/7 + 1/ 9 ( HERE THE NUMERATOR IS ALWAYS ONE 
 ANE THE DENOMANATOR ARE ODD NUMBERS  AND ALTERNATION - AND + ) 
 ALL THIS EXPRESSION CAN BE EXPRESSESD AS 
 [(-1)^k/2K + 1] 
IF YOU CONTINUE THIS WAY YOU WILL FINNALY GET PI / 4 
this is the leibniz formula of pi 
this formula is a fascinating example of how an infinites series  can 
be used too approximate a transcendental number like pi 
HOWEVER ITS IMPORTANT TO NOTE :
. THIS SERIES CONVERGES VERY SLOWLY , YOU WOULD NEED TO CALCULATE 
AN EXTREMELY LARGE NUMBER OF TERMS TO GET A REASONABLY ACCURATE APPROXIMATION OF PI 
. THERE ARE MORE EFFICEINT METHODS FOR CALCULATIN PI USED IN 
MODERN COMPUERS .

 """

# LETS IMPREMENT ALL THIS 

import math 
def leibniz(n_terms):
    pi_approx = 0 
    for k in range(n_terms):
        pi_approx += (-1)**k / ((2 * k) + 1 )


    return 4 * pi_approx

n_terms = 1000000

print(leibniz(n_terms))
# to take it to infinity 
print(4 * math.atan(1)) # this is inifity


"""  

n Python, math.atan(1) returns pi/4 in radians.  
Source icon

This is because atan is the inverse tangent function, and the tangent of pi/4 is 1.

So, math.atan(1) is essentially asking: "What angle has a tangent of 1?" The answer is pi/4 radians or 45 degrees.
"""



""" 
ANOTHER WAY TO ESTIMATE PY IS USING THIS , IMAGING YOU HAVE A CODINATE SYSTEM 
THAT IS A SQUIARE THROUNG ONE IN ALL DIRENCTION AND A CIRCURE 
THAT IS INSIDE THE SQUIRE , YOU PICK MANY RANDOM NUMBERS INSIDE THE SQUIRE, NOW 
YOU WILL HAVE MANY NUMBERS INSIDE THE CIRCLE AND OTHER OUTES IF YOU USE 
THE FOLLOWING FORMULA YOU WILL ALSO GET AN APPROXIMATE OF THE 
PI 

4 * inside circule / insid circule + outside circule  you will
get an apploximate of the pi 


x^2 + y^2 <= 1 -> thi is inside the circule 

 """

import random 
def monte_carlo_pi(n_points):
    inside_circule = 0 
    for _ in range(n_points):
        x , y = random.uniform(-1,1),random.uniform(-1,1)
        if x**2 + y**2 <=1:
            inside_circule +=1
    return 4 * inside_circule / n_points




n_points = 100000
print(monte_carlo_pi(n_points))
""" the other method is to use BUFFONS NEEDLE 

n Python, math.atan(1) returns pi/4 in radians.  
Source icon

This is because atan is the inverse tangent function, and the tangent of pi/4 is 1.

So, math.atan(1) is essentially asking: "What angle has a tangent of 1?" The answer is pi/4 radians or 45 degrees.
The Setup

    A floor is ruled with parallel lines a distance d apart.
    A needle of length l is dropped randomly onto the floor.

The Question

What is the probability that the needle will intersect one of the lines?
The Formula

For the case where the needle length l is less than or equal to the distance between the lines d, the probability P is given by:

P = (2 * l) / (π * d)

Explanation

The derivation of this formula involves calculus and geometric probability. It considers two random variables:  
Source icon

    The distance x from the center of the needle to the nearest line.
    The angle θ between the needle and the lines.

By analyzing the possible positions of the needle and using integral calculus, we arrive at the formula above.
Estimating Pi

An interesting application of Buffon's needle problem is to estimate the value of pi. By performing the experiment a large number of times and recording the number of times the needle intersects a line, we can approximate pi using the formula:  
Source icon

π ≈ (2 * number of drops) / (number of intersections * d)


 """

num_throws = 100000
line_spacing = 1
needle_lenght = 1 

crosses = 0 

for _ in range(num_throws):
    endpoint = random.uniform(0,line_spacing)
    angle = random.uniform(0,120)
    angle_in_radians = math.radians(angle)
    projection = needle_lenght * angle_in_radians

    if endpoint + projection > line_spacing : 
        crosses +=1 
    



print(2 * num_throws / crosses )


