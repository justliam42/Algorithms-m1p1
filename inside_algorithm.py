def inside(points, target_x, target_y):
    collisions = 0
    n = len(points)
    for i in range(n):
        # for each set of points(line), see if it colides with a
        # horizontal line pointing right from the point.
        # IE. is it within the two Ys and is it less than the x value
        # at that y? If so add a collision
        (xi1, yi1) = points[i]
        (xi2, yi2) = points[(i + 1) % n]
        # make one of the sides continuous so that
        # one collision occurs on the edge case of hitting a vertex
        if ((target_y >= yi1 and target_y < yi2) or 
            (target_y >= yi2 and target_y < yi1)):
            dx = xi2 - xi1
            dy = yi2 - yi1
            x = xi1 + (target_y - yi1) * (dx / dy)

            if x > target_x:
                collisions += 1

    # iff the horizontal line from the point collides with an odd number
    # of lines on the shape, than we are in the shape
    return collisions % 2 == 1

