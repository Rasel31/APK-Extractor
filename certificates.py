# from androguard.misc import *
#
# parrent_folder = "D:\\Progaurd Dataset\\TRIVIAL_APK"
#
#
# for subdir, dirs, files in os.walk(parrent_folder):
#
#     for file in files:
#
#         a, d, dx = AnalyzeAPK(subdir + '\\' + file)
#
#         print(a.get_app_name())
#
#         for cert in a.get_certificates():
#
#             print(cert.sha256_fingerprint)
#             print(cert.sha1_fingerprint)

import os

parrent_folder = "D:\\Progaurd Dataset\\STRING_ENCRYPTION_APK"

FAMILY = []

for subdir, dirs, files in os.walk(parrent_folder):

    for file in files:
        print(os.path.basename(subdir))
        print('\t', file)
