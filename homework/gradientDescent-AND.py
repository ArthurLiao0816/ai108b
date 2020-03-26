from net import Net
from net import Node
net = Net()

xinp=[0,0,1,1]
yinp=[0,1,0,1]
n=len(xinp)
while n>0:
    x = net.variable(n)
    y = net.variable(n)
    o  = net.add(net.add(x, y), -1)
    if(int(o.v) < 0 | int(o.v) == 0):
        o.variable = 0
    else:
        o.variable = 1
    net.gradient_descendent()
    n-=1

