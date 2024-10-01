from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


imagem1 = ('L:\Marketing\enviados\\19.jpg')
imagem2 = ('L:\Marketing\enviados\\445.jpg')
imagem3 = ('L:\Marketing\enviados\\424.jpg')
imagem4 = ('L:\Marketing\enviados\\465.jpg')
imagem5 = ('L:\Marketing\enviados\\473.jpg')

imagem6 = ('L:\Marketing\enviados\\335.jpg')
imagem7 = ('L:\Marketing\enviados\\445.jpg')
imagem8 = ('L:\Marketing\enviados\\467.jpg')
imagem9 = ('L:\Marketing\enviados\\450.jpg')
imagem10 = ('L:\Marketing\enviados\\108.jpg')

imagem11 = ('L:\Marketing\enviados\\1315.jpg')
imagem12 = ('L:\Marketing\enviados\\897.jpg')
imagem13 = ('L:\Marketing\enviados\\1463.jpg')
imagem14 = ('L:\Marketing\enviados\\1511.jpg')
imagem15 = ('L:\Marketing\enviados\\1568.jpg')
imagem16 = ('L:\Marketing\enviados\\1666.jpg')

header = ('L:\\TI\\Header e footer\\header.jpg')
footer = ('L:\\TI\\Header e footer\\footer.jpg')
fundo = ('fundo1.png')



def mm2p(milimetros): # Converte milimetros por PONTOS
    return milimetros / 0.352777

cnv = canvas.Canvas("meu_pdf.pdf", pagesize=A4) # Cria um pdf nomeando-o


cnv.drawImage(header,mm2p(0), mm2p(237),width=600,height=170)
cnv.drawImage(footer,mm2p(0), mm2p(0),width=600,height=85)
cnv.drawImage(fundo,mm2p(0),mm2p(30),width=595,height=600)

# # Primeira Linha
cnv.drawImage(imagem1,mm2p(13),mm2p(199),width=80,height=80)
cnv.drawString(mm2p(25),mm2p(230),text="Cod:1497457")
cnv.drawImage(imagem2,mm2p(63),mm2p(199),width=80,height=80)
cnv.drawString(mm2p(80),mm2p(230),text="Cod:1497457")
cnv.drawImage(imagem3,mm2p(113),mm2p(199),width=80,height=80)
cnv.drawString(mm2p(130),mm2p(230),text="Cod:1497457")
cnv.drawImage(imagem4,mm2p(163),mm2p(199),width=80,height=80)
cnv.drawString(mm2p(185),mm2p(230),text="Cod:1497457")

# # Segunda Linha
cnv.drawImage(imagem5,mm2p(13),mm2p(145),width=80,height=80)
cnv.drawImage(imagem6,mm2p(63),mm2p(145),width=80,height=80)
cnv.drawImage(imagem7,mm2p(113),mm2p(145),width=80,height=80)
cnv.drawImage(imagem8,mm2p(163),mm2p(145),width=80,height=80)

# # Terceira Linha
cnv.drawImage(imagem9,mm2p(13),mm2p(90),width=80,height=80)
cnv.drawImage(imagem10,mm2p(63),mm2p(90),width=80,height=80)
cnv.drawImage(imagem11,mm2p(113),mm2p(90),width=80,height=80)
cnv.drawImage(imagem12,mm2p(163),mm2p(90),width=80,height=80)

# # Quarta Linha
cnv.drawImage(imagem13,mm2p(13),mm2p(40),width=80,height=80)
cnv.drawImage(imagem14,mm2p(63),mm2p(40),width=80,height=80)
cnv.drawImage(imagem15,mm2p(113),mm2p(40),width=80,height=80)
cnv.drawImage(imagem16,mm2p(163),mm2p(40),width=80,height=80)

cnv.save()

