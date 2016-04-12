from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time

packageName = 'ru.rambler.mail'
activity = 'ru.rambler.mail.StartActivity'
apkName = 'rambler_mail-prod-debug-unaligned_1.apk'
device = MonkeyRunner.waitForConnection()

CORRECT_EMAIL_DATA = 'testyelosh'
CORRECT_PASSWORD_DATA = 'Cfd56ao199204'
INCORRECT_EMAIL_DATA = '@*$&&!_%*&_'
INCORRECT_PASSWORD_DATA = 'dsfsdgsdgsd'
TIME_OF_SLEEP_WHERE_TAKE_SNAPSHOT = 3
TIME_OF_SLEEP_WHERE_CLEAR = 2
NAME = "jdklf*#@)(48#&)@_**("
SIGNATURE = "jdklf*#@)(48#&)@_**(<SCRIPT>"


#Take snapshot from your screen
def snpShot(file):
    time.sleep(TIME_OF_SLEEP_WHERE_TAKE_SNAPSHOT) 
    res = device.takeSnapshot()
    time.sleep(TIME_OF_SLEEP_WHERE_TAKE_SNAPSHOT) 
    res.writeToFile(file, 'png')
    time.sleep(TIME_OF_SLEEP_WHERE_TAKE_SNAPSHOT) 
    
#Clear all textbox field from your activity    
def clearField(x,y):
    device.touch(x, y, MonkeyDevice.DOWN_AND_UP)
    device.type('')
    time.sleep(TIME_OF_SLEEP_WHERE_CLEAR) 
    
    
#Scrool Down on your activity screen    
def scrollFunction(x,y, diffValue, duration, steps):
    device.drag ((x, y), (x, y - diffValue), duration, steps)        


def openSettings():   
    device.touch(40, 87, MonkeyDevice.DOWN_AND_UP)
    time.sleep(3) 
    device.touch(400, 75, MonkeyDevice.DOWN_AND_UP)
    time.sleep(3)   
    
    
#Back to Autorization form    
def backToAutorizationForm():
    device.touch(40, 87, MonkeyDevice.DOWN_AND_UP)
    time.sleep(3) 
    device.touch(400, 75, MonkeyDevice.DOWN_AND_UP)
    time.sleep(3) 
    scrollFunction(300,800, 300, 1.0, 80)
    time.sleep(2) 
    device.touch(173, 780, MonkeyDevice.DOWN_AND_UP)
    time.sleep(8)     
    
    
#Start main activity        
def startActivityRamblerMail():
    time.sleep(2)
    device.installPackage(apkName)
    runComponent = packageName + '/' + activity
    device.startActivity(component=runComponent)
    snpShot('ScreenShotsMail/test1.png')


#Test - Check login with correct data (C255 on TestRail)    
def testClickOnLoginButtonWithCorrectData():
    device.touch(80, 360, MonkeyDevice.DOWN_AND_UP)    
    clearField(80,360)
    device.type(CORRECT_EMAIL_DATA)
    device.touch(70, 470, MonkeyDevice.DOWN_AND_UP)    
    clearField(70,470)    
    device.type(CORRECT_PASSWORD_DATA)
    time.sleep(0.5) 
    device.touch(260, 370, MonkeyDevice.DOWN_AND_UP)
    snpShot('ScreenShotsMail/Login_With_Correct_Data.png')  
    
    
def testOpenSettings():    
    openSettings()   
    

def testUpdateName():
    device.touch(50, 285, MonkeyDevice.DOWN_AND_UP)
    device.touch(90, 480, MonkeyDevice.DOWN)    
    clearField(90, 325)
    device.type(NAME)
    time.sleep(0.5)
    device.touch(460, 600, MonkeyDevice.DOWN_AND_UP)
    time.sleep(0.5)
    snpShot('ScreenShotsMail/Updated_name.png')  
    
def testUpdateSignature():
    device.touch(50, 410, MonkeyDevice.DOWN_AND_UP)
    device.touch(90, 480, MonkeyDevice.DOWN)    
    clearField(90, 325)
    device.type(SIGNATURE)
    device.touch(460, 600, MonkeyDevice.DOWN_AND_UP)
    time.sleep(0.5)
    snpShot('ScreenShotsMail/Updated_signature.png')  
    
def testNotifications():
    device.touch(490, 550, MonkeyDevice.DOWN_AND_UP)
    snpShot('ScreenShotsMail/Updated_notif_1.png')    
    device.touch(490, 550, MonkeyDevice.DOWN_AND_UP)
    snpShot('ScreenShotsMail/Updated_notif_2.png')   
    
      
startActivityRamblerMail()
testClickOnLoginButtonWithCorrectData()
testOpenSettings()
testUpdateName()
testUpdateSignature()
testNotifications()