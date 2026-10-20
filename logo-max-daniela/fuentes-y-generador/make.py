import sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
F='/tmp/claude-0/fonts/'
_c={}
def font(n):
    if n not in _c: _c[n]=TTFont(F+n)
    return _c[n]
def tp(fn,text,size,track=0):
    f=font(fn);gs=f.getGlyphSet();cmap=f.getBestCmap();upm=f['head'].unitsPerEm
    s=size/upm;x=0;pen=SVGPathPen(gs)
    for ch in text:
        g=cmap[ord(ch)]
        gs[g].draw(TransformPen(pen,(s,0,0,-s,x,0)))
        x+=gs[g].width*s+track
    return pen.getCommands(),x-track
def place(fn,text,size,x,y,fill,track=0,anchor='middle',extra=''):
    d,w=tp(fn,text,size,track)
    ox={'middle':x-w/2,'start':x,'end':x-w}[anchor]
    return f'<path transform="translate({ox:.1f} {y})" d="{d}" fill="{fill}" {extra}/>',w
OUT='/home/user/iarodada/logo-max-daniela/'
def save(name,w,h,body,title,defs=''):
    open(OUT+name,'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n<title>{title}</title>\n{defs}\n{body}\n</svg>\n')

# 7 Posavasos
cream='#F3E9D2';red='#7A1F2B';gold='#E0A63A'
b=[f'<circle cx="300" cy="300" r="290" fill="{red}"/>',
 f'<circle cx="300" cy="300" r="272" fill="none" stroke="{cream}" stroke-width="5"/>',
 f'<circle cx="300" cy="300" r="258" fill="none" stroke="{gold}" stroke-width="2"/>']
b.append(place('BebasNeue-Regular.ttf','BAR DE AMIGOS',34,300,142,gold,track=12)[0])
b.append(place('AlfaSlabOne-Regular.ttf','MAX',150,300,290,cream,track=6)[0])
b.append(place('AlfaSlabOne-Regular.ttf','DANIELS',92,300,372,cream,track=2)[0])
b.append(f'<line x1="100" y1="402" x2="155" y2="402" stroke="{gold}" stroke-width="3"/><line x1="445" y1="402" x2="500" y2="402" stroke="{gold}" stroke-width="3"/>')
b.append(place('BebasNeue-Regular.ttf','DESDE 1994',44,300,418,gold,track=8)[0])
b.append(place('BebasNeue-Regular.ttf','SIEMPRE ENTRE LOS NUESTROS',21,300,482,cream,track=5)[0])
save('7-posavasos.svg',600,600,'\n'.join(b),'Max Daniels - Posavasos')

# 8 La mesa
ink='#12302B';apr='#F0A35E';bone='#F6EFE3'
b=[f'<rect width="900" height="420" fill="{ink}"/>']
# mark: open ring + 4 friends + 1 amber candle
cx,cy,R=200,210,118
import math
a0,a1=math.radians(-62),math.radians(-28)   # gap = the door
x0,y0=cx+R*math.cos(a1),cy+R*math.sin(a1)
x1,y1=cx+R*math.cos(a0+2*math.pi),cy+R*math.sin(a0+2*math.pi)
b.append(f'<path d="M{x0:.1f} {y0:.1f} A{R} {R} 0 1 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{bone}" stroke-width="16" stroke-linecap="round"/>')
for dx,dy in [(-46,-46),(46,-46),(-46,46),(46,46)]:
    b.append(f'<circle cx="{cx+dx}" cy="{cy+dy}" r="21" fill="{bone}"/>')
b.append(f'<circle cx="{cx}" cy="{cy}" r="17" fill="{apr}"/>')
b.append(place('DMSerifDisplay-Regular.ttf','max',134,380,195,bone,track=-2,anchor='start')[0])
b.append(place('DMSerifDisplay-Regular.ttf','daniels',134,380,325,apr,track=-2,anchor='start')[0])
b.append(place('BebasNeue-Regular.ttf','BAR · DESDE 1994',30,384,364,bone,track=10,anchor='start',extra='opacity=".75"')[0])
save('8-la-mesa.svg',900,420,'\n'.join(b),'Max Daniels - La mesa')

# 9 Neon 90s
navy='#0E1020';pink='#FF4F8B';cyan='#5EE6E0'
defs='<defs><filter id="g" x="-20%" y="-40%" width="140%" height="180%"><feGaussianBlur stdDeviation="7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>'
b=[f'<rect width="800" height="500" fill="{navy}"/>','<g filter="url(#g)">',
 f'<rect x="50" y="50" width="700" height="400" rx="46" fill="none" stroke="{cyan}" stroke-width="6"/>']
b.append(place('Damion-Regular.ttf','Max Daniels',128,400,255,pink,extra='stroke="#FFD1E1" stroke-width="1.5"')[0])
b.append(f'<path d="M220 282 Q400 304 580 280" fill="none" stroke="{pink}" stroke-width="6" stroke-linecap="round"/>')
b.append(place('BebasNeue-Regular.ttf','DESDE 1994',50,400,380,cyan,track=14)[0])
b.append(f'<line x1="130" y1="366" x2="238" y2="366" stroke="{cyan}" stroke-width="4" stroke-linecap="round"/><line x1="562" y1="366" x2="670" y2="366" stroke="{cyan}" stroke-width="4" stroke-linecap="round"/>')
b.append(place('BebasNeue-Regular.ttf','BAR',34,400,128,cyan,track=16)[0])
b.append('</g>')
save('9-neon-90s.svg',800,500,'\n'.join(b),'Max Daniels - Neon 90s',defs)
