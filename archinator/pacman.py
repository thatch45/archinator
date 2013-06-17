'''
Bootstarp archlinux
'''

# Import python libs
import os
import subprocess

def prep_root(root):
    '''
    Ensure that the to install in has the needed directories
    '''
    basedirs = [
            os.path.join(root, 'var/cache/pacman/pkg'),
            os.path.join(root, 'var/lib/pacman'),
            os.path.join(root, 'var/log'),
            os.path.join(root, 'dev'),
            os.path.join(root, 'run'),
            os.path.join(root, 'etc'),
            ]
    for dir_ in basedirs:
        os.makedirs(dir_)
    tmp = os.path.join(root, 'tmp')
    os.makedirs(tmp)
    os.chmod(tmp, 1777)
    kdirs = [
            os.path.join(root, 'sys'),
            os.path.join(root, 'proc'),
            ]
    for dir_ in kdirs:
        os.makedirs(dir_)
        os.chmod(dir_, 0555)


def run_pacman(root, pkgs):
    '''
    Execute pacman on the prepared root
    '''
    cmd = ('pacman -Sy -r {0} '.format(root))
    for pkg in pkgs:
        cmd += '{0} '.format(pkg)
    subprocess.call(cmd, shell=True)
