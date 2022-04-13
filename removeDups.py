
def removeDups(array):
    myUnique = set()
    for unique in array:
      myUnique.add(unique)
    listOfMyUnique = list(myUnique) 
    for n in range(len(array)):
      if len(listOfMyUnique) < len(array):
          listOfMyUnique.append('_')
      else:
          break
    return len(myUnique), listOfMyUnique
    
print(removeDups([1,1,2]))
