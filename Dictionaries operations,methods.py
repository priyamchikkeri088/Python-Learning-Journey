# dictionary

birthday={
    "priya":"19-09-2005",
    "prajju":"08-09-2003",
    "virat":"05-10-1998"
}
print(birthday.get("prajju","not found")) # accessing  elements
print("adding sudeep to  the list") # adding sudeep in run time 
print("updating...") # updating priya date of birth
birthday["priya"]="19-12-2005"
birthday["sudeep"]="02-09-1973"
print(birthday)

meanings ={
      "bat":"used to hit ",
      "ball":"this is hit",
      "wicket":"to be protected"
      }
print(meanings)
print(meanings.keys()) #methods (returns keys )
print(meanings.values()) #returns values in dictionary
meanings.pop("bat") # deleting bat from dictionary
print(meanings)

d={
    "str":"str",
    "str":123,
    "frds":["pri","raksh","ramyyy"]
}
print(d)