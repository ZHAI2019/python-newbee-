#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on 2019_05_28_1738
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
from el_func import *

Searchflag = 0
reso =(1024,768)



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'main'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024,768), fullscr=False, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
W_Text = visual.TextStim(win=win, name='W_Text',
    text=u'\u6b22\u8fce\uff01',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Session_Start"
Session_StartClock = core.Clock()
S_S_Text = visual.TextStim(win=win, name='S_S_Text',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Start_Cue"
Start_CueClock = core.Clock()
S_C_Polygon = visual.Rect(
    win=win, name='S_C_Polygon',units='pix', 
    width=(80, 60)[0], height=(80, 60)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Cues"
CuesClock = core.Clock()
C_L_Image = visual.ImageStim(
    win=win, name='C_L_Image',
    image='sin', mask=None,
    ori=0, pos=(-0.6, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
C_R_Image = visual.ImageStim(
    win=win, name='C_R_Image',
    image='sin', mask=None,
    ori=0, pos=(0.6, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "Search"
SearchClock = core.Clock()
S_Image = visual.ImageStim(
    win=win, name='S_Image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1024,768),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "ITIS"
ITISClock = core.Clock()
I_Polygon = visual.ShapeStim(
    win=win, name='I_Polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Session_End"
Session_EndClock = core.Clock()
S_E_Text = visual.TextStim(win=win, name='S_E_Text',
    text=u'Session\u7ed3\u675f\uff01\n\u4f11\u606f\u4e00\u4e0b\uff1f\n\u6309\u7a7a\u683c\u7ee7\u7eed\uff01',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
E_Text = visual.TextStim(win=win, name='E_Text',
    text=u'\u7ed3\u675f\uff01\n\u611f\u8c22\u4f60\uff01\n\u6309\u7a7a\u683c\u9000\u51fa\uff01',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
t = 0
WelcomeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
W_Key = event.BuilderKeyResponse()
# keep track of which components have finished
WelcomeComponents = [W_Text, W_Key]
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Welcome"-------
while continueRoutine:
    # get current time


    

    t = WelcomeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *W_Text* updates
    if t >= 0.0 and W_Text.status == NOT_STARTED:
        # keep track of start time/frame for later
        W_Text.tStart = t
        W_Text.frameNStart = frameN  # exact frame index
        W_Text.setAutoDraw(True)
    
    # *W_Key* updates
    if t >= 0.0 and W_Key.status == NOT_STARTED:
        # keep track of start time/frame for later
        W_Key.tStart = t
        W_Key.frameNStart = frameN  # exact frame index
        W_Key.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(W_Key.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if W_Key.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            W_Key.keys = theseKeys[-1]  # just the last key pressed
            W_Key.rt = W_Key.clock.getTime()
            # was this 'correct'?
            if (W_Key.keys == str("'space'")) or (W_Key.keys == "'space'"):
                W_Key.corr = 1
            else:
                W_Key.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if W_Key.keys in ['', [], None]:  # No response was made
    W_Key.keys=None
    # was no response the correct answer?!
    if str("'space'").lower() == 'none':
       W_Key.corr = 1  # correct non-response
    else:
       W_Key.corr = 0  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('W_Key.keys',W_Key.keys)
thisExp.addData('W_Key.corr', W_Key.corr)
if W_Key.keys != None:  # we had a response
    thisExp.addData('W_Key.rt', W_Key.rt)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
B_4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'Block.xlsx'),
    seed=None, name='B_4')
thisExp.addLoop(B_4)  # add the loop to the experiment
thisB_4 = B_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisB_4.rgb)
if thisB_4 != None:
    for paramName in thisB_4:
        exec('{} = thisB_4[paramName]'.format(paramName))

for thisB_4 in B_4:
    currentLoop = B_4

    # abbreviate parameter names if possible (e.g. rgb = thisB_4.rgb)
    if thisB_4 != None:
        for paramName in thisB_4:
            exec('{} = thisB_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Session_Start"-------
    t = 0
    Session_StartClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    S_S_Text.setText(u'Session\u5f00\u59cb!\n\u6309\u7a7a\u683c\u7ee7\u7eed!')
    S_S_Key = event.BuilderKeyResponse()
    # keep track of which components have finished
    Session_StartComponents = [S_S_Text, S_S_Key]
    for thisComponent in Session_StartComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
#
    edfFile = 'jzy_search'
    tracker = el_do(host_address = "100.1.1.1", resolution = reso)
    tracker.communicate(str(Sub))
    tracker.message('BLOCK_INDEX: %d' %Block_ori)
    tracker.message('WHICH_TASK: b'+str(Block_ori))

    # -------Start Routine "Session_Start"-------
    while continueRoutine:
        # get current time
        


        
        t = Session_StartClock.getTime()
        
        
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *S_S_Text* updates
        if t >= 0.0 and S_S_Text.status == NOT_STARTED:
            # keep track of start time/frame for later
            S_S_Text.tStart = t
            S_S_Text.frameNStart = frameN  # exact frame index
            S_S_Text.setAutoDraw(True)
        
        # *S_S_Key* updates
        if t >= 0.0 and S_S_Key.status == NOT_STARTED:
            # keep track of start time/frame for later
            S_S_Key.tStart = t
            S_S_Key.frameNStart = frameN  # exact frame index
            S_S_Key.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(S_S_Key.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if S_S_Key.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0 :  # at least one key was pressed
                S_S_Key.keys = theseKeys[-1]  # just the last key pressed
                S_S_Key.rt = S_S_Key.clock.getTime()
                # was this 'correct'?
                if (S_S_Key.keys == str("'space'")) or (S_S_Key.keys == "'space'"):
                    S_S_Key.corr = 1
                else:
                    S_S_Key.corr = 0
                
                # a response ends the routine
                
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Session_StartComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Session_Start"-------
    for thisComponent in Session_StartComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if S_S_Key.keys in ['', [], None]:  # No response was made
        S_S_Key.keys=None
        # was no response the correct answer?!
        if str("'space'").lower() == 'none':
           S_S_Key.corr = 1  # correct non-response
        else:
           S_S_Key.corr = 0  # failed to respond (incorrectly)
    # store data for B_4 (TrialHandler)
    B_4.addData('S_S_Key.keys',S_S_Key.keys)
    B_4.addData('S_S_Key.corr', S_S_Key.corr)
    if S_S_Key.keys != None:  # we had a response
        B_4.addData('S_S_Key.rt', S_S_Key.rt)
    # the Routine "Session_Start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
       

    #tracker.setup()
    
    # set up handler to look after randomisation of conditions etc
    T_15 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(u'sub1.xlsx'),
        seed=None, name='T_15')
    thisExp.addLoop(T_15)  # add the loop to the experiment
    thisT_15 = T_15.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisT_15.rgb)
    if thisT_15 != None:
        for paramName in thisT_15:
            exec('{} = thisT_15[paramName]'.format(paramName))

    for thisT_15 in T_15:

        if thisT_15['Block'] == Block_ori: #Block
            
            currentLoop = T_15
            # abbreviate parameter names if possible (e.g. rgb = thisT_15.rgb)
            #thisT_15.
            if thisT_15 != None:
                for paramName in thisT_15:
                    exec('{} = thisT_15[paramName]'.format(paramName))

            # ------Prepare to start Routine "Start_Cue"-------
            t = 0
            Start_CueClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            S_C_Key = event.BuilderKeyResponse()
            # keep track of which components have finished
            Start_CueComponents = [S_C_Polygon, S_C_Key]
            for thisComponent in Start_CueComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            tracker.record(TrialNum)
            tracker.recordGo()
            # -------Start Routine "Start_Cue"-------
            while continueRoutine:
                # get current time

                
                t = Start_CueClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *S_C_Polygon* updates
                if t >= 0.0 and S_C_Polygon.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    S_C_Polygon.tStart = t
                    S_C_Polygon.frameNStart = frameN  # exact frame index
                    S_C_Polygon.setAutoDraw(True)
                
                # *S_C_Key* updates
                if t >= 0.0 and S_C_Key.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    S_C_Key.tStart = t
                    S_C_Key.frameNStart = frameN  # exact frame index
                    S_C_Key.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(S_C_Key.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if S_C_Key.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        S_C_Key.keys = theseKeys[-1]  # just the last key pressed
                        S_C_Key.rt = S_C_Key.clock.getTime()
                        # was this 'correct'?
                        if (S_C_Key.keys == str("'space'")) or (S_C_Key.keys == "'space'"):
                            S_C_Key.corr = 1
                        else:
                            S_C_Key.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Start_CueComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Start_Cue"-------
            for thisComponent in Start_CueComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if S_C_Key.keys in ['', [], None]:  # No response was made
                S_C_Key.keys=None
                # was no response the correct answer?!
                if str("'space'").lower() == 'none':
                   S_C_Key.corr = 1  # correct non-response
                else:
                   S_C_Key.corr = 0  # failed to respond (incorrectly)
            # store data for T_15 (TrialHandler)
            T_15.addData('S_C_Key.keys',S_C_Key.keys)
            T_15.addData('S_C_Key.corr', S_C_Key.corr)
            if S_C_Key.keys != None:  # we had a response
                T_15.addData('S_C_Key.rt', S_C_Key.rt)
            # the Routine "Start_Cue" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "Cues"-------
            t = 0
            CuesClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            C_L_Image.setImage(Obj_L)
            C_R_Image.setImage(Obj_R)
            C_R_Key = event.BuilderKeyResponse()
            # keep track of which components have finished
            CuesComponents = [C_L_Image, C_R_Image, C_R_Key]
            for thisComponent in CuesComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            tracker.message("ST-C")

            # -------Start Routine "Cues"-------
            while continueRoutine:
                # get current time
                
                t = CuesClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *C_L_Image* updates
                if t >= 0.0 and C_L_Image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    C_L_Image.tStart = t
                    C_L_Image.frameNStart = frameN  # exact frame index
                    C_L_Image.setAutoDraw(True)
                
                # *C_R_Image* updates
                if t >= 0.0 and C_R_Image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    C_R_Image.tStart = t
                    C_R_Image.frameNStart = frameN  # exact frame index
                    C_R_Image.setAutoDraw(True)
                
                # *C_R_Key* updates
                if t >= 0.0 and C_R_Key.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    C_R_Key.tStart = t
                    C_R_Key.frameNStart = frameN  # exact frame index
                    C_R_Key.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(C_R_Key.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if C_R_Key.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        C_R_Key.keys = theseKeys[-1]  # just the last key pressed
                        C_R_Key.rt = C_R_Key.clock.getTime()
                        # was this 'correct'?
                        if (C_R_Key.keys == str("'space'")) or (C_R_Key.keys == "'space'"):
                            C_R_Key.corr = 1
                        else:
                            C_R_Key.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in CuesComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Cues"-------
            for thisComponent in CuesComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if C_R_Key.keys in ['', [], None]:  # No response was made
                C_R_Key.keys=None
                # was no response the correct answer?!
                if str("'space'").lower() == 'none':
                   C_R_Key.corr = 1  # correct non-response
                else:
                   C_R_Key.corr = 0  # failed to respond (incorrectly)
            # store data for T_15 (TrialHandler)
            T_15.addData('C_R_Key.keys',C_R_Key.keys)
            T_15.addData('C_R_Key.corr', C_R_Key.corr)
            if C_R_Key.keys != None:  # we had a response
                T_15.addData('C_R_Key.rt', C_R_Key.rt)
            # the Routine "Cues" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "Search"-------
            t = 0
            SearchClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            S_Image.setImage(Scene)
            routineTimer.add(60.000000)
            # update component parameters for each repeat
            S_Key = event.BuilderKeyResponse()
            # keep track of which components have finished
            SearchComponents = [S_Image, S_Key]
            for thisComponent in SearchComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            tracker.message("C-S")
            # -------Start Routine "Search"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                
                t = SearchClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *S_Image* updates
                if t >= 0.0 and S_Image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    S_Image.tStart = t
                    S_Image.frameNStart = frameN  # exact frame index
                    S_Image.setAutoDraw(True)
                frameRemains = 0.0 + 60- win.monitorFramePeriod * 0.75  # most of one frame period left
                if S_Image.status == STARTED and t >= frameRemains:
                    S_Image.setAutoDraw(False)
                
                # *S_Key* updates
                if t >= 0.0 and S_Key.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    S_Key.tStart = t
                    S_Key.frameNStart = frameN  # exact frame index
                    S_Key.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(S_Key.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                frameRemains = 0.0 + 60- win.monitorFramePeriod * 0.75  # most of one frame period left
                if S_Key.status == STARTED and t >= frameRemains:
                    S_Key.status = STOPPED
                if S_Key.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        Searchflag = Searchflag+1
                        S_Key.keys.extend(theseKeys)  # storing all keys
                        S_Key.rt.append(S_Key.clock.getTime())
                        # was this 'correct'?
                        if (S_Key.keys == str("'space'")) or (S_Key.keys == "'space'"):
                            S_Key.corr = 1
                        else:
                            S_Key.corr = 0
                    if Searchflag==2:
                        continueRoutine = False
                        Searchflag=0
                        
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in SearchComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Search"-------
            for thisComponent in SearchComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if S_Key.keys in ['', [], None]:  # No response was made
                S_Key.keys=None
                # was no response the correct answer?!
                if str("'space'").lower() == 'none':
                   S_Key.corr = 1  # correct non-response
                else:
                   S_Key.corr = 0  # failed to respond (incorrectly)
            # store data for T_15 (TrialHandler)
            T_15.addData('S_Key.keys',S_Key.keys)
            T_15.addData('S_Key.corr', S_Key.corr)
            if S_Key.keys != None:  # we had a response
                T_15.addData('S_Key.rt', S_Key.rt)
            
            # ------Prepare to start Routine "ITIS"-------
            t = 0
            ITISClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            ITISComponents = [I_Polygon]
            for thisComponent in ITISComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "ITIS"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                tracker.message("S-I")
                t = ITISClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *I_Polygon* updates
                if t >= 0.0 and I_Polygon.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    I_Polygon.tStart = t
                    I_Polygon.frameNStart = frameN  # exact frame index
                    I_Polygon.setAutoDraw(True)
                frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
                if I_Polygon.status == STARTED and t >= frameRemains:
                    I_Polygon.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ITISComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ITIS"-------
            for thisComponent in ITISComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            tracker.recordDone()
            thisExp.nextEntry()
            
    # completed 1 repeats of 'T_15'
    
    
    # ------Prepare to start Routine "Session_End"-------
    t = 0
    Session_EndClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    S_E_Key = event.BuilderKeyResponse()
    # keep track of which components have finished
    Session_EndComponents = [S_E_Text, S_E_Key]
    for thisComponent in Session_EndComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Session_End"-------
    while continueRoutine:
        # get current time
        t = Session_EndClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *S_E_Text* updates
        if t >= 0.0 and S_E_Text.status == NOT_STARTED:
            # keep track of start time/frame for later
            S_E_Text.tStart = t
            S_E_Text.frameNStart = frameN  # exact frame index
            S_E_Text.setAutoDraw(True)
        
        # *S_E_Key* updates
        if t >= 0.0 and S_E_Key.status == NOT_STARTED:
            # keep track of start time/frame for later
            S_E_Key.tStart = t
            S_E_Key.frameNStart = frameN  # exact frame index
            S_E_Key.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(S_E_Key.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if S_E_Key.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                S_E_Key.keys = theseKeys[-1]  # just the last key pressed
                S_E_Key.rt = S_E_Key.clock.getTime()
                # was this 'correct'?
                if (S_E_Key.keys == str("'space'")) or (S_E_Key.keys == "'space'"):
                    S_E_Key.corr = 1
                else:
                    S_E_Key.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Session_EndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Session_End"-------
    for thisComponent in Session_EndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if S_E_Key.keys in ['', [], None]:  # No response was made
        S_E_Key.keys=None
        # was no response the correct answer?!
        if str("'space'").lower() == 'none':
           S_E_Key.corr = 1  # correct non-response
        else:
           S_E_Key.corr = 0  # failed to respond (incorrectly)
    # store data for B_4 (TrialHandler)
    B_4.addData('S_E_Key.keys',S_E_Key.keys)
    B_4.addData('S_E_Key.corr', S_E_Key.corr)
    if S_E_Key.keys != None:  # we had a response
        B_4.addData('S_E_Key.rt', S_E_Key.rt)
    # the Routine "Session_End" was not non-slip safe, so reset the non-slip timer


    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'B_4'


# ------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
E_Key = event.BuilderKeyResponse()
# keep track of which components have finished
EndComponents = [E_Text, E_Key]
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *E_Text* updates
    if t >= 0.0 and E_Text.status == NOT_STARTED:
        # keep track of start time/frame for later
        E_Text.tStart = t
        E_Text.frameNStart = frameN  # exact frame index
        E_Text.setAutoDraw(True)
    
    # *E_Key* updates
    if t >= 0.0 and E_Key.status == NOT_STARTED:
        # keep track of start time/frame for later
        E_Key.tStart = t
        E_Key.frameNStart = frameN  # exact frame index
        E_Key.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(E_Key.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if E_Key.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            E_Key.keys = theseKeys[-1]  # just the last key pressed
            E_Key.rt = E_Key.clock.getTime()
            # was this 'correct'?
            if (E_Key.keys == str("'space'")) or (E_Key.keys == "'space'"):
                E_Key.corr = 1
            else:
                E_Key.corr = 0
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

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if E_Key.keys in ['', [], None]:  # No response was made
    E_Key.keys=None
    # was no response the correct answer?!
    if str("'space'").lower() == 'none':
       E_Key.corr = 1  # correct non-response
    else:
       E_Key.corr = 0  # failed to respond (incorrectly)
tracker.communicateDone()
# store data for thisExp (ExperimentHandler)
thisExp.addData('E_Key.keys',E_Key.keys)
thisExp.addData('E_Key.corr', E_Key.corr)
if E_Key.keys != None:  # we had a response
    thisExp.addData('E_Key.rt', E_Key.rt)
thisExp.nextEntry()
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
