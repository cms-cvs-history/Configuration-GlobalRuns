import optparse

usage="--list"
parser = optparse.OptionParser(usage)
parser.add_option("--GT")
parser.add_option("--era")
parser.add_option("--release")
parser.add_option("--options",default="")
parser.add_option("--output",default="RECO,DQM")
(options,args)=parser.parse_args()

def Era_8PDs():
    alcaAndSkimMap={}
    alcaAndSkimMap['']=('','LogError')
    alcaAndSkimMap['ZeroBias']=('SiStripCalZeroBias','')
    alcaAndSkimMap['MinimumBias']=('SiStripCalZeroBias+SiStripCalMinBias+TkAlMinBias+HcalCalIsoTrk','')
    alcaAndSkimMap['EG']=('EcalCalElectron','')
    alcaAndSkimMap['Mu']=('MuAlCalIsolatedMu+MuAlOverlaps+TkAlMuonIsolated+DtCalib','')
    alcaAndSkimMap['JetMETTau']=('HcalCalDijets','')
    #alcaAndSkimMap['AlCaP0']=('EcalCalPi0Calib+EcalCalEtaCalib','')
    #alcaAndSkimMap['AlCaPhiSymEcal']=('EcalCalPhiSym+DQM','')
    #alcaAndSkimMap['HcalNZS']=('HcalCalMinBias','')
    #alcaAndSkimMap['Cosmics']=('TkAlBeamHalo+MuAlBeamHaloOverlaps+MuAlBeamHalo+TkAlCosmics0T+MuAlStandAloneCosmics+MuAlGlobalCosmics+MuAlCalIsolatedMu+HcalCalHOCosmics','')
    return alcaAndSkimMap

def Era_2PDs():
    alcaAndSkimMap={}
    alcaAndSkimMap['']=('','LogError')
    alcaAndSkimMap['ZeroBias']=('SiStripCalZeroBias','')
    alcaAndSkimMap['MinimumBias']=('SiStripCalMinBias+SiStripCalZeroBias+TkAlMinBias+TkAlMuonIsolated+MuAlCalIsolatedMu+MuAlOverlaps+HcalCalIsoTrk+HcalCalDijets+DtCalib+EcalCalElectron','')
    return alcaAndSkimMap

def Era_1PDs():
    alcaAndSkimMap={}
    alcaAndSkimMap['MinimumBias']=('SiStripCalMinBias+SiStripCalZeroBias+TkAlMinBias+TkAlMuonIsolated+MuAlCalIsolatedMu+MuAlOverlaps+HcalCalIsoTrk+HcalCalDijets+DtCalib+EcalCalElectron','LogError')
    return alcaAndSkimMap

evt=options.output.split(',')
tiers=[]
for e in evt:
        tiers.append(e)

tiers=','.join(tiers)

com='cmsDriver.py reco -s RAW2DIGI,L1Reco,RECO,DQM%s  --data --magField AutoFromDBCurrent --scenario pp --datatier '+tiers+' --eventcontent '+options.output+' --customise Configuration/GlobalRuns/reco_TLR_'+options.release+'.py --cust_function customisePPData --no_exec --python_filename=rereco_%sCollision_'+options.release+'.py --conditions %s '+options.options
skim='cmsDriver.py skim -s SKIM:%s --data --magField AutoFromDBCurrent --scenario pp --datatier '+tiers+' --eventcontent '+options.output+' --no_exec --python_filename=skim_%s'+options.release+'.py --conditions %s '+options.options

import os

alcaAndSkimMap=globals()["Era_%ss"%(options.era)]()
for PD in alcaAndSkimMap.keys():
    alcaArg=alcaAndSkimMap[PD][0]
    skimArg=alcaAndSkimMap[PD][1]
    c=com
    s=skim
    spec=options.era+'_'
    if 'AOD' in options.output:
        spec+='AOD_'
    if (PD==''):
        alca=''
        c=com+' --process reRECO'
    else:
        alca=',ALCA:%s'%(alcaArg,)
        spec+=PD+"_"
    if (options.options !=""):
        spec+="spec_"
    os.system(c%(alca,spec,options.GT))

    if (skimArg!=""):
        os.system(s%(skimArg,spec,options.GT))

