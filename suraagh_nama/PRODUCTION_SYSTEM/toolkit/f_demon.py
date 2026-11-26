from craft import *
from PIL import ImageDraw
img=load('plate_moraine.png')
RIDGE=[(0,30),(100,60),(160,92),(240,144),(320,185),(400,223),(480,244),(560,279),(640,320),(680,330),(720,325),(800,318),(880,322),(960,345),(1000,350),(1040,352),(1100,365),(1160,385),(1240,415),(1300,440),(1360,465),(1440,465),(1600,460),(1760,480),(1920,494)]
ground,sky=day_for_night(img,ridge=RIDGE,expo=.24)
# storm sky (real photo), mapped behind the ridge
st=Image.open('../storm/pex12372779.jpg').convert('RGB')
st=st.crop((0,0,st.width,int(st.height*.80))).resize((W,620),Image.LANCZOS)
S=np.zeros((H,W,3),np.float32);S[:620]=np.asarray(st).astype(np.float32)/255
S[620:]=S[619:620]
bo=Image.open('../storm/pxb1455285.jpg').convert('RGB');bo=bo.crop((420,120,1280,720)).resize((1100,770),Image.LANCZOS)
B=np.zeros((H,W,3),np.float32);B[0:770,820:1920]=np.asarray(bo).astype(np.float32)/255
bl=np.clip((B.mean(2,keepdims=True)-.45)*2.2,0,1)
ramp=np.clip((np.arange(W)-820)/260,0,1)[None,:,None]*np.clip((770-np.arange(H))/200,0,1)[:,None,None]
bl=bl*ramp
S=1-(1-S)*(1-np.clip(B*bl*1.6,0,1))
S=S*np.array([.85,.85,1.0])
lum=S.mean(2)
# ---- the demon: a vast shape inside the cloud, only readable where lightning lights the cloud from behind
dm=Image.new('L',(W,H),0);d=ImageDraw.Draw(dm)
cx,cy=1420,250
d.ellipse((cx-110,cy-140,cx+110,cy+80),fill=255)                      # head
d.polygon([(cx-95,cy-110),(cx-175,cy-290),(cx-60,cy-140)],fill=255)    # left horn
d.polygon([(cx+95,cy-110),(cx+190,cy-280),(cx+60,cy-140)],fill=255)    # right horn
d.polygon([(cx-520,cy+330),(cx-260,cy+80),(cx,cy+60),(cx+260,cy+80),(cx+560,cy+340)],fill=255)  # shoulders
dm=np.asarray(dm).astype(np.float32)/255
rr=np.random.default_rng(11)
N=sum(gaussian_filter(rr.random((H,W)).astype(np.float32),sg)*w for sg,w in ((40,1.0),(14,.6),(5,.35)))
N=(N-N.mean())/N.std()
soft=gaussian_filter(dm,22)
dm2=smooth(soft+N*.16,.38,.62)                     # cloud-broken silhouette
dmask=gaussian_filter(dm2,6)
rim=np.clip(gaussian_filter(dm2,4)-gaussian_filter(dm2,16),0,1)
ctex=np.clip(gaussian_filter(lum,2)/(lum.max()+1e-6),0,1)
light=gaussian_filter(np.clip(lum-.42,0,1),25)*3
S=S*(1-.6*dmask[...,None])
S+=(rim*np.clip(light*1.6+.08,0,1)*(.5+ctex))[...,None]*np.array([.62,.58,.85])*.9
# eyes: two faint embers deep in the cloud
yy,xx=np.mgrid[0:H,0:W]
for ex in (cx-48,cx+48):
    e=np.exp(-(((xx-ex)/9)**2+((yy-(cy-10))/5)**2))
    S+=e[...,None]*np.array([1.0,.35,.12])*.5
    S+=gaussian_filter(e,14)[...,None]*np.array([1.0,.3,.1])*2.5
out=ground*(1-sky[...,None])+S*sky[...,None]
# lightning flash lights the land a little (cool, from above)
flash=.35*gaussian_filter(np.clip(lum-.4,0,1),60)[...,None]
out+= (img.mean(2,keepdims=True)*.5)*np.clip(flash*4,0,.5)*np.array([.6,.6,.85])*(1-sky[...,None])
# lake catches the storm: faint purple sheen on water
r,g,b=img[...,0],img[...,1],img[...,2]
water=gaussian_filter((smooth(g-r,.06,.22)*smooth(b-r,.06,.22)*(yy>500)).astype(np.float32),2)
out+=water[...,None]*np.array([.07,.05,.11])
out=film(out,grain=.04,halation=.4,vign=.6)
to_img(out).save('out/bg_demon.png');print('ok')
