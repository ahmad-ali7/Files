import numpy as np,sys,json
from PIL import Image
from scipy.ndimage import zoom,gaussian_filter,binary_erosion
sys.path.insert(0,'../real');from craft import film,to_img,smooth
sat=np.asarray(Image.open('sat.jpg')).astype(np.float32)/255;H2,W2=sat.shape[:2]
E=np.load('elev.npy');hand=np.load('hand.npy');al=np.load('along.npy').astype(np.float32);d=np.load('dist.npy');lake=np.load('lake.npy').astype(np.float32)
P=np.load('path.npy');n=len(P)
up=lambda a:zoom(a,(H2/a.shape[0],W2/a.shape[1]),order=1)
hand2,al2,d2,lake2,E2=up(hand),up(al/n),up(d),up(lake)>.5,up(E)
# hillshade from DEM to restore relief under night grade
gy,gx=np.gradient(gaussian_filter(E2,1.5),7.8)
L=np.array([-.5,-.6,.62]);L/=np.linalg.norm(L)
nz=1/np.sqrt(gx**2+gy**2+1);hs=np.clip((-gx*L[0]-gy*L[1]+L[2])*nz,0,1)
def frame(front,depth=24,flash=0,out='f.png'):
    lum=sat.mean(2,keepdims=True);base=sat*.35+lum*.65
    col=(sat*.45+lum*.55)*(.42+.85*hs[...,None])*np.array([.62,.72,.98])
    col+=smooth(lum,.5,.8)*np.array([.25,.28,.36])*hs[...,None]   # snow
    # flood
    A=al/n
    depL=depth*(1-A*.7)*np.clip((front-A)*14,0,1)
    latL=1-smooth(d,4+3*smooth(A,.85,1.),9+6*smooth(A,.85,1.))
    flL=((hand<depL*latL)&(depL>1.5)&(A<=front)&(d<25)).astype(np.float32)
    fl=np.clip(zoom(flL,(H2/flL.shape[0],W2/flL.shape[1]),order=1),0,1)
    fl=gaussian_filter(fl,1.2)
    edge=np.clip(fl-gaussian_filter(binary_erosion(fl>.5,iterations=2).astype(np.float32),1.5),0,1)
    frontband=np.exp(-((al2-front)/.012)**2)*(fl>.2)*(front<.97)
    water=np.array([.10,.13,.17])
    sheen=gaussian_filter(np.random.default_rng(int(front*1000)).random(fl.shape).astype(np.float32),2.5)
    wcol=water+ (sheen-.5)[...,None]*np.array([.06,.07,.09])*1.2
    col=col*(1-fl[...,None]*.92)+wcol*fl[...,None]
    col+=edge[...,None]*np.array([.45,.5,.58])*.9+frontband[...,None]*np.array([.55,.58,.62])*.9
    # lake surface: dark with moon sheen
    lk=gaussian_filter(lake2.astype(np.float32),1)
    col=col*(1-lk[...,None]*.55)+lk[...,None]*sat*np.array([.18,.25,.32])
    col+=flash*base*.5
    img=to_img(film(np.clip(col,0,1),grain=.03,halation=.2,vign=.5))
    img=img.resize((1920,int(1920*H2/W2)),Image.LANCZOS)
    t=(img.height-1080)//2;img.crop((0,t,1920,t+1080)).save(out)
for k,f in [(1.0,'fl_100.png')]: frame(k,out=f)
print('ok')
