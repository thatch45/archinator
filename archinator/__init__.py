'''
Create archinator execution objects
'''

# import archinator libs
import archinator.cli

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
        print(self.opts)
        location = archinator.qemu.make_image(
                self.opts['image'],
                self.opts['size'],
                self.opts['format'])
        nbd = archinator.qemu.connect(location)
        archinator.parted.mklabel(nbd, 'msdos')
        archinator.parted.mkpart(nbd, 'primary', 'ext4', 1, -1)
        archinator.parted.probe(nbd)
        archinator.parted.mkfs('{0}p1'.format(nbd), 'ext4')
        mnt = archinator.qemu.mount(nbd)
