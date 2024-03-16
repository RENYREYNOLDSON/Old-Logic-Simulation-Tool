
import pygame
import sys,random,math,os,csv
from pygame.locals import*

pygame.init()

infoObject=pygame.display.Info()
screen=pygame.display.set_mode((1600,900))
pygame.display.set_caption("Logic Gates and Circuits, Simulation Software Prototype")
clock=pygame.time.Clock()

iconImg=pygame.image.load("icon.png").convert_alpha()
pygame.display.set_icon(iconImg)

andImg=pygame.image.load("and.png").convert_alpha()
orImg=pygame.image.load("or.png").convert_alpha()
notImg=pygame.image.load("not.png").convert_alpha()
switchImg=pygame.image.load("switch.png").convert_alpha()
switchOffImg=pygame.image.load("switchOff.png").convert_alpha()
lightOnImg=pygame.image.load("lightOn.png").convert_alpha()
lightOffImg=pygame.image.load("lightOff.png").convert_alpha()
wiresImg=pygame.image.load("wires.png").convert_alpha()
mouseImg=pygame.image.load("mouse.png").convert_alpha()
inputImg=pygame.image.load("input.png").convert_alpha()
outputImg=pygame.image.load("output.png").convert_alpha()
textImg=pygame.image.load("text.png").convert_alpha()
complexImg=pygame.image.load("complex.png").convert_alpha()
themeImg=pygame.image.load("theme.png").convert_alpha()
pulseImg=pygame.image.load("pulse.png").convert_alpha()
buttonImg=pygame.image.load("button.png").convert_alpha()
buttonOnImg=pygame.image.load("buttonOn.png").convert_alpha()
speakerOffImg=pygame.image.load("speakerOff.png").convert_alpha()
speakerOnImg=pygame.image.load("speakerOn.png").convert_alpha()
exitImg=pygame.image.load("exit.png").convert_alpha()
fullscreenImg=pygame.image.load("fullscreen.png").convert_alpha()
clearImg=pygame.image.load("clear.png").convert_alpha()
bufferImg=pygame.image.load("buffer.png").convert_alpha()
handImg=pygame.image.load("hand.png").convert_alpha()
nandImg=pygame.image.load("nand.png").convert_alpha()
norImg=pygame.image.load("nor.png").convert_alpha()
xorImg=pygame.image.load("xor.png").convert_alpha()
saveImg=pygame.image.load("save.png").convert_alpha()
loadImg=pygame.image.load("load.png").convert_alpha()

##Display Images
displayImg=pygame.image.load("display.png").convert_alpha()
display0Img=pygame.image.load("display0.png").convert_alpha()
display1Img=pygame.image.load("display1.png").convert_alpha()
display2Img=pygame.image.load("display2.png").convert_alpha()
display3Img=pygame.image.load("display3.png").convert_alpha()
display4Img=pygame.image.load("display4.png").convert_alpha()
display5Img=pygame.image.load("display5.png").convert_alpha()
display6Img=pygame.image.load("display6.png").convert_alpha()
display7Img=pygame.image.load("display7.png").convert_alpha()
display8Img=pygame.image.load("display8.png").convert_alpha()
display9Img=pygame.image.load("display9.png").convert_alpha()

beep=pygame.mixer.Sound("beep.wav")

mousex,mousey=0,0 #Position of the mouse
selected=""       #Holds name of the item selected
clicked=False     #True if the left mouse button has just been clicked
rightClick=False  #True if the right mouse button has just been clicked
mouseDown=False   #True if either mouse button is held down
downx,downy=0,0#Location where the mouse button first went down
gateIndex=0#The number/ID of the next item to be placed
startIndex,endIndex="",""#Index of the item a wire starts and ends at
outputIndex,inputIndex="",""#The index of a wires input and output
textx,texty=-100,-100#Sets location of informational text
currentText=""#String which holds information about items
theme=False#True if dark mode is enabled
fullscreen=False#True if fullscreen is enabled
font= pygame.font.Font('freesansbold.ttf', 15)##font


class Gate():#Main Gate Parent Class
    def __init__(self):#Constructor
        self.x=mousex-25#Item goes to mouse 
        self.y=mousey-25
        self.type=selected#Sets the gates type to selected item
        self.index=gateIndex#Sets new gates index to the gateIndex
        self.state=0#Sets gate to a negative state
        
class andGate(Gate):# AND gate class inherites Gate
    def __init__(self):#AND gate constructor as more attributes needed
        Gate.__init__(self)#Uses the Gate constructor
        self.outputs=[["free",25,0],["Full",0,0]]#Output availability and pixel locations
        self.inputs=[["free",34,49],["free",16,49]]#Input availability and pixel locations
        #Each in form [free?, x, y]
        
    def draw(self):# Draw AND gate method
        screen.blit(andImg,(self.x,self.y))#Draw andImg to the display
    def checkOn(self):#Check the state method
        state1=0#Temporary counter variable
        for i in wireList:
            if i.endIndex==self.index:#If a wire ends at this gate
                if i.state==1:
                    state1+=1#If the wires state is 1, add to state1
        if state1==2:
            return True#If both inputs 1 return True
        else:
            return False#Else return False

class Nand(Gate):
    def __init__(self):
        Gate.__init__(self)
        self.outputs=[["free",25,0],["Full",0,0]]
        self.inputs=[["free",34,49],["free",16,49]]
    def draw(self):
        screen.blit(nandImg,(self.x,self.y))
    def checkOn(self):
        state1=0
        for i in wireList:
            if i.endIndex==self.index:
                if i.state==1:
                    state1+=1
        if state1==2:
            return False
        else:
            return True
        

class orGate(Gate):
    def __init__(self):
        Gate.__init__(self)
        self.outputs=[["free",25,0],["Full",0,0]]
        self.inputs=[["free",34,49],["free",16,49]]
    def draw(self):
        screen.blit(orImg,(self.x,self.y))
    def checkOn(self):
        state1=0
        for i in wireList:
            if i.endIndex==self.index:
                if i.state==1:
                    state1+=1
        if state1>=1:
            return True
        else:
            return False

class Nor(Gate):
    def __init__(self):
        Gate.__init__(self)
        self.outputs=[["free",25,0],["Full",0,0]]
        self.inputs=[["free",34,49],["free",16,49]]
    def draw(self):
        screen.blit(norImg,(self.x,self.y))
    def checkOn(self):
        state1=0
        for i in wireList:
            if i.endIndex==self.index:
                if i.state==1:
                    state1+=1
        if state1>=1:
            return False
        else:
            return True

class Xor(Gate):
    def __init__(self):
        Gate.__init__(self)
        self.outputs=[["free",25,0],["Full",0,0]]
        self.inputs=[["free",34,49],["free",16,49]]
    def draw(self):
        screen.blit(xorImg,(self.x,self.y))
    def checkOn(self):
        state1=0
        for i in wireList:
            if i.endIndex==self.index:
                if i.state==1:
                    state1+=1
        if state1==1:
            return True
        else:
            return False

class notGate(Gate):
    def __init__(self):
        Gate.__init__(self)
        self.outputs=[["free",25,0],["Full",0,0]]
        self.inputs=[["free",25,49]]
    def draw(self):
        screen.blit(notImg,(self.x,self.y))
    def checkOn(self):
        state1=0
        for i in wireList:
            if i.endIndex==self.index:
                if i.state==1:
                    return False
                else:
                    return True


class Buffer(Gate):
    def __init__(self):
        Gate.__init__(self)
        self.outputs=[["free",25,0],["Full",0,0]]
        self.inputs=[["free",25,49]]
    def draw(self):
        screen.blit(bufferImg,(self.x,self.y))
    def checkOn(self):
        state1=0
        for i in wireList:
            if i.endIndex==self.index:
                if i.state==1:
                    return True
                else:
                    return False
                
class Pulse(Gate):
    def __init__(self):
        Gate.__init__(self)
        self.outputs=[["free",25,25],["Full",0,0]]
        self.inputs=[["Full",25,49]]
        self.count=0
    def draw(self):
        screen.blit(pulseImg,(self.x,self.y))
        self.count+=1
    def checkOn(self):
        if self.count>=60:
            self.count=0
        if self.count>=30:
            return True
        return False

class Button(Gate):
    def __init__(self):
        Gate.__init__(self)
        self.outputs=[["free",25,25],["Full",0,0]]
        self.inputs=[["Full",25,49]]
        self.down=11
    def draw(self):
        if self.down<=5:
            screen.blit(buttonOnImg,(self.x,self.y))
        else:
            screen.blit(buttonImg,(self.x,self.y))
        
    def checkOn(self):
        if clicked==True and collide(mousex,mousey,self.x,self.y,50,50) and selected=="mouse":
            self.down=0
        if self.down<=5:
            self.down+=1
            return True
        return False
    
                
class complexGate(Gate):
    def __init__(self):
        Gate.__init__(self)
        self.gateList=gateListCopy.copy()
        self.wireList=wireListCopy.copy()
        self.outputs=[]
        self.inputs=[]
        
        inCount,outCount=0,0
        for i in gateListCopy:
            if i.type=="light":
                outCount+=1
            elif i.type=="switch":
                inCount+=1
                
        for i in range(outCount):
            item=["free",(50/(outCount+1))*(i+1),5]
            self.outputs.append(item)
        for i in range(inCount):
            item=["free",(50/(inCount+1))*(i+1),45]
            self.inputs.append(item)


    def draw(self):
        screen.blit(complexImg,(self.x,self.y))
        for i in self.outputs:
            pygame.draw.line(screen,(0,0,0),(self.x+i[1],self.y+0),(self.x+i[1],self.y+i[2]),2)
        for i in self.inputs:
            pygame.draw.line(screen,(0,0,0),(self.x+i[1],self.y+50),(self.x+i[1],self.y+i[2]),2)
    def checkOn(self):
        pass

            

class Switch(Gate):
    def __init__(self):
        Gate.__init__(self)
        self.outputs=[["free",25,25],["Full",0,0]]
        self.inputs=[["Full",34,49]]
        self.state=0
        
    def draw(self):
        if self.state==1:
            screen.blit(switchImg,(self.x,self.y))
        else:
            screen.blit(switchOffImg,(self.x,self.y))
            
    def checkOn(self):
        if self.state==1:
            return True
        else:
            return False

class Light(Gate):
    def __init__(self):
        Gate.__init__(self)
        self.outputs=[["Full",0,0]]
        self.inputs=[["free",25,49]]
        
    def draw(self):
        for i in wireList:
            if i.endIndex==self.index and i.state==1:
                screen.blit(lightOnImg,(self.x,self.y))
                return
        screen.blit(lightOffImg,(self.x,self.y))


        

class Display(Gate):
    def __init__(self):
        Gate.__init__(self)
        self.outputs=[["Full",0,0]]
        self.inputs=[["free",8,49],["free",18,49],["free",32,49],["free",42,49]]
    def draw(self):
        total=0
        for i in wireList:
            if i.endIndex==self.index and i.state==1:
                if i.endx-self.x==self.inputs[3][1]:
                    total+=1
                elif i.endx-self.x==self.inputs[2][1]:
                    total+=2
                elif i.endx-self.x==self.inputs[1][1]:
                    total+=4
                elif i.endx-self.x==self.inputs[0][1]:
                    total+=8
        screen.blit(displayImg,(self.x,self.y))
        if total==0:
            screen.blit(display0Img,(self.x,self.y))
        elif total==1:
            screen.blit(display1Img,(self.x,self.y))  
        elif total==2:
            screen.blit(display2Img,(self.x,self.y))
        elif total==3:
            screen.blit(display3Img,(self.x,self.y))
        elif total==4:
            screen.blit(display4Img,(self.x,self.y))
        elif total==5:
            screen.blit(display5Img,(self.x,self.y))
        elif total==6:
            screen.blit(display6Img,(self.x,self.y))
        elif total==7:
            screen.blit(display7Img,(self.x,self.y))
        elif total==8:
            screen.blit(display8Img,(self.x,self.y))
        elif total==9:
            screen.blit(display9Img,(self.x,self.y))
        

class Speaker(Gate):
    def __init__(self):
        Gate.__init__(self)
        self.outputs=[["Full",0,0]]
        self.inputs=[["free",25,49]]
        
    def draw(self):
        for i in wireList:
            if i.endIndex==self.index and i.state==1:
                beep.play()
                screen.blit(speakerOnImg,(self.x,self.y))
                return
        screen.blit(speakerOffImg,(self.x,self.y))
        #pygame.mixer.stop()


        









class Wire():
    def __init__(self,startx,starty,endx,endy):

        self.startx=startx
        self.starty=starty
        self.endx=endx
        self.endy=endy
        self.startIndex=startIndex
        self.endIndex=endIndex
        self.state=0

    def draw(self):
        if self.state==0:
            if theme==False:



                
                pygame.draw.line(screen,(0,0,0),(self.startx,self.starty),(self.endx,self.endy),4)
                pygame.draw.line(screen,(255,255,255),(self.startx,self.starty),(self.endx,self.endy),2)
            else:
                pygame.draw.line(screen,(0,0,0),(self.startx,self.starty),(self.endx,self.endy),4)
                pygame.draw.line(screen,(255,255,255),(self.startx,self.starty),(self.endx,self.endy),2)
        else:
            pygame.draw.line(screen,(0,0,0),(self.startx,self.starty),(self.endx,self.endy),4)
            pygame.draw.line(screen,(0,255,0),(self.startx,self.starty),(self.endx,self.endy),2)


        for i in gateList:
            if i.index==self.startIndex:

                if i.checkOn()==True:
                    self.state=1

                else:
                    self.state=0
                return

class Text():
    def __init__(self,text,x,y):
        self.text=text
        self.x=x
        self.y=y
        self.imgBlack=font.render(text,True,(0,0,0))
        self.imgWhite=font.render(text,True,(255,255,255))
    def draw(self):
        if theme==False:
            screen.blit(self.imgBlack,(self.x,self.y))
        else:
            screen.blit(self.imgWhite,(self.x,self.y))

        


def load():
    list1=[]
    list2=[]
    list3=[]
    with open("saves.csv","r") as file:
        reader=csv.reader(file)

        num=0
        for i in reader:
            for item in i:
                if num==0:
                    list1.append(item)
                elif num==1:
                    list2.append(item)
                elif num==2:
                    list3.append(item)

            num+=1
        return list1,list2,list3

def save():
    with open("saves.csv","w",newline="") as file:
        writer=csv.writer(file)
        writer.writerow((gateList))
        writer.writerow((wireList))
        writer.writerow((textList))

        file.close()








gateList=[]
wireList=[]
textList=[]
gateListCopy,wireListCopy=[],[]
def collide(checkx,checky,x,y,w,h):
    if checkx>x and checkx<x+w and checky>y and checky<y+h:
        return True
    else:
        return False

    
def drawMenu():
    global selected,gateList,wireList,gateListCopy,wireListCopy,theme,fullscreen,screen,textList
    if theme==False:
        pygame.draw.rect(screen,(200,200,200),(0,0,1600,80),0)
    else:
        pygame.draw.rect(screen,(100,100,100),(0,0,1600,80),0)
    
    pygame.draw.line(screen,(0,0,0),(0,80),(1600,80),4)
    screen.blit(andImg,(20,20))
    screen.blit(orImg,(80,20))
    screen.blit(notImg,(140,20))
    screen.blit(switchImg,(200,20))
    screen.blit(lightOffImg,(260,20))
    screen.blit(wiresImg,(320,20))
    screen.blit(mouseImg,(380,20))

    screen.blit(textImg,(560,20))
    screen.blit(complexImg,(620,20))
    screen.blit(pulseImg,(680,20))
    screen.blit(buttonImg,(740,20))
    screen.blit(speakerOffImg,(800,20))
    screen.blit(bufferImg,(860,20))
    screen.blit(handImg,(920,20))
    screen.blit(nandImg,(980,20))
    screen.blit(norImg,(1040,20))
    screen.blit(xorImg,(1100,20))
    screen.blit(displayImg,(1160,20))


    screen.blit(saveImg,(1220,20))
    screen.blit(loadImg,(1280,20))    
    screen.blit(clearImg,(1340,20))
    screen.blit(themeImg,(1400,20))
    screen.blit(fullscreenImg,(1460,20))
    screen.blit(exitImg,(1520,20))


    if collide(mousex,mousey,20,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(20,20,50,50),2)
        if clicked==True:
            selected="and"
    elif collide(mousex,mousey,80,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(80,20,50,50),2)
        if clicked==True:
            selected="or"
    elif collide(mousex,mousey,140,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(140,20,50,50),2)
        if clicked==True:
            selected="not"
    elif collide(mousex,mousey,200,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(200,20,49,49),2)
        if clicked==True:
            selected="switch"
            
    elif collide(mousex,mousey,260,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(260,20,50,50),2)
        if clicked==True:
            selected="light"
    elif collide(mousex,mousey,320,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(320,20,50,50),2)
        if clicked==True:
            selected="wires"
            
    elif collide(mousex,mousey,380,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(380,20,50,50),2)
        if clicked==True:
            selected="mouse"

    elif collide(mousex,mousey,560,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(560,20,50,50),2)
        if clicked==True:
            selected="text"
    elif collide(mousex,mousey,680,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(680,20,50,50),2)
        if clicked==True:
            selected="pulse"
    elif collide(mousex,mousey,740,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(740,20,50,50),2)
        if clicked==True:
            selected="button"
    elif collide(mousex,mousey,800,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(800,20,50,50),2)
        if clicked==True:
            selected="speaker"
    elif collide(mousex,mousey,860,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(860,20,50,50),2)
        if clicked==True:
            selected="buffer"
    elif collide(mousex,mousey,620,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(620,20,50,50),2)
        if clicked==True:
            selected="complex"
            gateListCopy=gateList.copy()
            wireListCopy=wireList.copy()
            gateList=[]
            for i in gateListCopy:
                if i.type=="complex":
                    gateList.append(i)
            wireList=[]
            
    elif collide(mousex,mousey,920,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(920,20,50,50),2)
        if clicked==True:
            selected="hand"
    elif collide(mousex,mousey,980,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(980,20,50,50),2)
        if clicked==True:
            selected="nand"
    elif collide(mousex,mousey,1040,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(1040,20,50,50),2)
        if clicked==True:
            selected="nor"
    elif collide(mousex,mousey,1100,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(1100,20,50,50),2)
        if clicked==True:
            selected="xor"
            
    elif collide(mousex,mousey,1160,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(1160,20,50,50),2)
        if clicked==True:
            selected="display"
            
    elif collide(mousex,mousey,1220,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(1220,20,50,50),2)
        if clicked==True:
            save()
            
    elif collide(mousex,mousey,1280,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(1280,20,50,50),2)
        if clicked==True:
            gateList,wireList,textList=load()

            
    elif collide(mousex,mousey,1340,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(1340,20,50,50),2)
        if clicked==True:
            gateList=[]
            textList=[]
            wireList=[]
    elif collide(mousex,mousey,1400,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(1400,20,50,50),2)
        if clicked==True:
            theme=not theme
    elif collide(mousex,mousey,1460,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(1460,20,50,50),2)
        if clicked==True:
            if fullscreen==False:
                screen=pygame.display.set_mode((1600,900),FULLSCREEN)
                fullscreen=True
            else:
                screen=pygame.display.set_mode((1600,900))
                fullscreen=False
    elif collide(mousex,mousey,1520,20,50,50):
        pygame.draw.rect(screen,(0,0,0),(1520,20,50,50),2)
        if clicked==True:
            pygame.quit()
            sys.exit()
            
    if selected=="and":
        screen.blit(andImg,(mousex-25,mousey-25))
    elif selected=="or":
        screen.blit(orImg,(mousex-25,mousey-25))
    elif selected=="not":
        screen.blit(notImg,(mousex-25,mousey-25))
    elif selected=="switch":
        screen.blit(switchImg,(mousex-25,mousey-25))
    elif selected=="light":
        screen.blit(lightOffImg,(mousex-25,mousey-25))
    elif selected=="wires":
        pygame.draw.rect(screen,(255,0,0),(320,20,50,50),2)
    elif selected=="mouse":
        pygame.draw.rect(screen,(255,0,0),(380,20,50,50),2)
    elif selected=="hand":
        pygame.draw.rect(screen,(255,0,0),(920,20,50,50),2)        
    elif selected=="complex":
        screen.blit(complexImg,(mousex-25,mousey-25))
    elif selected=="text":
        pygame.draw.rect(screen,(255,0,0),(560,20,50,50),2)
    elif selected=="pulse":
        screen.blit(pulseImg,(mousex-25,mousey-25))
    elif selected=="button":
        screen.blit(buttonImg,(mousex-25,mousey-25))
    elif selected=="speaker":
        screen.blit(speakerOffImg,(mousex-25,mousey-25))
    elif selected=="buffer":
        screen.blit(bufferImg,(mousex-25,mousey-25))
    elif selected=="nand":
        screen.blit(nandImg,(mousex-25,mousey-25))
    elif selected=="nor":
        screen.blit(norImg,(mousex-25,mousey-25))
    elif selected=="xor":
        screen.blit(xorImg,(mousex-25,mousey-25))
    elif selected=="display":
        screen.blit(displayImg,(mousex-25,mousey-25))
        
def placeItem():
    global gateIndex,startIndex,endIndex,outputIndex,inputIndex,gateList,wireList,textx,texty  
    for i in gateList:
        if collide(mousex,mousey,i.x-20,i.y-20,90,90)==True:
            pygame.draw.rect(screen,(0,0,0),(i.x,i.y,50,50),2)
            
            if rightClick==True and mousey>110:
                wireDelete=[]
                for out in i.outputs:
                    wireCount=0
                    for wire in wireList:
                        
                        if wire.startIndex==i.index:
                            
                            for i2 in gateList:
                                if i2.index==wire.endIndex:
                                    for inp in i2.inputs:
                                        if i2.x+inp[1]-wire.endx<5 and i2.y+inp[2]-wire.endy<5:
                                            inp[0]="free"
                                            already=False
                                            for w in wireDelete:
                                                if w==wireCount:
                                                    already=True
                                            if already==False:
                                                wireDelete.append(wireCount)
                        wireCount+=1
                        
                for w in range(len(wireDelete)):
                    wireList.pop(wireDelete[w]-w)

                    
                for inp in i.inputs:
                    for wire in wireList:
                        if wire.endIndex==i.index:
                            for i2 in gateList:
                                if i2.index==wire.startIndex:
                                    wireList.remove(wire)
                gateList.remove(i)
        
    if clicked==True and mousey>110:
        if selected=="and":
            gateList.append(andGate())
            gateIndex+=1
        elif selected=="or":
            gateList.append(orGate())
            gateIndex+=1
        elif selected=="not":
            gateList.append(notGate())
            gateIndex+=1
        elif selected=="switch":
            gateList.append(Switch())
            gateIndex+=1
        elif selected=="light":
            gateList.append(Light())
            gateIndex+=1
        elif selected=="mouse":
            for i in gateList:
                if collide(mousex,mousey,i.x,i.y,50,50):
                    i.state=not i.state
        elif selected=="text":
            textx=mousex
            texty=mousey

        elif selected=="complex":
            gateList.append(complexGate())
            gateIndex+=1
        elif selected=="pulse":
            gateList.append(Pulse())
            gateIndex+=1           
        elif selected=="button":
            gateList.append(Button())
            gateIndex+=1
        elif selected=="speaker":
            gateList.append(Speaker())
            gateIndex+=1
        elif selected=="buffer":
            gateList.append(Buffer())
            gateIndex+=1
        elif selected=="nand":
            gateList.append(Nand())
            gateIndex+=1
        elif selected=="nor":
            gateList.append(Nor())
            gateIndex+=1
        elif selected=="xor":
            gateList.append(Xor())
            gateIndex+=1
        elif selected=="display":
            gateList.append(Display())
            gateIndex+=1 

def placeWires():
    global startIndex,endIndex,outputIndex,inputIndex,wireList,gateList
    
    if selected=="wires":

        if clicked==True:
            if startIndex=="":
                for i in gateList:
                    if collide(mousex,mousey,i.x,i.y,50,50):

                        outputIndex=0
                        startIndex=i.index

            else:
                for i in gateList:
                    if collide(mousex,mousey,i.x,i.y,50,50):
                        inCount=0
                        for inp in i.inputs:
                            if inp[0]=="free":
                                inputIndex=inCount
                                endIndex=i.index
                            inCount+=1
                            
                if endIndex!="":
                    iCount=0
                    for i in gateList:
                        if i.index==startIndex:
                            tCount=0
                            for t in gateList:
                                if t.index==endIndex:
                                    wireList.append(Wire(gateList[iCount].x+gateList[iCount].outputs[outputIndex][1],gateList[iCount].y+gateList[iCount].outputs[outputIndex][2],
                                                         gateList[tCount].x+gateList[tCount].inputs[inputIndex][1],gateList[tCount].y+gateList[tCount].inputs[inputIndex][2]))
                                    if gateList[tCount].type!="light" and gateList[tCount].type!="speaker" :
                                        gateList[tCount].inputs[inputIndex][0]="Full"
                                    startIndex=""
                                    endIndex=""
                                    outputIndex=""
                                    inputIndex=""
                                    return
                                tCount+=1
                        iCount+=1


        if startIndex!="":
            number=0
            for i in gateList:
                if i.index==startIndex:
                    if theme==False:
                        pygame.draw.line(screen,(0,0,0),(gateList[number].x+gateList[number].outputs[outputIndex][1],gateList[number].y+gateList[number].outputs[outputIndex][2]),(mousex,mousey),4)
                        pygame.draw.line(screen,(255,255,255),(gateList[number].x+gateList[number].outputs[outputIndex][1],gateList[number].y+gateList[number].outputs[outputIndex][2]),(mousex,mousey),2)
                    else:
                        pygame.draw.line(screen,(255,255,255),(gateList[number].x+gateList[number].outputs[outputIndex][1],gateList[number].y+gateList[number].outputs[outputIndex][2]),(mousex,mousey),2)
                number+=1
            

    else:
        startIndex=""
        endIndex=""



def drawItems():
    for i in wireList:
        i.draw()
    for i in gateList:
        i.draw()
    for i in textList:
        i.draw()

    if selected=="text":
        t=font.render(currentText,True,(0,0,0))
        screen.blit(t,(textx,texty))
        pygame.draw.line(screen,(0,0,0),(textx-2,texty),(textx-2,texty+15),2)

def round_down(num,divisor):
    return num-(num%divisor)

def drawDrag():
    if mouseDown==True and mousey>85 and downy>85:
        if selected=="mouse":
            pygame.draw.rect(screen,(255,0,0),(downx,downy,mousex-downx,mousey-downy),2)
            for i in gateList:
                if collide(i.x+25,i.y+25,downx,downy,mousex-downx,mousey-downy)==True:
                    pygame.draw.rect(screen,(0,0,0),(i.x,i.y,50,50),2)
        elif selected=="hand":
            for i in gateList:
                i.x=i.x+(mousex-lastx)
                i.y=i.y+(mousey-lasty)
            for i in wireList:
                i.startx=i.startx+(mousex-lastx)
                i.starty=i.starty+(mousey-lasty)
                i.endx=i.endx+(mousex-lastx)
                i.endy=i.endy+(mousey-lasty)
            for i in textList:
                i.x=i.x+(mousex-lastx)
                i.y=i.y+(mousey-lasty)
def grid():
    colour=(5,56,107)
    if theme==False:
        colour=(230,230,230)
    for i in range(80):
        pygame.draw.line(screen,colour,(i*20,0),(i*20,900),2)
    for t in range(45):
        pygame.draw.line(screen,colour,(0,t*20),(1600,t*20),2)


lastx,lasty=0,0

while True:
    if theme==False:##Checks which theme to show
        screen.fill((255,255,255))
    else:
        screen.fill((0,51,102))
    grid()##Draws the grid
    drawItems()#Draws all placed items
    drawMenu()#Draws the software's menu
    placeItem()#Manages the placing of items
    placeWires()#Manages the placing of wires
    drawDrag()#Shows a draggable box
   
    clicked=False#Resets the mouse button variables
    rightClick=False
    lastx,lasty=mousex,mousey#Sets last position to current position of mouse
    
    for event in pygame.event.get():#Loops through all input events
        if event.type==QUIT:#If user quits, then program closes
            pygame.quit()
            sys.exit()
            
        elif event.type==pygame.MOUSEMOTION:#If mouse moves
            mousex,mousey=event.pos
            mousex=round_down(mousex,10)#Sets x and y then rounds down to the nearest 10, for the grid
            mousey=round_down(mousey,10)
            
        elif event.type==pygame.MOUSEBUTTONUP:#If mouse button released
            mousex,mousey=event.pos
            mousex=round_down(mousex,10)#Sets x and y then rounds down to the nearest 10, for the grid
            mousey=round_down(mousey,10)
            if event.button==1:#Left mouse button
                clicked=True
            elif event.button==3:#Right mouse button
                rightClick=True
            mouseDown=False#Mouse is no longer down
            
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouseDown=True#When mouse button goes down set down location to current location of mouse
            downx,downy=event.pos
            
        elif event.type==pygame.KEYDOWN:#If a key is pressed down
            if selected=="text":#Allows the user to type a comment
                if event.key==pygame.K_BACKSPACE:
                    currentText=currentText[:-1]#Removes last letter from string
                elif event.key==pygame.K_RETURN:
                    textList.append(Text(currentText,textx,texty))#Adds comment to textList
                    currentText=""
                    textx=-100#Resets relevant variables
                    texty=-100
                else:
                    currentText+=event.unicode#Add pressed key to the comment






##Add fullscreen button                   DONE
##Add exit button                         DONE
##Add clear button (drop down menu?)      DONE
##Add speaker?                            DONE
##Add buffer gate?                        DONE
##Create SHEET to covour components
##Add text for menu and binary
##Drop down menu items
##Add mute button
##Different colour wires/LED's
##Drag mouse to select multiple
##Organise all items
##Add more themes
##Add saving and loading files-----------
##Fix drag boxes
##Moving around                          DONE  
    pygame.display.update()
    clock.tick(60)




















    





























