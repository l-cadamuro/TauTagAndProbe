import FWCore.ParameterSet.VarParsing as VarParsing
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Config as cms
process = cms.Process("TagAndProbe")

isMC = True
useGenMatch = False
useCustomHLT = False

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

#### handling of cms line options for tier3 submission
#### the following are dummy defaults, so that one can normally use the config changing file list by hand etc.

options = VarParsing.VarParsing ('analysis')
options.register ('skipEvents',
                  -1, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Number of events to skip")
options.register ('JSONfile',
                  "", # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "JSON file (empty for no JSON)")
options.outputFile = 'NTuple_SingleMu.root'
options.inputFiles = []
options.maxEvents  = -999
options.parseArguments()

if not isMC:
    from Configuration.AlCa.autoCond import autoCond
    process.GlobalTag.globaltag = '92X_dataRun2_HLT_v7'
    process.load('TauTagAndProbe.TauTagAndProbe.tagAndProbe_cff')
    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            '/store/data/Run2017B/SingleMuon/RAW-RECO/MuTau-PromptReco-v1/000/297/488/00000/5CA074E9-C45B-E711-9BDD-02163E0133FE.root'
        ),
    )



else:
    process.GlobalTag.globaltag = '92X_upgrade2017_TSG_For83XSamples_V5'
    process.load('TauTagAndProbe.TauTagAndProbe.MCanalysis_cff')
    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(            
            '/store/user/tstreble/HTauTau_MC_92Xmenu_MuTau/VBFHToTauTau_M125_13TeV_powheg_pythia8/HTauTau_MC_92Xmenu/170724_143442/0000/outputFULL_1.root'
        )
    )


if useCustomHLT:
    process.hltFilter.TriggerResultsTag = cms.InputTag("TriggerResults","","MYHLT")
    process.Ntuplizer.triggerSet = cms.InputTag("selectedPatTriggerCustom", "", "MYHLT")
    process.Ntuplizer.triggerResultsLabel = cms.InputTag("TriggerResults", "", "MYHLT")
    process.Ntuplizer.L2CaloJet_ForIsoPix_Collection = cms.InputTag("hltL2TausForPixelIsolation", "", "MYHLT")
    process.Ntuplizer.L2CaloJet_ForIsoPix_IsoCollection = cms.InputTag("hltL2TauPixelIsoTagProducer", "", "MYHLT")


if isMC and not useGenMatch:
    process.Ntuplizer.taus = cms.InputTag("goodTaus")


if options.JSONfile:
    print "Using JSON: " , options.JSONfile
    process.source.lumisToProcess = LumiList.LumiList(filename = options.JSONfile).getVLuminosityBlockRange()

if options.inputFiles:
    process.source.fileNames = cms.untracked.vstring(options.inputFiles)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

if options.maxEvents >= -1:
    process.maxEvents.input = cms.untracked.int32(options.maxEvents)
if options.skipEvents >= 0:
    process.source.skipEvents = cms.untracked.uint32(options.skipEvents)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.p = cms.Path(
    process.TAndPseq +
    process.NtupleSeq
)

# Silence output
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

# Adding ntuplizer
process.TFileService=cms.Service('TFileService',fileName=cms.string(options.outputFile))
