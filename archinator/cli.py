'''
Parse the command line arguments for the archinator
'''
# Import python libs
import argparse

def parse():
    '''
    parse the command line arguments
    '''
    parser = argparse.ArgumentParser('Archinator')

    parser.add_argument(
            '--image',
            '-i',
            default='arch.img',
            type=str,
            dest='image',
            help='The location of the image to create')

    parser.add_argument(
            '--size',
            '-s',
            default='8192',
            type=str,
            dest='size',
            help=('The size of the image to create in megabytes, defaults '
                  'to 8192'))

    parser.add_argument(
            '--format',
            '-f',
            default='qcow2',
            type=str,
            dest='format',
            help='The format of the image to create, defaults to qcow2')

    parser.add_argument(
            '--packages',
            '--pkg',
            default=['base'],
            nargs='*',
            dest='pkgs',
            help=('The names of the packages to be installed, defaults to '
                  '"base"'))

    parser.add_argument(
            '--profile',
            '-p',
            default='profile',
            type=str,
            dest='profile')

    parser.add_argument(
            '--profile-file',
            '-P',
            default='~/.archinator/profiles',
            )

    return parser.parse_args().__dict__
