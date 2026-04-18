slots = int(input("How many slots?: "))
single = int(input("How many singles?: "))
sixteen_stack = int(input("How many stacks of sixteens?: "))
sixteen = int(input("How many sixteens?: "))/16
normal_stack = int(input("How many stacks of normals?: "))
normal = int(input("How many normals?: "))/64
filled = single + sixteen_stack + sixteen + normal_stack + normal
print(1 + (filled)/slots*14)