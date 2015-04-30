import math
import copy
import time
import itertools
CardsNumber=4
ResultValue=24


def PointGame(n):
    i=0
    if(n==1):
        if matrix[0][0]==matrix[0][1]*24:
            return True
        else:
            return False
    for i in range(0,n):
        for j in range(i+1,n):
            # use two dimention array
            a=matrix[i][0]
            b=matrix[i][1]
            c=matrix[j][0]
            d=matrix[j][1]
            # python needs the deepcopy to copy the value to the destination
            matrix[j]=copy.deepcopy(matrix[n-1])

            expa=result[i]
            expb=result[j]
            result[j]=result[n-1]
    
            result[i]='('+expa+'+'+expb+')'
            matrix[i][0]=a*d+b*c
            matrix[i][1]=b*d
            
            if(PointGame(n-1)):
                return True
            
            result[i]='('+expa+'-'+expb+')'
            matrix[i][0]=a*d-b*c
            matrix[i][1]=b*d
            if(PointGame(n-1)):
                return True

            result[i]='('+expb+'-'+expa+')'
            matrix[i][0]=b*c-a*d
            matrix[i][1]=b*d
            if(PointGame(n-1)):
                return True

            result[i]='('+expa+'*'+expb+')'
            matrix[i][0]=a*c
            matrix[i][1]=b*d
            if(PointGame(n-1)):
                return True

            if c!=0:
                result[i]='('+expa+'/'+expb+')'
                matrix[i][0]=a*d
                matrix[i][1]=b*c
                
                if(PointGame(n-1)):
                    return True

            if a!=0:
                result[i]='('+expb+'/'+expa+')'
                matrix[i][0]=b*c
                matrix[i][1]=a*d
                
                if(PointGame(n-1)):
                    return True
            # restore the value
            matrix[i][0]=a
            matrix[i][1]=b
            matrix[j][0]=c
            matrix[j][1]=d

            result[i]=expa
            result[j]=expb
            i+=1
    return False

if __name__=='__main__':
    matrix=[]
    result=[]
    tests = [[2,7,10,7], [2,3,5,12], [1,6,11,13], [9,11,12,12], [1,3,9,10],
             [1,1,5,5],[1, 6, 11, 13], [ 2,  2, 13, 13]]
    for test in tests:
        for x in itertools.permutations(test,4):
            matrix=[]
            result=[]
            for val in x:
                matrix.append([int(val),1])
                result.append(str(val))            
            if(PointGame(CardsNumber)):
                print 'The solution is -->', result[0]+'=24'
                break
        else:
            print 'Fail' 
        
              
            
