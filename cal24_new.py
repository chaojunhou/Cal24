import math
import copy
import time
CardsNumber=4
ResultValue=24

matrix=[]
result=[]
bool=[]
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
    for i in range(0,CardsNumber):
        print 'the '+str(i)+'th number:'
        x=raw_input()
        matrix.append([int(x),1])
        result.append(x)
    start=time.clock()
    if(PointGame(CardsNumber)):
        print 'Success\n'
        print result[0]+'=24'
    else:
        print 'Fail.\n'
    print time.clock()-start
        
        
              
            
