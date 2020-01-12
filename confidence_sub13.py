#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on 2019_10_31_1713
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

reso =(1024,768)

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'confidence'  # from the Builder filename that created this script
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
    size=(1024, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "WELCOME"
WELCOMEClock = core.Clock()
WEL_TEXT = visual.TextStim(win=win, name='WEL_TEXT',
    text=u'\u6b22\u8fce\u53c2\u52a0\u672c\u5b9e\u9a8c\n\n\u60a8\u9700\u8981\u6309\u4e0b\u7a7a\u683c\u952e\u5f00\u59cb\uff01',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Block_str"
Block_strClock = core.Clock()
B_text = visual.TextStim(win=win, name='B_text',
    text=u'\u6309\u4e0b\u7a7a\u683c\u5f00\u59cb\u65b0BLOCK\uff01',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "GAP"
GAPClock = core.Clock()
GAP_CROSS = visual.ShapeStim(
    win=win, name='GAP_CROSS', vertices='cross',
    size=(0.025, 0.03),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "routine_2AFC"
routine_2AFCClock = core.Clock()
IMA_LEFT = visual.ImageStim(
    win=win, name='IMA_LEFT',
    image='sin', mask=None,
    ori=0, pos=(-0.55, 0), size=(0.95, 0.95),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
IMA_RIGHT = visual.ImageStim(
    win=win, name='IMA_RIGHT',
    image='sin', mask=None,
    ori=0, pos=(0.55, 0), size=(0.95, 0.95),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "DELAY"
DELAYClock = core.Clock()
DELAY_CROSS = visual.ShapeStim(
    win=win, name='DELAY_CROSS', vertices='cross',
    size=(0.025, 0.03),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "CONFIDENCE"
CONFIDENCEClock = core.Clock()
CON_TEXT = visual.TextStim(win=win, name='CON_TEXT',
    text='       Confidence\n\n\n1      2      3      4\n\n\nLow             High\n',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
ITI_CROSS = visual.ShapeStim(
    win=win, name='ITI_CROSS', vertices='cross',
    size=(0.025, 0.03),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "END"
ENDClock = core.Clock()
END_TEXT = visual.TextStim(win=win, name='END_TEXT',
    text=u'\u611f\u8c22\u60a8\u53c2\u52a0\u5b9e\u9a8c\uff01\n\n\u6309\u7a7a\u683c\u952e\u9000\u51fa\uff01',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WELCOME"-------
t = 0
WELCOMEClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
WEL_PRESS = event.BuilderKeyResponse()
# keep track of which components have finished
WELCOMEComponents = [WEL_TEXT, WEL_PRESS]
for thisComponent in WELCOMEComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "WELCOME"-------
while continueRoutine:
    # get current time
    t = WELCOMEClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WEL_TEXT* updates
    if t >= 0.0 and WEL_TEXT.status == NOT_STARTED:
        # keep track of start time/frame for later
        WEL_TEXT.tStart = t
        WEL_TEXT.frameNStart = frameN  # exact frame index
        WEL_TEXT.setAutoDraw(True)
    
    # *WEL_PRESS* updates
    if t >= 0.0 and WEL_PRESS.status == NOT_STARTED:
        # keep track of start time/frame for later
        WEL_PRESS.tStart = t
        WEL_PRESS.frameNStart = frameN  # exact frame index
        WEL_PRESS.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(WEL_PRESS.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if WEL_PRESS.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            WEL_PRESS.keys = theseKeys[-1]  # just the last key pressed
            WEL_PRESS.rt = WEL_PRESS.clock.getTime()
            # was this 'correct'?
            if (WEL_PRESS.keys == str("'space'")) or (WEL_PRESS.keys == "'space'"):
                WEL_PRESS.corr = 1
            else:
                WEL_PRESS.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WELCOMEComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WELCOME"-------
for thisComponent in WELCOMEComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if WEL_PRESS.keys in ['', [], None]:  # No response was made
    WEL_PRESS.keys=None
    # was no response the correct answer?!
    if str("'space'").lower() == 'none':
       WEL_PRESS.corr = 1  # correct non-response
    else:
       WEL_PRESS.corr = 0  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('WEL_PRESS.keys',WEL_PRESS.keys)
thisExp.addData('WEL_PRESS.corr', WEL_PRESS.corr)
if WEL_PRESS.keys != None:  # we had a response
    thisExp.addData('WEL_PRESS.rt', WEL_PRESS.rt)
thisExp.nextEntry()
# the Routine "WELCOME" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Block2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'Block_con.xlsx'),
    seed=None, name='Block2')
thisExp.addLoop(Block2)  # add the loop to the experiment
thisBlock2 = Block2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock2.rgb)
if thisBlock2 != None:
    for paramName in thisBlock2:
        exec('{} = thisBlock2[paramName]'.format(paramName))

for thisBlock2 in Block2:
    currentLoop = Block2
    # abbreviate parameter names if possible (e.g. rgb = thisBlock2.rgb)
    if thisBlock2 != None:
        for paramName in thisBlock2:
            exec('{} = thisBlock2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block_str"-------
    t = 0
    Block_strClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    B_key = event.BuilderKeyResponse()
    # keep track of which components have finished
    Block_strComponents = [B_text, B_key]
    for thisComponent in Block_strComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    edfFile = 'jzy_confidence'
    tracker = el_do(host_address = "100.1.1.1", resolution = reso)
    tracker.communicate(str(Sub))
    tracker.message('BLOCK_INDEX: %d' %Block_ori)
    tracker.message('WHICH_TASK: b'+str(Block_ori))
    
    # -------Start Routine "Block_str"-------
    while continueRoutine:
        # get current time
        t = Block_strClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *B_text* updates
        if t >= 0.0 and B_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            B_text.tStart = t
            B_text.frameNStart = frameN  # exact frame index
            B_text.setAutoDraw(True)
        
        # *B_key* updates
        if t >= 0.0 and B_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            B_key.tStart = t
            B_key.frameNStart = frameN  # exact frame index
            B_key.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(B_key.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if B_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                B_key.keys = theseKeys[-1]  # just the last key pressed
                B_key.rt = B_key.clock.getTime()
                # was this 'correct'?
                if (B_key.keys == str(u"'space'")) or (B_key.keys == u"'space'"):
                    B_key.corr = 1
                else:
                    B_key.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_strComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block_str"-------
    for thisComponent in Block_strComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if B_key.keys in ['', [], None]:  # No response was made
        B_key.keys=None
        # was no response the correct answer?!
        if str(u"'space'").lower() == 'none':
           B_key.corr = 1  # correct non-response
        else:
           B_key.corr = 0  # failed to respond (incorrectly)
    # store data for Block2 (TrialHandler)
    Block2.addData('B_key.keys',B_key.keys)
    Block2.addData('B_key.corr', B_key.corr)
    if B_key.keys != None:  # we had a response
        Block2.addData('B_key.rt', B_key.rt)
    # the Routine "Block_str" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "GAP"-------
    t = 0
    GAPClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    GAPComponents = [GAP_CROSS]
    for thisComponent in GAPComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "GAP"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = GAPClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *GAP_CROSS* updates
        if t >= 0.0 and GAP_CROSS.status == NOT_STARTED:
            # keep track of start time/frame for later
            GAP_CROSS.tStart = t
            GAP_CROSS.frameNStart = frameN  # exact frame index
            GAP_CROSS.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if GAP_CROSS.status == STARTED and t >= frameRemains:
            GAP_CROSS.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GAPComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "GAP"-------
    for thisComponent in GAPComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #tracker.setup()

    # set up handler to look after randomisation of conditions etc
    LOOP30 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(u'sub1_con.xlsx'),
        seed=None, name='LOOP30')
    thisExp.addLoop(LOOP30)  # add the loop to the experiment
    thisLOOP30 = LOOP30.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLOOP30.rgb)
    if thisLOOP30 != None:
        for paramName in thisLOOP30:
            exec('{} = thisLOOP30[paramName]'.format(paramName))
    
    for thisLOOP30 in LOOP30:
        if thisLOOP30['Block'] == Block_ori:
            currentLoop = LOOP30
            # abbreviate parameter names if possible (e.g. rgb = thisLOOP30.rgb)
            if thisLOOP30 != None:
                for paramName in thisLOOP30:
                    exec('{} = thisLOOP30[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "routine_2AFC"-------
            
            t = 0
            routine_2AFCClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            IMA_LEFT.setImage(Scene_L)
            IMA_RIGHT.setImage(Scene_R)
            CHA_TEXT = event.BuilderKeyResponse()
            # keep track of which components have finished
            routine_2AFCComponents = [IMA_LEFT, IMA_RIGHT, CHA_TEXT]
            for thisComponent in routine_2AFCComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            tracker.record(TrialNum)
            tracker.recordGo()
            tracker.message("2AFC")
            # -------Start Routine "routine_2AFC"-------
            while continueRoutine:
                # get current time
                t = routine_2AFCClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *IMA_LEFT* updates
                if t >= 0.0 and IMA_LEFT.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    IMA_LEFT.tStart = t
                    IMA_LEFT.frameNStart = frameN  # exact frame index
                    IMA_LEFT.setAutoDraw(True)
                
                # *IMA_RIGHT* updates
                if t >= 0.0 and IMA_RIGHT.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    IMA_RIGHT.tStart = t
                    IMA_RIGHT.frameNStart = frameN  # exact frame index
                    IMA_RIGHT.setAutoDraw(True)
                
                # *CHA_TEXT* updates
                if t >= 0.0 and CHA_TEXT.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    CHA_TEXT.tStart = t
                    CHA_TEXT.frameNStart = frameN  # exact frame index
                    CHA_TEXT.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(CHA_TEXT.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if CHA_TEXT.status == STARTED:
                    theseKeys = event.getKeys(keyList=['left', 'right'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        CHA_TEXT.keys = theseKeys[-1]  # just the last key pressed
                        CHA_TEXT.rt = CHA_TEXT.clock.getTime()
                        # was this 'correct'?
                        if (CHA_TEXT.keys == str("'left','right'")) or (CHA_TEXT.keys == "'left','right'"):
                            CHA_TEXT.corr = 1
                        else:
                            CHA_TEXT.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in routine_2AFCComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "routine_2AFC"-------
            for thisComponent in routine_2AFCComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if CHA_TEXT.keys in ['', [], None]:  # No response was made
                CHA_TEXT.keys=None
                # was no response the correct answer?!
                if str("'left','right'").lower() == 'none':
                   CHA_TEXT.corr = 1  # correct non-response
                else:
                   CHA_TEXT.corr = 0  # failed to respond (incorrectly)
            # store data for LOOP30 (TrialHandler)
            LOOP30.addData('CHA_TEXT.keys',CHA_TEXT.keys)
            LOOP30.addData('CHA_TEXT.corr', CHA_TEXT.corr)
            if CHA_TEXT.keys != None:  # we had a response
                LOOP30.addData('CHA_TEXT.rt', CHA_TEXT.rt)
            # the Routine "routine_2AFC" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "DELAY"-------
            t = 0
            DELAYClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            DELAYComponents = [DELAY_CROSS]
            for thisComponent in DELAYComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            tracker.message("DELAY")
            # -------Start Routine "DELAY"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = DELAYClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *DELAY_CROSS* updates
                if t >= 0.0 and DELAY_CROSS.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    DELAY_CROSS.tStart = t
                    DELAY_CROSS.frameNStart = frameN  # exact frame index
                    DELAY_CROSS.setAutoDraw(True)
                frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if DELAY_CROSS.status == STARTED and t >= frameRemains:
                    DELAY_CROSS.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in DELAYComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "DELAY"-------
            for thisComponent in DELAYComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # ------Prepare to start Routine "CONFIDENCE"-------
            t = 0
            CONFIDENCEClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            CON_PRESS = event.BuilderKeyResponse()
            # keep track of which components have finished
            CONFIDENCEComponents = [CON_TEXT, CON_PRESS]
            for thisComponent in CONFIDENCEComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            tracker.message("CONFIDENCE")
            # -------Start Routine "CONFIDENCE"-------
            while continueRoutine:
                # get current time
                t = CONFIDENCEClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *CON_TEXT* updates
                if t >= 0.0 and CON_TEXT.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    CON_TEXT.tStart = t
                    CON_TEXT.frameNStart = frameN  # exact frame index
                    CON_TEXT.setAutoDraw(True)
                
                # *CON_PRESS* updates
                if t >= 0.0 and CON_PRESS.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    CON_PRESS.tStart = t
                    CON_PRESS.frameNStart = frameN  # exact frame index
                    CON_PRESS.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(CON_PRESS.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if CON_PRESS.status == STARTED:
                    theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        CON_PRESS.keys = theseKeys[-1]  # just the last key pressed
                        CON_PRESS.rt = CON_PRESS.clock.getTime()
                        # was this 'correct'?
                        if (CON_PRESS.keys == str("'1','2','3','4'")) or (CON_PRESS.keys == "'1','2','3','4'"):
                            CON_PRESS.corr = 1
                        else:
                            CON_PRESS.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in CONFIDENCEComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "CONFIDENCE"-------
            for thisComponent in CONFIDENCEComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if CON_PRESS.keys in ['', [], None]:  # No response was made
                CON_PRESS.keys=None
                # was no response the correct answer?!
                if str("'1','2','3','4'").lower() == 'none':
                   CON_PRESS.corr = 1  # correct non-response
                else:
                   CON_PRESS.corr = 0  # failed to respond (incorrectly)
            # store data for LOOP30 (TrialHandler)
            LOOP30.addData('CON_PRESS.keys',CON_PRESS.keys)
            LOOP30.addData('CON_PRESS.corr', CON_PRESS.corr)
            if CON_PRESS.keys != None:  # we had a response
                LOOP30.addData('CON_PRESS.rt', CON_PRESS.rt)
            # the Routine "CONFIDENCE" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "ITI"-------
            t = 0
            ITIClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            ITIComponents = [ITI_CROSS]
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            tracker.message("ITI")
            # -------Start Routine "ITI"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ITIClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ITI_CROSS* updates
                if t >= 0.0 and ITI_CROSS.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ITI_CROSS.tStart = t
                    ITI_CROSS.frameNStart = frameN  # exact frame index
                    ITI_CROSS.setAutoDraw(True)
                frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
                if ITI_CROSS.status == STARTED and t >= frameRemains:
                    ITI_CROSS.setAutoDraw(False)
                
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
            
            # -------Ending Routine "ITI"-------
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            tracker.recordDone()
            thisExp.nextEntry()
        # completed 1 repeats of 'LOOP30'


    
# completed 1 repeats of 'Block2'


# ------Prepare to start Routine "END"-------
t = 0
ENDClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
END_PRESS = event.BuilderKeyResponse()
# keep track of which components have finished
ENDComponents = [END_TEXT, END_PRESS]
for thisComponent in ENDComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "END"-------
while continueRoutine:
    # get current time
    t = ENDClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *END_TEXT* updates
    if t >= 0.0 and END_TEXT.status == NOT_STARTED:
        # keep track of start time/frame for later
        END_TEXT.tStart = t
        END_TEXT.frameNStart = frameN  # exact frame index
        END_TEXT.setAutoDraw(True)
    
    # *END_PRESS* updates
    if t >= 0.0 and END_PRESS.status == NOT_STARTED:
        # keep track of start time/frame for later
        END_PRESS.tStart = t
        END_PRESS.frameNStart = frameN  # exact frame index
        END_PRESS.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(END_PRESS.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if END_PRESS.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            END_PRESS.keys = theseKeys[-1]  # just the last key pressed
            END_PRESS.rt = END_PRESS.clock.getTime()
            # was this 'correct'?
            if (END_PRESS.keys == str("'space'")) or (END_PRESS.keys == "'space'"):
                END_PRESS.corr = 1
            else:
                END_PRESS.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ENDComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "END"-------
for thisComponent in ENDComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if END_PRESS.keys in ['', [], None]:  # No response was made
    END_PRESS.keys=None
    # was no response the correct answer?!
    if str("'space'").lower() == 'none':
       END_PRESS.corr = 1  # correct non-response
    else:
       END_PRESS.corr = 0  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('END_PRESS.keys',END_PRESS.keys)
thisExp.addData('END_PRESS.corr', END_PRESS.corr)
if END_PRESS.keys != None:  # we had a response
    thisExp.addData('END_PRESS.rt', END_PRESS.rt)
thisExp.nextEntry()
tracker.communicateDone()
# the Routine "END" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
