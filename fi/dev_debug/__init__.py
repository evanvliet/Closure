import sys
from settings import in_the_cloud

def debug_break():
    """Enter debugger."""
    if in_the_cloud():
        return
    import pdb
    debugger = pdb.Pdb(stdin=sys.__stdin__, stdout=sys.__stdout__)
    debugger.set_trace(sys._getframe().f_back)
