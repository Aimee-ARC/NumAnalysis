""""

"""

import numpy as np
from sympy import *


ans=True
while ans: #### Here we created a menu so that the user can exit the program whenever he wants or enter as many problems as he wants
    print("""
    This program solves systems of linear equations of the form Ax=b, where A is a square matrix and b is a vector with constant values    
    
    1.Input a system of linear equations for a square matrix
    2.Exit/quit
    """)
    
    ans = input(" Please input the number of what you want to do next:")
    if ans=="1":
        
        print("""
              -------------------------------------------------------------------------------
              For solving Ax=b you will need to enter A, B and n, where
                  -> A stands for the matrix of coefficients A  of the form Ax=b
                  -> b stands for the vector of independent terms b of the form Ax=b
                  -> And n is the size of A, knowing that A is a square matrix of nxn size
              -------------------------------------------------------------------------------
              """)
              
        Size = int(input("Please enter the value of n: "))
        
        print("""
              ----------------------------------------------------------------------------------
              For entering the values of the matrix please follow the next instructions:
                  -> enter a value and then press the "enter" key then enter another value 
                     a list of numbers like this:
                      1
                      2
                      3
                  -> If you press enter without entering a value an error will show
                  -> Please enter first the values of the first row, from the value 0 to the value n 
                     (left to right), 
                     then enter the values of the second row of the matrix and so on
                  -> To enter the values of the vector b follow the same instructions just enter the 
                     first value (from top to bottom) and press the "enter" key then enter the following value
                  -> When you finish entering the values the program will automatically ask for the 
                     next set of values until you finis, then the program will show the solution 
                     (the one solution, infinite or no solution)
              -------------------------------------------------------------------------------------
              """)
              
        print ("Please enter the values of the Matrix A")
        MatrixA = [[float(input()) for c in range (Size)] for r in range(Size)] ## here we get the input by the user in the form of a list of the matrix A 
        
        print ("Please enter the values of the vector b")
        Matrixb = [float(input()) for r in range(Size)] ## here we get the input by the user in the form of a list of the vector b 
        
        Aumented = np.column_stack((MatrixA, Matrixb)) #here we create the aumented matrix.
        
        
        
        Constant = 1000  ##this constant is to multiply the matrix in order to solve the float problem. 
        
        ####now we multiple A, b and the aumented matrix to solve the float problem.
        
        DecimalA = np.array(MatrixA)
        NotDA = (DecimalA * Constant)
        
        DecimalB =np.array(Matrixb)
        NotDB =(DecimalB * Constant)
        
        MatrixAumented = np.array(Aumented) 
        NotDecimal = ( MatrixAumented * Constant)

        ### we obtain the determinant
        
        detA = (round (np.linalg.det(MatrixA) ) )
        print("This is the determinant of matrix A: ", detA)
        

        #### If the determinant is different from zero then the problem has a solution.
        #### If the determinant is cero then we can have infinite solutions ore none.
        if detA != 0:
        
            ### Now that we know that we have one solution we can use np.linalg.solve
            
            print ("This is the row-reduced matrix: ")
            M = Matrix(NotDecimal)
            M_rref = M.rref()  
            print (M_rref)
         
            print("This matrix has ONE solution that is the following, given in the same order that the variables were entered:")
            
            x = np.linalg.solve(NotDA,NotDB)
            print(x)
            
        else:
            
            print ("This is the row-reduced matrix: ")
            
            M = Matrix(NotDecimal)
            M_rref = M.rref()  
            print(M_rref)
        
            ### we covert the tuple element into an array. 
            RowRed =(M_rref[0])
            RowRedArr = np.array(RowRed)    
            
            ### we find the last element of the last row.
            LastElem = RowRedArr [Size-1:Size+1 ,Size:Size+1]
            
            ### if the last element is a cero then we know we have row of ceros and that means we have infinite solutions.
            if LastElem == 0:
                print("This matrix has infinite solutions")
            ### if it´s not cero we have an inconsistency and we have no solution.
            else:
                print("This matrix has no solutions")
        
    elif ans=="2":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")