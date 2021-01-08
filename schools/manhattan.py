import random
import shapely
from geovoronoi import voronoi_regions_from_coords
import matplotlib.pyplot as plt
import geopandas as gpd

# карта
def karta():
    x, y = random.randint(1, 99), random.randint(1, 99)
    r = random.randint(0, 1)
    eps = random.randint(-99, 99)
    while 0 > x+eps or x+eps >= 100 or 0 > y+eps or y+eps >= 100:
        eps = random.randint(-99, 99)
    if r == 1:
        streetsarr = [(x, y), (x+eps, y)]
        x += eps
    if r == 0:
        streetsarr = [(x, y), (x, y+eps)]
        y += eps

    for _ in range(5000):
        r = random.randint(0, 1)
        eps = random.randint(-99, 99)
        while 0 > x + eps or x + eps > 100 or 0 > y + eps or y + eps > 100:
            eps = random.randint(-99, 99)
        if r == 1:
            streetsarr.append((x+eps, y))
            x += eps
        if r == 0:
            streetsarr.append((x, y+eps))
            y += eps
    stre = shapely.geometry.LineString(streetsarr)
    return(stre, streetsarr)


stre, streetsarr=karta()
p=gpd.GeoSeries(stre)
p.plot()

# создаем датасет из школ
schools = []
schoolx = []
schooly = []
for i in range(50):
    x = random.randint(0, 99)
    y = random.randint(0, 99)
    if [x, y] not in streetsarr and [x, y] not in schools:
        schools.append([x, y])
        schoolx.append(x)
        schooly.append(y)
plt.plot(schoolx, schooly, 'bs')

# разбивам плоскость на диаграму вороного
coords = schools
boundary_shape=shapely.geometry.box(0, 0, 100, 100, ccw=True)
poly_shapes, pts, poly_to_pt_assignments = voronoi_regions_from_coords(coords, boundary_shape)

#xt=int(input("Введите координату xlearn: "))
#yt=int(input("Введите координату ylearn: "))
xt = yt = 50

for i in range(len(poly_shapes)):
    if shapely.geometry.Point(xt, yt).within(poly_shapes[i]):
        x, y = poly_shapes[i].exterior.xy
        plt.plot(x,y,color="pink")
        plt.plot(xt, yt, "go")
        plt.plot(schools[poly_to_pt_assignments[i][0]][0],schools[poly_to_pt_assignments[i][0]][1],"ro")
plt.show()

