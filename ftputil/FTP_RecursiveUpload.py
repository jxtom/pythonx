#!/usr/bin/python
# 递归上传目录至FTP

import os
from ftplib import FTP


def debug_print(s):
    print(s)


def upload_file(local_file, remote_file):
    fileh = open(local_file, 'rb')
    ftph.storbinary('STOR %s' % remote_file, fileh)
    fileh.close()
    debug_print('Delivered %s' % remote_file)


def upload_files(local_dir, remote_dir):
    if not os.path.isdir(local_dir):
        return

    localnames = os.listdir(local_dir)

    try:
        ftph.cwd(remote_dir)
    except:
        debug_print('Failed to switch directory %s' % remote_dir)

    for item in localnames:
        if item in execlude_files:
            continue

        src = os.path.join(local_dir, item)
        dest = os.path.join(remote_dir, item)

        if os.path.isdir(src):
            try:
                ftph.mkd(dest)
            except:
                debug_print('The directory already exists %s' % dest)

            upload_files(src, dest)
        else:
            upload_file(src, dest)


ftph = FTP('172.16.15.4', 'wpfex', 'update')

execlude_files = ['.DS_Store', '.vscode', '.svn']

upload_files('/data/temp/wpf更新/自动更新181/AutoUpdater/', '/wpfex166/AutoUpdater')
