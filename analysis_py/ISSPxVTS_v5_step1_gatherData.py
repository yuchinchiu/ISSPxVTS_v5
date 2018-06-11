# -*- coding: utf-8 -*-
"""
Created on 5/31/18

@author: yc180

This script go through all the log/txt in the folder and extract data to build a "group" DataFrame for later analysis
The output are two files: gpData.pkl & gpSbjInfo.pkl

from trialGen_v5.js

	this.phase      =[];   // cued=1, choice=2
	this.stim   	=[];   // 1,2,3,4,6,7,8,9
	this.stimCat    =[];   // LV, LN, SV, SN
	this.stimUnique =[];   // just unique Id for each stim.. 
	this.trialType  =[];   // 1 = switch, 0 = repetition, 2 = free-choice
	this.swProb  	=[];   // probability of switch, 75 or 25
	this.task    	=[];   // 1 = larger vs. small task, 2 = Living/Non-living, 99 = free choice
	this.response   =[];   // correct response (1-4)


"""

import os
import glob
import pandas as pd
import numpy as np
from copy import copy

workingDir = os.getcwd()
##os.path.dirname(os.path.realpath(__file__))
#%%
os.chdir("..")
# go up one level to the experiment directory
dataDir = os.getcwd() + os.sep + 'data' + os.sep + 'v5_batches' + os.sep  # where the log/txt files are located
# go back to the script Directory
os.chdir(workingDir)


fileList     = glob.glob(dataDir +  "*.log")
infofileList = glob.glob(dataDir +  "*.txt")


gpSbjInfo=pd.DataFrame()


## output = [this.runId,this.phase,this.stimUnique,this.stimCat,this.trialType,this.swProb,this.task,this.response,this.sbjResp,this.sbjACC,this.sbjRT];
colNames=['runId','phase','stimUnique','stimCat','trialType','swProb','task','response','sbjResp','sbjACC','sbjRT']
gpData = pd.DataFrame(np.empty((0,len(colNames)),dtype=int), columns=colNames)
SCNT=0

for f in range(0,len(fileList),1):
    SCNT=SCNT+1
    D = np.genfromtxt(fileList[f],delimiter=',',dtype=int)
    D = pd.DataFrame(np.transpose(np.reshape(D,(len(colNames),int(D.shape[0]/len(colNames))))),columns=colNames)
    D['sbjId']=SCNT
    
    txtFileName = fileList[f][:-3]+ "txt"
    # read in the corresponding text file and extract SRmapping, etc
    sbjInfo=np.genfromtxt(txtFileName, delimiter=":", dtype=str)
    sbjInfo=pd.DataFrame(np.transpose(sbjInfo))
    sbjInfo.columns = sbjInfo.iloc[0]
    sbjInfo.drop([0],axis=0,inplace=True)
    SRmapping = sbjInfo.loc[1,'SRmapping'].split(',') 
    # 0 was the index that become header, hasn't reset index, so taking 1
    sbjInfo['sbjId']=SCNT
    sbjInfo.index = sbjInfo.sbjId
    sbjInfo.drop('sbjId',axis=1,inplace=True)

    
    # make sure trials subj didn't respond, RT is marked as nan....
    D.loc[D['sbjResp']==99,'sbjRT']=np.nan    
    D['runId'] = D['runId']+1
    
    D['trialType_sw'] = copy(D['trialType']) # consider choice task and figure out the actual Switch vs. Repeat
    
    D.loc[(D.phase==1) & (D.trialType<=1),'trialType']=101  # forced-trials => phase 1 ALL CUED TRIALS
    D.loc[(D.phase==2) & (D.trialType<=1),'trialType']=101  # forced-trials with task-cues.. 0/1
    D.loc[(D.phase==2) & (D.trialType==2),'trialType']=102
    
    
    firstTrial=np.where(D.phase==2)[0][0] 
    currentTask = D.loc[firstTrial,'task']
    
    for i in range(firstTrial+1, len(D), 1):
        if(D.loc[i,'task']==99):  # no response on this trial, treat it as task-repeat
            D.loc[i,'trialType_sw']=np.nan            
            D.loc[i,'task']=np.nan
        else:            
            if(D.loc[i,'task']==currentTask):
                D.loc[i,'trialType_sw']=0
            else:
                D.loc[i,'trialType_sw']=1
                currentTask = D.loc[i,'task']
                    
    D['trialType_int'] = copy(D['trialType_sw'])  # use trialType_int to calculate switch rate.. null trial mark as np.nan
    D['task_int'] = copy(D['task'])
    D.task_int = D.task_int - 1  # becomes 0,1 (nan)  0 = size task, 1 = animacy
    
    ## to be fair, mark all the 1st trial in each run as NULL -> not switch not repeat
    for runId in D.runId.unique():
         firstTrial=np.where(D.runId==runId)[0][0] 
         D.loc[firstTrial,'trialType_int'] = np.nan
         D.loc[firstTrial,'sbjRT']=np.nan
         D.loc[firstTrial,'sbjACC']=np.nan
    
    
    gpSbjInfo = pd.concat([gpSbjInfo,sbjInfo],axis=0)
    gpData=pd.concat([gpData,D],axis=0)


#%%
# convert codings to categorical variables with meaningful names

gpData.phase          = gpData.phase.map({1:'training',2:'hybrid'})
gpData.trialType      = gpData.trialType.map({101:'cued',102:'choice'}) 
gpData.trialType_sw  = gpData.trialType_sw.map({0:'repeat',1:'switch'})  # this trialType variable is the 'design' .. not the actual SW/REP see above
gpData.swProb         = gpData.swProb.map({25:'sw25%',75:'sw75%'})
gpData.task           = gpData.task.map({1:'size', 2:'animacy'})


gpData['phase']         = pd.Categorical(gpData.phase, categories=['training','hybrid'],ordered=True)
gpData['trialType']     = pd.Categorical(gpData.trialType, categories=['cued','choice'],ordered=True)
gpData['trialType_sw']= pd.Categorical(gpData.trialType_sw, categories=['repeat','switch'],ordered=True)
gpData['swProb']        = pd.Categorical(gpData.swProb, categories=['sw25%','sw75%'],ordered=True)
gpData['task']          = pd.Categorical(gpData.task, categories=['size','animacy'],ordered=True)

# output DataFrame
os.chdir(workingDir)  # scripts directory


gpData.to_pickle('gpData.pkl')
gpSbjInfo.to_pickle('gpSbjInfo.pkl')


gpData.to_csv('gpData.csv',encoding='utf-8', index=False)
gpSbjInfo.to_csv('gpSbjInfo.csv',encoding='utf-8', index=False)


print(SCNT)