# Auto generated configuration file
# using: 
# Revision: 1.172 
# Source: /cvs/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: reco_FirstCollisions_36X -s RAW2DIGI,L1Reco,RECO,DQM --data --magField AutoFromDBCurrent --scenario pp --datatier RECO --eventcontent RECO --conditions GR_R_36X_V6::All --customise Configuration/GlobalRuns/customise_Collision_36X.py --no_exec --python_filename=rereco_FirstCollisions_36X.py
import FWCore.ParameterSet.Config as cms

process = cms.Process('RERECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryExtended_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('DQMOffline.Configuration.DQMOffline_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.6 $'),
    annotation = cms.untracked.string('reco_FirstCollisions_36X nevts:1'),
    name = cms.untracked.string('PyReleaseValidation')
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.options = cms.untracked.PSet(

)
# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('reco_FirstCollisions_36X_DIGI2RAW.root')
)

# Output definition
process.output = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    outputCommands = process.RECOEventContent.outputCommands,
    fileName = cms.untracked.string('reco_FirstCollisions_36X_RAW2DIGI_L1Reco_RECO_DQM.root'),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('')
    )
)

# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'GR_R_36X_V6::All'

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.dqmoffline_step = cms.Path(process.DQMOffline)
process.endjob_step = cms.Path(process.endOfProcess)
process.out_step = cms.EndPath(process.output)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.dqmoffline_step,process.endjob_step,process.out_step)


# Automatic addition of the customisation function

def customise(process):
    
    #####################################################################################################
    ####
    ####  Top level replaces for handling strange scenarios of early collisions
    ####

    ## TRACKING:
    ## Skip events with HV off
    process.newSeedFromTriplets.ClusterCheckPSet.MaxNumberOfPixelClusters=2000
    process.newSeedFromPairs.ClusterCheckPSet.MaxNumberOfCosmicClusters=10000
    process.secTriplets.ClusterCheckPSet.MaxNumberOfPixelClusters=2000
    process.fifthSeeds.ClusterCheckPSet.MaxNumberOfCosmicClusters = 10000
    process.fourthPLSeeds.ClusterCheckPSet.MaxNumberOfCosmicClusters=10000
    process.thTripletsA.ClusterCheckPSet.MaxNumberOfPixelClusters = 5000
    process.thTripletsB.ClusterCheckPSet.MaxNumberOfPixelClusters = 5000
        

    ###### FIXES TRIPLETS FOR LARGE BS DISPLACEMENT ######

    ### prevent bias in pixel vertex
    process.pixelVertices.useBeamConstraint = False
    
    ### pixelTracks
    #---- new parameters ----
    process.pixelTracks.RegionFactoryPSet.RegionPSet.nSigmaZ  = cms.double(4.06)
    process.pixelTracks.RegionFactoryPSet.RegionPSet.originHalfLength = cms.double(40.6)
    
    ### 0th step of iterative tracking
    #---- new parameters ----
    process.newSeedFromTriplets.RegionFactoryPSet.RegionPSet.nSigmaZ   = cms.double(4.06)
    process.newSeedFromTriplets.RegionFactoryPSet.RegionPSet.originHalfLength = 40.6

    ### 2nd step of iterative tracking
    #---- new parameters ----
    process.secTriplets.RegionFactoryPSet.RegionPSet.nSigmaZ  = cms.double(4.47)
    process.secTriplets.RegionFactoryPSet.RegionPSet.originHalfLength = 44.7

    ## Primary Vertex
    process.offlinePrimaryVerticesWithBS.PVSelParameters.maxDistanceToBeam = 2
    process.offlinePrimaryVerticesWithBS.TkFilterParameters.maxNormalizedChi2 = 20
    process.offlinePrimaryVerticesWithBS.TkFilterParameters.maxD0Significance = 100
    process.offlinePrimaryVerticesWithBS.TkFilterParameters.minPixelLayersWithHits = 2
    process.offlinePrimaryVerticesWithBS.TkFilterParameters.minSiliconLayersWithHits = 5
    process.offlinePrimaryVerticesWithBS.TkClusParameters.TkGapClusParameters.zSeparation = 1
    process.offlinePrimaryVertices.PVSelParameters.maxDistanceToBeam = 2
    process.offlinePrimaryVertices.TkFilterParameters.maxNormalizedChi2 = 20
    process.offlinePrimaryVertices.TkFilterParameters.maxD0Significance = 100
    process.offlinePrimaryVertices.TkFilterParameters.minPixelLayersWithHits = 2
    process.offlinePrimaryVertices.TkFilterParameters.minSiliconLayersWithHits = 5
    process.offlinePrimaryVertices.TkClusParameters.TkGapClusParameters.zSeparation = 1

    ## ECAL 
    process.ecalRecHit.ChannelStatusToBeExcluded = [ 1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 78, 142 ]

    ##Preshower
    process.ecalPreshowerRecHit.ESBaseline = 0

    ##Preshower algo for data is different than for MC
    process.ecalPreshowerRecHit.ESRecoAlgo = cms.untracked.int32(1)

    ## HCAL temporary fixes
    process.hfreco.firstSample  = 3
    process.hfreco.samplesToAdd = 4
    process.hfreco.PETstat.short_R = cms.vdouble([0.8])
    
    ## EGAMMA
    process.photons.minSCEtBarrel = 5.
    process.photons.minSCEtEndcap =5.
    process.photonCore.minSCEt = 5.
    process.conversionTrackCandidates.minSCEt =5.
    process.conversions.minSCEt =5.
    process.trackerOnlyConversions.rCut = 2.
    process.trackerOnlyConversions.vtxChi2 = 0.0005
    
    ###
    ###  end of top level replacements
    ###
    ###############################################################################################

    return (process)


# End of customisation function definition

process = customise(process)
