def downToZeroByThree(value):
    for i in range(value):
        if value != 1:
            print (value)
            if value >= 4 :
                print ("greater than or equal to 4")
            if value >=10:
                print ("greater than or equal to 10")
            value = value - 3          
    return value
                

downToZeroByThree(10)   