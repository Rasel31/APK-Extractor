import csv
import pandas


permission = []

permission_list = []

pattern_by_malware = []

with open('permissions1.txt', 'r') as reader:

    for line in reader:

        if 'No. APK' in line:

            if len(permission) > 0:

                pattern_by_malware.extend([permission[:]])

                permission.clear()

        if 'android' in line or 'com' in line or 'org' in line:

            a = []

            a.extend(line.split('.'))

            if a[-1] not in permission:

                permission.append(a[-1])

            if a[-1] not in permission_list:

                permission_list.append(a[-1])

#   --------------------------------------------------------------------------------------------------------------------

pattern_with_one_zero = []


for i in pattern_by_malware:

    single_pattern = [i * 0 for i in range(134)]

    for j in i:

        a = permission_list.index(j)
        single_pattern[a] = 1

    pattern_with_one_zero.extend([single_pattern[:]])
    single_pattern.clear()

#   --------------------------------------------------------------------------------------------------------------------

with open('permission-pattern2.csv', mode='w') as csv_pattern:

    # fieldnames = permission_list
    #
    # writer = csv.DictWriter(csv_pattern, fieldnames=fieldnames)
    #
    # writer.writeheader()

    writer = csv.writer(csv_pattern)
    writer.writerow(permission_list)

    # pattern_dict = {}
    #
    # for i in pattern_by_malware:
    #
    #     for j in i:
    #         if j in permission_list:
    #             pattern_dict[j] = 1
    #
    #     writer.writerow(pattern_dict)
    #     pattern_dict.clear()

    for i in pattern_with_one_zero:
        writer.writerow(i)


# for i in pattern_with_one_zero:
#     print(i)

print(len(pattern_with_one_zero))

# df = pandas.read_csv('permission-pattern1.csv')
#
# print(df)

# print(len(pattern_by_malware), pattern_by_malware)
# print(len(permission_list), permission_list)

# for i in permission:
#     print(i)
#
# print('*' * 30)
#
# for i in p_by_malware:
#     print(i)
#
# print(permission_list[:])
#
# print(len(permission))
# print(len(p_by_malware))
# print(len(permission_list))


