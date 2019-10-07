import os
import csv


def parse_files(path):
    x_y, x = dict(), list()
    for rout, dirs, files in os.walk(path):
        for file in files:
            with open(rout + file) as f:
                f_lines = f.readlines()
                raw_data = [c.split() for c in f_lines]
                x_y[file] = [{'x': int(float(a)), 'y': b.replace('.', ',')} for a, b in raw_data]
                x.extend(sorted(set([i['x'] for i in x_y[file]])))
    return x, x_y


x, x_y = parse_files('recources/')
result_dict = {i: [None] * len(x_y) for i in x}
files = list()
for n, k in enumerate(x_y):
    files.append(k)
    for coords in x_y[k]:
        result_dict[coords['x']][n] = coords['y']

redult_set = [(k, ) + tuple(v) for k, v in result_dict.items()]

with open('result.csv', 'w') as fp:
    writer = csv.writer(fp, dialect='excel', lineterminator='\n')
    writer.writerow(['x'] + ['y_(%s)' % f for f in files])
    writer.writerows(sorted(redult_set, key=lambda s: s[0]))
