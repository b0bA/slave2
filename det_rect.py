# determine all rectangles for a given set of points
from matplotlib import pyplot as plt
from matplotlib import patches

points = [(2.0, 1.0), (2.0, 3.0), (3.0, 1.0), (4.0, -1.0), (4.0, 4.0), (5.0, 2.0), (6.0, 0.0), (6.0, 1.0), (6.0, 3.0)]

fig, ax = plt.subplots(1)
ax.plot([x[0] for x in points], [y[1] for y in points], 'ro')

results = []
count = 0

for p0 in points:
    x0, y0 = p0
    for p1 in points:
        if p0 == p1:
            continue

        # create line l2 through p0 which is orthogonal to vector p1 - p0
        x1, y1 = p1
        v1 = (x1 - x0, y1 - y0) # v1 is p1 - p0
        v2 = (-v1[1], v1[0])    # v2 is orthogonal vector to v1
        # l2 = p0 + t*v2

        for p2 in points:
            if p2 == p0 or p2 == p1:
                continue
            # check if p2 lies on line l2
            x2, y2 = p2
            if (x2 - x0) * v2[1] == (y2 - y0) * v2[0]:
                # p2 lies on l2

                # determine midpoint pm of possible rectangle
                pm = (x1 + (x2-x1) / 2, y1 + (y2-y1) / 2)

                # determine last point p3 of the rectangle by mirroring p0 at pm and check if it is element of points
                p3 = ((x0 + 2*(pm[0] - x0)), y0 + 2*(pm[1] - y0))
                x3, y3 = p3

                if p3 in points:
                    result = sorted([p0, p1, p2, p3])
                    if result in results:
                        continue
                    results.append(result)
                    print(result)
                    count += 1

    # narrow search list
    points.remove(p0)

print(count)
plt.axis([-1, 7, -2, 5])
plt.show()