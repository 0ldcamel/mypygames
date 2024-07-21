print('Hello')
try:
    import sys, random, math, os
    import getopt, pygame
    from socket import *
    from pygame.locals import *

except ImportError as err:
    print(f'could not load module. {err}')
    sys.exit(2)