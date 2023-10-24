#main file
#TODO: work base stats in

#w
def stat_check(attacker, defender):
    print(attacker)
    print(defender)


Bolt_Rifle = {
    "BS" : 3,
    "A" : 2,
    "S" : 4,
    "AP" : -1,
    "D" : 1
}
Close_Combat_Weapon = {
    "WS" : 3,
    "A" : 1,
    "S" : 4,
    "AP" : 0,
    "D" : 1
}
marine = {
    "Pts" : 20,
    "T" : 4,
    "AS" : 3,
    "W" : 2,
    "Weapons" : [Bolt_Rifle, Close_Combat_Weapon] 
}

Choppa = {
  "WS":3,
  "A":3,
  "S":5,
  "AP":-1,
  "D":2
}
Slugga = {
  "BS":5,
  "A":1,
  "S":4,
  "AP":0,
  "D":1
}  
Ork_Nob = {
  "Pts : 14,
  "T" : 5,
  "AS" : 5,
  "W" : 2,
  "Weapons" : [Choppa, Slugga]
}


stat_check(marine, Ork_Nob)
