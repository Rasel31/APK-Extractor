import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter


file_path = "D:\\Androguard\\androguard-master\\Trivial permission-pattern.csv"

# data = pd.read_csv(file_path)

with open(file_path, 'r') as csv_reader:
    reader = csv.reader(csv_reader)

    headers = next(reader)

print(len(headers))

permission = []
counter = []

for k in range(len(headers)):

    with open(file_path, 'r') as csv_reader:

        reader = csv.reader(csv_reader)
        headers = next(reader)

        count = 0
        count2 = 0

        for header in headers[k + 1:k + 2]:

            # print(k+1, header)

            for i in reader:

                if count % 2 == 0:
                    pass
                else:
                    # print(count1, 'no position', i[count1])
                    if i[k + 1] == '1':
                        count2 += 1

                count += 1

            # print(header, 'Found', count2, 'times')
            permission.append(header)
            counter.append(count2)
            count2 = 0

print(permission[::])
print(counter[::])

print(len(permission))
print(len(counter))

a = dict(zip(permission, counter))

print(a.items())
print(sorted(a.values(), reverse=True))

print(sorted(a.items(), key=itemgetter(1), reverse=True)[:50])

counter = sorted(a.values(), reverse=True)[:50]

index = np.arange(len(sorted(a.keys(), key=itemgetter(1), reverse=True)[:50]))
plt.bar(index, counter)
plt.xlabel('Permissions', fontsize=10)
plt.ylabel('No. of Counted Permission', fontsize=10)
plt.xticks(index[:50], permission[:50], fontsize=5, rotation=90)
plt.title('152 Permissions Counter')
# plt.figure(figsize=(50*3.13, 4*3.13))
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.savefig('pattern.svg', dpi=700, orientation='portrait', quality=95)
plt.show()

