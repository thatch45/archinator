'''
Qemu Command Wrapper
====================

The qemu system comes with powerful tools, such as qemu-img and qemu-nbd which
are used here to build up images.
'''


# import python libs
import os
import subprocess
import glob
import tempfile
import time

# Import third party tools
import yaml

# Import archinator libs
import archinator.mount

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


def connect(image):
    '''
    Activate nbd for an image file.
    '''
    if not os.path.isfile(image):
        return ''
    subprocess.call('modprobe nbd max_part=63', shell=True)
    for nbd in glob.glob('/dev/nbd?'):
        if subprocess.call('fdisk -l {0}'.format(nbd)):
            while True:
                # Sometimes nbd does not "take hold", loop until we can verify
                subprocess.call(
                        'qemu-nbd -c {0} {1}'.format(nbd, image)
                        )
                if not subprocess.call('fdisk -l {0}'.format(nbd)):
                    break
            return nbd
    return ''


def mount(nbd):
    '''
    Pass in the nbd connection device location, mount all partitions and return
    a dict of mount points

    CLI Example::

        salt '*' qemu_nbd.mount /dev/nbd0
    '''
    ret = {}
    for part in glob.glob('{0}p*'.format(nbd)):
        root = os.path.join(
                tempfile.gettempdir(),
                'nbd',
                os.path.basename(nbd))
        m_pt = os.path.join(root, os.path.basename(part))
        time.sleep(1)
        mnt = archinator.mount.mount(m_pt, part, True)
        if mnt is not True:
            continue
        ret[m_pt] = part
    return ret


def init(image):
    '''
    Mount the named image via qemu-nbd and return the mounted roots

    CLI Example::

        salt '*' qemu_nbd.init /srv/image.qcow2
    '''
    nbd = connect(image)
    if not nbd:
        return ''
    return mount(nbd)


def clear(mnt):
    '''
    Pass in the mnt dict returned from nbd_mount to unmount and disconnect
    the image from nbd. If all of the partitions are unmounted return an
    empty dict, otherwise return a dict containing the still mounted
    partitions

    CLI Example::

        salt '*' qemu_nbd.clear '{/mnt/foo: /dev/nbd0p1}'
    '''
    if isinstance(mnt, str):
        mnt = yaml.load(mnt)
    ret = {}
    nbds = set()
    for m_pt, dev in mnt.items():
        mnt_ret = archinator.mount.umount(m_pt)
        if mnt_ret is not True:
            ret[m_pt] = dev
        nbds.add(dev[:dev.rindex('p')])
    if ret:
        return ret
    for nbd in nbds:
        subprocess.call('qemu-nbd -d {0}'.format(nbd))
    return ret
