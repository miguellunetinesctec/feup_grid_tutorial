import csv
import time

for i in range(120):
    with open('output/output.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([i, f"Data for iteration {i}"])
    time.sleep(1)