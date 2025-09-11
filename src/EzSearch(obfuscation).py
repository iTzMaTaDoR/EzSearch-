import sys,os,json,platform,subprocess
from pathlib import Path
from time import monotonic,sleep
from PyQt5.QtCore import Qt,QThread,pyqtSignal,QTimer,QPropertyAnimation,QRect
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton,QListWidget,QListWidgetItem,QFileDialog,QMessageBox,QSplitter,QFrame,QAction,QMenu,QToolButton

X1="EzSearch"
X2=Path.home()/f".{X1.lower()}_data.json"

def F1(F2):
 try:
  P=platform.system()
  os.startfile(F2) if P=="Windows" else subprocess.Popen(["open",F2]) if P=="Darwin" else subprocess.Popen(["xdg-open",F2])
 except Exception as e: QMessageBox.critical(None,"Error",f"Cannot open: {e}")

def F3(F4):
 try:
  P=platform.system()
  subprocess.Popen(["explorer","/select,",F4]) if P=="Windows" else subprocess.Popen(["open","-R",F4]) if P=="Darwin" else subprocess.Popen(["xdg-open",os.path.dirname(F4)])
 except Exception as e: QMessageBox.critical(None,"Error",f"Cannot reveal: {e}")

class T1(QThread):
 sB=pyqtSignal(list)
 sD=pyqtSignal(int)
 def __init__(self,R,Q,C):
  super().__init__()
  self.R=R
  self.Q=Q.lower()
  self.C=C
 def run(self):
  F=0
  B=[]
  for r in self.R:
   if self.C.is_set(): break
   for D,DN,FN in os.walk(r):
    if self.C.is_set(): break
    for f in FN:
     if self.C.is_set(): break
     if self.Q in f.lower():
      P=os.path.join(D,f)
      B.append(P)
      F+=1
      if len(B)>=50: self.sB.emit(B.copy());B.clear()
  if B: self.sB.emit(B.copy());B.clear()
  self.sD.emit(F)

class T2(QPushButton):
 def __init__(self,T="",I=None):
  super().__init__(T)
  I and self.setIcon(I)
  self.setCursor(Qt.PointingHandCursor)
  self.setStyleSheet("""QPushButton {background: qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 #00d4ff, stop:1 #0066ff);color: #000;border-radius: 10px;padding: 10px 18px;font-weight: 600;} QPushButton:hover {transform: translateY(-1px);}""")

class T3(QWidget):
 def __init__(self):
  super().__init__()
  self.setWindowTitle(X1)
  self.setAttribute(Qt.WA_TranslucentBackground,False)
  self.DA={"history":[],"favorites":[]}
  self.LD()
  self.CF=None
  self.TH=None
  self.LQ=0.0
  self.UI()
  self.SC()
 
 def LD(self):
  try:
   if X2.exists():
    with open(X2,"r",encoding="utf-8") as f: self.DA=json.load(f)
  except: self.DA={"history":[],"favorites":[]}
 
 def SD(self):
  try:
   with open(X2,"w",encoding="utf-8") as f: json.dump(self.DA,f,ensure_ascii=False,indent=2)
  except: pass
 
 def UI(self):
  self.setFont(QFont("Segoe UI",10))
  self.setMinimumSize(900,600)
  self.showMaximized()
  L1=QVBoxLayout();L1.setContentsMargins(16,16,16,16);L1.setSpacing(12)
  H1=QHBoxLayout()
  L2=QLabel("🔎");L2.setFont(QFont("Segoe UI Emoji",24));L2.setFixedWidth(48)
  T1Lbl=QLabel("EzSearch");T1Lbl.setFont(QFont("Segoe UI",20,QFont.Bold));T1Lbl.setStyleSheet("color: #00ffd5;")
  H1.addWidget(L2,alignment=Qt.AlignLeft);H1.addWidget(T1Lbl,alignment=Qt.AlignLeft);H1.addStretch()
  self.TB=QToolButton();self.TB.setText("🌙");self.TB.setCursor(Qt.PointingHandCursor);self.TB.clicked.connect(self.TT);H1.addWidget(self.TB)
  L1.addLayout(H1)
  self.SI=QLineEdit();self.SI.setPlaceholderText("Type file name or keyword...");self.SI.setStyleSheet("QLineEdit {padding:12px;border-radius:12px;background:#12141a;color:#eaf6ff;border:2px solid #1f6f9f;} QLineEdit:focus {border:2px solid #00ffd5;}");self.SI.textChanged.connect(self.ST)
  self.BB=T2("Browse");self.BB.clicked.connect(self.BF)
  self.BC=T2("Clear");self.BC.clicked.connect(self.CR)
  L3=QHBoxLayout();L3.addWidget(self.SI,stretch=1);L3.addWidget(self.BB);L3.addWidget(self.BC);L1.addLayout(L3)
  self.setLayout(L1)
 
 def SC(self):
  self.SI.setFocus()
 
 def TT(self):
  self.TB.setText("☀️" if self.TB.text()=="🌙" else "🌙")
 
 def ST(self,text):
  self.LQ=monotonic()
  # Debounce logic, thread start etc. here (can be similarly obfuscated)
 
 def BF(self):
  folder=QFileDialog.getExistingDirectory(self,"Select folder")
  if folder: pass
 
 def CR(self):
  if self.CF and not self.CF.is_set(): self.CF.set()

if __name__=="__main__":
 app=QApplication(sys.argv);app.setApplicationName(X1)
 w=T3();w.show();sys.exit(app.exec_())
