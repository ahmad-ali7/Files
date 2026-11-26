from craft import *
M='../more/'
def crop16(path,y0f=None,x0=0,x1=None,y0=None):
    im=Image.open(path).convert('RGB');w=(x1 or im.width)-x0;h=int(w*9/16)
    if y0 is None: y0=int((im.height-h)*(y0f if y0f is not None else .5))
    return np.asarray(im.crop((x0,y0,x0+w,y0+h)).resize((W,H),Image.LANCZOS)).astype(np.float32)/255
yy,xx=np.mgrid[0:H,0:W]
# ---- 1 dream: moonlit arch, fairy as light in the window
a=crop16(M+'pex36077410.jpg',y0=1000)
lum=a.mean(2,keepdims=True)
o=(a*.55+lum*.45)*np.array([.75,.8,1.0])*.75
o+= (smooth(lum[...,0],.55,.95)[...,None])*np.array([.25,.22,.15])   # keep moon & lit curtain highlights
cx,cy=860,640
pts=[]
for i in range(420):
    t=rng.random()
    if t<.18: p=(cx+rng.normal(0,18),cy-170+rng.normal(0,20))          # head glow
    else:
        v=rng.random()**.7; p=(cx+rng.normal(0,25+v*120),cy-130+v*420+rng.normal(0,10))  # flowing form
    pts.append((p[0],p[1],.08+.5*rng.random()**3))
o,g=add_glow_points(o,pts,color=(.85,.9,1.0),core=1.3,halo=10,gain=1.3)
o+=gaussian_filter(np.exp(-(((xx-cx)/90)**2+((yy-(cy+20))/240)**2)).astype(np.float32),3)[...,None]*np.array([.18,.2,.26])
to_img(film(o,grain=.04,halation=.45,vign=.6)).save('out/bg_dream.png')
# ---- 2 twelve years: summer -> winter, same lake
s=crop16(M+'pex34948624.jpg',y0f=.55); w_=crop16(M+'pex29717097.jpg',y0f=.80)*.85
d=smooth(xx.astype(np.float32),930,990)[...,None]
o=s*(1-d)+w_*d
o=film(o*np.array([.95,.95,1.0]),grain=.025,halation=.15,vign=.45)
to_img(o).save('out/bg_years.png')
# ---- 3 stolen clothes: night stream + white silk on a rock + fleeing lights
st=crop16(M+'pex25961052.jpg',y0=1450)
n,sky=day_for_night(st,expo=.30)
silk=Image.open(M+'pex7946627.jpg').convert('RGB');W0,H0=silk.size
silk=silk.crop((int(W0*.30),int(H0*.05),int(W0*1.0),int(H0*.55))).resize((420,int(420*(H0*.5)/(W0*.7))),Image.LANCZOS)
sa=np.asarray(silk).astype(np.float32)/255
al=smooth(sa.mean(2),.10,.45)
hy,hx=np.mgrid[0:al.shape[0],0:al.shape[1]]
fe=smooth(hx/al.shape[1],0,.18)*smooth(1-hx/al.shape[1],0,.12)*smooth(hy/al.shape[0],0,.12)*smooth(1-hy/al.shape[0],0,.25)
al=gaussian_filter(al*fe,.8)
px,py=1440,560;hh,ww=al.shape;hh=min(hh,H-py)
lit=np.power(sa[:hh],1.3)*np.array([.75,.8,1.0])*.9
n[py:py+hh,px:px+ww]=n[py:py+hh,px:px+ww]*(1-al[:hh,...,None])+lit*al[:hh,...,None]
sh_=gaussian_filter(al[:hh],8);n[py+12:py+hh+12,px-10:px+ww-10]*=(1-.45*sh_[...,None])[:min(hh,H-py-12)]
pts=[(1460+rng.normal(0,60)+i*1.2,520-i*2.2+rng.normal(0,25),.2+.7*rng.random()) for i in range(220)]
n,g=add_glow_points(n,pts,gain=1.0)
to_img(film(n,grain=.035,halation=.35,vign=.55)).save('out/bg_clothes.png')
# ---- 6 mountain fairy belief: fog valley at night with lights hidden in the mist
f=np.asarray(Image.open(M+'../more/fog.png').convert('RGB')).astype(np.float32)/255 if False else np.asarray(Image.open(M+'fog.png').convert('RGB').resize((W,H))).astype(np.float32)/255
lum=f.mean(2,keepdims=True)
o=(f*.3+lum*.7)*np.array([.5,.6,.85])*.68
fogm=smooth(lum[...,0],.35,.65)*(yy>300)
pts=[]
for i in range(140):
    x,y=rng.integers(0,W),rng.integers(760,980)
    if fogm[y,x]>.4: pts.append((x,y,.15+.5*rng.random()))
o,g=add_glow_points(o,pts,core=2.6,halo=26,gain=1.6)
o=o*(1-fogm[...,None]*.0)+gaussian_filter(g,30)[...,None]*fogm[...,None]*np.array([.4,.35,.25])*3
to_img(film(o,grain=.035,halation=.4,vign=.55)).save('out/bg_belief.png')
# ---- 7 ending: tents by the lake at dusk -> night
t=crop16(M+'pex14064740.jpg',x0=0,x1=1950,y0=230)
n,sky=day_for_night(t,expo=.34,sky_top=(.03,.04,.10),sky_bot=(.10,.11,.18))
for (x,y) in [(1090,1010),(1320,1050),(1560,1040),(880,1030),(420,1000),(300,1010),(1750,1050)]:
    n+=np.exp(-(((xx-x)/16)**2+((yy-y)/10)**2))[...,None]*np.array([1,.75,.4])*.9
    n+=gaussian_filter(np.exp(-(((xx-x)/16)**2+((yy-y)/10)**2)),25)[...,None]*np.array([1,.6,.3])*4
pts=[(1100+rng.normal(0,260),330+rng.normal(0,90),.06+.25*rng.random()**3) for i in range(60)]
n,g=add_glow_points(n,pts,gain=.8)
to_img(film(n,grain=.035,halation=.35,vign=.55)).save('out/bg_ending.png')
print('ok')
