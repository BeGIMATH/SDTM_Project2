import tkinter as tk
from .build  import tp4
from tkinter import messagebox as mBox
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from math import sqrt



from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d




import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.figure import Figure 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


# creating basic window
window = tk.Tk()
#window.geometry("500x500") # size of the window width:- 500, height:- 375
#window.resizable(0, 0) # this prevents from resizing the window
window.title("3D Vector Ploter")

def _msgBox():
    mBox.showinfo('Thanks for installing this software!', ' A simple 3DPloter of Vectors in')



root_menu = tk.Menu(window)
window.config(menu = root_menu)

#creating sub menus in the root menu
file_menu = tk.Menu(root_menu) #It initializes a new sub menu in the root menu
root_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Exit", command = window.quit)


about_menu = tk.Menu(root_menu)
root_menu.add_cascade(label="About",menu=about_menu)
about_menu.add_command(label="About the Calculator",command=_msgBox)




win1 = tk.LabelFrame(window)
win1.grid(column=0,row=0, sticky="wesn")

x_1 = tk.DoubleVar()
x_1.set("")

tk.Label(win1,text=" v1 ").grid(row=0,column=0,padx=10,pady=10)
tk.Entry(win1,textvariable=x_1,width=3).grid(row=1,column=0,padx=10,pady=10)


x_2 = tk.DoubleVar()
x_2.set("")

tk.Entry(win1,textvariable=x_2,width=3).grid(row=2,column=0,padx=10,pady=10)

x_3 = tk.DoubleVar()
x_3.set("")

tk.Entry(win1,textvariable=x_3,width=3).grid(row=3,column=0,padx=10,pady=10)


X_1 = tk.DoubleVar()
X_1.set("")
tk.Label(win1,text=" v2 ").grid(row=0,column=1,padx=10,pady=10)

tk.Entry(win1,textvariable=X_1,width=3).grid(row=1,column=1,padx=10,pady=10)

X_2 = tk.DoubleVar()
X_2.set("")


tk.Entry(win1,textvariable=X_2,width=3).grid(row=2,column=1,padx=10,pady=10)


X_3 = tk.DoubleVar()
X_3.set("")

tk.Entry(win1,textvariable=X_3,width=3).grid(row=3,column=1,padx=10,pady=10)


Xx_1 = tk.DoubleVar()
Xx_1.set("")

tk.Label(win1,text="v1 + v2").grid(row=0,column=2,padx=10,pady=10)
tk.Entry(win1,textvariable=Xx_1,width=4,state="readonly").grid(row=1,column=2,padx=10,pady=10)

Xx_2 = tk.DoubleVar()
Xx_2.set("")

tk.Entry(win1,textvariable=Xx_2,width=4,state="readonly").grid(row=2,column=2,padx=10,pady=10)


Xx_3 = tk.DoubleVar()
Xx_3.set("")


tk.Entry(win1,textvariable=Xx_3,width=4,state="readonly").grid(row=3,column=2,padx=10,pady=10)


XX_1 = tk.DoubleVar()
XX_1.set("")

tk.Label(win1,text="v1 x v2").grid(row=0,column=3,padx=10,pady=10)
tk.Entry(win1,textvariable=XX_1,width=4,state="readonly").grid(row=1,column=3,padx=10,pady=10)

XX_2 = tk.DoubleVar()
XX_2.set("")

tk.Entry(win1,textvariable=XX_2,width=4,state="readonly").grid(row=2,column=3,padx=10,pady=10)



XX_3 = tk.DoubleVar()
XX_3.set("")

tk.Entry(win1,textvariable=XX_3,width=4,state="readonly").grid(row=3,column=3,padx=10,pady=10)

Dot = tk.DoubleVar()
Dot.set(0)
tk.Label(win1,text="<v1,v2>").grid(row=0,column=6,padx=10,pady=10)

tk.Entry(win1,textvariable=Dot,width=3,state="readonly").grid(row=1,column=6,padx=10,pady=10)

theta = tk.DoubleVar()
theta.set(0)
tk.Entry(win1,textvariable=theta,width=3,state="readonly").grid(row=3,column=6,padx=10,pady=10)

def add_vectors():
    v1 = tp4.Vector_create(x_1.get(),x_2.get(),x_3.get())
    v2 = tp4.Vector_create(X_1.get(),X_2.get(),X_3.get())
    v3 = tp4.Vector_add(v1,v2)
    Xx_1.set(tp4.Vector_elem(v3,0))
    Xx_2.set(tp4.Vector_elem(v3,1))
    Xx_3.set(tp4.Vector_elem(v3,2))
    tp4.Vector_destroy(v1)
    tp4.Vector_destroy(v2)
    tp4.Vector_destroy(v3)

def cross_prod():
    v1 = tp4.Vector_create(x_1.get(),x_2.get(),x_3.get())
    v2 = tp4.Vector_create(X_1.get(),X_2.get(),X_3.get())
    v3 = tp4.Vector_cross(v1,v2)
    XX_1.set(tp4.Vector_elem(v3,0))
    XX_2.set(tp4.Vector_elem(v3,1))
    XX_3.set(tp4.Vector_elem(v3,2))
    tp4.Vector_destroy(v1)
    tp4.Vector_destroy(v2)
    tp4.Vector_destroy(v3)

def dot():
    v1 = tp4.Vector_create(x_1.get(),x_2.get(),x_3.get())
    v2 = tp4.Vector_create(X_1.get(),X_2.get(),X_3.get())
    Dot.set(tp4.Vector_dot(v1,v2))

def angle():
    v1 = tp4.Vector_create(x_1.get(),x_2.get(),x_3.get())
    v2 = tp4.Vector_create(X_1.get(),X_2.get(),X_3.get())
    theta.set(tp4.Vector_angle(v1,v2))





tk.Button(win1, text='<.> ', command=dot).grid(column=5,row=3,padx=10,pady=10)
tk.Button(win1, text=' x  ', command=cross_prod).grid(column=5,row=2,padx=10,pady=10)
tk.Button(win1, text=' +  ', command=add_vectors).grid(column=5,row=1,padx=10,pady=10)
tk.Button(win1, text= '\u03F4(,)',command=angle).grid(column=6,row=2,padx=10,pady=10)
#tk.Button(win1,text="Rotate",command=rotate).grid(column=5,row=1)

win2 = tk.LabelFrame(window)
win2.grid(columnspan=2,row=1, sticky="nsew")



def plot_vectors():

   
   
    # define origin
    o = np.array([0,0,0])

    # define ov1v2z0 axes
    v1 = np.array([x_1.get(),x_2.get(),x_3.get()])
    v2 = np.array([X_1.get(),X_2.get(),X_3.get()])
    z0 = np.array([Xx_1.get(),Xx_2.get(),Xx_3.get()])
    u0 = np.array([XX_1.get(),XX_2.get(),XX_3.get()])

    v1 = v1/np.linalg.norm(v1)
    v2 = v2/np.linalg.norm(v2)
    z0 = z0/np.linalg.norm(z0)
    u0 = u0/np.linalg.norm(u0)
    
    
    # produce figure
    
    fig = Figure()
    canvas = FigureCanvasTkAgg(fig,win2)
        
    ax = fig.add_subplot(111, projection='3d')
   
    # plot ov1v2z0 axes
    a = Arrow3D([o[0], v1[0]], [o[1], v1[1]], [o[2], v1[2]], mutation_scale=20, arrowstyle='-|>', color='k')
    ax.add_artist(a)
    a = Arrow3D([o[0], v2[0]], [o[1], v2[1]], [o[2], v2[2]], mutation_scale=20,arrowstyle='-|>', color='k')
    ax.add_artist(a)
    a = Arrow3D([o[0], z0[0]], [o[1], z0[1]], [o[2], z0[2]], mutation_scale=20, arrowstyle='-|>', color='k')
    ax.add_artist(a)
    a = Arrow3D([o[0], u0[0]], [o[1], u0[1]], [o[2], u0[2]], mutation_scale=20, arrowstyle='-|>', color='k')
    ax.add_artist(a)




    text_options = {'horizontalalignment': 'center',
                    'verticalalignment': 'center',
                    'fontsize': 14}

    # add label for origin
    ax.text(0.0,0.0,0,r'$o$', **text_options)

    # add labels for x axes
    ax.text(1.1*v1[0],1.1*v1[1],1.1*v1[2],r'$v_1$', **text_options)

    # add lables for y axes
    ax.text(1.1*v2[0],1.1*v2[1],1.1*v2[2],r'$v_2$', **text_options)

    # add lables for z axes
    ax.text(1.1*z0[0],1.1*z0[1],1.1*z0[2],r'$v_1 + v_2$', **text_options)

    ax.text(1.1*u0[0],1.1*u0[1],1.1*u0[2],r'$v_1 x v_2$', **text_options)

    #ax.set_ylim(-10,10)
    #ax.set_xlim(-10,10)
    # show figure
    ax.view_init(elev=-150, azim=0)

    
    ax.set_axis_off()
    
    plt.show()

        



    
    canvas.get_tk_widget().grid(row=0,column=0)
    print(v1)

tk.Button(win1,text="Plot",command=plot_vectors).grid(column=5,row=0)
window.mainloop()