#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), 2016_12_05_1336
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389
neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding
import json
import pandas as pd
from PIL import Image

from psychopy.iohub import launchHubServer
from psychopy import iohub

# create the process that will run in the background polling devices
io=launchHubServer()

# some default devices have been created that can now be used
display = io.devices.display
keyboard1 = io.devices.keyboard
mouse1=io.devices.mouse

# Hide the 'system mouse cursor'
mouse1.setSystemCursorVisibility(True)

reward1 = 3000
reward2 = 55000

rewardtime = 5.5
punish_time = 2 
channel = 1
ITI = 1500

required_wagering_time = 1.6


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'reversal_learning'  # from the Builder filename that created this script
expInfo = { u'monkey': u'SorM',u'listname': u'meta_day1_AS_160',u'conf_cut': 5000,u'high_or_low': 'high'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' %(expInfo['listname'],expInfo['monkey'], expName, expInfo['date'])


# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=False,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation


data_list={'image_left':[],'image_right':[],'start_touch':[],'rtime':[],'WT':[],'catch_ornot':[],'switch_ornot':[],
           'level':[],'side':[] ,'RT':[],'response':[],'ch':[],'task':[],'required_wagering_time':[],'response_type':[]}


# Setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "startpoint"

startpointClock = core.Clock()
reward_pauseClock = core.Clock()
punish_pauseClock = core.Clock()
EndClock = core.Clock()
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
mouse = event.Mouse(win=win)
x, y = [None, None]
#mouse.setPos((0,0))     #reset mouse on screen
event.clearEvents('mouse') #clear mouse position in ram
mouse.setVisible(0) #insure mouse not be seen

# Initialize components for Routine "test"
wt = core.Clock()
testClock = core.Clock()
reward_pauseClock = core.Clock()
ITIClock = core.Clock()




ISI_2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')


text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Press Space to Exit',    font='Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text=' ',    font=u'Arial',
    units=u'norm',
    pos=[0, 0], height= None, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

polygonleft = visual.Rect(win=win, name='polygonleft',
    width=[0.98, 0.98][0], height=[0.98, 0.98][1],
    ori=0, pos=[-0.55, 0],
    lineWidth=1, lineColor=[1,1,0], lineColorSpace='rgb',
    fillColor=[1,1,0], fillColorSpace='rgb',
    opacity=1,depth=1.0, 
interpolate=True)

polygon_cue_ind = visual.Rect(win=win, name='polygon_cue_ind',
    width=[0.98, 0.98][0], height=[0.98, 0.98][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,0], lineColorSpace='rgb',
    fillColor=[1,1,0], fillColorSpace='rgb',
    opacity=1,depth=4.0, 
interpolate=True)


polygonright = visual.Rect(win=win, name='polygonright',
    width=[0.98, 0.98][0], height=[0.98, 0.98][1],
    ori=0, pos=[0.55, 0],
    lineWidth=1, lineColor=[1,1,0], lineColorSpace='rgb',
    fillColor=[1,1,0], fillColorSpace='rgb',
    opacity=1,depth=1.0, 
interpolate=True)


polygon_cue = visual.Rect(win=win, name='polygon_cue',
    width=[0.75, 0.75][0], height=[0.75, 0.75][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1,depth=0.0, 
interpolate=True)


#leftsti = visual.Polygon(win=win, name='polygon',
#    edges = 90, size=[0.5, 0.8],
#    ori=0, pos=[0, 0],
#    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
#    fillColor=[1,1,1], fillColorSpace='rgb',
#    opacity=1,depth=-1.0, interpolate=True)

leftsti = visual.ImageStim(win=win, name='pic_left',
    image='sin', mask=None,
    ori=0, pos=[-0.62, 0], size=[0.8,0.8],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

image_left = 'Ppic_pool/clip_040.mp4-6.jpeg'
leftsti.setImage(image_left)

rightsti = visual.ImageStim(win=win, name='pic_left',
    image='sin', mask=None,
    ori=0, pos=[0.62, 0], size=[0.8,0.8],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
    
image_right = 'Ppic_pool/MP71.mp4-5.jpeg'
rightsti.setImage(image_right)

# Initialize components for Routine "reward_pause"

polygon_rd = visual.Rect(win=win, name='polygon',
    width=[0.75, 0.75][0], height=[0.75, 0.75][1],
    ori=0, pos=[0, 0],
    lineWidth=0, lineColor=[192,192,192], lineColorSpace='rgb',
    fillColor=[0,255,0], fillColorSpace='rgb',
    opacity=1,depth=0.0, 
interpolate=True)

# Create some handy timers

text = visual.TextStim(win=win, ori=0, name='text',
    text=u'\nstage: touch\n\nspace to start',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
routine_1Clock = core.Clock()

t = 0
routine_1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
routine_1Components = []
routine_1Components.append(key_resp_2)
routine_1Components.append(text)
for thisComponent in routine_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED


continueRoutine = True
while continueRoutine:
    # get current time
    t = routine_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "routine_1"-------
for thisComponent in routine_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)




##############################################
io.clearEvents('all')

###############################################

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('list_pool/AS/' + expInfo['listname'] + '.xlsx'),   ##'meta_list_pool/'+ expInfo['listname'] + '.xlsx'
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)




import socket 
host = "192.168.1.2"# set to IP address of target computer
if channel == 1:
    port = 13021
elif channel ==3:
    port =13023
addr = (host, port)
UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#n = 0

#swlist = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]
#swlist2 = swlist + swlist
#swlist3 = swlist2 + swlist2
#swlist4 = swlist3 + swlist3
#swlist5 = swlist4 +swlist3 +swlist2 + swlist

n = 0

pic_list=data.importConditions('list_pool/AS/'+ expInfo['listname'] + '.xlsx')


for thisTrial in trials:


    if n == 120: #gaga
        
        break

    
    position, posDelta = mouse1.getPositionAndDelta()
    mouse_dX,mouse_dY=posDelta
    left_button, middle_button, right_button = mouse1.getCurrentButtonStates()
    e1 = mouse1.getEvents(event_type=(iohub
                                    .EventConstants
                                    .MOUSE_BUTTON_PRESS))
    e2 = mouse1.getEvents(event_type=(iohub
                                    .EventConstants
                                    .MOUSE_BUTTON_RELEASE))
    


    #required_wagering_time = 3

    #sw = swlist5[n]
    #n = n + 1
    
    #currentpic = pic_list[n]
    
    #switch_ornot = currentpic.get(u'switch_ornot') #%(expInfo['subject'])
    #catch_ornot = currentpic.get(u'catch_ornot') #%(expInfo['subject'])
    #dist_onepeak = currentpic.get(u'dist_onepeak') #%(expInfo['subject'])

    
    currentpic = pic_list[n]
    print(currentpic)
    picture_1 = currentpic.get(u'picture_1')#%(expInfo['subject'])
    picture_2 = currentpic.get(u'picture_2') #%(expInfo['subject'])
    dist_onepeak = currentpic.get(u'dist_onepeak')
    switch_ornot =currentpic.get(u'catch_ornot')
    catch_ornot = currentpic.get(u'switch_ornot')
    ID = currentpic.get(u'ID')

    required_wagering_time = dist_onepeak
    
    n = n + 1
    
    
    if random()>0.50:
        correctAns = 1
        image_left = picture_1#%(expInfo['subject'])
        image_right = picture_2 #%(expInfo['subject'])
        leftsti.setImage(image_left)
        rightsti.setImage(image_right)
        
      #  if sw == 2:
      #      correctAns = - 1

    else:
        correctAns = -1
        image_left =picture_2 #%(expInfo['subject'])
        image_right = picture_1 #%(expInfo['subject'])
        leftsti.setImage(image_left)
        rightsti.setImage(image_right)
            
          #  if sw == 2:
          #      correctAns =  1
          
        
    pic1 = picture_1
    pic2 = picture_2
    print('correct:',picture_1,'incorrect:',picture_2,dist_onepeak,'ID',ID,switch_ornot)

    currentLoop = trials

############################################
    T1 = -999
    wt.reset()
    #T1 = wt.getTime()
    
    currentLoop = trials
    #t = trialClock.getTime()

###########################################

    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)


    #time_rd = 10000
    #ch_rd = 1
    #data_rd = str(time_rd)+str(ch_rd)


    #------Prepare to start Routine "startpoint"-------
    response = -1
    judge = 0
    t = 0
    startpointClock.reset()  # clock 
    frameN = -1

    startpointComponents = []
    #startpointComponents.append(mouse)
    startpointComponents.append(polygon_cue_ind)
    # keep track of which components have finished
    #startpointComponents = []
    startpointComponents.append(polygon_cue)
    for thisComponent in startpointComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "startpoint"-------
    continueRoutine = True
    while continueRoutine:
        
        position, posDelta = mouse1.getPositionAndDelta()
        mouse_dX,mouse_dY=posDelta
        left_button, middle_button, right_button = mouse1.getCurrentButtonStates()
        
        e1 = mouse1.getEvents(event_type=(iohub
                                .EventConstants
                                .MOUSE_BUTTON_PRESS))
        e2 = mouse1.getEvents(event_type=(iohub
                                .EventConstants
                                    .MOUSE_BUTTON_RELEASE))
        # get current time
        #t = testClock.getTime()
        t = startpointClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_3* updates
        if t >= 0.0 and polygon_cue.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_cue.tStart = t  # underestimates by a little under one frame
            polygon_cue.frameNStart = frameN  # exact frame index
            polygon_cue.setAutoDraw(True)
        # *mouse* updates

        if e1 :
            #t2 = testClock.getTime()
            #mouse.time.append(t)
            Delt = t# t2-t
            T1 = wt.getTime()
            x1, y1 = e1[0].x_position, e1[0].y_position
                
            if polygon_cue.contains((x1, y1), units='pix'):
                judge = 1
                side = -1
                time1 = e1[-1].time
                #polygon_cue_ind.setAutoDraw(True)
                response = 9


        T2 = wt.getTime()

        if T2-T1 >= 0.5 and response == 9 and judge == 1 :
        
            WT= T2 - T1
            response_type = 1 #high conf correct
            task = 0
            ch = channel
            start_touch = Delt
            side = 0  # or 8
            level= 0
            RT = 0
            #level= int((round(level, 6))*1000)
            #WT = int(WT*1000)
            #stepreward = 0.08
            rtime = reward1
            mylist = [start_touch, rtime, WT, level, side,RT, response, ch,required_wagering_time,response_type, task]
            json_string = json.dumps(mylist)
            #json_string = bytes(json_string,encoding="utf-8")
            UDPSock.sendto(json_string, addr)
            
            continueRoutine = False              

                    
        if  e2 :
            judge = 0
            #polygon_cue_ind.setAutoDraw(False)
            polygonleft.setAutoDraw(False)

        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still run.ning
        for thisComponent in startpointComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            trials.saveAsPickle(filename)
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "startpoint"-------
    for thisComponent in startpointComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    routineTimer.reset()

    level = 0
#    start_touch = 0





    # the Routine "startpoint" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()


    #------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock
    ITI_cue = 1 #ITI=ITI/1000
    frameN = -1

    routineTimer.add(1)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = []
    ITIComponents.append(ISI_2)
    ITIComponents.append(text_3)
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "ITI"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *ISI_2* period
        if t >= 0.0 and ISI_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_2.tStart = t  # underestimates by a little under one frame
            ISI_2.frameNStart = frameN  # exact frame index
            ISI_2.start(ITI_cue)
        elif ISI_2.status == STARTED: #one frame should pass before updating params and completing
            ISI_2.complete() #finish the static period

        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
            text_3.text='keys: %r'%(level)
        if text_3.status == STARTED and t >= (0.0 + (0.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_3.setAutoDraw(False)

        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "test"-------

    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    click = []
    cor_ans = []  
    
    
    t = 0
    testClock.reset()  # clock 
    frameN = -1

    judge = 0
    #mouse.setPos((0,0))     #reset mouse on screen
    event.clearEvents('mouse') #clear mouse position in ram
    mouse.setVisible(0) #insure mouse not be seen
    io.clearEvents('all')
    response = -1

    # set rewarding_time and channel

    
    # keep track of which components have finished
    testComponents = []
    testComponents.append(mouse)
    # keep track of which components have finished
    #testComponents = []
    testComponents.append(leftsti)
    testComponents.append(rightsti)
    testComponents.append(polygonleft)
    testComponents.append(polygonright)

    for thisComponent in testComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test"-------
    continueRoutine = True

    x1, y1 = [None, None]
    MISST = 9999
    key = 0
    relase = 0
    T1 = -999
    wt.reset()
    
    while continueRoutine:

        position, posDelta = mouse1.getPositionAndDelta()
        mouse_dX,mouse_dY=posDelta
        left_button, middle_button, right_button = mouse1.getCurrentButtonStates()
        e1 = mouse1.getEvents(event_type=(iohub
                                        .EventConstants
                                        .MOUSE_BUTTON_PRESS))
        e2 = mouse1.getEvents(event_type=(iohub
                                        .EventConstants
                                        .MOUSE_BUTTON_RELEASE))




        # get current time
        t = testClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        

        # *leftsti* updates
        if t >= 0.0 and leftsti.status == NOT_STARTED:
            # keep track of start time/frame for later
            leftsti.tStart = t  # underestimates by a little under one frame
            leftsti.frameNStart = frameN  # exact frame index
            leftsti.setAutoDraw(True)
        
        # *rightsti* updates
        if t >= 0.0 and rightsti.status == NOT_STARTED:
            # keep track of start time/frame for later
            rightsti.tStart = t  # underestimates by a little under one frame
            rightsti.frameNStart = frameN  # exact frame index
            rightsti.setAutoDraw(True)
        # *mouse* updates
        


        if e1 :
            if  side == -1:
                #polygonleft.setAutoDraw(True)
                rightsti.setAutoDraw(False)
            if side == 1:
                #polygonright.setAutoDraw(True)
                leftsti.setAutoDraw(False)
                
            #t2 = testClock.getTime()
            #mouse.time.append(t)
            #Delt = t# t2-t
            #T1 = wt.getTime()
            x1, y1 = e1[0].x_position, e1[0].y_position
            MISST = 999

            if correctAns == -1:
                
                if leftsti.contains((x1, y1), units='pix') and relase == 0 :

                    T1 = wt.getTime()
                    Delt = t
                    #T1 = wt.getTime()
                    judge = 1
                    side = -1
                    time1 = e1[-1].time
                    #polygonleft.setAutoDraw(True)
                    rightsti.setAutoDraw(False)
                    response = 1

                if rightsti.contains((x1, y1), units='pix') and relase == 0 :

                    T1 = wt.getTime()
                    Delt = t
                    judge = 1
                    side = 1
                    time1 = e1[-1].time
                    #polygonright.setAutoDraw(True)
                    leftsti.setAutoDraw(False)
                    response = 0
                
            if correctAns == 1:
                
                if leftsti.contains((x1, y1), units='pix') and relase == 0 :
                    
                    T1 = wt.getTime()
                    Delt = t
                    judge = 1
                    side = -1
                    time1 = e1[-1].time
                    #polygonleft.setAutoDraw(True)
                    rightsti.setAutoDraw(False)
                    response = 0

                if rightsti.contains((x1, y1), units='pix') and relase == 0 :

                    T1 = wt.getTime()
                    Delt = t
                    judge = 1
                    side = 1
                    time1 = e1[-1].time
                    #polygonright.setAutoDraw(True)
                    leftsti.setAutoDraw(False)
                    response = 1
                
                
#                    image.setAutoDraw(True)
#            if rightsti.contains((x1, y1), units='pix'):
#                side = 1
#                time0 = e1[-1].time
#                polygonright.setAutoDraw(True)
#                judge = 1
                
        T2 = wt.getTime()
        x, y = mouse.getPos()
        
        
        if T2-T1 > required_wagering_time and response == 1 and judge == 1 and T2 > MISST and relase == 1 and catch_ornot != 0 : #and T2 > MISST
            
            WT= T2 - T1
            response_type = 5 # low conf correct
            task = 7
            ch = channel
            response = 1
            RT=Delt
            #level= 0
            rtime = reward2
            mylist = [start_touch, rtime, WT, level, side,RT, response, ch,required_wagering_time,response_type,pic1,pic2,switch_ornot, catch_ornot,task]      #[start_touch, rtime, WT, level, side,RT, response,movie_location1,movie_location2,image_left,image_right,required_wagering_time,response_type,conf_cut,ch,task]
            json_string = json.dumps(mylist)
                #json_string = bytes(json_string,encoding="utf-8")
            UDPSock.sendto(json_string, addr)
                
            continueRoutine = False            
            #polygonright.setAutoDraw(False)
            #polygonleft.setAutoDraw(False)
        
        
        
        if T2-T1 >= required_wagering_time and response == 1 and judge == 1 and catch_ornot == 0 :

            #print(T1)
        
            WT= T2 - T1
            response_type = 1 #high conf correct
            task = 7
            ch = channel
            RT=Delt
            #side = 7  # or 8
            level= 0
            #level= int((round(level, 6))*1000)
            #WT = int(WT*1000)
            #stepreward = 0.08
            rtime = reward2
            mylist = [start_touch, rtime, WT, level, side,RT, response, ch,required_wagering_time,response_type,pic1,pic2,switch_ornot, catch_ornot,task]
            json_string = json.dumps(mylist)
            #json_string = bytes(json_string,encoding="utf-8")
            UDPSock.sendto(json_string, addr)
            
            continueRoutine = False            
            
#        if T2-T1 >= 0.5:

        #key = 1

        if e2 and judge == 1 :
            
            #polygonright.setAutoDraw(False)
            #polygonleft.setAutoDraw(False)
            relase = 1
            T_DLT = wt.getTime()

            #print('T_DLT',T_DLT)
            #print(T2)
            MISST = T_DLT + 0.8


        #print('T2', T2)
        #print('MISST', MISST)
        #print(judge)
        if T2-T1 < required_wagering_time and response == 1 and judge == 1 and T2 > MISST and relase == 1 :
            
            #print('T2', T2)
            #print('MISST', MISST)
            #print('low conf')
            
            WT= T2 - T1
            response_type = 2 # low conf correct
            task = 7
            ch = channel
            response = 1
            RT=Delt
                #side = 7  # or 8
            level= 0
                #level= int((round(level, 6))*1000)
                #WT = int(WT*1000)
                #stepreward = 0.08
            rtime = 0
            mylist = [start_touch, rtime, WT, level, side,RT, response, ch,required_wagering_time,response_type,pic1,pic2,switch_ornot, catch_ornot,task]
            json_string = json.dumps(mylist)
                #json_string = bytes(json_string,encoding="utf-8")
            UDPSock.sendto(json_string, addr)
                
            continueRoutine = False            
            #polygonright.setAutoDraw(False)
            #polygonleft.setAutoDraw(False)
            
        if response == 0 and judge == 1 and T2 > MISST and relase == 1:
            
            #print(T2)
            #print(MISST)
            #print('high conf')
            
            WT= T2 - T1
            
            if WT < required_wagering_time:
                response_type = 3 # low conf incorrect
            else:
                response_type = 4 # high conf incorrect
                
            task = 7
            ch = channel
            response = 0
            RT=Delt
            #side = 7  # or 8
            level= 0
            #level= int((round(level, 6))*1000)
            #WT = int(WT*1000)
            #stepreward = 0.08
            rtime = 0
            mylist = [start_touch, rtime, WT, level, side,RT, response, ch,required_wagering_time,response_type,pic1,pic2,switch_ornot, catch_ornot,task]
            json_string = json.dumps(mylist)
            #json_string = bytes(json_string,encoding="utf-8")
            UDPSock.sendto(json_string, addr)
            
            continueRoutine = False            
            #polygonright.setAutoDraw(False)
            #polygonleft.setAutoDraw(False)



#        if  e2 and judge == 0 and key == 0 :
#            
#            judge = 0
#            polygonright.setAutoDraw(False)
#            polygonleft.setAutoDraw(False)
#            leftsti.setAutoDraw(True)
#            rightsti.setAutoDraw(True)

#            time2 = e2[-1].time
#            if time1 == 0 and time0!=0:
#                duration = time2 - time0
#            if time0 == 0 and time1!=0:
#                duration = time2 - time1
#            message3.setText(u"duration: %s acc: "% (duration) ) #% (mouse_events[-1].time )) # % (mouse_events[-1].time )
#            message3.draw()
            
        #mouse.setPos((0,0))     #reset mouse on screen

    
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test"-------
    for thisComponent in testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    event.clearEvents('mouse') #clear mouse position in ram
    mouse.setVisible(0) #insure mouse not be seen
    # the Routine "test" was not non-slip safe, so reset the non-slip timer


    data_list['image_left'].append(image_left)
    data_list['image_right'].append(image_right)
    data_list['start_touch'].append(start_touch)
    data_list['rtime'].append(rtime)
    data_list['WT'].append(WT)
    data_list['level'].append(level)
    data_list['side'].append(side)
    data_list['RT'].append(RT)
    data_list['response'].append(response)
    data_list['ch'].append(ch)
    data_list['task'].append(task)
    data_list['catch_ornot'].append(catch_ornot)
    data_list['switch_ornot'].append(switch_ornot)

    data_list['required_wagering_time'].append(required_wagering_time)
    data_list['response_type'].append(response_type)

    #data_list['image_left'].append(image_left)
    #data_list['image_right'].append(image_right)

    df = pd.DataFrame(data_list)
    df.to_csv(filename + 'result.csv')

    print (response_type)
    #------Prepare to start Routine "reward_pause"-------
    continueRoutine = False
    if response_type == 1 or response_type == 5:
        continueRoutine = True
        
        
    #------Prepare to start Routine "reward_pause"-------
    routineTimer.reset()
    io.clearEvents('all')
    t = 0
    reward_pauseClock.reset()  # clock 
    frameN = -1
    routineTimer.add(rewardtime)
    # update component parameters for each repeat
    # keep track of which components have finished
    reward_pauseComponents = []
    reward_pauseComponents.append(leftsti)
    reward_pauseComponents.append(rightsti)
    reward_pauseComponents.append(polygonleft)
    reward_pauseComponents.append(polygonright)

    for thisComponent in reward_pauseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "reward_pause"-------

    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = reward_pauseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        if correctAns == -1:
            if t >= 0.0 and leftsti.status == NOT_STARTED:
                # keep track of start time/frame for later
                leftsti.tStart = t  # underestimates by a little under one frame
                leftsti.frameNStart = frameN  # exact frame index
                leftsti.setAutoDraw(True)
            #if leftsti.status == STARTED and t >= (0.0 + (rewardtime-win.monitorFramePeriod*0.75)): #most of one frame period left
            #    leftsti.setAutoDraw(False)

            if t >= 0.0 and polygonleft.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygonleft.tStart = t  # underestimates by a little under one frame
                polygonleft.frameNStart = frameN  # exact frame index
                #polygonleft.setAutoDraw(True)

            #if polygonleft.status == STARTED and t >= (0.0 + (rewardtime-win.monitorFramePeriod*0.75)): #most of one frame period left
             #   polygonleft.setAutoDraw(False)
                
        if correctAns == 1:
            if t >= 0.0 and rightsti.status == NOT_STARTED:
                # keep track of start time/frame for later
                rightsti.tStart = t  # underestimates by a little under one frame
                rightsti.frameNStart = frameN  # exact frame index
                rightsti.setAutoDraw(True)
            #if rightsti.status == STARTED and t >= (0.0 + (rewardtime-win.monitorFramePeriod*0.75)): #most of one frame period left
            #    rightsti.setAutoDraw(False)

            if t >= 0.0 and polygonright.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygonright.tStart = t  # underestimates by a little under one frame
                polygonright.frameNStart = frameN  # exact frame index
                #polygonright.setAutoDraw(True)

            #if polygonright.status == STARTED and t >= (0.0 + (rewardtime-win.monitorFramePeriod*0.75)): #most of one frame period left
            #   polygonright.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reward_pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "reward_pause"-------
    for thisComponent in reward_pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
            

    #------Prepare to start Routine "punish_pauseComponents"-------
    continueRoutine = False
    if response_type == 2 or response_type ==3 or response_type ==4:
        continueRoutine = True
    t = 0
    punish_pauseClock.reset()  # clock 
    frameN = -1
    
    routineTimer.reset()
    routineTimer.add(2)
    
    # update component parameters for each repeat
    # keep track of which components have finished
    punish_pauseComponents = []
    punish_pauseComponents.append(polygon_rd)
    punish_pauseComponents.append(text_3)
    
    for thisComponent in punish_pauseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "punish_pauseComponents"-------
    #continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
#        # get current time
        t = punish_pauseClock.getTime()
#        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.text=''
            text_3.setAutoDraw(True)
            
        if text_3.status == STARTED and t >= (2 + (-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in punish_pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "punish_pauseComponents"-------
    for thisComponent in punish_pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)




    #------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock
    #ITI=ITI/1000
    frameN = -1
    routineTimer.reset()
    routineTimer.add(2)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = []
    #ITIComponents.append(ISI_2)
    ITIComponents.append(text_3)
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "ITI"-------
    continueRoutine = True

    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *ISI_2* period
        #if t >= 0.0 and ISI_2.status == NOT_STARTED:
            # keep track of start time/frame for later
        #    ISI_2.tStart = t  # underestimates by a little under one frame
        #    ISI_2.frameNStart = frameN  # exact frame index
        #    ISI_2.start(ITI)
        #elif ISI_2.status == STARTED: #one frame should pass before updating params and completing
        #    ISI_2.complete() #finish the static period

        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.text=''
            text_3.setAutoDraw(True)
            
        if text_3.status == STARTED and t >= (2 + (-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_3.setAutoDraw(False)

        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)


    thisExp.nextEntry()
    

#------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
EndComponents = []
EndComponents.append(text_2)
EndComponents.append(key_resp_2)
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "End"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

    
    
# completed 5000 repeats of 'trials'



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
