import re, json
t=open('script.txt').read()
sents=[s.strip() for s in re.split(r'(?<=[۔؟?])\s+', t.replace('\n',' ')) if s.strip()]
cues=[]
MAX=10
for s in sents:
    w=s.split()
    if len(w)<=MAX+2: cues.append(s); continue
    # split at commas into chunks, then merge small ones
    parts=[p.strip() for p in re.split(r'(?<=،)\s+', s)]
    cur=''
    for p in parts:
        if cur and len((cur+' '+p).split())>MAX: cues.append(cur); cur=p
        else: cur=(cur+' '+p).strip()
    if cur: cues.append(cur)
# hard-split any still too long
out=[]
for c in cues:
    w=c.split()
    while len(w)>14:
        k=len(w)//2 if len(w)<24 else 11
        out.append(' '.join(w[:k])); w=w[k:]
    out.append(' '.join(w))
json.dump(out,open('cues_ur.json','w'),ensure_ascii=False,indent=0)
for i,c in enumerate(out): print(i,len(c.split()),c)
print(len(out))
