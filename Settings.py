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
    #for i in range(1, 11):
        #device.touch(x, y + 30 * i, MonkeyDevice.DOWN)
        #time.sleep(2)
    device.drag ((x, y), (x, y - diffValue), duration, steps)        

    
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


#Test - Click on login button without data (C253 on TestRail)
def testClickOnLoginButtonWithoutData():
    device.touch(260, 550, MonkeyDevice.DOWN_AND_UP)
    snpShot('ScreenShotsMail/Login_Without_Data.png')


#Test - Check registration button (C31684 on TestRail)
def testClickOnRegistrationButtonAndClickBack():
    device.touch(390, 900, MonkeyDevice.DOWN_AND_UP)
    time.sleep(2) 
    device.touch(55, 80, MonkeyDevice.DOWN_AND_UP)
    time.sleep(2) 
    
#Test - Check login with incorrect data (C247 on TestRail)    
def testClickOnLoginButtonWithIncorrectData():
    device.touch(80, 360, MonkeyDevice.DOWN_AND_UP)    
    device.type(INCORRECT_EMAIL_DATA)
    device.touch(70, 470, MonkeyDevice.DOWN_AND_UP)        
    device.type(INCORRECT_PASSWORD_DATA)
    time.sleep(0.5) 
    device.touch(260, 370, MonkeyDevice.DOWN_AND_UP)
    snpShot('ScreenShotsMail/Login_With_Incorrect_Data.png')    
    
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
    backToAutorizationForm()
    
#Test - Check login without  email (C253 on TestRail)    
def testClickOnLoginButtonWithoutEmail():
    device.touch(80, 360, MonkeyDevice.DOWN_AND_UP)    
    clearField(80, 360)
    device.touch(70, 470, MonkeyDevice.DOWN_AND_UP)    
    clearField(70, 470)    
    device.type(CORRECT_PASSWORD_DATA)
    device.touch(260, 370, MonkeyDevice.DOWN_AND_UP)
    snpShot('ScreenShotsMail/Login_Without_Email.png')    

#Test - Check login without  password (C253 on TestRail)        
def testClickOnLoginButtonWithoutPassword():
    device.touch(80, 360, MonkeyDevice.DOWN_AND_UP)    
    clearField(80, 360)
    device.type(CORRECT_EMAIL_DATA)
    device.touch(70, 470, MonkeyDevice.DOWN_AND_UP)    
    time.sleep(0.5) 
    clearField(70, 470)     
    device.touch(260, 370, MonkeyDevice.DOWN_AND_UP)
    snpShot('ScreenShotsMail/Login_Without_Password.png')    

    
startActivityRamblerMail()
testClickOnLoginButtonWithoutData()
testClickOnRegistrationButtonAndClickBack()
testClickOnLoginButtonWithIncorrectData()
testClickOnLoginButtonWithCorrectData()
testClickOnLoginButtonWithoutEmail()
testClickOnLoginButtonWithoutPassword()