import csv

class ContactTracer():
  '''
  Use adjacency-list based Graph to trace contagion contacts.

  Attributes:
    contacts; dictonary; keys: Vertex object, value: list of Vertex objects that are the outgoing edges from key.
    edge_weights; dictionary; keys: tuple of Vertex objects (from_vertex, to_vertex); value: float, weight of the edge between those verticies
  '''
  def __init__(self, filename):
    
    self.contacts = {}
    self.edge_weights = {}
    self.read_file(filename)
    
    
  def read_file(self,filename):
    with open(filename, mode='r') as file:
      csvFile = csv.reader(file)
      # each line in the csv is formatted
      # name, contact1, contact2, ...
      for line in csvFile:
        # remainder of values is names of all contacts
        for contact_label in line[1:]:
          #contact = self.get_vertex(contact_label)
          self.add_edge(line[0],contact_label)

  def get_vertex(self, vertex_label):
    '''
      Return the Vertex object associated with a label. If the label has no vertex, create one.

    Attributes:
      self; Graph.
      vertex_label; string; uniquie ID/label of vertex.
    Return:
      Vertex object with the label.
    '''
    for vertex in self.contacts.keys():
      if vertex.label == vertex_label:
        return vertex
    new_vtx = Vertex(vertex_label)
    self.contacts[new_vtx] = []
    return new_vtx

  def get_edge_weight(self, from_vtx, to_vtx):
    '''
    Return the edge weight between two verticies
    Parameters:
      from_vtx; Vertex.
      to_vtx; Vertex.
    '''
    return self.edge_weights[(from_vtx,to_vtx)]
    
  def add_edge(self, from_vtx_label, to_vtx_label, weight=1):
    '''
    Add edge of given weight (default 1) between to verticies.
    Parameters:
      from_vtx_label; string.
      to_vtx_label; string.
    Return: None
    '''
    # get or create Vertex objects for each label
    fm_vtx = self.get_vertex(from_vtx_label) 
    to_vtx = self.get_vertex(to_vtx_label)

    # add to_vertex to from vertex's adjacency list
    self.contacts[fm_vtx].append(to_vtx)
    # set eight of that edge
    self.edge_weights[(fm_vtx, to_vtx)] = weight
    
  def __str__(self):
    '''
    Return string representing all verticies and their adjacent verticies.
    Paramseters: self.
    Return: string.
    '''
    """
    s = ''
    for key in self.contacts:
      #if len(self.contacts[key]) != 0:
      s += str(key) + ' had contact with '
      for vertex in self.contacts[key]:
        s += str(vertex.label) + ' '
      #if len(self.contacts[key]) != 0:
      s += "\n"
    #wanted to check what was in self.edge_weights
    """
    s = ''
    for key in self.edge_weights:
      v , v2 = key
      s+= str(v.label) + ' ' + str(v2.label) + '\n'
    
    # TODO
    return s

  def get_potential_zombies(self):
    '''
    Return a list of Vertex objects of all potential zombies, i.e., verticies with no outgoing edges.
    Paramteres: self.
    Return: listof Vertex objects.
    '''
    zombies = []
    '''
    TODO
    '''
    for key in self.contacts:
      if len(self.contacts[key]) == 0:
        zombies.append(key)
    return zombies
  
  def get_patient_zeros(self):
    '''
    Returns list of Vertex objects of the patient zeros, i.e., verticies with no incoming edges.
    
    Paramters: self.
    Return: list of Vertex objects.
    '''

    '''TODO'''
    #easier way to do this without traversing the graph
   
    #can improve
    #visted = []
    not_visted = list(self.contacts.keys())
    for key in self.edge_weights:
      #v2 is needed not v
      v , visit = key
      if visit in not_visted:
        not_visted.remove(visit)
    return not_visted
    """
    for key in self.contacts:
      if key not in visted:
        not_visted.append(key)
    return not_visted
    vertex_stack = []
    """
    
    
    

  def dijkstra_shortest_path(self, start_vertex):
    '''
      Runs Dijkstra's shortest path algorithm to find shortest path from start_vertex_label to all
      other connected verticies.
      Prints all shortest distances.
    Parameters:
      start_vertex_label: label of vertex in graph. if label does not exist, does nothing. 
    Return: None
    '''
    if start_vertex not in self.contacts:
      return
    # Set up
    # set all verticies initial distance to infinity
    # and initial pred_vertex to None
    for vertex in self.contacts:
      vertex.distance = float('inf')
      vertex.prev_vertex = None
    # create deep copy of all verticies to start them in unvisited list
    unvisited = list(self.contacts.keys())[:]
    '''TODO'''
  
  def print_shortest_path(self, start_vertex, end_vertex):
    '''
    Print shortest path and length of shortest path between twoVerticies.
    Parameters:
      start_vertex:Vertex.
      end_vertex:Vertes.
    Return:
    None
    '''
    self.dijkstra_shortest_path(start_vertex)
    path=""
    current_vertex = end_vertex
    # end vertex stores distance
    dist = current_vertex.distance

    while current_vertex != start_vertex:
      path = " -> " + str(current_vertex.label) + path
      current_vertex = current_vertex.prev_vertex
    path = start_vertex.label + path + ". Dist: "+ str(dist) +'\n'
    print(path)
    

class Vertex:
  def __init__(self, label):
    self.label = label
    self.distance = float('inf')
    self.prev_vertex = None

  def __str__(self):
    return self.label
