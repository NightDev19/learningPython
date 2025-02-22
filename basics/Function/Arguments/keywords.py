'''
Extension of Arguments
'''

#Keyword
def printFamily(firstNames,lastName):
    print(f"{firstNames} {lastName}")
    
printFamily("John","Doe")

# arbitrary with keyword
def printFamily(*firstNames,lastName):
    for name in firstNames:
        print(f"{name} {lastName}")
        
printFamily("John","Jane","Jenny",lastName="Doe")