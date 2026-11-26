from craft import *
img=load('plate_wide.png')
RIDGE=[(0,10),(200,30),(330,35),(450,90),(560,130),(700,170),(900,230),(1000,262),(1100,255),(1200,245),(1300,250),(1450,275),(1530,270),(1600,300),(1750,330),(1920,390)]
out,sky=day_for_night(img,ridge=RIDGE)
out=stars(out,sky)
yy,xx=np.mgrid[0:H,0:W]
mg=np.exp(-(((xx-1800)/800)**2+((yy+150)/520)**2))
out+= (mg*sky)[...,None]*np.array([.16,.18,.24])
r,g,b=img[...,0],img[...,1],img[...,2]
water=smooth(g-r,.06,.22)*smooth(b-r,.06,.22)*(yy>560)
water=gaussian_filter(water.astype(np.float32),2)
# water reflects the night sky a little (lighter than land)
out+= water[...,None]*np.array([.025,.035,.06])
mp=np.exp(-((xx-1450)/160)**2)*water*smooth(yy,600,700)
out+= gaussian_filter(mp,(1,6))[...,None]*np.array([.10,.12,.16])
pts=[]
P0,P1,P2,P3=np.array([180,40]),np.array([760,-80]),np.array([1500,260]),np.array([1060,792])
for i in range(360):
    u=rng.random()**.8
    a=1-u;p=a**3*P0+3*a*a*u*P1+3*a*u*u*P2+u**3*P3
    p=p+rng.normal(0,(1-u)*85+10,2)
    br=rng.random()**2.2
    pts.append((p[0],p[1],.15+.85*br))
for i in range(80):
    pts.append((1060+rng.normal(0,120),795+rng.normal(0,6),.25+.6*rng.random()))
out,glow=add_glow_points(out,pts,gain=1.1)
out=reflect_lights(out,glow,water,horizon_y=797,strength=.5)
out=film(out)
to_img(out).save('out/R04_fairies_real.png')
