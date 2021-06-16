import csv
import numpy as np

output_data = True
para = 0

def write_pt(pt):
    x = int((pt[0] + 3) * 1000)
    y = int((pt[1] + 2) * 1000)
    return """<circle cx="{}" cy = "{}" fill="black" r="20"/>""".format(x, y)

for theta in np.arange(0.03, 2*np.pi, 0.03):
    print("here")
    para += 1
    phi = 2 * np.pi * (np.sin(theta * 0.142))
    def transformation1(x):
        return np.array([[np.cos(theta), -np.sin(theta)],
                         [np.sin(theta), np.cos(theta)]]).dot(x) / np.sqrt(2)

    def transformation2(x):
        y = np.array([[np.cos(phi + theta), -np.sin(phi + theta)],
                         [np.sin(phi + theta), np.cos(phi + theta)]]).dot(x) / np.sqrt(2) + np.array([1, 0])
        return y

    def transformation3(x):
        y = np.array([[np.cos(2*phi + theta), -np.sin(2*phi + theta)],
                         [np.sin(2*phi + theta), np.cos(2*phi + theta)]]).dot(x) / np.sqrt(2) + np.array([0, 1])

        return y

    pts = [[0,0], [1,0]]
    pts = [np.transpose(pt) for pt in pts]

    for i in range(11):
        print(i)
        s1 = [transformation1(pt) for pt in pts]
        s2 = [transformation2(pt) for pt in pts]
        s3 = [transformation3(pt) for pt in pts]
        pts = s3 + s2 + s1

    if output_data:
        with open("data/data{}.csv".format(para), 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["x","y"])
            for pt in pts:
                writer.writerow(pt)
    else:
        svg = [write_pt(pt) for pt in pts]
        with open("ptclouds/curve{}.svg".format(para), 'w') as f:
            f.write("""
        <svg width="{x}" height="{x}" version="1.1" xmlns="http://www.w3.org/2000/svg">
            {}
        </svg>
        """.format("\n    ".join(svg), x = 6000))
