import sys
import x
for arg in sys.argv[1:]:
    print '==== %s' % arg
    for w in x.suggestions(arg):
        print w
