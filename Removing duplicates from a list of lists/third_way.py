

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
print [k[i] for i in range(len(k)) if i == 0 or k[i] != k[i-1]]
    
   
