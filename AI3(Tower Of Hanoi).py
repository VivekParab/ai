def TowerOfHanoi(n, from_rod, to_rod, aux_rod): 
    if n == 0: 
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod) 
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 
    print(from_rod, to_rod, aux_rod)
    
  
# Driver code 
N = 3
arr=['A','B','C']
# A, C, B are the name of rods 
TowerOfHanoi(N, arr[0], arr[1], arr[2])
print (arr)