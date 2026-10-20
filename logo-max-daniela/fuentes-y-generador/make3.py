from make import *
import math
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
C='Cinzel[wght].ttf';P='PlayfairDisplay[wght].ttf';PI='PlayfairDisplay-Italic[wght].ttf';PO='PoiretOne-Regular.ttf'
gold='#C9A24B';champ='#E8D5A3'

def arc(fn,text,size,cx,cy,r,fill,track=0,top=True):
    f=font(fn);gs=f.getGlyphSet();cm=f.getBestCmap();s=size/f['head'].unitsPerEm
    ws=[gs[cm[ord(c)]].width*s for c in text];tot=sum(ws)+track*(len(text)-1)
    ang=tot/r;a=-ang/2;out=''
    for c,w in zip(text,ws):
        mid=a+(w/2)/r
        th=mid if top else -mid
        # position on circle measured from top (top) or bottom
        px=cx+r*math.sin(mid) if top else cx+r*math.sin(mid)
        py=cy-r*math.cos(mid) if top else cy+r*math.cos(mid)
        rot=math.degrees(mid) if top else -math.degrees(mid)
        pen=SVGPathPen(gs);gs[cm[ord(c)]].draw(TransformPen(pen,(s,0,0,-s,-w/2,0)))
        out+=f'<path transform="translate({px:.1f} {py:.1f}) rotate({rot:.1f})" d="{pen.getCommands()}" fill="{fill}"/>'
        step=(w+track)/r
        a+=step
    return out

# 13 Club
b=['<rect width="900" height="560" fill="#101010"/>',
 f'<rect x="40" y="40" width="820" height="480" fill="none" stroke="{gold}" stroke-width="3"/>',
 f'<rect x="54" y="54" width="792" height="452" fill="none" stroke="{gold}" stroke-width="1"/>']
b.append(place(C,'MAX DANIELS',80,450,290,champ,track=10)[0])
b.append(f'<line x1="170" y1="338" x2="410" y2="338" stroke="{gold}" stroke-width="2"/><line x1="490" y1="338" x2="730" y2="338" stroke="{gold}" stroke-width="2"/>')
b.append(f'<path d="M450 322 L466 338 L450 354 L434 338 Z" fill="{gold}"/>')
b.append(place(C,'COCKTAIL BAR',30,450,196,gold,track=14)[0])
b.append(place(C,'ESTABLECIDO EN 1994',26,450,408,gold,track=10)[0])
save('13-club-clasico.svg',900,560,'\n'.join(b),'Max Daniels - Club clásico')

# 14 Sello con monograma
b=['<rect width="640" height="640" fill="#F5EFE2"/>']
ink='#1B2A41';wine='#7A1F2B'
b.append(f'<circle cx="320" cy="320" r="290" fill="{ink}"/><circle cx="320" cy="320" r="274" fill="none" stroke="{champ}" stroke-width="3"/><circle cx="320" cy="320" r="190" fill="none" stroke="{champ}" stroke-width="2"/>')
b.append(arc(C,'MAX DANIELS',46,320,320,232,champ,track=10,top=True))
b.append(arc(C,'BAR · 1994',34,320,320,262,gold,track=10,top=False))
b.append(f'<circle cx="64" cy="320" r="6" fill="{gold}"/><circle cx="576" cy="320" r="6" fill="{gold}"/>')
b.append(place(PI,'M',180,246,386,champ,track=0)[0])
b.append(place(P,'D',180,396,386,gold,track=0)[0])
save('14-sello-monograma.svg',640,640,'\n'.join(b),'Max Daniels - Sello monograma')

# 15 Art deco
navy='#0F1B2D'
b=[f'<rect width="700" height="700" fill="{navy}"/>']
cx,cy=350,300
for i in range(13):
    a=math.radians(180+i*15)
    x2,y2=cx+200*math.cos(a),cy+200*math.sin(a)
    b.append(f'<line x1="{cx+62*math.cos(a):.1f}" y1="{cy+62*math.sin(a):.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{gold}" stroke-width="{4 if i%2==0 else 2}"/>')
for r in (200,176):
    b.append(f'<path d="M{cx-r} {cy} A{r} {r} 0 0 1 {cx+r} {cy}" fill="none" stroke="{gold}" stroke-width="{4 if r==200 else 1.5}"/>')
b.append(f'<path d="M{cx-62} {cy} A62 62 0 0 1 {cx+62} {cy} Z" fill="{gold}"/>')
b.append(f'<line x1="130" y1="{cy}" x2="570" y2="{cy}" stroke="{gold}" stroke-width="4"/>')
b.append(place(PO,'MAX DANIELS',84,350,430,champ,track=8,extra=f'stroke="{champ}" stroke-width="2.2"')[0])
b.append(f'<line x1="150" y1="470" x2="550" y2="470" stroke="{gold}" stroke-width="2"/>')
b.append(place(C,'BAR  ·  1994',32,350,520,gold,track=16)[0])
save('15-art-deco.svg',700,700,'\n'.join(b),'Max Daniels - Art déco')
