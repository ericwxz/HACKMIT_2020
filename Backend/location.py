import data
import pandas as pd
import numpy as np
import pickle

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

    def propagate_points(self, name):
        #do smth
        node = self.search(name)
        if not node:
            print("Location not seen before")
            return
        current = node
        while current:
            current.points += 1
            current = current.prev
    
    def search(self, name, print_mode=0, save_mode=0):
        if not self:
            print("Invalid node")
            return None
        if save_mode == 1:
            return_list = []
        q = []
        q.append(self)
        while len(q) > 0:
            current = q.pop(0)
            if save_mode == 1:
                return_list.append(current)
            if print_mode == 1:
                print(str(current))
            for c in current.children:
                q.append(c)
            if current.name == name:
                return current
        if save_mode == 1:
            return return_list
        return None

    def print_tree(self):
        return self.search(None, print_mode=1)

    def save(self, filepath):
        """
            File format: name, 
        """
        all_nodes = self.search(None, save_mode=1)
        all_nodes = pd.DataFrame(all_nodes)
        filepath = filepath +'locations.pkl'
        all_nodes.to_pickle(filepath)

    def load(self, filepath):
        filepath = filepath +'locations.pkl'
        all_nodes = pd.read_pickle(filepath)
        head = all_nodes.iloc[0][0]
        #head.search(None, print_mode=1)
        return head

    def __eq__(self, other):
        return self.name == other.name
    def __str__(self):
        if not self.prev:
            return "Name: {}, level: {}, points: {}, prev: None".format(self.name, self.level, self.points)
        return "Name: {}, level: {}, points: {}, prev: {}".format(self.name, self.level, self.points, self.prev.name)

if __name__ == "__main__":
    """Receives fields from JSON doc and updates fields"""
    # head = Location()
    # #print(str(head))
    # head.add_entry("California", "Los Angeles", "Beverly Hills", "90035")
    # head.add_entry("California", "Los Angeles", "Hollywood", "90038")
    # head.add_entry("New York", "Queens", "Brooklyn Manor", "11421")
    # #print(str(head.children[0].children[0]))

    # #fulfilled request in 90035, 90038
    # head.propagate_points("90035")
    # head.propagate_points("90038")
    
    

    # head.print_tree