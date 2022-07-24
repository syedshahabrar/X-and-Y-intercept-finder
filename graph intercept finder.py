def getXandYintercepts(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    if y1 == y2:
        print ('y intercept is ', y1)
        print ('x intercept does not exist')
    elif x1 == x2:
        print ('y intercept does not exist')
        print ('x intercept is ', x1)
    else:   
        slope = (y2-y1) / (x2-x1)
        c = y1 - slope * x1
        x_intercept = - c / slope
        y_intercept = c
        print ('y intercept is ', y_intercept)
        print ('x intercept is ', x_intercept)

p1 = (5, 2)
p2 = (7, 2)
getXandYintercepts(p1, p2)