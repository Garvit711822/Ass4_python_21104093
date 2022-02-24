def TowerOfHanoi(disks,source,destination,path):
    if disks==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(int(disks)-1,source,path,destination)
    print("Move disk",disks,"from source",source,"to destination",destination)
    TowerOfHanoi(int(disks)-1,path,destination,source)

#given 3 disks
disks=3
#Let A,B and C are the three rods
TowerOfHanoi(disks,'A','B','C')