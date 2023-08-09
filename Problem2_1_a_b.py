def downToZeroByThree(value):
    for i in range(value):
        if value != 1:
            print (value)
            value = value - 3          
    return value
                
print ("Down To Zero By Three where value = 10")
downToZeroByThree(10)  

print ("Down To Zero By Three where value = 10")
downToZeroByThree(6)        