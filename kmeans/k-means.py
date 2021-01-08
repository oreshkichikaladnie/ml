import numpy as np
from sklearn.cluster import KMeans
import random
from studio import stddraw

# Рисовалка
stddraw.setXscale(0,100)
stddraw.setYscale(0,100)


def dataset():
    rp = []
    ts = []
    tu = []
    for i in range(7000):
        x = random.randint(0,100)
        y = random.randint(0,100)
        rp.append([x,y])
        if 20**2 <= (x-50)**2+(y-50)**2 <= 30**2 or (x-50)**2+(y-50)**2 <= 5**2:
            ts.append([x,y])
    xx1,yy1,rr1,xx2,yy2,rr2=random.randint(1,90),random.randint(1,90),random.randint(5,50),random.randint(1,90),random.randint(1,90),random.randint(5,50)
    for i in range(5000):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        if (x-xx1)**2+(y-yy1)**2 <= rr1**2 or (x-xx2)**2+(y-yy2)**2<=rr2**2:
            tu.append([x,y])
    rp = np.array(rp)
    ts = np.array(ts)
    tu = np.array(tu)
    return rp, ts, tu


def paint(labels,arr):
    for i in range(len(labels)):
        if labels[i]==0:
            stddraw.setPenColor(stddraw.PINK)
        if labels[i]==1:
            stddraw.setPenColor(stddraw.ORANGE)
        stddraw.point(arr[i][0], arr[i][1])


rp, ts, tu = dataset()
data=rp
kmeans = KMeans(n_clusters=2,random_state=0).fit(data)

paint(kmeans.labels_, data)
for i in range(len(kmeans.cluster_centers_)):
    stddraw.setPenColor(stddraw.RED)
    stddraw.point(kmeans.cluster_centers_[i][0],kmeans.cluster_centers_[i][1])
stddraw.show()
