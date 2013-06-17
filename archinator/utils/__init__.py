'''
Some basic utils to use and re-use
'''
# Import python libs
import subprocess


def chroot_cmd(root, cmd):
    '''
    Safely execute under a chroot
    '''
    c_cmd = 'chroot {0} /bin/sh -c \'{1}\''.format(root, cmd)
    return subprocess.call(c_cmd, shell=True)
