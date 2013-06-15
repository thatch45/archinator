'''
Routines to call qemu for vm image work
'''

# import python libs
import os
import subprocess

def make_image(location, size, fmt):
    '''
    Create the base vm image
    '''
    full = os.path.abspath(location)
    if not os.path.isdir(os.path.basename(full)):
        return ''
    cmd = 'qemu-img create -f {0} {1} {2}M'.format(
            fmt,
            location,
            size)
    try:
        subprocess.check_call(cmd, shell=True)
    except subprocess.CalledProcessError:
        return ''
    return location
