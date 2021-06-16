import csv

max_x = 0
max_y = 0
min_x = 0
min_y = 0
avg_x = 0
avg_y = 0
count = 0
for i in range(1, 210):
    with open("data/data{}.csv".format(i)) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader, None)
        for row in reader:
            max_x = max(max_x, float(row[0]), float(row[1]))
            max_y = max(max_y, float(row[2]), float(row[3]))
            min_x = min(min_x, float(row[0]), float(row[1]))
            min_y = min(min_y, float(row[2]), float(row[3]))
            avg_x += float(row[0]) + float(row[1])
            avg_y += float(row[2]) + float(row[3])
            count += 1
print("max_x: {}".format(max_x))
print("max_y: {}".format(max_y))
print("min_x: {}".format(min_x))
print("min_y: {}".format(min_y))
print("avg_x: {}".format(avg_x/count))
print("avg_y: {}".format(avg_x/count))
