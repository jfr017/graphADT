from contact_tracing import *

ct = ContactTracer("data/data1.csv")
print("All Data:")
print(ct)


bord = "-"*10+'\n'

print(bord,"Potential Zombies:\n")
zombies = ct.get_potential_zombies()
for zom in zombies:
  print(zom)

print(bord,"Patient Zeros:\n")
p_zeros = ct.get_patient_zeros()
for patient in p_zeros:
  print(patient)




print(bord,"Closest Patient-Zero - Zombie Connections:\n")
for zom in zombies:
  closest_patient = None 
  closest_dist = float('inf')
  for pat in p_zeros:
    ct.dijkstra_shortest_path(pat)
    if zom.distance < closest_dist:
      closest_dist = zom.distance
      closest_patient = pat

  if closest_patient != None:
    ct.print_shortest_path(closest_patient,zom)

