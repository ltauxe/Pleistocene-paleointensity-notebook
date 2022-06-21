import pandas as pd
from pmagpy import pmag as pmag
import numpy as np
import matplotlib.pyplot as plt

def modified_do_TS(ax,amin,amax, **kwargs):
    timescale='gts12'
    #ax.set_title('GTS12')
    ax.axis([-.25,1.5,amax,amin])
    ax.axes.get_xaxis().set_visible(False)
    TS,Chrons=pmag.get_ts(timescale)
    X,Y,Y2=[0,1],[],[]
    cnt=0
    if amin<TS[1]: # in the Brunhes
                Y=[amin,amin] # minimum age
                Y1=[TS[1],TS[1]] # age of the B/M boundary
                ax.fill_between(X,Y,Y1,facecolor='black') # color in Brunhes, black
    for d in TS[1:]:
                pol=cnt%2
                cnt+=1
                if d<=amax and d>=amin:
                    
                    ind=TS.index(d)
                    Y=[TS[ind],TS[ind]]
                    Y1=[TS[ind+1],TS[ind+1]]
                    if pol: ax.fill_between(X,Y,Y1,facecolor='black') # fill in every other time
    ax.plot([0,1,1,0,0],[amin,amin,amax,amax,amin],'k-')
    plt.yticks(np.arange(amin,amax+1,1))
    ax.set_ylabel("Age (Ma): "+timescale)
    ax2=ax.twinx()
    ax2.axis('off')

    Chrons = np.array(Chrons)
    if "label" in kwargs.keys() and "labelbounds" in kwargs.keys():
        label = kwargs['label']
        ages = kwargs['labelbounds']
    else:
        label = Chrons[:, 0]
        ages = Chrons[:,1]
        ages = ages.astype('float64')

    for k in range(len(ages)-1):
                age=ages[k]
                cnext=ages[k+1]
                d=cnext-(cnext-age)/3.
                if d>=amin and d<amax:
                    ax2.plot([1,1.5],[age,age],'k-') # make the Chron boundary tick
                    ax2.text(1.05,d,label[k]) #
    ax2.axis([-.25,1.5,amax,amin])
    
    
def do_TS(ax,amin,amax):
    timescale='gts12'
    ax.set_title('GTS12')
    ax.axis([-.25,1.5,amax,amin])
    ax.axes.get_xaxis().set_visible(False)
    TS,Chrons=pmag.get_ts(timescale)
    X,Y,Y2=[0,1],[],[]
    cnt=0
    if amin<TS[1]: # in the Brunhes
                Y=[amin,amin] # minimum age
                Y1=[TS[1],TS[1]] # age of the B/M boundary
                ax.fill_between(X,Y,Y1,facecolor='black') # color in Brunhes, black
    for d in TS[1:]:
                pol=cnt%2
                cnt+=1
                if d<=amax and d>=amin:
                    
                    ind=TS.index(d)
                    Y=[TS[ind],TS[ind]]
                    Y1=[TS[ind+1],TS[ind+1]]
                    if pol: ax.fill_between(X,Y,Y1,facecolor='black') # fill in every other time
    ax.plot([0,1,1,0,0],[amin,amin,amax,amax,amin],'k-')
    plt.yticks(np.arange(amin,amax+1,1))
    ax.set_ylabel("Age (Ma): "+timescale)
    ax2=ax.twinx()
    ax2.axis('off')

    for k in range(len(Chrons)-1):
                c=Chrons[k]
                cnext=Chrons[k+1]
                d=cnext[1]-(cnext[1]-c[1])/3.
                if d>=amin and d<amax:
                    ax2.plot([1,1.5],[c[1],c[1]],'k-') # make the Chron boundary tick
                    ax2.text(1.05,d,c[0]) #
    ax2.axis([-.25,1.5,amax,amin])
    
    
def label_chrons(ax,x,chrons,levels):
    for c in range(len(chrons)):
        ax.text(x,levels[c],'- '+chrons[c],va='center')
        
def get_ages(section):
    section=section.to_dict('records')
    ind=0
    while(ind<len(section)):
        c=section[ind]['Chron'].strip('\(').strip('\)')
        if c in chron_list:
            age=Chrons[Chrons.Chron==c].Age.values[0]
            section[ind]['age']=age
        ind+=1
    return section
