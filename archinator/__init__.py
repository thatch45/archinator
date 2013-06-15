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
        print(self.opts)
