import sys; sys.path.insert(0,'.')
from craft import load, day_for_night, stars, smooth
from anim_core import *
# base plate (night lake, no lights) at 1.1x
img=load('plate_wide.png')
RIDGE=[(0,10),(200,30),(330,35),(450,90),(560,130),(700,170),(900,230),(1000,262),(1100,255),(1200,245),(1300,250),(1450,275),(1530,270),(1600,300),(1750,330),(1920,390)]
base,sky=day_for_night(img,ridge=RIDGE); base=stars(base,sky)
yy,xx=np.mgrid[0:H,0:W]
base+= (np.exp(-(((xx-1800)/800)**2+((yy+150)/520)**2))*sky)[...,None]*np.array([.16,.18,.24])
r,g,b=img[...,0],img[...,1],img[...,2]
water=gaussian_filter((smooth(g-r,.06,.22)*smooth(b-r,.06,.22)*(yy>560)).astype(np.float32),2)
base+=water[...,None]*np.array([.025,.035,.06])
big=np.asarray(Image.fromarray((np.clip(base,0,1)*255).astype(np.uint8)).resize((int(W*1.1),int(H*1.1)),Image.LANCZOS)).astype(np.float32)/255
rng=np.random.default_rng(3)
N=360; delay=rng.random(N)*5.0; off=rng.normal(0,1,(N,2)); spd=.13+rng.random(N)*.06; tw=rng.random(N)*6.28; br=.15+.85*rng.random(N)**2.2
P0,P1,P2,P3=np.array([180,40]),np.array([760,-80]),np.array([1500,260]),np.array([1060,792])
pool=np.stack([1060+rng.normal(0,120,N),795+rng.normal(0,6,N)],1)
DUR=12;FPS=25;w=Writer('clips/R04_fairies.mp4',FPS)
for k in range(DUR*FPS):
    t=k/FPS
    f=cam_crop(big,t,DUR,1.0,1.06,dx=-40,dy=20)
    pts=[]
    for i in range(N):
        u=(t-delay[i])*spd[i]
        if u<=0: continue
        if u<1:
            a=1-u;p=a**3*P0+3*a*a*u*P1+3*a*u*u*P2+u**3*P3
            p=p+off[i]*((1-u)*85+10)+np.array([np.sin(t*1.3+tw[i])*12*(1-u),0])
            pts.append((p[0],p[1],br[i]*(.75+.25*np.sin(t*5+tw[i]))))
        else:
            q=pool[i];pts.append((q[0]+np.sin(t*.8+tw[i])*6,q[1],(.25+.6*br[i])*(.6+.4*np.sin(t*3+tw[i]))))
    f,gl=glow(f,pts,gain=1.1)
    # reflection on water
    refl=np.zeros_like(gl);hy=797;n=min(hy,H-hy);refl[hy:hy+n]=gl[:hy][::-1][:n]
    refl=gaussian_filter(refl,(6,1.5))*(np.sin(np.arange(H)[:,None]*.9+t*4)*.5+.5)
    f=f+(refl*water)[...,None]*np.array([1,.82,.55])*.5
    w.add(film(f,k))
w.close();print('done')
