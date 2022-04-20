#DBScan file
###Parameters:
#Data Matrix
#Minpts
#e

###Returns:
#means
#clusters found
##Label points:
#Core
#Border
#Noise

#Get distance between 2 points
def distance(mean_point, distance_point):
    return math.sqrt(sum([(mean_point[index] - distance_point[index]) ** 2 for index in range(len(mean_point))]))

class Point(self):
    #Point is a tuple of point values
    def __init__(self, point):
        self.point = point
        self.label =  "noise"

    
