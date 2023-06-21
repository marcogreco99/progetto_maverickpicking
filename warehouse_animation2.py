# warehouse_animation2
# Università della Calabria - 2021/2022
# Authors: Marco Greco
# Contacts: mrcgreco@icloud.com
import turtle

sc = None
trtl = None
text1 = None
text2 = None
text3 = None
text4 = None
text5 = None
text6 = None
text7 = None
text8 = None
text9 = None
attiv = None
caseid = None
barraloading = None
barraloading2 = None
barrainevasi = None
barraprelievi = None
barrasaltarighe = None
barraprelieviparziali = None
rettangolo = None
prelievi = None
inevasi = None
saltarighe = None
prelieviparziali = None

arrow = None

countp= None
counti=None
countsr=None
countpp=None
counttot = None

dim = None
y = None
start = None

attivitacorrente = None
cid = None

corsiex = None  # [numCor: xx]
corsieys = None
corsieye = None  # [numCor: yyEnd]
corsieye2 = None  # [numCorBlockD: yyEnd]

postopresa = None
redAct = None

def initialize():
    global sc, trtl, text1, text2, text3, text4, text5, text6, \
        text7, text8, text9, attiv, caseid, barraloading, barraloading2, barrainevasi, \
        barraprelievi, barrasaltarighe, barraprelieviparziali, rettangolo, prelievi, inevasi, saltarighe, prelieviparziali, arrow, countp,\
        counti, countsr, countpp, counttot, dim, y, start, attivitacorrente, cid, corsiex, corsieys, corsieye, corsieye2, postopresa, redAct

    sc = turtle.Screen()
    turtle.TurtleScreen._RUNNING=True
    trtl = turtle.Turtle()
    trtl.shape("circle")
    trtl.shapesize(0.3)
    text1 = turtle.Turtle()
    text2 = turtle.Turtle()
    text3 = turtle.Turtle()
    text4 = turtle.Turtle()
    text5 = turtle.Turtle()
    text6 = turtle.Turtle()
    text7 = turtle.Turtle()
    text8 = turtle.Turtle()
    text9 = turtle.Turtle()
    attiv = turtle.Turtle()
    caseid = turtle.Turtle()
    barraloading = turtle.Turtle()
    barraloading2 = turtle.Turtle()
    barrainevasi = turtle.Turtle()
    barraprelievi = turtle.Turtle()
    barrasaltarighe = turtle.Turtle()
    barraprelieviparziali = turtle.Turtle()
    rettangolo = turtle.Turtle()
    prelievi = turtle.Turtle()
    inevasi = turtle.Turtle()
    saltarighe = turtle.Turtle()
    prelieviparziali = turtle.Turtle()

    arrow = turtle.Turtle()
    arrow.hideturtle()
    arrow.pensize(2)

    sc.setup(width=1.0, height=1.0)

    trtl.left(90)
    trtl.color('black')

    countp=0
    counti=0
    countsr=0
    countpp=0
    counttot = 0

    dim = 7
    y = -320
    start = -410

    attivitacorrente = ""
    cid = ""

    corsiex = {}  # [numCor: xx]
    corsieys = y - dim * 3 - (dim / 2)
    corsieye = {}  # [numCor: yyEnd]
    corsieye2 = {}  # [numCorBlockD: yyEnd]

    postopresa = {}
    redAct = set()



def frecciaSu(corsia,h):
    arrow.up()
    arrow.goto(corsiex[corsia],y+h*dim)
    arrow.down()
    arrow.left(90)
    arrow.forward(10)
    arrow.left(145)
    arrow.forward(5)
    arrow.backward(5)
    arrow.left(70)
    arrow.forward(5)
    arrow.setheading(0)

def frecciaGiu(corsia,h):
    arrow.up()
    arrow.goto(corsiex[corsia],y+h*dim+10)
    arrow.down()
    arrow.setheading(270)
    arrow.forward(10)
    arrow.left(145)
    arrow.forward(5)
    arrow.backward(5)
    arrow.left(70)
    arrow.forward(5)
    arrow.setheading(0)

def drawLine(val, yy, numB):
    trtl.up()
    trtl.setpos(val, yy)
    trtl.down()

    for i in range(numB):
        trtl.forward(dim)
        trtl.right(90)
        trtl.forward(dim)
        trtl.right(90)
        trtl.forward(dim)
        trtl.right(90)
        trtl.forward(dim)
        trtl.right(90)
        yy += dim
        trtl.setpos(val, yy)


def drawLineGray(val, yy, numB):
    trtl.fillcolor("lightgray")
    trtl.up()
    trtl.setpos(val, yy)
    trtl.down()
    trtl.begin_fill()
    for i in range(numB):
        trtl.forward(dim)
        trtl.right(90)
        trtl.forward(dim)
        trtl.right(90)
        trtl.forward(dim)
        trtl.right(90)
        trtl.forward(dim)
        trtl.right(90)
        yy += dim
        trtl.setpos(val, yy)
    trtl.end_fill()
    trtl.fillcolor("black")


def gotoStart():
    turtle.tracer(0)
    trtl.up()
    trtl.left(90)
    trtl.goto(start + dim * 110, y - dim * 3 - (dim / 2))
    turtle.tracer(1)


def creaBarra(t, h, l, xx, yy):
    t.hideturtle()
    t.pensize(3)
    t.up()
    t.goto(xx, yy)
    t.down()
    t.goto(xx + l, yy)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.goto(xx, yy + h)
    t.left(90)
    t.forward(h)
    t.right(90)
    t.up()
    t.goto(xx + 2, yy + 2)
    t.left(180)
    t.down()
    t.pensize(1)


def createWarehouse():
    global attiv, attivitacorrente
    turtle.tracer(0)

    print("start: "+str(start))
    print("y: "+str(y))

    drawLineGray(start, y - 3 * dim, 3)
    drawLine(start, y, 35)
    drawLine(start, trtl.ycor() + dim * 2, 31)

    drawLineGray(start + 3 * dim, y - 3 * dim, 3)
    drawLine(start + 3 * dim, y, 35)
    drawLine(start + 3 * dim, trtl.ycor() + dim * 2, 32)
    drawLineGray(start + 4 * dim, y - 3 * dim, 3)
    drawLine(start + 4 * dim, y, 35)
    drawLine(start + 4 * dim, trtl.ycor() + dim * 2, 32)

    for i in range(12):
        drawLineGray(dim * (i) + start + 7 * dim + (dim * 3 * i), y - 3 * dim, 3)
        drawLine(dim * (i) + start + 7 * dim + (dim * 3 * i), y, 35)
        drawLine(dim * (i) + start + 7 * dim + (dim * 3 * i), trtl.ycor() + dim * 2, 41)
        drawLineGray(dim * (i) + start + 8 * dim + (dim * 3 * i), y - 3 * dim, 3)
        drawLine(dim * (i) + start + 8 * dim + (dim * 3 * i), y, 35)
        drawLine(dim * (i) + start + 8 * dim + (dim * 3 * i), trtl.ycor() + dim * 2, 41)

    drawLineGray(start + dim * 3 * (i) + (i) * dim + 11 * dim, y - 3 * dim, 3)
    drawLine(start + dim * 3 * (i) + (i) * dim + 11 * dim, y, 35)
    drawLine(start + dim * 3 * (i) + (i) * dim + 11 * dim, trtl.ycor() + dim * 2, 38)
    drawLineGray(start + dim * 3 * (i) + (i) * dim + 12 * dim, y - 3 * dim, 3)
    drawLine(start + dim * 3 * (i) + (i) * dim + 12 * dim, y, 35)
    drawLine(start + dim * 3 * (i) + (i) * dim + 12 * dim, trtl.ycor() + dim * 2, 38)

    drawLineGray(start + dim * 3 * (i) + (i) * dim + 15 * dim, y - 3 * dim, 3)
    drawLine(start + dim * 3 * (i) + (i) * dim + 15 * dim, y, 35)
    drawLine(start + dim * 3 * (i) + (i) * dim + 15 * dim, trtl.ycor() + dim * 2, 31)
    drawLineGray(start + dim * 3 * (i) + (i) * dim + 16 * dim, y - 3 * dim, 3)
    drawLine(start + dim * 3 * (i) + (i) * dim + 16 * dim, y, 35)
    drawLine(start + dim * 3 * (i) + (i) * dim + 16 * dim, trtl.ycor() + dim * 2, 31)

    drawLineGray(dim * (0) + start + dim * 3 * (i) + (i) * dim + 19 * dim + (dim * 3 * 0), y - 3 * dim, 3)
    drawLine(dim * (0) + start + dim * 3 * (i) + (i) * dim + 19 * dim + (dim * 3 * 0), y, 35)
    drawLine(dim * (0) + start + dim * 3 * (i) + (i) * dim + 19 * dim + (dim * 3 * 0), trtl.ycor() + dim * 2, 31)
    drawLineGray(dim * (0) + start + dim * 3 * (i) + (i) * dim + 20 * dim + (dim * 3 * 0), y - 3 * dim, 3)
    drawLine(dim * (0) + start + dim * 3 * (i) + (i) * dim + 20 * dim + (dim * 3 * (0)), y, 68)

    for j in range(1, 4):
        drawLineGray(dim * (j) + start + dim * 3 * (i) + (i) * dim + 19 * dim + (dim * 3 * (j)), y - 3 * dim, 3)
        drawLine(dim * (j) + start + dim * 3 * (i) + (i) * dim + 19 * dim + (dim * 3 * (j)), y, 68)
        drawLineGray(dim * (j) + start + dim * 3 * (i) + (i) * dim + 20 * dim + (dim * 3 * (j)), y - 3 * dim, 3)
        drawLine(dim * (j) + start + dim * 3 * (i) + (i) * dim + 20 * dim + (dim * 3 * (j)), y, 68)

    for k in range(4):
        drawLineGray(
            dim * (k) + start + dim * 3 * (i) + (i) * dim + 23 * dim + dim * (j) + (dim * 3 * (j)) + (dim * 3 * k),
            y - 3 * dim, 3)
        drawLine(dim * (k) + start + dim * 3 * (i) + (i) * dim + 23 * dim + dim * (j) + (dim * 3 * (j)) + (dim * 3 * k),
                 y, 36)
        drawLineGray(
            dim * (k) + start + dim * 3 * (i) + (i) * dim + 24 * dim + dim * (j) + (dim * 3 * (j)) + (dim * 3 * k),
            y - 3 * dim, 3)
        drawLine(dim * (k) + start + dim * 3 * (i) + (i) * dim + 24 * dim + dim * (j) + (dim * 3 * (j)) + (dim * 3 * k),
                 y, 36)

    drawLineGray(start + dim * 3 * (i) + (i) * dim + dim * (k) + (dim * 3 * k) + dim * (j) + dim * 3 * (j) + 27 * dim,
                 y - 3 * dim, 3)
    drawLine(start + dim * 3 * (i) + (i) * dim + dim * (k) + (dim * 3 * k) + dim * (j) + dim * 3 * (j) + 27 * dim, y,
             30)
    drawLine(start + dim * 3 * (i) + (i) * dim + dim * (k) + (dim * 3 * k) + dim * (j) + dim * 3 * (j) + 28 * dim,
             y - 3 * dim, 30)
    drawLine(start + dim * 3 * (i) + (i) * dim + dim * (k) + (dim * 3 * k) + dim * (j) + dim * 3 * (j) + 28 * dim, y,
             30)

    for v in range(3):
        drawLine(dim * (v) + start + dim * 3 * (i) + (i) * dim + dim * (k) + (dim * 3 * k) + dim * (j) + dim * 3 * (
            j) + 31 * dim + (dim * 3 * v), y - 3 * dim, 36)
        drawLine(dim * (v) + start + dim * 3 * (i) + (i) * dim + dim * (k) + (dim * 3 * k) + dim * (j) + dim * 3 * (
            j) + 31 * dim + (dim * 3 * v), y, 36)
        drawLine(dim * (v) + start + dim * 3 * (i) + (i) * dim + dim * (k) + (dim * 3 * k) + dim * (j) + dim * 3 * (
            j) + 32 * dim + (dim * 3 * v), y - 3 * dim, 36)
        drawLine(dim * (v) + start + dim * 3 * (i) + (i) * dim + dim * (k) + (dim * 3 * k) + dim * (j) + dim * 3 * (
            j) + 32 * dim + (dim * 3 * v), y, 36)

    drawLine(start + dim * 3 * (i) + (i) * dim + dim * (k) + (dim * 3 * k) + dim * (j) + dim * 3 * (j) + dim * (
        v) + dim * 3 * v + 35 * dim, y - 3 * dim, 36)
    drawLine(start + dim * 3 * (i) + (i) * dim + dim * (k) + (dim * 3 * k) + dim * (j) + dim * 3 * (j) + dim * (
        v) + dim * 3 * v + 35 * dim, y, 36)

    # Disegno i posti presa in alto
    drawLine(dim * (0) + start + dim * 3 * (i) + (i) * dim + 20 * dim + (dim * 3 * 0), y + 68 * dim + 7 * dim, 26)

    drawLine(dim * (1) + start + dim * 3 * (i) + (i) * dim + 19 * dim + (dim * 3 * 1), y + 68 * dim + 4 * dim, 24)
    drawLine(dim * (1) + start + dim * 3 * (i) + (i) * dim + 20 * dim + (dim * 3 * 1), y + 68 * dim + 4 * dim, 24)

    drawLine(dim * (1) + start + dim * 3 * (i) + (i) * dim + 23 * dim + (dim * 3 * 1), y + 68 * dim + 4 * dim, 24)
    drawLine(dim * (1) + start + dim * 3 * (i) + (i) * dim + 24 * dim + (dim * 3 * 1), y + 68 * dim + 4 * dim, 24)

    drawLine(dim * (1) + start + dim * 3 * (i) + (i) * dim + 27 * dim + (dim * 3 * 1), y + 68 * dim + 4 * dim, 24)
    drawLine(dim * (1) + start + dim * 3 * (i) + (i) * dim + 28 * dim + (dim * 3 * 1), y + 68 * dim + 4 * dim, 24)

    drawLine(dim * (0) + start + dim * 3 * (i) + (i) * dim + 23 * dim + dim * (j) + (dim * 3 * (j)) + (dim * 3 * 0),
             y + 36 * dim + 11 * dim, 54)

    trtl.speed(1)
    for i in range(28):
        corsiex[61 + i] = start + dim * 110 - i * 28
    ci = 61
    for a in range(3):
        corsieye[ci + a] = y + 36 * dim + (dim / 2)
    ci += a + 1
    for b in range(1):
        corsieye[ci + b] = y + 30 * dim + (dim / 2)
    ci += b + 1
    for c in range(4):
        corsieye[ci + c] = y + 36 * dim + (dim / 2)
    ci += c + 1
    for e in range(4):
        corsieye[ci + e] = y + 96 * dim + (dim / 2)
    for d in range(4):
        corsieye2[ci + d] = y + 68 * dim + (dim / 2)
    ci += d + 1
    for f in range(1):
        corsieye[ci + f] = y + 69 * dim + (dim / 2)
    ci += f + 1
    for g in range(1):
        corsieye[ci + g] = y + 75 * dim + (dim / 2)
    ci += g + 1
    for h in range(12):
        corsieye[ci + h] = y + 78 * dim + (dim / 2)
    ci += h + 1
    for i in range(1):
        corsieye[ci + i] = y + 69 * dim + (dim / 2)
    ci += i + 1
    for z in range(1):
        corsieye[ci + z] = y + 68 * dim + (dim / 2)

    for i in range(1, 213, 2):
        postopresa[i + 12] = corsieys + (int(i / 2) + 1) * dim
        postopresa[i + 13] = corsieys + (int(i / 2) + 1) * dim

    turtle.tracer(0)

    text1.up()
    text1.hideturtle()
    text1.goto(corsiex[88] - 46 * dim, y + 80 * dim)
    text1.write("Attività: ", move=False, font=('Arial', 20, 'bold'))

    text2.up()
    text2.hideturtle()
    text2.goto(corsiex[88] - 46 * dim, y + 89 * dim)
    text2.write("ID Lista: ", move=False, font=('Arial', 20, 'bold'))

    text9.up()
    text9.hideturtle()
    text9.goto(corsiex[64]+2*dim+dim/2, y + 97 * dim)
    text9.write("Statistiche di Lista", move=False, font=('Times New Roman', 20, 'bold'))

    rettangolo.up()
    rettangolo.hideturtle()
    rettangolo.color("gray")
    rettangolo.fillcolor("gray")
    # rettangolo.hideturtle()
    rettangolo.goto(corsiex[64] - dim, y + 96 * dim)
    rettangolo.begin_fill()
    rettangolo.down()
    rettangolo.forward(261 + dim)
    rettangolo.right(90)
    rettangolo.forward(y + 97 * dim - (y + 80 * dim) + dim / 2)
    rettangolo.right(90)
    rettangolo.forward(261 + dim)
    rettangolo.right(90)
    rettangolo.forward(y + 97 * dim - (y + 80 * dim) + dim / 2)
    rettangolo.end_fill()

    for i in range(61,88,2):
        frecciaSu(i,7)

    for i in range(62,89,2):
        frecciaGiu(i,7)

    for i in range(69,88,2):
            frecciaSu(i,50)

    for i in range(70,89,2):
        frecciaGiu(i,50)


    prelievi.hideturtle()
    prelievi.color("white")
    prelievi.up()
    prelievi.goto(corsiex[64] + dim * 16 + 123, y + 92 * dim + 2)
    prelievi.write("0", move=False, font=('Times New Roman', 10, 'bold'))

    creaBarra(barraprelievi, 10, 120, corsiex[64] + dim * 15, y + 92 * dim + 4)
    barraprelievi.fillcolor("lightgreen")
    barraprelievi.color("lightgreen")


    saltarighe.hideturtle()
    saltarighe.color("white")
    saltarighe.up()
    saltarighe.goto(corsiex[64] + dim * 16 + 123, y + 88 * dim + 2)
    saltarighe.write("0", move=False, font=('Times New Roman', 10, 'bold'))

    creaBarra(barrasaltarighe, 10, 120, corsiex[64] + dim * 15, y + 88 * dim + 4)
    barrasaltarighe.fillcolor("red")
    barrasaltarighe.color("red")


    inevasi.hideturtle()
    inevasi.color("white")
    inevasi.up()
    inevasi.goto(corsiex[64] + dim * 16 + 123, y + 84 * dim + 2)
    inevasi.write("0", move=False, font=('Times New Roman', 10, 'bold'))

    creaBarra(barrainevasi, 10, 120, corsiex[64] + dim * 15, y + 84 * dim + 4)
    barrainevasi.fillcolor("red")
    barrainevasi.color("red")


    prelieviparziali.hideturtle()
    prelieviparziali.color("white")
    prelieviparziali.up()
    prelieviparziali.goto(corsiex[64] + dim * 16 + 123, y + 80 * dim + 2)
    prelieviparziali.write("0", move=False, font=('Times New Roman', 10, 'bold'))

    creaBarra(barraprelieviparziali, 10, 120, corsiex[64] + dim * 15, y + 80 * dim + 4)
    barraprelieviparziali.fillcolor("red")
    barraprelieviparziali.color("red")

    text3.up()
    text3.color("white")
    text3.hideturtle()
    text3.goto(corsiex[64], y + 80 * dim)
    text3.write("Prelievi Parziali ", move=False, font=('Times New Roman', 10, 'bold'))

    text4.up()
    text4.color("white")
    text4.hideturtle()
    text4.goto(corsiex[64], y + 84 * dim)
    text4.write("Inevasi ", move=False, font=('Times New Roman', 10, 'bold'))

    text5.up()
    text5.color("white")
    text5.hideturtle()
    text5.goto(corsiex[64], y + 88 * dim)
    text5.write("Salta Righe ", move=False, font=('Times New Roman', 10, 'bold'))

    text6.up()
    text6.color("white")
    text6.hideturtle()
    text6.goto(corsiex[64], y + 92 * dim)
    text6.write("Prelievi ", move=False, font=('Times New Roman', 10, 'bold'))

    attiv.up()
    attiv.hideturtle()
    attiv.goto(text1.xcor() + dim * 17, y + 80 * dim)
    attiv.write(attivitacorrente, move=False, font=('Arial', 20, 'bold'))

    caseid.up()
    caseid.hideturtle()
    caseid.goto(text2.xcor() + dim * 17, y + 89 * dim)
    caseid.write(cid, move=False, font=('Arial', 20, 'bold'))

    text7.up()
    text7.hideturtle()
    text7.goto(corsiex[64]+4*dim+dim/2,y + 66 * dim)
    text7.write("Completamento Lista", move=False, font=('Time New Roman',15,'bold'))

    text8.up()
    text8.hideturtle()
    text8.goto(corsiex[64]+4*dim+dim/2,y + 56 * dim)
    text8.write("Completamento Log", move=False, font=('Time New Roman',15,'bold'))


    creaBarra(barraloading, 20, 261, corsiex[64], y + 63 * dim)
    barraloading.fillcolor("lightblue")
    barraloading.color("lightblue")

    creaBarra(barraloading2, 20, 261, corsiex[64], y + 53 * dim)
    barraloading2.fillcolor("lightblue")
    barraloading2.color("lightblue")

    turtle.tracer(1)


def get_corsia(val):
    for key, value in corsiex.items():
        if val == value:
            return key

    return "non esiste questa corsia"


def get_postop(val):
    for key, value in postopresa.items():
        if val == value:
            return key

    return "non esiste questo posto presa"


def goOn(corsia, postop):
    corsiaAttuale = get_corsia(trtl.xcor())

    if corsiaAttuale % 2 == 0:
        if corsia - corsiaAttuale == 0:
            trtl.goto(corsiex[corsia], postopresa[postop])
        else:
            #AGGIUNGERE CONTROLLI CORSIA 70
            if corsia % 2 == 1:
                trtl.goto(corsiex[corsiaAttuale], corsieys)
                trtl.goto(corsiex[corsia], corsieys)
                trtl.goto(corsiex[corsia], postopresa[postop])
            else:
                trtl.goto(corsiex[corsiaAttuale], corsieys)
                trtl.goto(corsiex[corsia-1],corsieys)
                trtl.goto(corsiex[corsia-1],corsieye[corsia-1])
                trtl.goto(corsiex[corsia-1],corsieye[corsia])
                trtl.goto(corsiex[corsia], postopresa[postop])
    else:
        if corsia - corsiaAttuale == 0:
            trtl.goto(corsiex[corsia], postopresa[postop])
        else:
            if corsia % 2 == 1:#aggiustare 69 e 71
                trtl.goto(corsiex[corsiaAttuale], corsieye[corsiaAttuale])
                corsiaAttuale += 1
                trtl.goto(corsiex[corsiaAttuale], corsieye[corsiaAttuale - 1])
                trtl.goto(corsiex[corsiaAttuale], corsieys)
                trtl.goto(corsiex[corsia], corsieys)
                trtl.goto(corsiex[corsia],postopresa[postop])
            else:
                if corsiaAttuale < 69:
                    trtl.goto(corsiex[corsiaAttuale],corsieye[61]) #warning corsia 64/65
                    if corsia<=69:
                        trtl.goto(corsiex[corsia],corsieye[61])
                        trtl.goto(corsiex[corsia],postopresa[postop])
                    else:
                        trtl.goto(corsiex[69],corsieye[61])
                        if (corsia<=72):
                            if (postop<=230 and postop>=159):
                                trtl.goto(corsiex[69],corsieye[69])
                                trtl.goto(corsiex[corsia],corsieye[corsia])
                                trtl.goto(corsiex[corsia],postopresa[postop])
                            else:
                                trtl.goto(corsiex[69],corsieye2[70])
                                trtl.goto(corsiex[corsia],corsieye2[corsia])
                                trtl.goto(corsiex[corsia],postopresa[postop])
                        else:
                            trtl.goto(corsiex[69],corsieye2[70])
                            trtl.goto(corsiex[74],corsieye[75])
                            if(corsia==74):
                                trtl.goto(corsiex[74],postopresa[postop])
                            else:
                                trtl.goto(corsiex[74],corsieye[76])#s o e?
                                if(corsia<=86):
                                    trtl.goto(corsiex[corsia],corsieye[corsia])
                                    trtl.goto(corsiex[corsia],postopresa[postop])
                                else:
                                    trtl.goto(corsiex[87],corsieye[87])
                                    trtl.goto(corsiex[87],corsieye[88])
                                    trtl.goto(corsiex[88],corsieye[88])
                                    trtl.goto(corsiex[corsia],postopresa[postop])
                elif corsiaAttuale<=74:
                    if get_postop(trtl.ycor())<=230 and get_postop(trtl.ycor())>=159:
                        trtl.goto(corsiex[corsiaAttuale],corsieye[70])
                        trtl.goto(corsiex[corsiaAttuale+1],corsieye[70])
                    else:
                        trtl.goto(corsiex[corsiaAttuale],corsieye2[69])
                    if (corsia<=72):
                        if (postop<=230 and postop>=159):
                            trtl.goto(corsiex[get_corsia(trtl.xcor())],corsieye[69])
                            trtl.goto(corsiex[corsia],corsieye[corsia])
                            trtl.goto(corsiex[corsia],postopresa[postop])
                        else:
                            trtl.goto(corsiex[get_corsia(trtl.xcor())],corsieye2[70])
                            trtl.goto(corsiex[corsia],corsieye2[corsia])
                            trtl.goto(corsiex[corsia],postopresa[postop])
                    else:

                        if get_postop(trtl.ycor())<=230 and get_postop(trtl.ycor())>=159:
                            trtl.goto(corsiex[corsiaAttuale],corsieye[70])
                            trtl.goto(corsiex[corsiaAttuale+1],corsieye[70])
                            trtl.goto(corsiex[corsiaAttuale+1],corsieye2[70])
                        trtl.goto(corsiex[74],corsieye[75])
                        if(corsia==74):
                            trtl.goto(corsiex[74],postopresa[postop])
                        else:
                            trtl.goto(corsiex[74],corsieye[76])#s o e?
                            if(corsia<=86):
                                trtl.goto(corsiex[corsia],corsieye[corsia])
                                trtl.goto(corsiex[corsia],postopresa[postop])
                            else:
                                trtl.goto(corsiex[87],corsieye[87])
                                trtl.goto(corsiex[87],corsieye[88])
                                trtl.goto(corsiex[88],corsieye[88])
                                trtl.goto(corsiex[corsia],postopresa[postop])
                elif corsiaAttuale<=85:
                    trtl.goto(corsiex[corsiaAttuale],corsieye[76])
                    trtl.goto(corsiex[corsia],corsieye[corsia])
                    trtl.goto(corsiex[corsia],postopresa[postop])
                else:
                    trtl.goto(corsiex[87],corsieye[88])
                    trtl.goto(corsiex[88],corsieye[88])
                    trtl.goto(corsiex[corsia],postopresa[postop])

def goBack(corsia, postop):

    corsiaAttuale = get_corsia(trtl.xcor())

    if corsiaAttuale % 2 == 0:
        if corsiaAttuale - corsia == 0:
            trtl.goOn(corsia, postop)
        else:
            trtl.goto(corsiex[corsiaAttuale],corsieys)
            if(corsia%2==1):
                trtl.goto(corsiex[corsia],corsieys)
                trtl.goto(corsiex[corsia],postopresa[postop])
            else:
                trtl.goto(corsiex[corsia+1],corsieys)
                trtl.goto(corsiex[corsia+1],corsieye[corsia+1])
                trtl.goto(corsiex[corsia],corsieye[corsia])
                trtl.goto(corsiex[corsia],postopresa[postop])
    else:
        if corsiaAttuale - corsia == 0:
            trtl.goOn(corsia, postop)
        else:
            trtl.goto(corsiex[corsiaAttuale],corsieye[corsiaAttuale-1])
            if(corsia%2==1):
                trtl.goto(corsiex[corsiaAttuale-1],corsieye[corsiaAttuale-1])
                trtl.goto(corsiex[corsiaAttuale-1],corsieys)
                trtl.goto(corsiex[corsia],corsieys)
                trtl.goto(corsiex[corsia],postopresa[postop])
            else:
                if(corsia==corsiaAttuale-1):
                    trtl.goto(corsiex[corsia],corsieye[corsia])
                    trtl.goto(corsiex[corsia],postopresa[postop])
                else:
                    trtl.goto(corsiex[corsiaAttuale-1],corsieye[corsiaAttuale-1])
                    trtl.goto(corsiex[corsiaAttuale-1],corsieys)
                    trtl.goto(corsiex[corsia-1],corsieys)
                    trtl.goto(corsiex[corsia-1],corsieye[corsia-1])
                    trtl.goto(corsiex[corsia],corsieye[corsia])
                    trtl.goto(corsiex[corsia],postopresa[postop])


def eseguiAttivita(attivita, fo):
    global attivitacorrente, attiv, redAct, countp, counti, countpp, countsr
    match (attivita):
        case 'PRELIEVO':
            forwardBar(barraprelievi, fo, 6)
            countp+=1
            prelievi.undo()
            prelievi.write(countp, move=False, font=('Times New Roman', 10, 'bold'))
            attivitacorrente = 'PRELIEVO'
            attiv.undo()
            attiv.color("lightgreen")
            attiv.write(attivitacorrente, move=False, font=('Arial', 20, 'bold',))
            trtl.color("lightgreen")
            for r in redAct:
                if trtl.xcor() == r.xcor() and trtl.ycor() == r.ycor():
                    r.hideturtle()
                    redAct.remove(r)
                    break
            trtl.left(90)
            trtl.right(90)
            trtl.color("black")
            attivitacorrente = ""
            attiv.undo()
            attiv.write(attivitacorrente, move=False, font=('Arial', 20, 'bold'))
        case 'PRELIEVO PARZIALE':
            forwardBar(barraprelieviparziali, fo, 6)
            countpp+=1
            prelieviparziali.undo()
            prelieviparziali.write(countpp, move=False, font=('Times New Roman', 10, 'bold'))
            attivitacorrente = 'PRELIEVO PARZIALE'
            attiv.undo()
            attiv.color("red")
            attiv.write(attivitacorrente, move=False, font=('Arial', 20, 'bold'))
            trtl.color("red")
            trtl2 = turtle.Turtle()
            redAct.add(trtl2)
            trtl2.color("red")
            trtl2.shape("circle")
            trtl2.shapesize(0.3)
            turtle.tracer(0)
            trtl2.up()
            trtl2.goto(trtl.xcor(), trtl.ycor())
            turtle.tracer(1)
            trtl.left(90)
            trtl.right(90)
            trtl.color("black")
            attivitacorrente = ""
            attiv.undo()
            attiv.write(attivitacorrente, move=False, font=('Arial', 20, 'bold'))
        case 'INEVASO':
            forwardBar(barrainevasi, fo, 6)
            counti+=1
            inevasi.undo()
            inevasi.write(counti, move=False, font=('Times New Roman', 10, 'bold'))
            attivitacorrente = 'INEVASO'
            attiv.undo()
            attiv.color("red")
            attiv.write(attivitacorrente, move=False, font=('Arial', 20, 'bold'))
            trtl.color("red")
            trtl2 = turtle.Turtle()
            redAct.add(trtl2)
            trtl2.color("red")
            trtl2.shape("circle")
            trtl2.shapesize(0.3)
            turtle.tracer(0)
            trtl2.up()
            trtl2.goto(trtl.xcor(), trtl.ycor())
            turtle.tracer(1)
            trtl.left(90)
            trtl.right(90)
            trtl.color("black")
            attivitacorrente = ""
            attiv.undo()
            attiv.write(attivitacorrente, move=False, font=('Arial', 20, 'bold'))
        case 'SALTARIGA':
            forwardBar(barrasaltarighe, fo, 6)
            countsr+=1
            saltarighe.undo()
            saltarighe.write(countsr, move=False, font=('Times New Roman', 10, 'bold'))
            attivitacorrente = 'SALTARIGA'
            attiv.undo()
            attiv.color("red")
            attiv.write(attivitacorrente, move=False, font=('Arial', 20, 'bold'))
            trtl.color("red")
            trtl2 = turtle.Turtle()
            redAct.add(trtl2)
            trtl2.color("red")
            trtl2.shape("circle")
            trtl2.shapesize(0.3)
            turtle.tracer(0)
            trtl2.up()
            trtl2.goto(trtl.xcor(), trtl.ycor())
            turtle.tracer(1)
            trtl.left(90)
            trtl.right(90)
            trtl.color("black")
            attivitacorrente = ""
            attiv.undo()
            attiv.write(attivitacorrente, move=False, font=('Arial', 20, 'bold',))


def forwardBar(t, n, h):
    turtle.tracer(0)
    t.begin_fill()
    t.forward(n)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(n)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.up()
    t.forward(n)
    t.down()
    t.end_fill()
    turtle.tracer(1)

def startEmulation(dict):
    global counttot, countp, counti, countpp, countsr

    for lista in dict:
        counttot+=len(dict[lista])
    for i in dict[lista]:
        if i[0] == "-" or i[0] == "V1" or i[0] == "V2" or i[0] == "R" or list(map(int, i[0].split(".")))[0] == 99:
            counttot-=1

    for k in dict:
        count = 0
        p = 0
        inev = 0
        pp = 0
        sr = 0


        for i in dict[k]:
            if i[0] == "-" or i[0] == "V1" or i[0] == "V2" or i[0] == "R" or list(map(int, i[0].split(".")))[0] == 99:
                count += 1
            else:
                if i[1] == 'PRELIEVO': p += 1
                if i[1] == 'INEVASO': inev += 1
                if i[1] == 'PRELIEVO PARZIALE': pp += 1
                if i[1] == 'SALTARIGA': sr += 1
        num = len(dict[k]) - count
        forwardof = 259 / num
        forwardof2 = 117 / num
        forwardof3 = 257/counttot
        cid = k
        caseid.undo()
        caseid.write(str(cid), move=False, font=('Arial', 20, 'bold'))
        for i in dict[k]:
            if i[0] != "-" and i[0] != "V1" and i[0] != "V2" and list(map(int, i[0].split(".")))[0] != 99:
                coor = list(map(int, i[0].split(".")))
                if get_corsia(trtl.xcor()) % 2 == 0:
                    if (get_corsia(trtl.xcor()) < coor[0] or (
                            get_corsia(trtl.xcor()) == coor[0] and postopresa[coor[1]] <= trtl.ycor())):
                        goOn(coor[0], coor[1])
                        eseguiAttivita(i[1], forwardof2)
                        forwardBar(barraloading, forwardof, 16)
                        forwardBar(barraloading2, forwardof3,16)
                    else:
                        goBack(coor[0], coor[1])
                        eseguiAttivita(i[1], forwardof2)
                        forwardBar(barraloading, forwardof, 16)
                        forwardBar(barraloading2, forwardof3,16)
                else:
                    if (get_corsia(trtl.xcor()) < coor[0] or (
                            get_corsia(trtl.xcor()) == coor[0] and postopresa[coor[1]] >= trtl.ycor())):
                        goOn(coor[0], coor[1])
                        eseguiAttivita(i[1], forwardof2)
                        forwardBar(barraloading, forwardof, 16)
                        forwardBar(barraloading2, forwardof3,16)
                    else:
                        goBack(coor[0], coor[1])
                        eseguiAttivita(i[1], forwardof2)
                        forwardBar(barraloading, forwardof, 16)
                        forwardBar(barraloading2, forwardof3,16)
        for r in redAct:
            r.hideturtle()
        redAct.clear()
        cid = ""
        caseid.undo()
        caseid.write(cid, move=False, font=('Arial', 20, 'bold'))
        turtle.tracer(0)
        for i in range(num * 13):
            barraloading.undo()
        for i in range(p * 13):
            barraprelievi.undo()
        for i in range(inev * 13):
            barrainevasi.undo()
        for i in range(pp * 13):
            barraprelieviparziali.undo()
        for i in range(sr * 13):
            barrasaltarighe.undo()


        countp = 0
        counti = 0
        countsr = 0
        countpp = 0

        prelievi.undo()
        prelievi.write(countp, move=False, font=('Times New Roman', 10, 'bold'))
        inevasi.undo()
        inevasi.write(counti, move=False, font=('Times New Roman', 10, 'bold'))
        saltarighe.undo()
        saltarighe.write(countsr, move=False, font=('Times New Roman', 10, 'bold'))
        prelieviparziali.undo()
        prelieviparziali.write(countpp, move=False, font=('Times New Roman', 10, 'bold'))
        turtle.tracer(1)
        gotoStart()


def main(diz):
    global sc
    initialize()
    createWarehouse()
    gotoStart()
    print(diz)
    startEmulation(diz)
    sc.mainloop()
