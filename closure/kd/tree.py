'''
Created on Mar 6, 2012

@author: eric
'''

# from datetime.datetime import utcnow
import time
import kd

class Node(object):
    '''
    A kd-node.
    '''
    def __init__(self, x, axis):
        '''
        Constructor
    int axis ;
    Xtype x[SD];
    unsigned int id ;
    bool checked ;
    bool orientation ;

    KDNode(Xtype* x0, int axis0);

    KDNODE*    Insert(Xtype* x);
    KDNODE*    FindParent(Xtype* x0);

    KDNODE* Parent ;
    KDNODE* Left ;
    KDNODE* Right ;
        '''
        self.axis = axis
        self.x = x
        self.checked = False
        self.orientation = False
        self.id = 0
        self.left = None
        self.right = None
        self.parent = None
        
    def insert(self, x):
        parent = self.find_parent(x)
        if parent.x == x:
            return None
        new_axis = parent.axis + 1
        if new_axis >= len(x):
            new_axis = 0
        node = Node(x, new_axis)
        node.parent = parent
        if x[parent.axis] > self.x[parent.axis]:
            parent.right = node
            node.orientation = True
        else:
            parent.left = node
            node.orientation = False
        return node

    def find_parent(self, x):
        parent = None
        next = self
        split = 0
        while next:
            split = next.axis
            parent = next
            if x[split] == self.x[split]:
                next = next.right
            else:
                next = next.left
        return parent

class Tree(object):
    '''
    A kd-tree.
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.root = None
        self.start = time.time()
        self.finish = time.time()
        self.counter = 0
        self.min = 'a'
        self.nearest_neighbor = None
        self.id = 1
        self.list_buf = []
        self.list_n = 0
        self.checked_nodes = []
        self.n_checked_nodes = 0
        self.x_min = ''
        self.x_max = ''
        
        
        
    def add(self, x):
        if len(self.list_buf) > kd.max_points:
            return 0
        if self.root:
            pnode = self.root.insert(x)
            if not pnode:
                return 0
            pnode.id = self.id
            self.id += 1
        else:
            self.root = Node(x, 0)
            self.root.id = self.id
            self.id += 1
            self.list_buf.append(self.root)
        return 1
            
    def find_nearest(self, x):
        if not self.root:
            return None ;
    
        self.checked_nodes = 0;
    
        parent = self.root.find_parent(x)
        self.nearest_neighbour = parent
        self.min = kd.distance(x, parent.x)
    
        if x == parent.x:
            return self.nearest_neighbour
    
        self.search_parent(parent, x)
        self.uncheck()
        
        return self.nearest_neighbour
    
    def check_subtree(self, node, x):
        if not node or node.checked:
            return
        
        self.checked_nodes.append(node)
        node.checked = True
        self.set_bounding_cube(node, x)
        
        dim = node.axis
        d = node.x[dim] - x[dim]
        
        if d*d > self.min:
            if node.x[dim] > x[dim]:
                self.check_subtree(node.left, x)
            else:
                self.check_subtree(node.right, x)
        
        else:
            self.check_subtree(node.left, x)
            self.check_subtree(node.right, x)
        
    
    def set_bounding_cube(self, node, x):
        pass
    
    def search_parent(self, node, x):
        pass
    
    def uncheck(self):
        pass
    
    def time_frequency(self):
        return kd.QueryPerformanceFrequency(self.counter)
        pass
    
    def start_time(self):
        self.start = time.time()
    
    '''
        node*  Root ;
        KDTree();
    
        bool                add(Xtype* x);
        node*                find_nearest(Xtype* x0);
        node*                find_nearest_brute(Xtype* x) ;
    
        inline    void        check_subtree(node* node, Xtype* x);
        inline  void        set_bounding_cube(node* node, Xtype* x);
        inline node*        search_parent(node* parent, Xtype* x);
        void                uncheck();
    
        LARGE_INTEGER        TimeStart, TimeFinish; 
        LARGE_INTEGER        CounterFreq;  
    
        void GetTimerFrequency(){    
            QueryPerformanceFrequency(&CounterFreq);
        }
    
        void StartTimer(){
        QueryPerformanceCounter(&TimeStart);
  '''