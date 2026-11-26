import json, re, textwrap
rows=[l.split('\t') for l in open('cues.tsv').read().strip().split('\n')]
T=json.load(open('times.json'))
UR=[('K Two','K2'),('Camp Three','Camp 3'),('Camp Four','Camp 4'),('آٹھ ہزار میٹر','8,000 میٹر'),('سترہ سو روپے','1,700 روپے'),
('دو ہزار تئیس','2023'),('دو ہزار چوبیس','2024'),('دو ہزار پچیس','2025'),('چھبیس اور ستائیس جولائی','26 اور 27 جولائی'),
('تیس سے اسّی','30 سے 80'),('تمام چودہ','تمام 14'),('بانوے دنوں','92 دنوں'),('ستر صفحوں','70 صفحوں'),('دو لاکھ روپے','2 لاکھ روپے'),
('بیس ہزار ڈالر','20,000 ڈالر'),('ایک لاکھ ستر ہزار ڈالر','1,70,000 ڈالر'),('بیس سے تیس لاکھ','20 سے 30 لاکھ'),
('دس سے گیارہ بجے','10 سے 11 بجے'),('تین سے پانچ لوگ','3 سے 5 لوگ')]
def disp_ur(s):
    for a,b in UR: s=s.replace(a,b)
    return s
lat=re.compile(r'^[A-Za-z]')
n=len(rows); st=[0]*n; en=[0]*n
for i in range(n):
    a,b,q=T[i]
    st[i]=a-0.12
    if i and lat.match(rows[i][0]): st[i]=max(T[i-1][1]+0.08, a-0.7)
    if i: st[i]=max(st[i], en[i-1]+0.02) if en[i-1] else st[i]
    en[i]=b+0.35
    if i+1<n:
        nxt=T[i+1][0]-0.12
        if lat.match(rows[i+1][0]): nxt=max(b+0.08, T[i+1][0]-0.7)
        en[i]=min(en[i], nxt-0.02) if nxt-b<1.2 else en[i]
    if lat.match(rows[i][0][-12:].split()[-1] if False else 'x'): pass
for i in range(n):
    if en[i]-st[i]<1.0:
        en[i]=st[i]+1.0
        if i+1<n and st[i+1]<en[i]+0.02: st[i+1]=en[i]+0.02
    if i+1<n and en[i]>st[i+1]-0.02: en[i]=st[i+1]-0.02
st[0]=max(0,st[0])
def ts(x):
    ms=int(round(x*1000)); return '%02d:%02d:%02d,%03d'%(ms//3600000,ms//60000%60,ms//1000%60,ms%1000)
def wrap(s,w):
    return '\n'.join(textwrap.wrap(s,w)) if len(s)>w else s
for lang,col,w,fn in [('ur',0,48,disp_ur),('en',1,44,lambda s:s),('hi',2,44,lambda s:s)]:
    out=[]
    for i,r in enumerate(rows):
        out.append(f'{i+1}\n{ts(st[i])} --> {ts(en[i])}\n{wrap(fn(r[col]),w)}\n')
    open(f'K2_Hassan_{lang}.srt','w',encoding='utf-8').write('\n'.join(out))
json.dump([st,en],open('final_times.json','w'))
# checks
ov=[i for i in range(n-1) if en[i]>st[i+1]]; short=[i for i in range(n) if en[i]-st[i]<0.99]
cps=[(i,round(len(rows[i][1])/(en[i]-st[i]),1)) for i in range(n) if len(rows[i][1])/(en[i]-st[i])>22]
print('overlaps',ov,'short',short); print('fast EN lines (>22 chars/s):',cps)
for k,name in [(0,'Intro'),(22,'Act 1'),(68,'Act 2'),(115,'Act 3'),(162,'Summit')]:
    print(name, '%d:%02d'%(st[k]//60, st[k]%60))
