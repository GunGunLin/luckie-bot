#  Luckie-Bot FINAL v2 — M5StickC-Plus

# ── Step 1: 先初始化屏幕，确保显示正常 ──────────────────────
import os, sys, io
import M5
from M5 import *
import time

M5.begin()
Lcd.setRotation(1)   # 横屏 240×135
Lcd.clear(0x0d0d1e)
Lcd.setTextColor(0x6a5acd, 0x0d0d1e)
Lcd.setTextSize(1)
Lcd.setCursor(8, 8)
Lcd.print("Luckie-Bot")
Lcd.setCursor(8, 24)
Lcd.setTextColor(0x444466, 0x0d0d1e)
Lcd.print("Starting...")

# ── Step 2: 其余模块（失败不影响屏幕）──────────────────────
import sys, select, time, math
from machine import Pin

# SK6812 灯带

NUM_LEDS = 16
STRIP_OK = False
strip = None
try:
    from hardware import RGB
    strip = RGB(io=26, n=NUM_LEDS, type="SK6812")
    
    STRIP_OK = True
except Exception as e:
    print("灯带初始化错误:", e) # 打印错误方便调试
    
    STRIP_OK = False
    strip = None

# ── 颜色常量 ─────────────────────────────────────────────────
BG=0x0d0d1e; PURPLE=0x6a5acd; GOLD=0xd4af37; WHITE=0xffffff
GRAY=0x888888; GREEN=0x00dd77; CYAN=0x00ccff; PINK=0xff88aa
DARK=0x1a1a2e; RED=0xff4466

W, H = 240, 135

# ── 分类 ────────────────────────────────────────────────────
CATS       = ['财运', '学业', '情感', '综合']
CAT_COLORS = [GOLD,   CYAN,   PINK,   GREEN]
cat_idx    = 0
current_cat = ''
mode = 'CATEGORY'

EL=(85,52); ER=(155,52); MX,MY=120,88

# ═══════════════════════════════════════════════════════════
#  灯带（SK6812 GRB顺序）
# ═══════════════════════════════════════════════════════════

def strip_fill(r, g, b):
    if not STRIP_OK: 
        return
    # SK6812 颜色顺序：G R B（如颜色不对，调换 r/g 位置）
    for i in range(NUM_LEDS):
        strip[i] = (g, r, b)
    strip.write()

def strip_off():
    strip_fill(0, 0, 0)

strip_mode  = 'OFF'
strip_phase = 0.0
strip_tick  = 0

def set_strip(m):
    global strip_mode, strip_phase
    strip_mode = m
    strip_phase = 0.0
    if m == 'OFF': strip_off()

def hsv(h, s=1.0, v=0.3):
    i = int(h*6); f = h*6-i
    p=v*(1-s); q=v*(1-f*s); t=v*(1-(1-f)*s)
    rgb=[(v,t,p),(q,v,p),(p,v,t),(p,q,v),(t,p,v),(v,p,q)][i%6]
    return int(rgb[0]*255),int(rgb[1]*255),int(rgb[2]*255)

def update_strip():
    global strip_phase, strip_tick
    if not STRIP_OK: return
    strip_tick += 1
    if strip_tick % 3 != 0: return
    strip_phase += 0.04

    if strip_mode == 'BREATHE':
        v = int((math.sin(strip_phase)*.5+.5)*55)
        strip_fill(v//3, 0, v)
    elif strip_mode == 'PULSE':
        v = int(abs(math.sin(strip_phase*4))*75)
        strip_fill(v, int(v*.6), 0)
    elif strip_mode == 'RAINBOW':
        for i in range(NUM_LEDS):
            r,g,b = hsv((strip_phase + i/NUM_LEDS)%1.0)
            strip[i] = (g, r, b)   # SK6812 GRB
        strip.write()
    elif strip_mode == 'WARM':
        v = int((math.sin(strip_phase*.4)*.08+.92)*55)
        strip_fill(v, int(v*.55), 0)

# ═══════════════════════════════════════════════════════════
#  绘图工具
# ═══════════════════════════════════════════════════════════
def draw_arc(cx,cy,r,a0,a1,color,thick=2):
    steps=10; prev=None
    for i in range(steps+1):
        t=i/steps; a=math.radians(a0+(a1-a0)*t)
        x=int(cx+r*math.cos(a)); y=int(cy+r*math.sin(a))
        if prev:
            for d in range(thick):
                Lcd.drawLine(prev[0],prev[1]+d,x,y+d,color)
        prev=(x,y)

def draw_heart(cx,cy,size,color):
    r=size//2
    Lcd.fillCircle(cx-r,cy-r//2,r,color)
    Lcd.fillCircle(cx+r,cy-r//2,r,color)
    for i in range(size):
        Lcd.drawLine(cx-(size-i),cy-r//2+i,cx+(size-i),cy-r//2+i,color)

def status_bar(hint='A:切换  B:确认'):
    Lcd.drawLine(0, H-16, W, H-16, DARK)
    Lcd.setTextColor(0x303050, BG)
    Lcd.setTextSize(1)
    Lcd.setCursor(6, H-12)
    Lcd.print(hint)

# ═══════════════════════════════════════════════════════════
#  表情
# ═══════════════════════════════════════════════════════════
def clear_face():
    Lcd.clear(BG)
    status_bar()

def face_idle():
    clear_face()
    draw_arc(EL[0],EL[1]+4,12,200,340,WHITE,2)
    draw_arc(ER[0],ER[1]+4,12,200,340,WHITE,2)
    draw_arc(MX,MY-6,14,20,160,GOLD,2)
    Lcd.setTextColor(PURPLE,BG); Lcd.setTextSize(2)
    Lcd.setCursor(170,20); Lcd.print("z")
    Lcd.setTextSize(1); Lcd.setCursor(183,12); Lcd.print("z")
    Lcd.setCursor(192,6); Lcd.print("z")

def face_awake():
    clear_face()
    for ex,ey in [EL, ER]:
        Lcd.drawCircle(ex,ey,13,WHITE)
        Lcd.fillCircle(ex+2,ey+2,6,PURPLE)
        Lcd.fillCircle(ex+4,ey,3,WHITE)
    Lcd.drawLine(MX-14,MY,MX+14,MY,GOLD)
    Lcd.drawLine(MX-14,MY+1,MX+14,MY+1,GOLD)

def face_think():
    clear_face()
    Lcd.drawCircle(EL[0],EL[1],12,WHITE)
    Lcd.fillCircle(EL[0]+2,EL[1]+2,5,CYAN)
    Lcd.fillCircle(EL[0]+4,EL[1],2,WHITE)
    Lcd.fillRect(ER[0]-13,ER[1]-2,26,5,WHITE)
    Lcd.fillRect(ER[0]-13,ER[1]-1,26,3,BG)
    Lcd.drawLine(MX-8,MY+2,MX+14,MY-2,GOLD)
    Lcd.drawLine(MX-8,MY+3,MX+14,MY-1,GOLD)
    for i,x in enumerate([38,48,60]):
        Lcd.fillCircle(x,18,3+i,PURPLE)

def face_happy():
    clear_face()
    for cx,cy in [EL, ER]:
        Lcd.drawLine(cx-12,cy+8,cx,cy-4,WHITE)
        Lcd.drawLine(cx,cy-4,cx+12,cy+8,WHITE)
        Lcd.drawLine(cx-11,cy+9,cx+1,cy-3,WHITE)
        Lcd.drawLine(cx+1,cy-3,cx+13,cy+9,WHITE)
    for r in range(20,24): draw_arc(MX,MY-6,r,18,162,GOLD,1)
    for r in range(10,19): draw_arc(MX,MY-6,r,25,155,RED,1)
    Lcd.fillCircle(EL[0]-6,MY-8,10,0x4a0020)
    Lcd.fillCircle(ER[0]+6,MY-8,10,0x4a0020)

def face_love():
    clear_face()
    draw_heart(EL[0],EL[1],10,PINK)
    draw_heart(ER[0],ER[1],10,PINK)
    draw_arc(MX,MY-8,24,10,170,PINK,3)
    Lcd.fillCircle(30,20,5,PINK)
    Lcd.fillCircle(210,20,5,PINK)

def face_breathe_in():
    clear_face()
    draw_arc(EL[0],EL[1]+2,11,210,330,WHITE,2)
    draw_arc(ER[0],ER[1]+2,11,210,330,WHITE,2)
    Lcd.drawLine(MX-12,MY,MX+12,MY,GOLD)
    Lcd.drawLine(MX-12,MY+1,MX+12,MY+1,GOLD)
    Lcd.fillCircle(EL[0]-8,MY-6,10,0x3a0830)
    Lcd.fillCircle(ER[0]+8,MY-6,10,0x3a0830)
    Lcd.setTextColor(GREEN,BG); Lcd.setTextSize(1)
    Lcd.setCursor(W//2-14,8); Lcd.print("*IN*")

def face_breathe_out():
    clear_face()
    draw_arc(EL[0],EL[1]+2,11,210,330,WHITE,2)
    draw_arc(ER[0],ER[1]+2,11,210,330,WHITE,2)
    Lcd.drawCircle(MX,MY,10,CYAN)
    Lcd.drawCircle(MX,MY,11,CYAN)
    Lcd.setTextColor(CYAN,BG); Lcd.setTextSize(1)
    Lcd.setCursor(W//2-18,8); Lcd.print("*OUT*")

FACES = {
    'IDLE':face_idle,'AWAKE':face_awake,'THINK':face_think,
    'HAPPY':face_happy,'LOVE':face_love,
    'BREATHE_IN':face_breathe_in,'BREATHE_OUT':face_breathe_out,
}
def set_face(name):
    if name in FACES: FACES[name]()

# ═══════════════════════════════════════════════════════════
#  专属屏幕
# ═══════════════════════════════════════════════════════════
def screen_category():
    Lcd.clear(BG)
    Lcd.setTextColor(PURPLE,BG); Lcd.setTextSize(1)
    Lcd.setCursor(8,8); Lcd.print("-- 选择占卜类型 --")
    Lcd.drawLine(0,22,W,22,PURPLE)
    for i,cat in enumerate(CATS):
        y = 26+i*22
        if i == cat_idx:
            Lcd.fillRect(4,y,W-8,20,0x181830)
            Lcd.setTextColor(CAT_COLORS[i],0x181830)
            Lcd.setTextSize(2); Lcd.setCursor(14,y+2)
            Lcd.print("> "+cat)
        else:
            Lcd.setTextColor(0x2a2a4a,BG)
            Lcd.setTextSize(1); Lcd.setCursor(22,y+6)
            Lcd.print(cat)
    Lcd.drawLine(0,H-16,W,H-16,DARK)
    Lcd.setTextColor(0x3a3a5a,BG); Lcd.setTextSize(1)
    Lcd.setCursor(6,H-12); Lcd.print("A:切换  B:确认")

def screen_pick(cat):
    Lcd.clear(BG)
    Lcd.setTextColor(PURPLE,BG); Lcd.setTextSize(1)
    Lcd.setCursor(8,8); Lcd.print("-- 能量感应中 --")
    Lcd.drawLine(0,22,W,22,PURPLE)
    col = GOLD
    for i,c in enumerate(CATS):
        if c == cat: col = CAT_COLORS[i]; break
    Lcd.setTextColor(col,BG); Lcd.setTextSize(3)
    Lcd.setCursor(max(8, W//2-len(cat)*12), 33); Lcd.print(cat)
    for i in range(3):
        Lcd.fillCircle(88+i*22,82,6,PURPLE)
        Lcd.drawCircle(88+i*22,82,8,0x2a2a4a)
    Lcd.setTextColor(CYAN,BG); Lcd.setTextSize(1)
    Lcd.setCursor(8,98); Lcd.print("伸手感应 握拳锁定")
    Lcd.drawLine(0,H-16,W,H-16,DARK)
    Lcd.setTextColor(0x3a3a5a,BG); Lcd.setTextSize(1)
    Lcd.setCursor(6,H-12); Lcd.print("A:---  B:返回")

def screen_picked(count):
    Lcd.clear(BG)
    Lcd.setTextColor(GOLD,BG); Lcd.setTextSize(1)
    Lcd.setCursor(8,10); Lcd.print("已抽到:")
    Lcd.setTextColor(WHITE,BG); Lcd.setTextSize(3)
    Lcd.setCursor(W//2-28,38); Lcd.print(str(count)+"/3")
    for i in range(3):
        cx=70+i*52; cy=90
        if i < count:
            Lcd.fillCircle(cx,cy,10,PURPLE); Lcd.fillCircle(cx,cy,5,GOLD)
        else:
            Lcd.drawCircle(cx,cy,10,0x2a2a4a)
    if count >= 3:
        Lcd.setTextColor(GREEN,BG); Lcd.setTextSize(1)
        Lcd.setCursor(50,108); Lcd.print("命运已定！")

# ═══════════════════════════════════════════════════════════
#  串口
# ═══════════════════════════════════════════════════════════
rx_buffer = ''
def send(msg): print(msg)

def process_command(cmd):
    global mode, cat_idx, current_cat
    cmd = cmd.strip()

    if   cmd == 'PING':            send('PONG')
    elif cmd == 'MODE:CATEGORY':   mode='CATEGORY'; screen_category()
    elif cmd == 'MODE:PICK':       mode='PICK'; screen_pick(current_cat)
    elif cmd == 'MODE:IDLE':       mode='IDLE'; set_face('AWAKE')
    elif cmd.startswith('PICKED:'):
        n = int(cmd[7:]); screen_picked(n)
        if n >= 3:
            set_strip('RAINBOW')
            M5.Speaker.tone(440,120); time.sleep_ms(150)
            M5.Speaker.tone(660,120); time.sleep_ms(150)
            M5.Speaker.tone(880,250)
    elif cmd.startswith('FACE:'):  set_face(cmd[5:])
    elif cmd == 'BREATHE:IN':      set_face('BREATHE_IN'); set_strip('BREATHE')
    elif cmd == 'BREATHE:OUT':     set_face('BREATHE_OUT'); set_strip('BREATHE')
    elif cmd == 'BREATHE:DONE':    set_face('HAPPY'); set_strip('WARM')
    elif cmd.startswith('STRIP:'):
        arg = cmd[6:].upper()
        if ',' in arg:
            p=arg.split(','); strip_fill(int(p[0]),int(p[1]),int(p[2]))
            global strip_mode; strip_mode='STATIC'
        else:
            set_strip(arg)
    elif cmd.startswith('VIBE:'):
        try: M5.Speaker.tone(200, int(cmd[5:]))
        except: pass

# ═══════════════════════════════════════════════════════════
#  启动
# ═══════════════════════════════════════════════════════════
time.sleep_ms(200)
screen_category()   # 上电显示分类选择
time.sleep_ms(300)
send('READY')

while True:
    M5.update()
    update_strip()

    if M5.BtnA.wasPressed():
        if mode == 'CATEGORY':
            cat_idx = (cat_idx+1) % len(CATS)
            screen_category()
            colors = {'财运':(80,50,0),'学业':(0,40,80),'情感':(80,0,40),'综合':(0,60,20)}
            c = colors.get(CATS[cat_idx],(40,0,80))
            strip_fill(*c)
            # --- 修复处 1: 删掉前面的 global 关键字 ---
            strip_mode = 'STATIC' 
        else:
            send('EVT:BTN_A')

    if M5.BtnB.wasPressed():
        if mode == 'CATEGORY':
            current_cat = CATS[cat_idx]
            send('EVT:CAT:'+current_cat)
            mode = 'PICK'
            screen_pick(current_cat)
            set_strip('PULSE')
        elif mode == 'PICK':
            mode = 'CATEGORY'
            screen_category()
            send('EVT:CAT_CANCEL')
            set_strip('OFF')
        else:
            send('EVT:BTN_B')

    # --- 修复处 2: 将 selectselect 改为 select.select ---
    if select.select([sys.stdin],[],[],0)[0]:
        char = sys.stdin.read(1)
        if char in ('\n','\r'):
            if rx_buffer: 
                process_command(rx_buffer)
                rx_buffer = ''
        else:
            rx_buffer += char
            if len(rx_buffer) > 128: rx_buffer = ''

    time.sleep_ms(20)