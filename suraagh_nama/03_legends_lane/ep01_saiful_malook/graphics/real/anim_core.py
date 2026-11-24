import numpy as np, subprocess, os
from PIL import Image
from scipy.ndimage import gaussian_filter, map_coordinates
W,H=1920,1080
def cam_crop(big, t, dur, z0=1.0, z1=1.07, dx=0, dy=0):
    """slow push-in on an oversized plate (big is HxWx3 float, >= 1.1x frame)."""
    u=t/dur; u=u*u*(3-2*u)
    z=z0+(z1-z0)*u
    bh,bw=big.shape[:2]
    cw,ch=W/z*(bw/W/1.1), H/z*(bh/H/1.1)
    cx=bw/2+dx*u; cy=bh/2+dy*u
    # handheld micro-drift
    cx+=np.sin(t*.7)*3+np.sin(t*1.9)*1.2; cy+=np.cos(t*.5)*2+np.sin(t*2.3)*.8
    x0,y0=cx-cw/2,cy-ch/2
    ys=y0+np.arange(H)*(ch/H); xs=x0+np.arange(W)*(cw/W)
    out=np.empty((H,W,3),np.float32)
    # bilinear sample via separable indexing
    yi=np.clip(ys,0,bh-1.001); xi=np.clip(xs,0,bw-1.001)
    y0i=yi.astype(int); x0i=xi.astype(int); fy=(yi-y0i)[:,None,None]; fx=(xi-x0i)[None,:,None]
    a=big[y0i][:,x0i];b=big[y0i][:,x0i+1];c=big[y0i+1][:,x0i];d=big[y0i+1][:,x0i+1]
    out=(a*(1-fx)+b*fx)*(1-fy)+(c*(1-fx)+d*fx)*fy
    return out
def glow(out, pts, color=(1,.86,.58), core=1.6, halo=14, gain=1.0):
    acc=np.zeros((H,W),np.float32)
    for x,y,a in pts:
        xi,yi=int(x),int(y)
        if 0<=xi<W and 0<=yi<H: acc[yi,xi]+=a
    c=gaussian_filter(acc,core)*core*core*6.3; h=gaussian_filter(acc,halo)*halo*halo*6.3*.04
    g=c+h
    return out+g[...,None]*np.array(color)*gain, g
GR=np.random.default_rng(5).standard_normal((8,H,W)).astype(np.float32)
GR=np.stack([gaussian_filter(g,.7) for g in GR])
VIG=None
def film(out, k, grain=.035, vign=.55, halation=.3):
    global VIG
    if VIG is None:
        yy,xx=np.mgrid[0:H,0:W];d=np.sqrt(((xx-W/2)/(W/2))**2+((yy-H/2)/(H/2))**2)
        s=np.clip((d-.55)/(1.45-.55),0,1);VIG=(1-vign*s*s*(3-2*s)).astype(np.float32)
    lum=out.mean(2);hl=gaussian_filter(np.clip(lum-.55,0,None),18)
    out=out+hl[...,None]*np.array([1,.45,.25])*halation
    out=out*VIG[...,None]
    out=out+GR[k%8][...,None]*grain*(.4+.6*np.sqrt(np.clip(out.mean(2,keepdims=True),0,1)))
    return np.clip(out,0,1)
class Writer:
    def __init__(self,path,fps=25):
        self.p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(fps),'-i','-','-c:v','libx264','-crf','16','-preset','medium','-pix_fmt','yuv420p','-movflags','+faststart',path],stdin=subprocess.PIPE)
    def add(self,f): self.p.stdin.write((np.clip(f,0,1)*255+.5).astype(np.uint8).tobytes())
    def close(self): self.p.stdin.close(); self.p.wait()
