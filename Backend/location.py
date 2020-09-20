class Location():
    
    def __init__(self, name='US', children=None, level=0, prev=None):
        """Initialises the name of the location, the possible list
        of children and the level. Level can be 0:country, 1:state,
        2:City, 3:County, 4:Zipcode
        """
        self.name = name
        self.children = []
        self.level = level
        self.points = 0
        self.prev = prev
    
    def add_entry(self, *args):
        current = self
        level = 1
        prev = self
        for region_boundary in args:
            if region_boundary not in [child.name for child in current.children]:
                #create instance of state
                new_region = Location(name=region_boundary, level=level, prev=prev)
                current.children.append(new_region)
            else:
                for child in current.children:
                    if child.name == region_boundary:
                        #need this object to dive in further
                        new_region = child
        
            #Have the state, now do the city
            current = new_region
            level +=1
            prev = new_region            

    def propagate_points(self):
        #do smth
        pass
    
    def search(self, name, print_mode=0):
        if not self:
            print("Invalid node")
            return None
        q = []
        q.append(self)
        while len(q) > 0:
            current = q.pop(0)
            if print_mode == 1:
                print(str(current))
            for c in current.children:
                q.append(c)
            if current.name == name:
                return current
        return None

    def print_tree(self):
        return self.search(None, print_mode=1)


    def __eq__(self, other):
        return self.name == other.name
    def __str__(self):
        return "Name: {}, level: {}, points: {}".format(self.name, self.level, self.points)

if __name__ == "__main__":
    """Receives fields from JSON doc and updates fields"""
    head = Location()
    #print(str(head))
    head.add_entry("California", "Los Angeles", "Beverly Hills", "90035")
    head.add_entry("California", "Los Angeles", "Hollywood", "90038")
    head.add_entry("New York", "Queens", "Brooklyn Manor", "11421")
    #print(str(head.children[0].children[0]))
    head.print_tree()