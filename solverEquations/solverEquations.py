""""

CONSTRAINTS: 
1. If the function is not written correctly, like writing X instead of x, will end the program
2. Giving intervals where no sign changes will throw an exception
3. Giving incorrect data  types will end the program
4. If there is a mistake while typing values, the user must end giving inputs until the option (4) to exit is given
"""

#LIBRARIES
import numpy as np
from sympy import*
from sympy.abc import x
from sympy import lambdify

##########  BISECTION FUNCTION  ##########
def my_bisection (f,a,b,tol):
    
    '''Approximate solution of f(x)=0 by bisection method.
    
    Parameters
    ----------
    f : function
        Function for which we are searching for a solution f(x)=0.
    a : number
        left value of the interval.
    b : number
        right value of the interval.
    tol : number
        tolerance.

    '''

    if np.sign (f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")

    m = (a+b)/2   
        
    if np.abs(f(m))<tol: 
            return m
    elif np.sign(f(a)) == np.sign(f(m)):  
            return my_bisection(f,m,b,tol)
    elif np.sign(f(b)) == np.sign(f(m)):  
            return my_bisection(f,a,m,tol)


##########  NEWTON FUNCTION  ##########
def newton(f,Df,x0,epsilon,max_iter):
    
    '''Approximate solution of f(x)=0 by Newton's method.
    
    Parameters
    ----------
    f : function
        Function for which we are searching for a solution f(x)=0.
    Df : function
        Derivative of f(x).
    x0 : number
        Initial guess for a solution f(x)=0.
    epsilon : number
        Stopping criteria is abs(f(x)) < epsilon.
    max_iter : integer
        Maximum number of iterations of Newton's method.

    '''
    
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None


##########  MODIFIED NEWTON FUNCTION  ##########

def newton_Mod(f,Df,Df2,x0,epsilon,max_iter):
    '''Approximate solution of f(x)=0 by Newton's method.

    Parameters
    ----------
    f : function
        Function for which we are searching for a solution f(x)=0.
    Df : function
        Derivative of f(x).
    Df2: function
        Second derivative of f(x)
    x0 : number
        Initial guess for a solution f(x)=0.
    epsilon : number
        Stopping criteria is abs(f(x)) < epsilon.
    max_iter : integer
        Maximum number of iterations of Newton's method.
    '''
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        Df2xn = Df2(xn)
        den = Dfxn**2 - fxn*Df2xn
        if den == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - (fxn*Dfxn/den)
    print('Exceeded maximum iterations. No solution found.')
    return None
        
############# MENU ############
ans=True
while ans:
    print("This program solves equations of the form f(x)=0, with bisection, newton and modified newton methods. If you write uppercase X, the program will show an error, so please use lowercase x and  please input the number of what you want to do next:")
    print("""
    1. Bisection Method
    2. Newton Method 
    3. Modified Newton Method 
    4.Exit/Quit
    """)
    
    ans = input("what method would you like to use?: ")

    #OPTION 1: BISECTION 
    if ans=="1":
      print(""" \n You chose the Bisection Method, you will need to enter some parameters: function, 
            tolerance and interval. If there is not a solution, the program will throw and exception and end.""")
     

      function = input("Please type the function in terms of x: ")
      f = lambdify(x,function)    
      a= float (input("The left value of the interval: ")) 
      b= float (input("The right value of the interval: "))  
      tol= float (input("The value of tolerance: "))   

      root = my_bisection(f,a,b,tol)
      print("Estimated root of the equation is = ", root)

     # OPTION 2: NEWTON  
    elif ans=="2":
      print("""\n You chose the Newton Method, If there is not a solution, the program will throw and exception and end.
              You will need to enter some parameters:function, 
              the derivative of the function, initial guess (x0), stopping criteria (epsilon)
              and the maximum number of iterations.
              """)

      x =symbols ('x')
      function = input("Please type the function in terms of x: ") 
      f = lambdify(x,function)  

      function = input("Please type the derivative of the function in terms of x: ")
      Df = lambdify(x,function)  
    
      x0 = float(input("Please type the value for x0: "))
      epsilon = float(input("Please type the epsilon value:"))
      max_iter = int(input("Please type the maximum iterations:"))

      estimate = newton(f, Df,x0, epsilon,max_iter)
      print("Estimated root of the equation is =", estimate)
    

     #OPTION 3: NEWTON-MOD 
    elif ans=="3":
      print("""\n You chose the Newton Method, If there is not a solution, the program will throw and exception and end. 
              You will need to enter some parameters:function, 
              the derivative of the function, the second derivative of the function,initial guess (x0), 
              stopping criteria (epsilon) and the maximum number of iterations:""")

      function = input("Please type the function in terms of x:")
      f = lambdify(x,function)  
      
      function = input("Please type the derivative of the function in terms of x: ")
      Df = lambdify(x,function)  

      function = input("Please type the second derivative of the function in terms of x:")
      Df2 = lambdify(x,function)  

      x0 = float(input("Please type the value for x0: "))
      epsilon = float(input("Please type the epsilon value:"))
      max_iter = int(input("Please type the maximum iterations:"))

      root = newton_Mod(f, Df, Df2, x0, epsilon, max_iter)
      print("Estimated root of the equation is =", root)

    #OPTION 4: EXIT
    elif ans=="4":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")