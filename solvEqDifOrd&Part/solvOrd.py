

#REQUIRED LIBRARIES
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from prettytable import PrettyTable


#EULER'S METHOD FUNCTION
def euler (t0, tn, n, y0):
    
    h = abs (tn - t0)/n
    t = linspace(0, tn, n+1)
    y = zeros (n + 1)
    y [0] = y0
    
    for k in range (0, n):
        y [k+1] = y[k] + h *f (t[k], y[k])
    return y


#RUNGE-KUTTA "CLASSIC" ORDER 4 METHOD FUNCTION
def RK4 (t0, tn, n, y0):
    
    h = abs (tn - t0)/n
    t = linspace(t0, tn, n+1)
    y = zeros (n+1)
    y[0] = y0
    
    for i in range (0, n):
        s1 = f (t[i], y[i])
        s2 = f(t[i]+h/2, y[i]+s1*h/2)
        s3 = f(t[i]+h/2, y[i]+s2*h/2)
        s4 = f(t[i]+h, y[i]+s3*h)
        y[i+1] = y[i] + h*(s1+2*s2+2*s3+s4)/6
    return y


# MENU
print("""
1.Example 1
2.Example 2
3.Example 3
4.Example 4
5.Example 5
6.Example 6
7.Example 7
8.Example 8
9.Example 9
10.Example 10
11.Exit/Quit
""")


ans=True
while ans:
    ans = input("What would you like to do? ")

    if ans=="1":
      ########################################################################### Problem 1

      print("-----------------------------------------")
      print("Problem 1:")
      print("-----------------------------------------")

      #f in the IVP y’ = f(t,y), y(t0)=y0
      def f(t,y):
        return (0.04)*y 
    
      fg = 1    
      t0 = 0     
      tn = 6    
      y0 = 5000  
      h = 1/12   

      n = int(abs(tn-t0)/h)

      t = linspace(t0,tn,n+1)
      print('size of t: ', len(t))
      
      ye = euler(t0,tn,n,y0)
      print('Using Euler:')
      print('ye[12]', ye[12], 'for ', t[12*1], 'years')
      print('ye[24]', ye[24], 'for ', t[12*2], 'years')
      print('ye[36]', ye[36], 'for ', t[12*3], 'years')
      print('ye[48]', ye[48], 'for ', t[12*4], 'years')
      print('ye[60]', ye[60], 'for ', t[12*5], 'years')
      print('ye[72]', ye[72], 'for ', t[12*6], 'years')
      
      yrk = RK4(t0,tn,n,y0)
      print('Using Runge-Kutta:')
      print('yrk[12]', yrk[12*1], 'for ', t[12*1], 'years')
      print('yrk[24]', yrk[12*2], 'for ', t[12*2], 'years')
      print('yrk[36]', yrk[12*3], 'for ', t[12*3], 'years')
      print('yrk[48]', yrk[12*4], 'for ', t[12*4], 'years')
      print('yrk[69]', yrk[12*5], 'for ', t[12*5], 'years')
      print('yrk[72]', yrk[12*6], 'for ', t[12*6], 'years')
      
      
      # Script to produce graphs (ONLY 1 GRAPH)

      fg = plt.figure()
      plt.plot(t,yrk,'r+',label='Runge-Kutta')
      plt.plot(t,ye,'b--',label='Euler')
      plt.grid()
      fg.suptitle('Problem 1:', fontsize=12)
      plt.legend()
      plt.show()

  
    elif ans=="2":
      ########################################################################### Problem 2

      print("-----------------------------------------")
      print("Problem 2:")
      print("-----------------------------------------")

      #f in the IVP y’ = f(t,y), y(t0)=y0
      
      def f(t,y):
        return (0.01)*y 

      fg = 2      
      t0 = 0      
      tn = 6  
      y0 = 5000
      h = 1/12

      n = int(abs(tn-t0)/h)

      t = linspace(t0,tn,n+1)
      
      print('size of t: ', len(t))
      
      ye1 = euler(t0,tn,n,y0)
      yrk1 = RK4(t0,tn,n,y0)
      
      def f(t,y):
          return (0.02)*y
      
      ye2 = euler(t0,tn,n,y0)
      yrk2 = RK4(t0,tn,n,y0)
      
      def f(t,y):
          return (0.03)*y
      
      ye3 = euler(t0,tn,n,y0)
      yrk3 = RK4(t0,tn,n,y0)
      
      def f(t,y):
          return (0.04)*y
      
      ye4 = euler(t0,tn,n,y0)
      yrk4 = RK4(t0,tn,n,y0)
      
      def f(t,y):
          return (0.05)*y
      
      ye5 = euler(t0,tn,n,y0)
      yrk5 = RK4(t0,tn,n,y0)
      
      def f(t,y):
          return (0.06)*y
      
      ye6 = euler(t0,tn,n,y0)
      yrk6 = RK4(t0,tn,n,y0)
      
      print('Using Euler:')
      print('ye1[12]', ye1[60], 'for ', t[12*1], 'years')
      print('ye2[24]', ye2[60], 'for ', t[12*2], 'years')
      print('ye3[36]', ye3[60], 'for ', t[12*3], 'years')
      print('ye4[48]', ye4[60], 'for ', t[12*4], 'years')
      print('ye5[60]', ye5[60], 'for ', t[12*5], 'years')
      print('ye6[72]', ye6[60], 'for ', t[12*6], 'years')
      
      print('Using Runge-Kutta:')
      print('yrk1[60]', yrk1[60], 'for ', t[12*1], 'years')
      print('yrk2[60]', yrk2[60], 'for ', t[12*2], 'years')
      print('yrk3[60]', yrk3[60], 'for ', t[12*3], 'years')
      print('yrk4[60]', yrk4[60], 'for ', t[12*4], 'years')
      print('yrk5[60]', yrk5[60], 'for ', t[12*5], 'years')
      print('yrk6[60]', yrk6[60], 'for ', t[12*6], 'years')
      
      # Script to produce graphs (1 GRAPH)

      fg = plt.figure()
      plt.plot(t,yrk1, color='#6A0E00',ls='dashed',label='Runge-Kutta 1%')
      plt.plot(t,yrk2, color='#600087',ls='dashed',label='Runge-Kutta 2%')
      plt.plot(t,yrk3, color='#001CE6',ls='dashed',label='Runge-Kutta 3%')
      plt.plot(t,yrk4, color='#FF24DE',ls='dashed',label='Runge-Kutta 4%')
      plt.plot(t,yrk5, color='#05CB32',ls='dashed',label='Runge-Kutta 5%')
      plt.plot(t,yrk6, color='#18FD53',ls='dashed',label='Runge-Kutta 6%')
      
      plt.plot(t,ye1,'b+',label='Euler 1%')
      plt.plot(t,ye2,'g+',label='Euler 2%')
      plt.plot(t,ye3,'r+',label='Euler 3%')
      plt.plot(t,ye4,'c+',label='Euler 4%')
      plt.plot(t,ye5,'m+',label='Euler 5%')
      plt.plot(t,ye6,'k+',label='Euler 6%')
      
      plt.grid()
      fg.suptitle('Problem 2', fontsize=12)
      plt.legend()
      plt.show()

    elif ans=="3":
    ########################################################################### Problem 3

      print("-----------------------------------------")
      print("Problem 3:")
      print("-----------------------------------------")


      #f in the IVP y’ = f(t,y), y(t0)=y0
      def f(t,y):
        return (0.03)*y

      fg = 3
      t0 = 0
      tn = 15 
      y0 = 10000
      h = 1/2

      n = int(abs(tn-t0)/h)

      t = linspace(t0,tn,n+1)
      print('size of t: ', len(t))
      ye = euler(t0,tn,n,y0)
      
      print('Using Euler:')
      print('ye[10]', ye[10], 'for ', t[10], 'years')
      print('ye[20]', ye[20], 'for ', t[20], 'years')
      print('ye[30]', ye[30], 'for ', t[30], 'years')
      yrk = RK4(t0,tn,n,y0)
      print('Using Runge-Kutta:')
      print('yrk[10]', yrk[10], 'for ', t[10], 'years')
      print('yrk[20]', yrk[20], 'for ', t[20], 'years')
      print('yrk[30]', yrk[30], 'for ', t[30], 'years')
      
      # Script to produce graphs (1 GRAPH)

      fg = plt.figure()
      plt.plot(t,yrk,'r+',label='Runge-Kutta')
      plt.plot(t,ye,'b--',label='Euler')
      plt.grid()
      fg.suptitle('Problem 3', fontsize=12)
      plt.legend()
      plt.show()

    elif ans=="4":
      ########################################################################### Problem 4

      print("-----------------------------------------")
      print("Problem 4:")
      print("-----------------------------------------")

      #f in the IVP y’ = f(t,y), y(t0)=y0
      def f(t,y):
        return (0.0375)*y

      fg = 4
      t0 = 0
      tn = 10 
      y0 = 500
      h = 1/4

      n = int(abs(tn-t0)/h)

      t = linspace(t0,tn,n+1)
      print('size of t: ', len(t))
      ye = euler(t0,tn,n,y0)
      print('Using Euler:')
      print('ye[4]', ye[4], 'for ', t[4], 'years')
      print('ye[8]', ye[8], 'for ', t[8], 'years')
      print('ye[40]', ye[40], 'for ', t[40], 'years')
      yrk = RK4(t0,tn,n,y0)
      print('Using Runge-Kutta:')
      print('yrk[4]', yrk[4], 'for ', t[4], 'years')
      print('yrk[8]', yrk[8], 'for ', t[8], 'years')
      print('yrk[40]', yrk[40], 'for ', t[40], 'years')
      
      # Script to produce graphs (ONE GRAPH)

      fg = plt.figure()
      plt.plot(t,yrk,'r+',label='Runge-Kutta')
      plt.plot(t,ye,'b--',label='Euler')
      plt.grid()
      fg.suptitle('Problem 4', fontsize=12)
      plt.legend()
      plt.show()

    
    elif ans=="5":

      ########################################################################### Problem 5

      print("-----------------------------------------")
      print("Problem 5:")
      print("-----------------------------------------")

      #f in the IVP y’ = f(t,y), y(t0)=y0
      def f(t,y):
        return (y**2)-(y**3)
      
      fg = 5
      t0 = 0
      tn = 200  
      y0 = 0.01
      h = 2/5

      n = int(abs(tn-t0)/h)

      t = linspace(t0,tn,n+1)
      print('size of t: ', len(t))
      ye = euler(t0,tn,n,y0)
      print('Using Euler:')
      print('Final value: ', ye[-1], 'for ', t[-1], 'time')
      yrk = RK4(t0,tn,n,y0)
      print('Using Runge-Kutta:')
      print('Final value: ', yrk[-1], 'for ', t[-1], 'time')
      
     
      # Script to produce graphs

      fg = plt.figure()
      plt.plot(t,yrk,'r+',label='Runge-Kutta')
      plt.plot(t,ye,'b--',label='Euler')
      
      plt.grid()
      fg.suptitle('Problem 5', fontsize=12)
      plt.legend()
      plt.show()
      

    
    elif ans=="6":
      ########################################################################### Problem 6
##########duda
      print("-----------------------------------------")
      print("Problem 6:")
      print("-----------------------------------------")

      #f in the IVP y’ = f(t,y), y(t0)=y0
      
      def f(t,y):
        return (y**2)-(y**3)

      fg = 6
      t0 = 0
      tn = 2000 
      y0 = 1/1000
      h = 1

      n = int(abs(tn-t0)/h)

      t = linspace(t0,tn,n+1)
      print('size of t: ', len(t))
      
      ye = euler(t0,tn,n,y0)

      print('Using Euler for radius 0.9:')
      yedex = absolute (ye -0.90).argmin()
      print({t[yedex]})
      
      yrk = RK4(t0,tn,n,y0)
      print('Using Runge-Kutta for radius 0.9:')
      yrkdex = absolute (yrk -0.90).argmin()
      print({t[yrkdex]})
      
      # Script to produce graphs

      fg = plt.figure()
      plt.plot(t,yrk,'r+',label='Runge-Kutta')
      plt.plot(t,ye,'b--',label='Euler')
      plt.grid()
      fg.suptitle('Problem 6', fontsize=12)
      plt.legend()
      
      plt.show()
      
      
      
    
    elif ans=="7":
      ########################################################################### Problem 7

      print("-----------------------------------------")
      print("Problem 7:")
      print("-----------------------------------------")


      #f in the IVP y’ = f(t,y), y(t0)=y0
      
      def f(t,y):
        return y

      #Analytic Solution
      def fanalit(y):
       return exp(y)

      fg = 7
      t0 = 0
      tn = 1  
      y0 = 1
      h = 0.1

      n = int(abs(tn-t0)/h)

      t = linspace(t0,tn,n+1)

      
      ye = euler(t0,tn,n,y0)
      print('Using Euler:')
      A = ye[-1]
     
      print('ye[-1]', "%.4f" % A , 'for ', t[-1], 'evaluated on y(1)')
      yrk = RK4(t0,tn,n,y0)
      B = yrk[-1]
      print('Using Runge-Kutta:')
      print('yrk[-1]', "%.4f" % B, 'for ', t[-1], 'evaluated on y(1)') 
       
      ysol = fanalit(t)
       

      Table7a = PrettyTable(["Xn", "Yn using Euler", "Yn using RK","Actual value (Analytic Solution)", "Abs. error for Euler", "%Rel. error for Euler", "Abs. error for RK", "%Rel. error for RK"])
      for i in range (len(t)):
          x_n = t[i]
          y_ne = ye[i]
          y_nRK = yrk[i]
          Act_Value = ysol[i]
          Abs_errorE = abs(ysol[i]-ye[i])
          Rel_errorE = abs(ysol[i]-ye[i])/ysol[i]*100
          Abs_errorRK = abs(ysol[i]-yrk[i])
          Rel_errorRK = abs(ysol[i]-yrk[i])/ysol[i]*100
          Table7a.add_row([round(x_n,4), round(y_ne,4), round(y_nRK,4), round(Act_Value,4), round(Abs_errorE,4), round(Rel_errorE,4), round(Abs_errorRK,4) ,round(Rel_errorRK,4)])
      print(Table7a)


      fg = plt.figure()
      plt.plot(t,yrk,'r+',label='Runge-Kutta')
      plt.plot(t,ye,'b--',label='Euler')
      plt.plot(t, ysol, 'c', label='Analytic')
      plt.grid()
      fg.suptitle('Problem 7 with 0.1', fontsize=12)
      plt.legend()
      plt.show()
      
      fg = 7.1
      t0 = 0
      tn = 1  
      y0 = 1
      h = 0.05

      n = int(abs(tn-t0)/h)

      t = linspace(t0,tn,n+1)
      print('size of t: ', len(t))
      
      
      ye = euler(t0,tn,n,y0)
      print('Using Euler:')
      A = ye[-1]
     
      print('ye[-1]', "%.4f" % A , 'for ', t[-1], 'evaluated on y(1)')
      yrk = RK4(t0,tn,n,y0)
      B = yrk[-1]
      print('Using Runge-Kutta:')
      print('yrk[-1]', "%.4f" % B, 'for ', t[-1], 'evaluated on y(1)') 
      
      ysol = fanalit(t)
      print("Solucion analitica: ", ysol)

      Table7b = PrettyTable(["Xn", "Yn using Euler", "Yn using RK","Actual value (Analytic Solution)", "Abs. error for Euler", "%Rel. error for Euler", "Abs. error for RK", "%Rel. error for RK"])
      for i in range (len(t)):
          x_n = t[i]
          y_ne = ye[i]
          y_nRK = yrk[i]
          Act_Value = ysol[i]
          Abs_errorE = abs(ysol[i]-ye[i])
          Rel_errorE = abs(ysol[i]-ye[i])/ysol[i]*100
          Abs_errorRK = abs(ysol[i]-yrk[i])
          Rel_errorRK = abs(ysol[i]-yrk[i])/ysol[i]*100
          Table7b.add_row([round(x_n,4), round(y_ne,4), round(y_nRK,4), round(Act_Value,4), round(Abs_errorE,4), round(Rel_errorE,4), round(Abs_errorRK,4) ,round(Rel_errorRK,4)])
      print(Table7b)


      # Script to produce graphs

      fg = plt.figure()
      plt.plot(t,yrk,'r+',label='Runge-Kutta')
      plt.plot(t,ye,'b--',label='Euler')
      plt.plot(t, ysol, 'c', label='Analytic')
      plt.grid()
      fg.suptitle('Problem 7 with 0.05', fontsize=12)
      plt.legend()
      plt.show()

    
    elif ans=="8":
      ########################################################################### Problem 8

      print("-----------------------------------------")
      print("Problem 8:")
      print("-----------------------------------------")

      #f in the IVP y’ = f(t,y), y(t0)=y0
      def f(t,y):
        return 2*t*y

      #Analytic Solution
      def fanalit(y):
       return exp(t**2-1)

      fg = 8
      t0 = 1
      tn = 1.5  
      y0 = 1
      h = 0.1

      n = int(abs(tn-t0)/h)

      t = linspace(t0,tn,n+1)
      
      print('size of t: ', len(t))
      ye = euler(t0,tn,n,y0)
      print('Using Euler:')
      A = ye[-1]
     
      print('ye[-1]', "%.4f" % A , 'for ', t[-1], 'evaluated on y(1.5)')
      yrk = RK4(t0,tn,n,y0)
      B = yrk[-1]
      print('Using Runge-Kutta:')
      print('yrk[-1]', "%.4f" % B, 'for ', t[-1], 'evaluated on y(1.5)') 
       
      ysol = fanalit(t)
      print("Solucion analitica: ", ysol)

      Table8a = PrettyTable(["Xn", "Yn using Euler", "Yn using RK","Actual value (Analytic Solution)", "Abs. error for Euler", "%Rel. error for Euler", "Abs. error for RK", "%Rel. error for RK"])
      for i in range (len(t)):
          x_n = t[i]
          y_ne = ye[i]
          y_nRK = yrk[i]
          Act_Value = ysol[i]
          Abs_errorE = abs(ysol[i]-ye[i])
          Rel_errorE = abs(ysol[i]-ye[i])/ysol[i]*100
          Abs_errorRK = abs(ysol[i]-yrk[i])
          Rel_errorRK = abs(ysol[i]-yrk[i])/ysol[i]*100
          Table8a.add_row([round(x_n,4), round(y_ne,4), round(y_nRK,4), round(Act_Value,4), round(Abs_errorE,4), round(Rel_errorE,4), round(Abs_errorRK,4) ,round(Rel_errorRK,4)])
      print(Table8a)

      # Script to produce graphs

      fg = plt.figure()
      plt.plot(t,yrk,'r+',label='Runge-Kutta')
      plt.plot(t,ye,'b--',label='Euler')
      plt.plot(t, ysol, 'c', label='Analytic')
      plt.grid()
      fg.suptitle('Problem 8 with 0.1', fontsize=12)
      plt.legend()
      plt.show()
      
      fg = 8.1
      t0 = 1
      tn = 1.5 
      y0 = 1
      h = 0.05

      n = int(abs(tn-t0)/h)

      t = linspace(t0,tn,n+1)
      print('size of t: ', len(t))

      print('size of t: ', len(t))
      ye = euler(t0,tn,n,y0)
      print('Using Euler:')
      A = ye[-1]
     
      print('ye[-1]', "%.4f" % A , 'for ', t[-1], 'evaluated on y(1.5)')
      yrk = RK4(t0,tn,n,y0)
      B = yrk[-1]
      print('Using Runge-Kutta:')
      print('yrk[-1]', "%.4f" % B, 'for ', t[-1], 'evaluated on y(1.5)') 

      ysol = fanalit(t)
      print("Solucion analitica: ", ysol)

      Table8b = PrettyTable(["Xn", "Yn using Euler", "Yn using RK","Actual value (Analytic Solution)", "Abs. error for Euler", "%Rel. error for Euler", "Abs. error for RK", "%Rel. error for RK"])
      for i in range (len(t)):
          x_n = t[i]
          y_ne = ye[i]
          y_nRK = yrk[i]
          Act_Value = ysol[i]
          Abs_errorE = abs(ysol[i]-ye[i])
          Rel_errorE = abs(ysol[i]-ye[i])/ysol[i]*100
          Abs_errorRK = abs(ysol[i]-yrk[i])
          Rel_errorRK = abs(ysol[i]-yrk[i])/ysol[i]*100
          Table8b.add_row([round(x_n,4), round(y_ne,4), round(y_nRK,4), round(Act_Value,4), round(Abs_errorE,4), round(Rel_errorE,4), round(Abs_errorRK,4) ,round(Rel_errorRK,4)])
      print(Table8b)

      # Script to produce graphs

      fg = plt.figure()
      plt.plot(t,yrk,'r+',label='Runge-Kutta')
      plt.plot(t,ye,'b--',label='Euler')
      plt.plot(t, ysol, 'c', label='Analytic')
      plt.grid()
      fg.suptitle('Problem 8 with 0.05', fontsize=12)
      plt.legend()
      plt.show()
    
    elif ans=="9":
      ########################################################################### Problem 9

      print("-----------------------------------------")
      print("Problem 9:")
      print("-----------------------------------------")

      #f in the IVP y’ = f(t,y), y(t0)=y0
      def f(t,y):
        return 2*(cos(t))*y

      fg = 9.1
      t0 = 0
      tn = 50 
      y0 = 1
      h = 0.25

      n = int(abs(tn-t0)/h)

      t = linspace(t0,tn,n+1)
      print('size of t: ', len(t))
      ye = euler(t0,tn,n,y0)
      #print('Using Euler:')
      #print('ye[12]', ye[12], 'for ', t[-1], 'years')
      yrk = RK4(t0,tn,n,y0)
      #print('Using Runge-Kutta:')
      #print('yrk[12]', ye[12], 'for ', t[12*5], 'years')
      
      # Script to produce graphs

      fg = plt.figure()
      plt.plot(t,yrk,'r+',label='Runge-Kutta')
      plt.plot(t,ye,'b--',label='Euler')
      plt.grid()
      fg.suptitle('Problem 9 with 0.25', fontsize=12)
      #axis([0,tn,-60,40])
      plt.legend()
      plt.show()
      
      h = 0.1

      n = int(abs(tn-t0)/h)

      t = linspace(t0,tn,n+1)
      print('size of t: ', len(t))
      ye = euler(t0,tn,n,y0)
      #print('Using Euler:')
      #print('ye[12]', ye[12], 'for ', t[-1], 'years')
      yrk = RK4(t0,tn,n,y0)
      #print('Using Runge-Kutta:')
      #print('yrk[12]', ye[12], 'for ', t[12*5], 'years')
      
      # Script to produce graphs

      fg = plt.figure()
      plt.plot(t,yrk,'r+',label='Runge-Kutta')
      plt.plot(t,ye,'b--',label='Euler')
      plt.grid()
      fg.suptitle('Problem 9 with 0.1', fontsize=12)
      #axis([0,tn,-60,40])
      plt.legend()
      plt.show()
      
      h = 0.05

      n = int(abs(tn-t0)/h)

      t = linspace(t0,tn,n+1)
      print('size of t: ', len(t))
      ye = euler(t0,tn,n,y0)
      #print('Using Euler:')
      #print('ye[12]', ye[12], 'for ', t[-1], 'years')
      yrk = RK4(t0,tn,n,y0)
      #print('Using Runge-Kutta:')
      #print('yrk[12]', ye[12], 'for ', t[12*5], 'years')
      
      # Script to produce graphs

      fg = plt.figure()
      plt.plot(t,yrk,'r+',label='Runge-Kutta')
      plt.plot(t,ye,'b--',label='Euler')
      plt.grid()
      fg.suptitle('Problem 9 with 0.05', fontsize=12)
      #axis([0,tn,-60,40])
      plt.legend()
      plt.show()


    elif ans=="10":
      ########################################################################### Problem 10

      print("-----------------------------------------")
      print("Problem 10:")
      print("-----------------------------------------")

      #f in the IVP y’ = f(t,y), y(t0)=y0
      
      def f(t,y):
        return y*(10-(2*y))

      fg = 10.1
      t0 = 0
      tn = 50
      y0 = 1

      h = 0.25

      n = int(abs(tn-t0)/h)

      t = linspace(t0,tn,n+1)
      print('size of t: ', len(t))
      ye = euler(t0,tn,n,y0)
      #print('Using Euler:')
      #print('ye[12]', ye[12], 'for ', t[-1], 'years')
      yrk = RK4(t0,tn,n,y0)
      #print('Using Runge-Kutta:')
      #print('yrk[12]', ye[12], 'for ', t[12*5], 'years')
      
      # Script to produce graphs

      fg = plt.figure()
      plt.plot(t,yrk,'r+',label='Runge-Kutta')
      plt.plot(t,ye,'b--',label='Euler')
      plt.grid()
      fg.suptitle('Problem 10 with 0.25', fontsize=12)
      #axis([0,tn,-60,40])
      plt.legend()
      plt.show()
      
      h = 0.1

      n = int(abs(tn-t0)/h)

      t = linspace(t0,tn,n+1)
      print('size of t: ', len(t))
      ye = euler(t0,tn,n,y0)
      #print('Using Euler:')
      #print('ye[12]', ye[12], 'for ', t[-1], 'years')
      yrk = RK4(t0,tn,n,y0)
      #print('Using Runge-Kutta:')
      #print('yrk[12]', ye[12], 'for ', t[12*5], 'years')
      
      # Script to produce graphs

      fg = plt.figure()
      plt.plot(t,yrk,'r+',label='Runge-Kutta')
      plt.plot(t,ye,'b--',label='Euler')
      plt.grid()
      fg.suptitle('Problem 10 with 0.1', fontsize=12)
      #axis([0,tn,-60,40])
      plt.legend()
      plt.show()
      
      h = 0.05

      n = int(abs(tn-t0)/h)

      t = linspace(t0,tn,n+1)
      print('size of t: ', len(t))
      ye = euler(t0,tn,n,y0)
      #print('Using Euler:')
      #print('ye[12]', ye[12], 'for ', t[-1], 'years')
      yrk = RK4(t0,tn,n,y0)
      #print('Using Runge-Kutta:')
      #print('yrk[12]', ye[12], 'for ', t[12*5], 'years')
      
      # Script to produce graphs

      fg = plt.figure()
      plt.plot(t,yrk,'r+',label='Runge-Kutta')
      plt.plot(t,ye,'b--',label='Euler')
      plt.grid()
      fg.suptitle('Problem 10 with 0.05', fontsize=12)
      #axis([0,tn,-60,40])
      plt.legend()
      plt.show()
    
    elif ans=="11":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")