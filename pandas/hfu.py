import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-20, 20, 100)
y = np.sin(x) 
z = np.cos(x)  
o = np.tan(x)

plt.plot(
    x, y, 
    marker='o',
    markersize=4, 
    markerfacecolor="#40c9ff", 
    markeredgecolor='#40c9ff', 
    linewidth=3, 
    color="#a10bc7", 
    label='Sine Wave')

plt.plot(x, z, 
        marker='o', 
        markersize=4, 
        markerfacecolor="#ff6b6b", 
        markeredgecolor='#ff6b6b', 
        linewidth=3, 
        color="#ff6b6b", 
        label='Cosine Wave')

plt.plot(x, o, 
        marker='o', 
        markersize=4, 
        markerfacecolor="#fffb00", 
        markeredgecolor='#fffb00', 
        linewidth=3, 
        color="#ffa500", 
        label='Tangent Wave')


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine, Cosine, and Tangent Waves')

plt.grid(True, which='both', linestyle='dotted', linewidth=1.5, color="#1cc7e6")
plt.legend(["Sine Wave", "Cosine Wave", "Tangent Wave"], loc='upper left', fontsize=10, title_fontsize='13', shadow=True, fancybox=True, facecolor="#9afcef", edgecolor='#000000')
plt.show()