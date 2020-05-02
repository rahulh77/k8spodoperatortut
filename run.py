"""
Entry point of script.
"""

import time
import sys
def main():
    """main function to invoke update_manifest."""
    timetosleep = int(sys.argv[1])
    print('started')
    print(f'sleeping for {timetosleep} seconds:')
    time.sleep(timetosleep)
    print('done')


if __name__ == '__main__':
    main()
