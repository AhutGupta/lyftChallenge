from geopy.distance import great_circle;

class Point:
    lat = 32.132832 
    long= -81.250125
    def __init__(self, lati, longi):
        self.lat = lati
        self.long = longi

def Distance( X, Y ):
    Point1 = (X.lat, X.long)
    Point2 = (Y.lat, Y.long)
    distance = great_circle(Point1, Point2).miles
    return distance

#Enter the co-ordinates here
A = Point(47.606209, -122.332071)
B = Point(37.368830, -122.03635)
C = Point(30.267153, -97.743061)
D = Point(40.714353,-74.005973)

AB = Distance(A, B)
CD = Distance(C, D)
Detour1 = CD
Detour2 = AB
difference = Detour1-Detour2
if(difference<0):
    difference *= -1
    print "Driver 1's detour is shorter. By "+str(difference)+" miles"
elif(difference>0):
    print "Driver 2's detour is shorter. By "+str(difference)+" miles"
else:
    print "Both the detours are of the same distance."
    
    


    
    
        
    
