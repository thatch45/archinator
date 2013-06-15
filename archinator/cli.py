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

    args = parser.parse_args()
    print args
