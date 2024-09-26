def tower_of_hanoi(n,source,target, auxilary):
    if n == 1:
        print(f" move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1,source,auxilary,target)
    print(f" move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1,auxilary,target,source)

num_disk = 3
tower_of_hanoi(num_disk,'A','B','C')    
               



           
    







            


 






    
 









