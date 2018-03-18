import itertools

if __name__ == '__main__':
    
    k =  [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    new_k =[]

    print "The initial list is:"
    print k
    print
    print "Starting script..."
    print
    k.sort()
print "list without duplicates"     
print list(k for k,_ in itertools.groupby(k))
    
   
