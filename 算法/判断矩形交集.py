class Rectangle(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def isInterset(self,r):
        if self.x<=r.x+r.width and r.x<=self.x+self.width and \
                self.y<=r.y+r.height and r.y<=self.y+self.height:
            return True
        return False
    def intersetRectangle(self,r):
        if self.isInterset(r):
            return Rectangle(max(self.x,r.x),max(self.y,r.y),
                             min(r.x+r.width,self.x+self.width)-max(self.x,r.x),
                             min(r.y+r.height,self.y+self.height)-max(self.y,r.y))
        return None

import matplotlib.pyplot as plt
import matplotlib.patches as patches
S=Rectangle(0.1,0.1,0.5,0.5)
R=Rectangle(0.2,0.2,0.6,0.5)
fig=plt.figure()
ax=fig.add_subplot(111,aspect='equal')
ax.add_patch(patches.Rectangle((S.x,S.y),S.width,S.height,facecolor='red'))
ax.add_patch(patches.Rectangle((R.x,R.y),R.width,R.height,facecolor='blue'))
if S.isInterset(R):
    interset=S.intersetRectangle(R)
    print('x:{0},y:{1},w:{2},h:{3}'.format(interset.x,interset.y,interset.width,interset.height))
    ax.add_patch(patches.Rectangle((interset.x,interset.y),interset.width,interset.height,facecolor='green'))
    fig.savefig('rectangle1.png',dpi=90,bbox_inches='tight')
    plt.show()
