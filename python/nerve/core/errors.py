#! /usr/bin/env python

# ------------------------------------------------------------------------------
class SpecificationError(Exception):
    pass
# ------------------------------------------------------------------------------

def main():
    '''
    Run help if called directly
    '''

    import __main__
    help(__main__)
# ------------------------------------------------------------------------------

__all__ = ['SpecificationError']

if __name__ == '__main__':
    main()