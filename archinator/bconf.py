'''
Run some basic post configuration, grub, fstab, locale, passwd, mkinitcpio
'''

# Import python libs
import os

# Import archinator libs
import archinator.utils

def fstab(root, virtio=False):
    '''
    Set up the fstab
    '''
    fstab = os.path.join(root, 'etc/fstab')
    with open(fstab, 'w+') as fp_:
        line = ('/dev/{0}da1               /               ext4'
                'rw,relatime,data=ordered        0 1').format(
                        'v' if virtio else 's')
        fp_.write(line)

def set_locale(root, locale):
    '''
    set up the locale
    '''
    pass

def grub(mount, root):
    '''
    Install grub
    '''
    cmd = 'grub-mkconfig -o /boot/grub/grub.cfg'
    archinator.utils.chroot_cmd(cmd)
    cmd = 'grub-install {0}'.format(mount)
