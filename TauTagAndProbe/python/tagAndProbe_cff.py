import FWCore.ParameterSet.Config as cms

print "Running on data"

# filter HLT paths for T&P
import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt


HLTLIST = cms.VPSet(
    cms.PSet (
        HLT = cms.string("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v"),
        path1 = cms.vstring ("hltL3crIsoL1sMu16erTauJet20erL1f0L2f10QL3f17QL3trkIsoFiltered0p09", "hltOverlapFilterIsoMu17LooseIsoPFTau20"),
        path2 = cms.vstring ("hltPFTau20TrackLooseIsoAgainstMuon", "hltOverlapFilterIsoMu17LooseIsoPFTau20"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sSingleMu16erL1f0L2f10QL3f17QL3trkIsoFiltered0p09", "hltOverlapFilterSingleIsoMu17LooseIsoPFTau20"),
        path2 = cms.vstring ("hltPFTau20TrackLooseIsoAgainstMuon", "hltOverlapFilterSingleIsoMu17LooseIsoPFTau20"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ), ### ok
    cms.PSet (
        HLT = cms.string("HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v"),
        path1 = cms.vstring ("hltL3crIsoL1sMu18erTauJet20erL1f0L2f10QL3f19QL3trkIsoFiltered0p09", "hltOverlapFilterIsoMu19LooseIsoPFTau20"),
        path2 = cms.vstring ("hltPFTau20TrackLooseIsoAgainstMuon", "hltOverlapFilterIsoMu19LooseIsoPFTau20"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ), ### ok
    cms.PSet (
        HLT = cms.string("HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sSingleMu18erIorSingleMu20erL1f0L2f10QL3f19QL3trkIsoFiltered0p09", "hltOverlapFilterSingleIsoMu19LooseIsoPFTau20"),
        path2 = cms.vstring ("hltPFTau20TrackLooseIsoAgainstMuon", "hltOverlapFilterSingleIsoMu19LooseIsoPFTau20"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ), ### ok
    cms.PSet (
        HLT = cms.string("HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sSingleMu20erIorSingleMu22erL1f0L2f10QL3f21QL3trkIsoFiltered0p09", "hltOverlapFilterSingleIsoMu21LooseIsoPFTau20"),
        path2 = cms.vstring ("hltPFTau20TrackLooseIsoAgainstMuon", "hltOverlapFilterSingleIsoMu21LooseIsoPFTau20"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu19_eta2p1_MediumIsoPFTau32_Trk1_eta2p1_Reg_v"),
        path1 = cms.vstring ("hltL3crIsoL1sMu18erIsoTau26erL1f0L2f10QL3f19QL3trkIsoFiltered0p09", "hltOverlapFilterIsoMu19MediumIsoPFTau32Reg"),
        path2 = cms.vstring ("hltPFTau32TrackPt1MediumIsolationL1HLTMatchedReg", "hltOverlapFilterIsoMu19MediumIsoPFTau32Reg"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu21_eta2p1_MediumIsoPFTau32_Trk1_eta2p1_Reg_v"),
        path1 = cms.vstring ("hltL3crIsoL1sMu20erIsoTau26erL1f0L2f10QL3f21QL3trkIsoFiltered0p09", "hltOverlapFilterIsoMu21MediumIsoPFTau32Reg"),
        path2 = cms.vstring ("hltPFTau32TrackPt1MediumIsolationL1HLTMatchedReg", "hltOverlapFilterIsoMu21MediumIsoPFTau32Reg"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu19_eta2p1_MediumCombinedIsoPFTau32_Trk1_eta2p1_Reg_v"),
        path1 = cms.vstring ("hltL3crIsoL1sMu18erIsoTau26erL1f0L2f10QL3f19QL3trkIsoFiltered0p09", "hltOverlapFilterIsoMu19MediumCombinedIsoPFTau32Reg"),
        path2 = cms.vstring ("hltPFTau32TrackPt1MediumCombinedIsolationL1HLTMatchedReg", "hltOverlapFilterIsoMu19MediumCombinedIsoPFTau32Reg"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu21_eta2p1_MediumCombinedIsoPFTau32_Trk1_eta2p1_Reg_v"),
        path1 = cms.vstring ("hltL3crIsoL1sMu20erIsoTau26erL1f0L2f10QL3f21QL3trkIsoFiltered0p09", "hltOverlapFilterIsoMu21MediumCombinedIsoPFTau32Reg"),
        path2 = cms.vstring ("hltPFTau32TrackPt1MediumCombinedIsolationL1HLTMatchedReg", "hltOverlapFilterIsoMu21MediumCombinedIsoPFTau32Reg"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    )
)

## I need not to throw an exception because some paths were disables during the data taking
hltFilter = hlt.hltHighLevel.clone(
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    # HLTPaths = ['HLT_IsoMu22_v*'],
    HLTPaths = ['HLT_IsoMu22_eta2p1_v*', 'HLT_IsoTkMu22_eta2p1_v*', 'HLT_IsoMu22_v*', 'HLT_IsoTkMu22_v*'],
    andOr = cms.bool(True), # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False) #if True: throws exception if a trigger path is invalid
)

## only events where slimmedMuons has exactly 1 muon
muonNumberFilter = cms.EDFilter ("muonNumberFilter",
    src = cms.InputTag("slimmedMuons")
)

## good muons for T&P
goodMuons = cms.EDFilter("PATMuonRefSelector",
        src = cms.InputTag("slimmedMuons"),
        cut = cms.string(
                'pt > 24 && abs(eta) < 2.1 ' # kinematics
                '&& ( (pfIsolationR04().sumChargedHadronPt + max(pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - 0.5 * pfIsolationR04().sumPUPt, 0.0)) / pt() ) < 0.15 ' # isolation
                '&& isLooseMuon()' # quality -- medium muon
        ),
        filter = cms.bool(True)
)

## good taus - apply analysis selection
goodTaus = cms.EDFilter("PATTauRefSelector",
        src = cms.InputTag("slimmedTaus"),
        cut = cms.string(
                'pt > 20 && abs(eta) < 2.1 ' #kinematics
                '&& abs(charge) > 0 && abs(charge) < 2 ' #sometimes 2 prongs have charge != 1
                '&& tauID("decayModeFinding") > 0.5 ' # tau ID
                '&& tauID("byTightIsolationMVArun2v1DBoldDMwLT") > 0.5 '
                '&& tauID("againstMuonTight3") > 0.5 ' # anti Muon tight
                '&& tauID("againstElectronVLooseMVA6") > 0.5 ' # anti-Ele loose
        ),
        filter = cms.bool(True)
)

## b jet veto : no additional b jets in the event (reject tt) -- use in sequence with
bjets = cms.EDFilter("PATJetRefSelector",
        src = cms.InputTag("slimmedJets"),
        cut = cms.string(
                'pt > 20 && abs(eta) < 2.4 ' #kinematics
                '&& bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") > 0.8484' # b tag with medium WP
        ),
        filter = cms.bool(True)
)

TagAndProbe = cms.EDFilter("TauTagAndProbeFilter",
        taus  = cms.InputTag("goodTaus"),
        muons = cms.InputTag("goodMuons"),
        met   = cms.InputTag("slimmedMETs")
)

Ntuplizer = cms.EDAnalyzer("Ntuplizer",
    treeName = cms.string("TagAndProbe"),
    muons = cms.InputTag("TagAndProbe"),
    taus = cms.InputTag("TagAndProbe"),
    triggerList = HLTLIST,
    triggerSet = cms.InputTag("selectedPatTrigger"),
    triggerResultsLabel = cms.InputTag("TriggerResults", "", "HLT"),
    L1Tau = cms.InputTag("caloStage2Digis", "Tau", "RECO"),
    Vertexes = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll")
)

TAndPseq = cms.Sequence(
    hltFilter        +
    muonNumberFilter +
    goodMuons        +
    goodTaus         +
    ~bjets           +
    TagAndProbe
)

NtupleSeq = cms.Sequence(
    Ntuplizer
)
