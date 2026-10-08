#!/usr/bin/env python3
"""Genera los PDF desde las fuentes Markdown y las evidencias; no ejecuta pruebas."""
from pathlib import Path
import csv,re,html,json
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, Flowable, KeepInFrame
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as PILImage
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pdf';OUT.mkdir(parents=True,exist_ok=True)
FONT=Path('/System/Library/Fonts/Supplemental')
for name,file in [('Text','Arial.ttf'),('TextBold','Arial Bold.ttf'),('TextItalic','Arial Italic.ttf')]:
 if (FONT/file).exists():pdfmetrics.registerFont(TTFont(name,str(FONT/file)))
 else: raise RuntimeError('Configurar fuentes Arial del sistema para reproducir la maquetación.')
pdfmetrics.registerFontFamily('Text',normal='Text',bold='TextBold',italic='TextItalic',boldItalic='TextBold')
NAVY=colors.HexColor('#10263b');CYAN=colors.HexColor('#00a8bd');GRAY=colors.HexColor('#526577');LIGHT=colors.HexColor('#edf4f7')
W,H=A4;CW=W-92
styles={
 'body':ParagraphStyle('body',fontName='Text',fontSize=10,leading=14.4,textColor=NAVY,spaceAfter=8,splitLongWords=True),
 'small':ParagraphStyle('small',fontName='Text',fontSize=8.1,leading=11,textColor=GRAY,spaceAfter=5,splitLongWords=True),
 'cell':ParagraphStyle('cell',fontName='Text',fontSize=8.5,leading=11.5,textColor=NAVY,spaceAfter=0,splitLongWords=True),
 'h1':ParagraphStyle('h1',fontName='TextBold',fontSize=22,leading=27,textColor=NAVY,spaceAfter=18,keepWithNext=True),
 'h2':ParagraphStyle('h2',fontName='TextBold',fontSize=14,leading=18,textColor=NAVY,spaceBefore=13,spaceAfter=9,keepWithNext=True),
 'h3':ParagraphStyle('h3',fontName='TextBold',fontSize=11,leading=15,textColor=CYAN,spaceBefore=10,spaceAfter=6,keepWithNext=True),
 'code':ParagraphStyle('code',fontName='Courier',fontSize=8,leading=11,backColor=LIGHT,borderPadding=8,spaceBefore=4,spaceAfter=12,splitLongWords=True),
}
EVS=list(csv.DictReader((ROOT/'evidencias/indice.csv').open())); EVM={x['id']:x for x in EVS}
PAGES={}
FIGURES={}
def inline(s,links=True):
 s=s.replace('—','-').replace('–','-').replace('\u2011','-').replace('→',' > ')
 s=html.escape(s)
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1',s)
 s=re.sub(r'`([^`]+)`',r'<font name="Courier">\1</font>',s)
 s=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',s)
 if links:s=re.sub(r'EV-[A-Z]+-\d{3}',lambda m:f'<a href="#{m[0]}" color="#007d91">{m[0]}</a>' if m[0] in EVM else m[0],s)
 return s

def para(s,sty='body',links=True):return Paragraph(inline(s,links),styles[sty])
def footer(c,d):
 c.saveState();c.setStrokeColor(CYAN);c.setLineWidth(1);c.line(46,H-38,W-46,H-38)
 c.setFillColor(GRAY);c.setFont('Text',8);c.drawString(46,H-29,'MNZHACK  /  DC-1  /  PTES');c.drawRightString(W-46,H-29,'07 OCT 2026  |  v0.3')
 c.line(46,38,W-46,38);c.drawString(46,25,'LABORATORIO ACADÉMICO  ·  USO RESTRINGIDO');c.drawRightString(W-46,25,str(d.page));c.restoreState()
class Doc(SimpleDocTemplate):
 def afterFlowable(self,f):
  if isinstance(f,Paragraph) and getattr(f,'toc_title',None):
   key=f.toc_key;self.canv.bookmarkPage(key);self.canv.addOutlineEntry(f.toc_title,key,0,False)
   self.notify('TOCEntry',(0,f.toc_title,self.page,key))
  if isinstance(f,Paragraph) and getattr(f,'ev_id',None):
   self.canv.bookmarkPage(f.ev_id);PAGES[f.ev_id]=self.page

def heading(title,key):
 p=para(title,'h1',False);p.toc_title=title;p.toc_key=key;return p
class Diagram(Flowable):
 def __init__(self,kind):Flowable.__init__(self);self.kind=kind;self.width=CW;self.height=300 if kind=='attack' else 280
 def draw(self):
  c=self.canv
  if self.kind=='attack':
   sets=[('LAB-JACD',['ARP / HTTP Drupal','SQLi > sesión www-data','Enumeración local / find SUID','EUID 0 > bandera final'],['EV-JACD-001 / 016','EV-JACD-014 / 003 / 009','EV-JACD-007 / 008','EV-JACD-004 / 010']),('LAB-DQH',['ARP / SSH password','Credencial > sesión flag4','Enumeración local / find SUID','EUID 0 > bandera final'],['EV-DQH-001 / 006','EV-DQH-008 / 009','EV-DQH-011','EV-DQH-011 / 012'])]
   for col,(title,steps,refs) in enumerate(sets):
    x=col*(CW/2+5);bw=CW/2-10;c.setFillColor(NAVY);c.setFont('TextBold',11);c.drawString(x,self.height-15,title)
    for j,(step,ref) in enumerate(zip(steps,refs)):
     y=self.height-78-j*65;c.setFillColor(LIGHT);c.roundRect(x,y,bw,49,5,fill=1,stroke=0)
     c.setFillColor(NAVY);c.setFont('TextBold',9);c.drawString(x+10,y+30,step);c.setFont('Text',8);c.drawString(x+10,y+13,ref)
     if j<3:c.setStrokeColor(CYAN);c.line(x+bw/2,y-2,x+bw/2,y-13);c.line(x+bw/2,y-13,x+bw/2-3,y-9);c.line(x+bw/2,y-13,x+bw/2+3,y-9)
  else:
   rows=[('JACD','192.168.18.129','192.168.18.130','MAC ...55:ea:9d'),('DQH','192.168.18.129','192.168.18.130','MAC ...45:c1:6e'),('EJVA','192.168.81.129','192.168.81.130','MAC ...79:c1:61'),('JDOG','Parrot / IP no acreditada','192.168.128.4','Objetivo candidato UTM')]
   for j,(name,src,dst,note) in enumerate(rows):
    y=self.height-65-j*65
    c.setFillColor(NAVY);c.setFont('TextBold',9);c.drawString(0,y+35,name)
    for x,txt,label in [(48,src,'ATACANTE'),(286,dst,'OBJETIVO')]:
     c.setFillColor(LIGHT);c.roundRect(x,y,206,50,4,fill=1,stroke=0);c.setFillColor(GRAY);c.setFont('Text',7);c.drawString(x+8,y+36,label);c.setFont('TextBold',9);c.setFillColor(NAVY);c.drawString(x+8,y+19,txt)
    c.setStrokeColor(CYAN);c.line(258,y+24,281,y+24);c.line(281,y+24,277,y+27);c.setFont('Text',7);c.setFillColor(GRAY);c.drawString(294,y+6,note)

def markdown(text,links=True):
 lines=text.splitlines();out=[];i=0
 while i<len(lines):
  line=lines[i].strip()
  if not line:i+=1;continue
  if line.startswith('```'):
   lang=line[3:];code=[];i+=1
   while i<len(lines) and not lines[i].startswith('```'):code.append(lines[i]);i+=1
   i+=1
   if lang=='mermaid':out.append(Diagram('attack'))
   else:out.append(Paragraph('<br/>'.join(html.escape(x).replace(' ','&#160;') for x in code),styles['code']))
   continue
  if line.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    cells=lines[i].strip().strip('|').split('|');i+=1
    if all(re.fullmatch(r'\s*:?-+:?\s*',x) for x in cells):continue
    rows.append([para(x.strip(),'cell',links) for x in cells])
   n=len(rows[0]);tw=[CW/n]*n
   if n==2:tw=[CW*.26,CW*.74]
   t=Table(rows,colWidths=tw,repeatRows=1,hAlign='LEFT')
   t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#d8ecf0')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,LIGHT]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,0),1,CYAN)]));out+=[t,Spacer(1,12)];continue
  if line.startswith('#'):
   level=len(line)-len(line.lstrip('#'));out.append(para(line.lstrip('# ').strip(),'h2' if level<=3 else 'h3',links));i+=1;continue
  if line.startswith('!['):i+=1;continue
  if line.startswith('- '):out.append(para('• '+line[2:],'body',links));i+=1;continue
  buf=[line];i+=1
  while i<len(lines) and lines[i].strip() and not re.match(r'^(#|\||```|!\[|- )',lines[i].strip()):buf.append(lines[i].strip());i+=1
  out.append(para(' '.join(buf),'body',links))
 return out

def cover(guide=False):
 title='Guía de cierre\ny sustentación' if guide else 'Evaluación de seguridad\nDC-1'
 items=[Spacer(1,55),para('MNZHACK / SEGURIDAD INFORMÁTICA','h2',False),Spacer(1,23)]
 for l in title.splitlines():items.append(Paragraph(l,ParagraphStyle('cover',fontName='TextBold',fontSize=36,leading=43,textColor=NAVY,spaceAfter=8)))
 items += [Spacer(1,18),para('GUÍA INTERNA DE PREPARACIÓN' if guide else 'INFORME EJECUTIVO Y TÉCNICO · PTES','h2',False),Spacer(1,22)]
 items += [para('Dos vías de acceso documentadas. Una causa compartida de escalamiento. Evidencia, impacto y remediación con límites explícitos.','body',False),Spacer(1,25)]
 for name in ['Juan David Ocampo Gonzalez | 38402','Jaime Andres Cardona Diaz | 40549','Daniel Quintero Hurtado | 31429','Eduardo Jose Villamil Arce | 37831']:items.append(para(name,'body',False))
 items += [Spacer(1,30),para('Periodo: 3-8 octubre 2026  /  Corte: 7 octubre 2026','small',False),para('Versión 0.3 para revisión del equipo. No acredita pruebas adicionales ni aprobación cruzada.','small',False)]
 if not guide:items.append(para('Institución y docente no informados. Nombre MnzHack indicado por el equipo; la asignación escribe Mzlhack. Aclaración administrativa pendiente.','small',False))
 return items

def toc():
 t=TableOfContents();t.levelStyles=[ParagraphStyle('toc',fontName='Text',fontSize=9.5,leading=13,textColor=NAVY,spaceBefore=2,leftIndent=0,firstLineIndent=0)]
 return t

def generate_report():
 src=(ROOT/'informe/INFORME.md').read_text();sections=re.split(r'^## (\d\d\. [^\n]+)\n',src,flags=re.M)
 story=cover();first=story[1];first.toc_title='01. Portada';first.toc_key='s1'
 for j in range(1,len(sections),2):
  title,body=sections[j:j+2];n=int(title[:2])
  if n==1:continue
  if n not in {5,7,12,17,18,23}: story.append(PageBreak())
  else: story.append(Spacer(1,22))
  story.append(heading(title,f's{n}'))
  if n==3:story.append(toc());continue
  if n==25:
   intro,*evparts=re.split(r'^### (EV-[A-Z]+-\d{3}[^\n]*)\n',body,flags=re.M)
   story+=markdown(intro)
   for k in range(0,len(evparts),2):
    label,detail=evparts[k:k+2];eid=re.match(r'EV-[A-Z]+-\d{3}',label)[0];row=EVM[eid]
    story.append(PageBreak());num=len(FIGURES)+1;FIGURES[eid]=f'Figura {num:02d}'
    h=para(f'Figura {num:02d} | {label}','h2',False);h.ev_id=eid;story.append(h)
    # Metadata and every explanatory paragraph from the editorial source are retained.
    detail=re.sub(r'!\[[^\]]*\]\([^\n]+\)','',detail)
    detail=re.sub(r'PENDIENTE: numeración de figura, página y revisión de legibilidad en PDF\.','',detail)
    if 'Instancia:' not in detail:
     detail=f'Instancia: {row["instancia"]}. Autor: {row["autor"]}. Fecha exacta: {row["fecha"]}.\n\n'+detail
    if '**Acción:**' not in detail:
     detail+='\n\n**Relevancia:** '+('Sustenta '+row['hallazgo_ids']+'; interpretar junto con los límites de esa ficha.' if row['hallazgo_ids'] else 'Identifica la superficie o el contexto de esta instancia; no confirma una vulnerabilidad por sí sola.')

    captions=markdown(detail)
    capheight=sum(x.wrap(CW,1000)[1]+getattr(x,'spaceAfter',0)+getattr(x,'spaceBefore',0) for x in captions)
    hashp=para('SHA-256: '+row['sha256'],'small',False)
    hh=h.wrap(CW,1000)[1]+24
    avail=max(80,min(510,H-130-hh-capheight-65))
    path=ROOT/row['ruta'];iw,ih=PILImage.open(path).size;scale=min(CW/iw,avail/ih)
    story += [Image(str(path),width=iw*scale,height=ih*scale),Spacer(1,10)]+captions+[hashp]
   continue
  if n==20:
   saved={k:styles[k] for k in ['body','h2','h3']}
   styles['body']=ParagraphStyle('detailbody',parent=saved['body'],fontSize=9,leading=12,spaceAfter=6)
   styles['h2']=ParagraphStyle('detailh2',parent=saved['h2'],fontSize=13,leading=16,spaceBefore=8,spaceAfter=7)
   styles['h3']=ParagraphStyle('detailh3',parent=saved['h3'],spaceBefore=7,spaceAfter=4)
   parts=re.split(r'(?=^### PT-\d{3})',body,flags=re.M)
   story+=markdown(parts[0])
   for k,part in enumerate(parts[1:]):
    if k:story.append(PageBreak())
    story.append(KeepInFrame(CW,620 if k==0 else 700,markdown(part),mode="shrink",hAlign="LEFT",vAlign="TOP"))
   styles.update(saved)
  else:story+=markdown(body)
  if n==10:story+=[Spacer(1,10),Diagram('arch'),para('Figura A | Arquitectura lógica reconstruida a partir de las evidencias citadas.','small')]
 path=OUT/'PARCIAL_PENTEST_MnzHack_DC-1.pdf'
 doc=Doc(str(path),pagesize=A4,rightMargin=46,leftMargin=46,topMargin=55,bottomMargin=53,title='MnzHack - Informe de pentest DC-1',author='Equipo MnzHack')
 doc.multiBuild(story,onFirstPage=footer,onLaterPages=footer)
 return path

def generate_guide():
 src=(ROOT/'docs/GUIA_SUSTENTACION.md').read_text();sections=re.split(r'^## (\d\d\. [^\n]+)\n',src,flags=re.M)
 story=cover(True)+[PageBreak(),heading('Índice de preparación','guide-index'),toc()]
 for j in range(1,len(sections),2):
  title,body=sections[j:j+2];story+=[PageBreak(),heading(title,'g'+title[:2])]+markdown(body,links=False)
 path=OUT/'GUIA_SUSTENTACION_MnzHack_DC-1.pdf'
 doc=Doc(str(path),pagesize=A4,rightMargin=46,leftMargin=46,topMargin=55,bottomMargin=53,title='MnzHack - Guía práctica y sustentación',author='Equipo MnzHack')
 doc.multiBuild(story,onFirstPage=footer,onLaterPages=footer);return path
if __name__=='__main__':
 paths=[generate_report(),generate_guide()]
 for i,row in enumerate(EVS,1):row['figura']=FIGURES[row['id']];row['pagina_pdf']=str(PAGES[row['id']])
 with (ROOT/'evidencias/indice.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(EVS[0]),lineterminator="\n");w.writeheader();w.writerows(EVS)
 (ROOT/'tmp/pdfs/paginas-evidencias.json').write_text(json.dumps(PAGES,indent=2))
 for p in paths:print(p,len(PdfReader(p).pages),'páginas')
