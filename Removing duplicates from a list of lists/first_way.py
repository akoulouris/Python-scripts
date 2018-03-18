

if __name__ == '__main__':
    
    k =  [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    new_k =[]

    print "The initial list is:"
    print k
    print
    print "Starting script..."
    print
    for elem in k:
        if elem not in new_k:
            new_k.append(elem)
            k = new_k
print "list without duplicates"     
print k
    
   
