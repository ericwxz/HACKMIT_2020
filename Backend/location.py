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
    
    def add_entry(self, state, city, county, zipcode):
        current = self
        level = 1
        prev = self
        for region_boundary in list(state, city, county, zipcode):
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
    
    def search(self, name):
        pass

    def print_tree(self):
        pass


    def __eq__(self, other):
        return self.name == other.name

if __name__ == "__main__":
    """Receives fields from JSON doc and updates fields"""
    head = Location()
    Location.add_entry(head, state, city, county, zipcode)

    #new login
    new = Location(name = "California", )