'''
Create archinator execution objects
'''
# Import python libs
import sys

# import archinator libs
import archinator.cli
import archinator.qemu
import archinator.parted

class Archinator:
    '''
    Run the routines to generate Arch!!
    '''
    def __init__(self):
        self.opts = archinator.cli.parse()

    def run(self):
        '''
        Run the archinator!
        '''
        # make vm image
        # partition
        # Format
        # Install
        # basic configs
        # grub (or probably syslinux)
        location = archinator.qemu.make_image(
                self.opts['image'],
                self.opts['size'],
                self.opts['format'])
        if not location:
            print('Failed to create image {0}'.format(self.opts['image']))
            sys.exit(10)
        nbd = archinator.qemu.connect(location)
        if not nbd:
            print('Failed to mount image {0}'.format(location))
            sys.exit(10)
        archinator.parted.mklabel(nbd, 'msdos')
        archinator.parted.mkpart(nbd, 'primary', 'ext4', 1, -1)
        archinator.parted.probe(nbd)
        archinator.parted.mkfs('{0}p1'.format(nbd), 'ext4')
        mnt = archinator.qemu.mount(nbd)
