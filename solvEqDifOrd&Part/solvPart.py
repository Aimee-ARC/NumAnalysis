import numpy as np 
from lib_funciones_particulares import*


print("""
1.Problem 1
2.Problem 2
3.Problem 3
4.Problem 4
5.Problem 5
6.Exit/Quit
""")

ans=True
while ans:
    ans = input("What would you like to do? ")

    if ans=="1":
      ########################################################################### Problem 1

      print("-----------------------------------------")
      print("Example 1:")
      print("-----------------------------------------")
      
      def I(x):
          
          if x>=0 and x<= 0.5:
              return 2*x
          elif x>= 0.5 and x<= 1:
              return 2 -2*x

      ### Data A

      aK = 1
      aL = 1 
      aNx = 20
      adx = 0.05 #L/Nx
      aT = 0.12
      adt = 0.0012 #T/Nt
      aNt = int(aT/adt)
      aF = 0.48 #dt*K/dx**2   

      ans = solver_FE_simple(I,aK,aL,adt,aF,aT)

      u_n = ans[0]
      x = ans[1]
      t = ans[2]
      cpu = ans[3]
      u_array =ans[4]

      figure1a(1.1,t, u_array, aNt, aNx, aL)

      ### Data B

      bK = 1
      bL = 1 
      bNx = 20
      bdx = 0.05 #L/Nx
      bT = 0.13
      bdt = 0.0013 #T/Nt
      bNt = int(bT/bdt)
      bF = 0.52 #dt*K/dx**2   

      ans = solver_FE_simple(I,bK,bL,bdt,bF,bT)

      u_n = ans[0]
      x = ans[1]
      t = ans[2]
      cpu = ans[3]
      u_array =ans[4]

      figure1b(1.2,t, u_array, bNt, bNx, bL)




    elif ans=="2":
      ########################################################################### Problem 2

      print("-----------------------------------------")
      print("Problem 2:")
      print("-----------------------------------------")
      
      def I(x):
          return np.sin(((np.pi)/2)*x)

      def sol(t, t0, y0):
          return np.exp(-((np.pi**2)/4)*t0)*np.sin((np.pi/2)*y0)


      K = 1
      L = 2 
      Nx = 4 #m
      dx = L/Nx
      T = 0.1
      Nt = 2 #N
      dt = T/Nt
      F = dt*K/dx**2   


      ans = solver_FE_simple(I,K,L,dt,F,T)


      u_n = ans[0]
      x = ans[1]
      t = ans[2]
      cpu = ans[3]
      u_array =ans[4]

      figure2(2,t, u_array, Nt, Nx, L)

      y0 = np.linspace(0,L,Nx+1)
      usol = sol(t,0.1,y0)
      plt.plot(y0 ,usol,color='k',label='Exact 0.1',marker='x',  linestyle='dashed')
      usol = sol(t,0.05,y0)
      plt.plot(y0 ,usol,color='k',label='Exact 0.05',marker='x',  linestyle='dashed')
      usol = sol(t,0,y0)
      plt.plot(y0 ,usol,color='k',label='Exact 0',marker='x',  linestyle='dashed')

      plt.legend()
      plt.grid(True)
      plt.show()




    elif ans=="3":
    ########################################################################### Problem 3

      print("-----------------------------------------")
      print("Problem 3:")
      print("-----------------------------------------")
      def I(x):
          return np.sin(2*(np.pi)*x)

      def sol(t, t0, y0):
          return np.exp(-4*((np.pi)**2)*t0)*np.sin(2*np.pi*y0)

      #############Data A
      K = 1
      L = 2
      Nx = 5 #L/dx
      dx =  0.4 #L/Nx
      T = 0.5
      Nt = 50 #T/dt
      dt = 0.01 #T/Nt
      F = dt*K/dx**2   


      ans = solver_FE_simple(I,K,L,dt,F,T)


      u_n = ans[0]
      x = ans[1]
      t = ans[2]
      cpu = ans[3]
      u_array =ans[4]

      figure3a(3.1,t, u_array, Nt, Nx, L)


      nt = Nt
      time = t
      y_time = u_array
      x_sec_min = 0
      x_sec_max = L
      nx = Nx
      xlab = 'Length[cm]'
      ylab = 'Heat[C°]'
      legend = False


      for i in range (0, Nt+1):
          if t[i]== 0.5:
              print ('u(x,t)', u_array[i], 'for t=', t[i])
              fig_title='Solution for 3a t='+str(t[i])
              XYplot(x, u_array[i], x_sec_min, x_sec_max, xlab, ylab, fig_title, 'blue', False)
              y0 = np.linspace(0, L, Nx+1)
              usol = sol(t, 0.5, y0)
              plt.plot(y0, usol, color = 'cyan', label= 'Exact sol')
              plt.legend()

      ################Data B
      K = 1
      L = 2
      Nx = 5 #L/dx
      dx =  0.4 #L/Nx
      T = 0.5
      Nt = 1 #T/dt
      dt = 0.5 #T/Nt
      F = dt*K/dx**2   


      ans = solver_FE_simple(I,K,L,dt,F,T)


      u_n = ans[0]
      x = ans[1]
      t = ans[2]
      cpu = ans[3]
      u_array =ans[4]

      figure3b(3.2,t, u_array, Nt, Nx, L)


      nt = Nt
      time = t
      y_time = u_array
      x_sec_min = 0
      x_sec_max = L
      nx = Nx
      xlab = 'Length[cm]'
      ylab = 'Heat[C°]'
      legend = False


      for i in range (0, Nt+1):
          if t[i]== 0.5:
              print ('u(x,t)', u_array[i], 'for t=', t[i])
              fig_title='Solution 3b for t='+str(t[i])
              XYplot(x, u_array[i], x_sec_min, x_sec_max, xlab, ylab, fig_title, 'blue', False)
              y0 = np.linspace(0, L, Nx+1)
              usol = sol(t, 0.5, y0)
              plt.plot(y0, usol, color = 'cyan', label= 'Exact sol')
              plt.legend()
      
      


    elif ans=="4":
      ########################################################################### Problem 4

      print("-----------------------------------------")
      print("Problem 4:")
      print("-----------------------------------------")
      
      def I(x):
          return np.sin(x)

      def sol(t, t0, y0):
          return (np.exp(-t0))* (np.sin(y0))


      K = 1
      L = np.pi 
      Nx = 10
      dx = np.pi/10 #L/Nx
      T = 0.5
      Nt = 10
      dt = 0.05 #T/Nt
      F = dt*K/dx**2   


      ans = solver_FE_simple(I,K,L,dt,F,T)


      u_n = ans[0]
      x = ans[1]
      t = ans[2]
      cpu = ans[3]
      u_array =ans[4]

      figure4(4,t, u_array, Nt, Nx, L)

      nt = Nt
      time = t
      y_time = u_array
      x_sec_min = 0
      x_sec_max = L
      nx = Nx
      xlab = 'Length[cm]'
      ylab = 'Heat[C°]'
      legend = False


      for i in range (0, Nt+1):
          if t[i]== 0.5:
              print ('u(x,t)', u_array[i], 'for t=', t[i])
              fig_title='Solution 4 for t='+str(t[i])
              XYplot(x, u_array[i], x_sec_min, x_sec_max, xlab, ylab, fig_title, 'blue', False)
              y0 = np.linspace(0, L, Nx+1)
              usol = sol(t, 0.5, y0)
              plt.plot(y0, usol, color = 'cyan', label= 'Exact sol')
              plt.legend()




    
    elif ans=="5":

      ########################################################################### Problem 5

      
      
      print("-----------------------------------------")
      print("Problem 5:")
      print("-----------------------------------------")
      
      def I(x):
          return (np.cos(np.pi*(x - 0.5)))

      def sol(t, t0, y0):
          return (np.exp(- t0))* (np.cos(np.pi*(y0 - 0.5)))


      K = 1/((np.pi)**2)
      L = 1 
      Nx = 10
      dx = 0.1 #L/Nx
      T = 0.4
      Nt = 10
      dt = 0.04 #T/Nt
      F = dt*K/dx**2   


      ans = solver_FE_simple(I,K,L,dt,F,T)


      u_n = ans[0]
      x = ans[1]
      t = ans[2]
      cpu = ans[3]
      u_array =ans[4]

      figure5(5,t, u_array, Nt, Nx, L)

      nt = Nt
      time = t
      y_time = u_array
      x_sec_min = 0
      x_sec_max = L
      nx = Nx
      xlab = 'Length[cm]'
      ylab = 'Heat[C°]'
      legend = False


      for i in range (0, Nt+1):
          if t[i]== 0.4:
              print ('u(x,t)', u_array[i], 'for t=', t[i])
              fig_title='Solution 5 for t='+str(t[i])
              XYplot(x, u_array[i], x_sec_min, x_sec_max, xlab, ylab, fig_title, 'blue', False)
              y0 = np.linspace(0, L, Nx+1)
              usol = sol(t, 0.4, y0)
              plt.plot(y0, usol, color = 'cyan', label= 'Exact sol')
              plt.legend()
              
      
      def I(x):
          return (np.cos(np.pi))*(x - 0.5)

      def sol(t, t0, y0):
          return (np.exp(- t0))* (np.cos(np.pi)*(y0 - 0.5))


      K = 1/((np.pi)**2)
      L = 1 
      Nx = 10
      dx = 0.1 #L/Nx
      T = 0.4
      Nt = 10
      dt = 0.04 #T/Nt
      F = dt*K/dx**2   


      ans = solver_FE_simple(I,K,L,dt,F,T)


      u_n = ans[0]
      x = ans[1]
      t = ans[2]
      cpu = ans[3]
      u_array =ans[4]

      figure5(5,t, u_array, Nt, Nx, L)

      nt = Nt
      time = t
      y_time = u_array
      x_sec_min = 0
      x_sec_max = L
      nx = Nx
      xlab = 'Length[cm]'
      ylab = 'Heat[C°]'
      legend = False


      for i in range (0, Nt+1):
          if t[i]== 0.4:
              print ('u(x,t)', u_array[i], 'for t=', t[i])
              fig_title='Solution 5 for t='+str(t[i])
              XYplot(x, u_array[i], x_sec_min, x_sec_max, xlab, ylab, fig_title, 'blue', False)
              y0 = np.linspace(0, L, Nx+1)
              usol = sol(t, 0.4, y0)
              plt.plot(y0, usol, color = 'cyan', label= 'Exact sol')
              plt.legend()




    elif ans=="6":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")

