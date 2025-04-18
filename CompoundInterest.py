# Linear Regression model for FPC 2025
# Helps us generate graphs and predict returns from investments
# It assumes that all growth or decline is linear
import matplotlib.pyplot as plt 
import numpy as np

def linear_model(w,x,b):
    return (w*x)+b

amts = int(input("How many income streams >> "));
mn = int(input("How many months >> "))
stream_list = [] # List of monthly rates for income streams
capitals = [] # Initial amount of $ put into each stream
names = []

print('\n')

for a in range(1,amts+1):
    capitals.append(float(input(f"amount of investment capital for source #{a} >> ")))
    stream_list.append(float(input(f"monthly income rate for source #{a} >> ")))
    names.append(str(input(f"name of source #{a} >> ")))
masterp=[] #list of points for plt
tks=[] # at the end, how much do they have
ofs=float(input("Monthly offset >> "))
for i in range(0,len(stream_list)):
    rate=(stream_list[i])+1
    points = []
    tmp=0
    for j in range(0,mn):
        if j == 0: 
            tmp=linear_model(capitals[i], rate, b=ofs)
        else:
            tmp=linear_model(tmp,rate,b=ofs)
        points.append(tmp)
    masterp.append(points)
    tks.append(points[-1])

tks=sum(tks)

xaxis=np.linspace(0,amts, len(masterp[0]))
fig, ax = plt.subplots(figsize=(8,6))

for xg in range(0,len(masterp)):
    ax.plot(xaxis,masterp[xg],label=names[xg],marker='o')

ax.legend()
ax.set_xlabel("Months")
ax.set_ylabel("Money")
ax.set_title("Growth of Investments")

plt.show()

print(f"All of your sources combined will make {tks} after {mn} months")