import FWCore.ParameterSet.Config as cms

print "Running on data"

# filter HLT paths for T&P
import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt

HLTLIST_TAG = cms.VPSet(
    #MuTau SingleL1
    cms.PSet (
        HLT = cms.string("HLT_IsoMu27_v"),
        path1 = cms.vstring ("hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p07"),
        path2 = cms.vstring (""),
        leg1 = cms.int32(13),
        leg2 = cms.int32(13)
    ),
)


HLTLIST = cms.VPSet(
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_LooseChargedIsoPFTau20_SingleL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sSingleMu22erL1f0L2f10QL3f24QL3trkIsoFiltered0p07", "hltOverlapFilterIsoMu24LooseChargedIsoPFTau20"),
        path2 = cms.vstring ("hltPFTau20TrackLooseChargedIsoAgainstMuon", "hltOverlapFilterIsoMu24LooseChargedIsoPFTau20"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_LooseChargedIsoPFTau20_TightID_SingleL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sSingleMu22erL1f0L2f10QL3f24QL3trkIsoFiltered0p07", "hltOverlapFilterIsoMu24LooseChargedIsoTightOOSCPhotonsPFTau20"),
        path2 = cms.vstring ("hltPFTau20TrackLooseChargedIsoTightOOSCPhotonsAgainstMuon", "hltOverlapFilterIsoMu24LooseChargedIsoTightOOSCPhotonsPFTau20"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_MediumChargedIsoPFTau20_SingleL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sSingleMu22erL1f0L2f10QL3f24QL3trkIsoFiltered0p07", "hltOverlapFilterIsoMu24MediumChargedIsoPFTau20"),
        path2 = cms.vstring ("hltPFTau20TrackMediumChargedIsoAgainstMuon", "hltOverlapFilterIsoMu24MediumChargedIsoPFTau20"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_MediumChargedIsoPFTau20_TightID_SingleL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sSingleMu22erL1f0L2f10QL3f24QL3trkIsoFiltered0p07", "hltOverlapFilterIsoMu24MediumChargedIsoTightOOSCPhotonsPFTau20"),
        path2 = cms.vstring ("hltPFTau20TrackMediumChargedIsoTightOOSCPhotonsAgainstMuon", "hltOverlapFilterIsoMu24MediumChargedIsoTightOOSCPhotonsPFTau20"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_TightChargedIsoPFTau20_SingleL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sSingleMu22erL1f0L2f10QL3f24QL3trkIsoFiltered0p07", "hltOverlapFilterIsoMu24TightChargedIsoPFTau20"),
        path2 = cms.vstring ("hltPFTau20TrackTightChargedIsoAgainstMuon", "hltOverlapFilterIsoMu24TightChargedIsoPFTau20"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_TightChargedIsoPFTau20_TightID_SingleL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sSingleMu22erL1f0L2f10QL3f24QL3trkIsoFiltered0p07", "hltOverlapFilterIsoMu24TightChargedIsoTightOOSCPhotonsPFTau20"),
        path2 = cms.vstring ("hltPFTau20TrackTightChargedIsoTightOOSCPhotonsAgainstMuon", "hltOverlapFilterIsoMu24TightChargedIsoTightOOSCPhotonsPFTau20"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_LooseChargedIsoPFTau35_Trk1_eta2p1_Reg_CrossL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sBigOrMuXXerIsoTauYYerL1f0L2f10QL3f20QL3trkIsoFiltered0p07", "hltOverlapFilterIsoMu24LooseChargedIsoPFTau35MonitoringReg"),
        path2 = cms.vstring ("hltSelectedPFTau35TrackPt1LooseChargedIsolationL1HLTMatchedReg", "hltOverlapFilterIsoMu24LooseChargedIsoPFTau35MonitoringReg"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_LooseChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_CrossL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sBigOrMuXXerIsoTauYYerL1f0L2f10QL3f20QL3trkIsoFiltered0p07", "hltOverlapFilterIsoMu24LooseChargedIsoAndTightOOSCPhotonsPFTau35MonitoringReg"),
        path2 = cms.vstring ("hltSelectedPFTau35TrackPt1LooseChargedIsolationAndTightOOSCPhotonsL1HLTMatchedReg", "hltOverlapFilterIsoMu24LooseChargedIsoAndTightOOSCPhotonsPFTau35MonitoringReg"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_MediumChargedIsoPFTau35_Trk1_eta2p1_Reg_CrossL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sBigOrMuXXerIsoTauYYerL1f0L2f10QL3f20QL3trkIsoFiltered0p07", "hltOverlapFilterIsoMu24MediumChargedIsoPFTau35MonitoringReg"),
        path2 = cms.vstring ("hltSelectedPFTau35TrackPt1MediumChargedIsolationL1HLTMatchedReg", "hltOverlapFilterIsoMu24MediumChargedIsoPFTau35MonitoringReg"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_MediumChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_CrossL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sBigOrMuXXerIsoTauYYerL1f0L2f10QL3f20QL3trkIsoFiltered0p07", "hltOverlapFilterIsoMu24MediumChargedIsoAndTightOOSCPhotonsPFTau35MonitoringReg"),
        path2 = cms.vstring ("hltSelectedPFTau35TrackPt1MediumChargedIsolationAndTightOOSCPhotonsL1HLTMatchedReg", "hltOverlapFilterIsoMu24MediumChargedIsoAndTightOOSCPhotonsPFTau35MonitoringReg"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_TightChargedIsoPFTau35_Trk1_eta2p1_Reg_CrossL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sBigOrMuXXerIsoTauYYerL1f0L2f10QL3f20QL3trkIsoFiltered0p07", "hltOverlapFilterIsoMu24TightChargedIsoPFTau35MonitoringReg"),
        path2 = cms.vstring ("hltSelectedPFTau35TrackPt1TightChargedIsolationL1HLTMatchedReg", "hltOverlapFilterIsoMu24TightChargedIsoPFTau35MonitoringReg"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_TightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_CrossL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sBigOrMuXXerIsoTauYYerL1f0L2f10QL3f20QL3trkIsoFiltered0p07", "hltOverlapFilterIsoMu24TightChargedIsoAndTightOOSCPhotonsPFTau35MonitoringReg"),
        path2 = cms.vstring ("hltSelectedPFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsL1HLTMatchedReg", "hltOverlapFilterIsoMu24TightChargedIsoAndTightOOSCPhotonsPFTau35MonitoringReg"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
 
)



hltFilter = hlt.hltHighLevel.clone(
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = ['HLT_IsoMu27_v*'],
    andOr = cms.bool(True), # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(True) #if True: throws exception if a trigger path is invalid
)

## good muons for T&P
goodMuons = cms.EDFilter("PATMuonRefSelector",
        src = cms.InputTag("slimmedMuons"),
        cut = cms.string(
         #       'pt > 5 && abs(eta) < 2.1 ' # kinematics
                'pt > 27 && abs(eta) < 2.1 ' # kinematics
                '&& ( (pfIsolationR04().sumChargedHadronPt + max(pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - 0.5 * pfIsolationR04().sumPUPt, 0.0)) / pt() ) < 0.1 ' # isolation
                '&& isLooseMuon()' # quality -- medium muon
        ),
        filter = cms.bool(True)
)

## good taus - apply analysis selection
goodTaus = cms.EDFilter("PATTauRefSelector",
        src = cms.InputTag("slimmedTaus"),
        cut = cms.string(
        #        'pt > 5 && abs(eta) < 2.1 ' #kinematics
                'pt > 20 && abs(eta) < 2.1 ' #kinematics
                '&& abs(charge) > 0 && abs(charge) < 2 ' #sometimes 2 prongs have charge != 1
                '&& tauID("decayModeFinding") > 0.5 ' # tau ID
                '&& tauID("byLooseIsolationMVArun2v1DBoldDMwLT") > 0.5 '
                '&& tauID("againstMuonTight3") > 0.5 ' # anti Muon tight
                #'&& tauID("againstElectronVLooseMVA6") > 0.5 ' # anti-Ele loose
        ),
        filter = cms.bool(True)
)


patTriggerUnpacker = cms.EDProducer("PATTriggerObjectStandAloneUnpacker",
  patTriggerObjectsStandAlone = cms.InputTag("slimmedPatTrigger"),
  triggerResults = cms.InputTag('TriggerResults', '', "HLT"),
  unpackFilterLabels = cms.bool(True)
)



TagAndProbe = cms.EDFilter("TauTagAndProbeFilter",
        taus  = cms.InputTag("goodTaus"),
        muons = cms.InputTag("goodMuons"),
        met   = cms.InputTag("slimmedMETs"),
        useMassCuts = cms.bool(False)
)

Ntuplizer = cms.EDAnalyzer("Ntuplizer",
    treeName = cms.string("TagAndProbe"),
    genCollection = cms.InputTag(""),
    muons = cms.InputTag("TagAndProbe"),
    taus = cms.InputTag("TagAndProbe"),
    triggerList = HLTLIST,
    triggerList_tag = HLTLIST_TAG,
    triggerSet = cms.InputTag("patTriggerUnpacker"),
    triggerResultsLabel = cms.InputTag("TriggerResults", "", "HLT"),
    L1Tau = cms.InputTag("caloStage2Digis", "Tau", "RECO"),
    #L1EmuTau = cms.InputTag("simCaloStage2Digis"),
    L1EmuTau = cms.InputTag("simCaloStage2Digis", "MP"),
    Vertexes = cms.InputTag("offlineSlimmedPrimaryVertices"),
    L2CaloJet_ForIsoPix_Collection = cms.InputTag("hltL2TausForPixelIsolation", "", "TEST"),
    L2CaloJet_ForIsoPix_IsoCollection = cms.InputTag("hltL2TauPixelIsoTagProducer", "", "TEST")   
)

TAndPseq = cms.Sequence(
    hltFilter        +
    goodMuons +
    goodTaus +
    TagAndProbe
)

NtupleSeq = cms.Sequence(
    patTriggerUnpacker +
    Ntuplizer
)
