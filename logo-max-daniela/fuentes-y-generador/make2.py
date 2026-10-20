from make import *
T='TitanOne-Regular.ttf';B='BebasNeue-Regular.ttf'
dark='#2B1B17'

def shadow(text,size,x,y,fill,sh,off=7,track=0,fn=T,sw=0):
    s=place(fn,text,size,x+off,y+off,sh,track)[0]
    m=place(fn,text,size,x,y,fill,track,extra=f'stroke="{dark}" stroke-width="{sw}" stroke-linejoin="round" paint-order="stroke"' if sw else '')[0]
    return s+m

# 10 Brindis con cara
b=['<rect width="700" height="700" fill="#FFC93C"/>']
for cx,cy,r in [(120,150,26),(590,120,18),(560,230,10)]:
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FF6F91" stroke="{dark}" stroke-width="6"/>')
def glass(rot,cx,drink,face):
    g=f'<g transform="rotate({rot} {cx} 330)" stroke="{dark}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round">'
    g+=f'<path d="M{cx-78} 200 H{cx+78} L{cx+64} 410 Q{cx+62} 428 {cx+44} 428 H{cx-44} Q{cx-62} 428 {cx-64} 410 Z" fill="#FFF6E5"/>'
    g+=f'<path d="M{cx-73} 268 H{cx+73} L{cx+64} 410 Q{cx+62} 428 {cx+44} 428 H{cx-44} Q{cx-62} 428 {cx-64} 410 Z" fill="{drink}"/>'
    g+=f'<path d="M{cx-73} 268 H{cx+73}" fill="none"/>'
    g+=f'<circle cx="{cx-26}" cy="318" r="9" fill="{dark}" stroke="none"/><circle cx="{cx+26}" cy="318" r="9" fill="{dark}" stroke="none"/>'
    g+=f'<circle cx="{cx-44}" cy="346" r="9" fill="#FF6F91" stroke="none"/><circle cx="{cx+44}" cy="346" r="9" fill="#FF6F91" stroke="none"/>'
    g+= f'<path d="M{cx-18} 342 Q{cx} 372 {cx+18} 342 Z" fill="{dark}"/>' if face=='open' else f'<path d="M{cx-18} 344 Q{cx} 366 {cx+18} 344" fill="none"/>'
    g+='</g>'
    return g
b.append(glass(14,225,'#FF8A3D','open'));b.append(glass(-14,475,'#4ECDC4','smile'))
b.append(f'<g stroke="{dark}" stroke-width="9" stroke-linecap="round"><path d="M350 130 V86"/><path d="M308 148 L286 110"/><path d="M392 148 L414 110"/></g>')
b.append(f'<g fill="#fff" stroke="{dark}" stroke-width="6"><circle cx="350" cy="205" r="12"/><circle cx="318" cy="228" r="7"/><circle cx="382" cy="228" r="7"/></g>')
b.append(shadow('MAX DANIELS',80,350,570,'#FFF6E5',dark,off=8,track=2,sw=10))
b.append(f'<rect x="215" y="610" width="270" height="52" rx="26" fill="{dark}"/>')
b.append(place(B,'DESDE 1994 · BAR DE AMIGOS'.replace(' · BAR DE AMIGOS',''),38,350,650,'#FFC93C',track=10)[0])
save('10-brindis-con-cara.svg',700,700,'\n'.join(b),'Max Daniels - Brindis con cara')

# 11 Mascota aceituna (sticker)
b=['<rect width="700" height="700" fill="#2EC4B6"/>']
st=f'stroke="{dark}" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"'
mascot=f'''<g>
 <path d="M345 90 L395 330" fill="none" stroke="#fff" stroke-width="34" stroke-linecap="round"/>
 <path d="M345 90 L395 330" fill="none" {st}/>
 <ellipse cx="350" cy="350" rx="150" ry="170" fill="#9BD13D" {st}/>
 <path d="M240 255 Q232 330 250 390" fill="none" stroke="#C6EF70" stroke-width="16" stroke-linecap="round"/>
 <circle cx="350" cy="198" r="42" fill="#E63946" {st}/>
 <path d="M338 192 Q350 178 366 188" fill="none" stroke="#FF8A93" stroke-width="9" stroke-linecap="round"/>
 <circle cx="305" cy="330" r="23" fill="#fff" {st}/><circle cx="395" cy="330" r="23" fill="#fff" {st}/>
 <circle cx="311" cy="334" r="10" fill="{dark}"/><circle cx="401" cy="334" r="10" fill="{dark}"/>
 <path d="M280 300 Q305 284 328 296" fill="none" {st}/><path d="M372 296 Q395 284 420 300" fill="none" {st}/>
 <path d="M290 395 Q350 470 410 395 Z" fill="{dark}" {st}/>
 <path d="M322 428 Q350 462 378 428 Q350 414 322 428Z" fill="#FF6F91"/>
 <circle cx="270" cy="378" r="14" fill="#FF6F91" opacity=".8"/><circle cx="430" cy="378" r="14" fill="#FF6F91" opacity=".8"/>
</g>'''
b.append('<g transform="translate(35 0) scale(.9)">'+mascot+'</g>')
b.append(f'<g transform="rotate(-5 350 580)">'+shadow('MAX DANIELS',80,350,590,'#fff',dark,off=7,sw=12)+'</g>')
b.append(f'<g transform="rotate(-5 350 640)">'+place(B,'DESDE 1994',44,350,652,dark,track=12)[0]+'</g>')
save('11-mascota-aceituna.svg',700,700,'\n'.join(b),'Max Daniels - Mascota aceituna')

# 12 Memphis 90s
b=['<rect width="700" height="700" fill="#FFF3DF"/>']
b.append(f'<circle cx="590" cy="110" r="70" fill="#FF6F91" stroke="{dark}" stroke-width="7"/>')
b.append(f'<path d="M80 150 L170 150 L125 70 Z" fill="#4ECDC4" stroke="{dark}" stroke-width="7" stroke-linejoin="round"/>')
b.append(f'<path d="M60 560 q25 -40 50 0 t50 0 t50 0 t50 0" fill="none" stroke="{dark}" stroke-width="9" stroke-linecap="round"/>')
b.append(f'<path d="M470 600 q25 -40 50 0 t50 0 t50 0" fill="none" stroke="#FF6F91" stroke-width="9" stroke-linecap="round"/>')
for x,y,c in [(160,260,'#FFC93C'),(560,300,'#4ECDC4'),(90,400,'#FF6F91'),(620,470,'#FFC93C'),(400,60,'#2B1B17'),(480,70,'#4ECDC4')]:
    b.append(f'<circle cx="{x}" cy="{y}" r="11" fill="{c}"/>')
b.append(f'<rect x="240" y="40" width="56" height="56" fill="#FFC93C" stroke="{dark}" stroke-width="7" transform="rotate(18 268 68)"/>')
b.append(f'<g transform="rotate(-7 350 350)">')
b.append(shadow('MAX',190,350,300,'#FF6F91','#4ECDC4',off=12,sw=10))
b.append(shadow('DANIELS',118,350,430,'#FFC93C',dark,off=9,sw=10))
b.append(f'<rect x="105" y="470" width="490" height="62" rx="31" fill="{dark}"/>')
b.append(place(B,'BAR · DESDE 1994',40,350,515,'#FFF3DF',track=10)[0])
b.append('</g>')
save('12-memphis-90s.svg',700,700,'\n'.join(b),'Max Daniels - Memphis 90s')
