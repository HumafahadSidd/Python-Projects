def triParam():
    # print(int(input("Enter ist side of value:")))
    # print(int(input("Enter 2nd side of value:")))
    # print(int(input("Enter 3rd side of value:")))
    a :float=float(input("Enter the first side length: "))
    b :float=float(input("Enter the second side length: "))
    c :float=float(input("Enter the third side length: "))
    d :float=a+b+c
    print("The perimeter of the triangle is ",d)

if __name__ == '__main__':
 triParam()      
    