#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 12:46:24 2019

@author: no-face
"""

import pandas as pd
import numpy as np


depressants= pd.read_csv('/Users/no-face/Desktop/PsychiatricMedSideEffects - Anti-Depressants.csv')
antipsychotics = pd.read_csv('/Users/no-face/Desktop/PsychiatricMedSideEffects - Antipsychotics.csv')
mood_stabilizers= pd.read_csv('/Users/no-face/Desktop/PsychiatricMedSideEffects - Mood Stabilizers.csv')
anxiolytics= pd.read_csv('/Users/no-face/Desktop/PsychiatricMedSideEffects - Anxiolytics (Anti-anxiety), Hypnotics and Sedatives.csv')
antidepressants_list= np.unique(depressants['Name of Medication'])
antipsychotics_list= np.unique(antipsychotics['Name of Medication'])
mood_stabilizers_list= np.unique(mood_stabilizers['Name of Medication'])
anxiolytics_list= np.unique(anxiolytics['Name of Medication'])

feature_scaling_file= pd.read_csv('/Users/no-face/Desktop/PsychiatricMedSideEffects - feature scaling.csv')
feature= np.unique(list(depressants['Side Effects'])+ list(antipsychotics['Side Effects'])+ list(mood_stabilizers['Side Effects']) + list(anxiolytics['Side Effects']))
dictionary_depressants= {}
dictionary_antipsychotics={}
dictionary_mood_stabilizers= {}
dictionary_anxiolytics= {}

scoreD= {}
scoreA= {}
scoreM= {}
scoreAx= {}

dict_comp= {}
for i in range(len(feature_scaling_file)):
    dict_comp[feature_scaling_file.loc[i, 'symptom']]=feature_scaling_file.loc[i, 'factor'] 

for depressant in antidepressants_list:
    dictionary_depressants[depressant]= list(depressants['Name of Medication']).count(depressant)

for antipsychotic in antipsychotics_list:
    dictionary_antipsychotics[antipsychotic]= list(antipsychotics['Name of Medication']).count(antipsychotic)

for mood_stabilizer in mood_stabilizers_list:
    dictionary_mood_stabilizers[mood_stabilizer]= list(mood_stabilizers['Name of Medication']).count(mood_stabilizer)

for anxiolytic in anxiolytics_list:
    dictionary_anxiolytics[anxiolytic]= list(anxiolytics['Name of Medication']).count(anxiolytic)


for depressant in antidepressants_list:
    sample= depressants.loc[depressants['Name of Medication']==depressant, 'Side Effects']
    factor= 0
    for SideEffect in sample:
        factor= factor + np.average(feature_scaling_file.loc[feature_scaling_file['symptom']==SideEffect, 'factor'])
    scoreD[depressant]= factor
    
for mood_stabilizer in mood_stabilizers_list:
    sample= mood_stabilizers.loc[mood_stabilizers['Name of Medication']==mood_stabilizer, 'Side Effects']
    factor= 0
    for SideEffect in sample:
        factor= factor + np.average(feature_scaling_file.loc[feature_scaling_file['symptom']==SideEffect, 'factor'])
    scoreM[mood_stabilizer]= factor   
    
for antipsychotic in antipsychotics_list:
    sample= antipsychotics.loc[antipsychotics['Name of Medication']==antipsychotic, 'Side Effects']
    factor= 0
    for SideEffect in sample:
        factor= factor + np.average(feature_scaling_file.loc[feature_scaling_file['symptom']==SideEffect, 'factor'])
    scoreA[antipsychotic]= factor   

    
    
for anxiolytic in anxiolytics_list:
    sample= anxiolytics.loc[anxiolytics['Name of Medication']==anxiolytic, 'Side Effects']
    factor= 0
    for SideEffect in sample:
        factor= factor + dict_comp[SideEffect]
    scoreAx[anxiolytic]= factor 