import sys, json
from faster_whisper import WhisperModel
m = WhisperModel(sys.argv[2], device="cpu", compute_type="int8", cpu_threads=4)
import wave, numpy as np
wf=wave.open(sys.argv[1]); a=np.frombuffer(wf.readframes(wf.getnframes()),dtype=np.int16).astype(np.float32)/32768
segs, info = m.transcribe(a, language="ur", word_timestamps=True, beam_size=5, vad_filter=False)
out=[]
for s in segs:
    out.append({"s":s.start,"e":s.end,"t":s.text,"w":[[w.start,w.end,w.word] for w in s.words]})
    print(round(s.start,1), s.text, flush=True)
json.dump(out, open(sys.argv[3],"w"), ensure_ascii=False)
print("DONE")
