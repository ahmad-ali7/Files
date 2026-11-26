import math,os,subprocess,io,json
import numpy as np
from PIL import Image
LAT0,LAT1,LON0,LON1=34.855,34.935,73.615,73.745
def tx(lon,z): return (lon+180)/360*2**z
def ty(lat,z): r=math.radians(lat); return (1-math.log(math.tan(r)+1/math.cos(r))/math.pi)/2*2**z
def fetch(url,path):
    if not os.path.exists(path) or os.path.getsize(path)<100:
        subprocess.run(['curl','-s','-A','Mozilla/5.0','-o',path,url])
    return path
def mosaic(z,kind):
    x0,x1=int(tx(LON0,z)),int(tx(LON1,z)); y0,y1=int(ty(LAT1,z)),int(ty(LAT0,z))
    rows=[]
    for y in range(y0,y1+1):
        row=[]
        for x in range(x0,x1+1):
            if kind=='dem': p=fetch(f"https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png",f"tiles/d{z}_{x}_{y}.png")
            else: p=fetch(f"https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless_3857/default/g/{z}/{y}/{x}.jpg",f"tiles/s{z}_{x}_{y}.jpg")
            row.append(np.asarray(Image.open(p).convert('RGB')))
        rows.append(np.concatenate(row,1))
    m=np.concatenate(rows,0)
    # crop to bbox
    px0=(tx(LON0,z)-x0)*256; px1=(tx(LON1,z)-x0)*256; py0=(ty(LAT1,z)-y0)*256; py1=(ty(LAT0,z)-y0)*256
    return m[int(py0):int(py1),int(px0):int(px1)]
d=mosaic(13,'dem').astype(np.float32)
elev=d[...,0]*256+d[...,1]+d[...,2]/256-32768
s=mosaic(14,'sat')
print('dem',elev.shape,elev.min(),elev.max(),'sat',s.shape)
np.save('elev.npy',elev); Image.fromarray(s).save('sat.jpg',quality=92)
mpp=2*math.pi*6378137*math.cos(math.radians((LAT0+LAT1)/2))/(256*2**13)
json.dump({'bbox':[LAT0,LAT1,LON0,LON1],'mpp':mpp,'shape':elev.shape},open('meta.json','w'))
print('m/px',mpp)
