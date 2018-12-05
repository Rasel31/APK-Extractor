from androguard.misc import *
import csv

parrent_folder = "D:\\Progaurd Dataset\\TRIVIAL+STRING_ENCRYPTION+REFLECTION+CLASS_ENCRYPTION_APK"

count = 1

permission_list = []

permission_by_malware = []

pattern_with_one_zero_by_malware = []

FAMILY = []

for subdir, dirs, files in os.walk(parrent_folder):

    for file in files:

        # if count > 1120:

        print(count, 'No. APk', file)

        a, d, dx = AnalyzeAPK(subdir + '\\' + file)

        FAMILY.append(os.path.basename(subdir))

        temp_permission = []

        temp_permission_by_malware = []

        for i in a.get_permissions():

            temp_permission.extend(i.split('.'))
            temp_permission_by_malware.append(temp_permission[-1])

            if temp_permission[-1] not in permission_list:
                permission_list.append(temp_permission[-1])

        temp_permission.clear()
        permission_by_malware.extend([temp_permission_by_malware[:]])
        temp_permission_by_malware.clear()

        count += 1

for i in permission_by_malware:

    single_pattern = [i * 0 for i in range(len(permission_list))]

    for j in i:
        a = permission_list.index(j)
        single_pattern[a] = 1

    pattern_with_one_zero_by_malware.extend([single_pattern[:]])
    single_pattern.clear()

print(permission_list[:])
print(pattern_with_one_zero_by_malware[:])

with open('TRIVIAL+STRING_ENCRYPTION+REFLECTION+CLASS_ENC-permission-pattern.csv', mode='w') as csv_pattern:

    writer = csv.writer(csv_pattern)
    permission_list.insert(0, 'FAMILY')
    writer.writerow(permission_list)

    count = 0

    for i in FAMILY:
        pattern_with_one_zero_by_malware[count].insert(0, i)
        count += 1

    for i in pattern_with_one_zero_by_malware:

        writer.writerow(i)

print(len(permission_list))
print(len(pattern_with_one_zero_by_malware))

