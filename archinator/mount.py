'''
Manage mounting devices
'''

# Import python libs
import os
import subprocess


def mount(name, device, mkmnt=False, fstype='', opts='defaults'):
    '''
    Mount a device
    '''
    if isinstance(opts, str):
        opts = opts.split(',')
    if not os.path.exists(name) and mkmnt:
        os.makedirs(name)
    lopts = ','.join(opts)
    args = '-o {0}'.format(lopts)
    if fstype:
        args += ' -t {0}'.format(fstype)
    cmd = 'mount {0} {1} {2} '.format(args, device, name)
    subprocess.call(cmd)
    return True


def umount(name):
    '''
    Attempt to unmount a device by specifying the directory it is mounted on
    '''
    cmd = 'umount {0}'.format(name)
    subprocess.call(cmd)
    return True

