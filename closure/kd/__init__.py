#from datetime.datetime import utcnow

max_points = 10
rmax = 1000
points_num = 10000
test_num = 50

def QueryPerformanceFrequency(x):
    return 1

def distance(s, t):
    ''' for all i and j, d[i,j] will hold the Levenshtein distance between
    // the first i characters of s and the first j characters of t;
    // note that d has (m+1)x(n+1) values
    '''
    d = []
    m = len(s)
    n = len(t)
    
    for i in range(m + 1):
        d.append([0 for c in range(n + 1)])
        # d[i, 0] := i // the distance of any first string to an empty second string
        d[i][0] = i
    for j in range(n + 1):
        # d[0, j] := j // the distance of any second string to an empty first string
        d[0][j] = j
        
    for j in range(n + 1):        
        d[0][j] = j
        for j in range(n): # range(1, n + 1):       
            for i in range(m): # range(1, m + 1):
                if s[i] == t[j]:  
                    d[i + 1][j + 1] = d[i][j]       # no operation required
                else:
                    d[i + 1][j + 1] = min(
                        d[1][j + 1] + 1,  # a deletion
                        d[i + 1][j] + 1,  # an insertion
                        d[i][j] + 1 # a substitution
                        )
    return d[m][n]
