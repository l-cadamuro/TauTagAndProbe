#ifndef NTUPLIZER_H
#define NTUPLIZER_H

#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <utility>
#include <TNtuple.h>
#include <TString.h>
#include <bitset>


#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include <FWCore/Framework/interface/Frameworkfwd.h>
#include <FWCore/Framework/interface/Event.h>
#include <FWCore/Framework/interface/ESHandle.h>
#include <FWCore/Utilities/interface/InputTag.h>
#include <DataFormats/PatCandidates/interface/Muon.h>
#include <DataFormats/PatCandidates/interface/Tau.h>
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "DataFormats/L1Trigger/interface/Tau.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

// for track propagator - use methods from fastsim
#include "FastSimulation/BaseParticlePropagator/interface/BaseParticlePropagator.h"
#include "FastSimulation/Particle/interface/RawParticle.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"


#include "tParameterSet.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"



//Set this variable to decide the number of triggers that you want to check simultaneously
#define NUMBER_OF_MAXIMUM_TRIGGERS 64


/*
██████  ███████  ██████ ██       █████  ██████   █████  ████████ ██  ██████  ███    ██
██   ██ ██      ██      ██      ██   ██ ██   ██ ██   ██    ██    ██ ██    ██ ████   ██
██   ██ █████   ██      ██      ███████ ██████  ███████    ██    ██ ██    ██ ██ ██  ██
██   ██ ██      ██      ██      ██   ██ ██   ██ ██   ██    ██    ██ ██    ██ ██  ██ ██
██████  ███████  ██████ ███████ ██   ██ ██   ██ ██   ██    ██    ██  ██████  ██   ████
*/

class Ntuplizer : public edm::EDAnalyzer {
    public:
        /// Constructor
        explicit Ntuplizer(const edm::ParameterSet&);
        /// Destructor
        virtual ~Ntuplizer();

    private:
        //----edm control---
        virtual void beginJob() ;
        virtual void beginRun(edm::Run const&, edm::EventSetup const&);
        virtual void analyze(const edm::Event&, const edm::EventSetup&);
        virtual void endJob();
        virtual void endRun(edm::Run const&, edm::EventSetup const&);
        void Initialize();
        bool hasFilters(const pat::TriggerObjectStandAlone&  obj , const std::vector<std::string>& filtersToLookFor);

        std::pair<float,float> getEtaPhiAtEcalEntrance(const pat::TauRef& tau, const edm::EventSetup &iSetup);
        // bool atECalEntrnce(const edm::EventSetup &iSetup, const pat::PackedCandidate &cand, math::XYZPoint &pos, math::XYZTLorentzVector &mom);
        bool atECalEntrnce(const edm::EventSetup &iSetup, const reco::Candidate &cand, math::XYZPoint &pos, math::XYZTLorentzVector &mom);

        TTree *_tree;
        TTree *_triggerNamesTree;
        std::string _treeName;
        // -------------------------------------
        // variables to be filled in output tree
        ULong64_t       _indexevents;
        Int_t           _runNumber;
        Int_t           _lumi;
        unsigned long _tauTriggerBits;
        float _tauPt;
        float _tauEta;
        float _tauPhi;
        int   _tauCharge;
        int   _tauDecayMode;
        float _tauEtaAtEcalEntrance;
        float _tauPhiAtEcalEntrance;
        float _tauEtaAtEcalEntranceCheck; // the embedded quantity, as a xcheck for propagation
        float _hltPt;
        float _hltEta;
        float _hltPhi;
        int _l1tQual;
        float _l1tPt;
        float _l1tEta;
        float _l1tPhi;
        int _l1tIso;
        Bool_t _hasTriggerMuonType;
        Bool_t _hasTriggerTauType;
        Bool_t _isMatched;
        Bool_t _isOS;
        int _foundJet;
        float _muonPt;
        float _muonEta;
        float _muonPhi;
        int _Nvtx;
        float _rho;

        edm::EDGetTokenT<pat::MuonRefVector>  _muonsTag;
        edm::EDGetTokenT<pat::TauRefVector>   _tauTag;
        edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> _triggerObjects;
        edm::EDGetTokenT<edm::TriggerResults> _triggerBits;
        edm::EDGetTokenT<l1t::TauBxCollection> _L1TauTag  ;
        edm::EDGetTokenT<std::vector<reco::Vertex>> _VtxTag;
        edm::EDGetTokenT<double> _rhoTag;

        //!Contains the parameters
        tVParameterSet _parameters;

        edm::InputTag _processName;
        //! Maximum
        std::bitset<NUMBER_OF_MAXIMUM_TRIGGERS> _tauTriggerBitSet;



        HLTConfigProvider _hltConfig;


};

/*
██ ███    ███ ██████  ██      ███████ ███    ███ ███████ ███    ██ ████████  █████  ████████ ██  ██████  ███    ██
██ ████  ████ ██   ██ ██      ██      ████  ████ ██      ████   ██    ██    ██   ██    ██    ██ ██    ██ ████   ██
██ ██ ████ ██ ██████  ██      █████   ██ ████ ██ █████   ██ ██  ██    ██    ███████    ██    ██ ██    ██ ██ ██  ██
██ ██  ██  ██ ██      ██      ██      ██  ██  ██ ██      ██  ██ ██    ██    ██   ██    ██    ██ ██    ██ ██  ██ ██
██ ██      ██ ██      ███████ ███████ ██      ██ ███████ ██   ████    ██    ██   ██    ██    ██  ██████  ██   ████
*/

// ----Constructor and Destructor -----
Ntuplizer::Ntuplizer(const edm::ParameterSet& iConfig) :
_muonsTag       (consumes<pat::MuonRefVector>                     (iConfig.getParameter<edm::InputTag>("muons"))),
_tauTag         (consumes<pat::TauRefVector>                      (iConfig.getParameter<edm::InputTag>("taus"))),
_triggerObjects (consumes<pat::TriggerObjectStandAloneCollection> (iConfig.getParameter<edm::InputTag>("triggerSet"))),
_triggerBits    (consumes<edm::TriggerResults>                    (iConfig.getParameter<edm::InputTag>("triggerResultsLabel"))),
_L1TauTag       (consumes<l1t::TauBxCollection>                   (iConfig.getParameter<edm::InputTag>("L1Tau"))),
_VtxTag         (consumes<std::vector<reco::Vertex>>              (iConfig.getParameter<edm::InputTag>("Vertexes"))),
_rhoTag         (consumes<double>                                 (iConfig.getParameter<edm::InputTag>("rho")))
{
    this -> _treeName = iConfig.getParameter<std::string>("treeName");
    this -> _processName = iConfig.getParameter<edm::InputTag>("triggerResultsLabel");

    TString triggerName;
    edm::Service<TFileService> fs;
    this -> _triggerNamesTree = fs -> make<TTree>("triggerNames", "triggerNames");
    this -> _triggerNamesTree -> Branch("triggerNames",&triggerName);

    //Building the trigger arrays
    const std::vector<edm::ParameterSet>& HLTList = iConfig.getParameter <std::vector<edm::ParameterSet> > ("triggerList");
    for (const edm::ParameterSet& parameterSet : HLTList) {
        tParameterSet pSet;
        pSet.hltPath = parameterSet.getParameter<std::string>("HLT");
        triggerName = pSet.hltPath;
        pSet.hltFilters1 = parameterSet.getParameter<std::vector<std::string> >("path1");
        pSet.hltFilters2 = parameterSet.getParameter<std::vector<std::string> >("path2");
        pSet.leg1 = parameterSet.getParameter<int>("leg1");
        pSet.leg2 = parameterSet.getParameter<int>("leg2");
        this -> _parameters.push_back(pSet);

        this -> _triggerNamesTree -> Fill();
    }


    this -> Initialize();
    return;
}

Ntuplizer::~Ntuplizer()
{}

void Ntuplizer::beginRun(edm::Run const& iRun, edm::EventSetup const& iSetup)
{
    Bool_t changedConfig = false;

    if(!this -> _hltConfig.init(iRun, iSetup, this -> _processName.process(), changedConfig)){
        edm::LogError("HLTMatchingFilter") << "Initialization of HLTConfigProvider failed!!";
        return;
    }

    const edm::TriggerNames::Strings& triggerNames = this -> _hltConfig.triggerNames();
    //std::cout << " ===== LOOKING FOR THE PATH INDEXES =====" << std::endl;
    for (tParameterSet& parameter : this -> _parameters){
        const std::string& hltPath = parameter.hltPath;
        bool found = false;
        for(unsigned int j=0; j < triggerNames.size(); j++)
        {
            //std::cout << triggerNames[j] << std::endl;
            if (triggerNames[j].find(hltPath) != std::string::npos) {
                found = true;
                parameter.hltPathIndex = j;

                //std::cout << "### FOUND AT INDEX #" << j << " --> " << triggerNames[j] << std::endl;
            }
        }
        if (!found) parameter.hltPathIndex = -1;
    }

}

void Ntuplizer::Initialize() {
    this -> _indexevents = 0;
    this -> _runNumber = 0;
    this -> _lumi = 0;
    this -> _tauPt = -1.;
    this -> _isMatched = false;
    this -> _hltPt = -1;
    this -> _hltEta = 666;
    this -> _hltPhi = 666;
    this -> _l1tPt = -1;
    this -> _l1tEta = 666;
    this -> _l1tPhi = 666;
    this -> _l1tQual = -1;
    this -> _l1tIso = -1;
    this -> _foundJet = 0;
}


void Ntuplizer::beginJob()
{
    edm::Service<TFileService> fs;
    this -> _tree = fs -> make<TTree>(this -> _treeName.c_str(), this -> _treeName.c_str());

    //Branches
    this -> _tree -> Branch("EventNumber",&_indexevents,"EventNumber/l");
    this -> _tree -> Branch("RunNumber",&_runNumber,"RunNumber/I");
    this -> _tree -> Branch("lumi",&_lumi,"lumi/I");
    this -> _tree -> Branch("tauTriggerBits", &_tauTriggerBits, "tauTriggerBits/l");
    this -> _tree -> Branch("tauPt",  &_tauPt,  "tauPt/F");
    this -> _tree -> Branch("tauEta", &_tauEta, "tauEta/F");
    this -> _tree -> Branch("tauPhi", &_tauPhi, "tauPhi/F");
    this -> _tree -> Branch("tauCharge", &_tauCharge, "tauCharge/I");
    this -> _tree -> Branch("tauDecayMode", &_tauDecayMode, "tauDecayMode/I");
    this -> _tree -> Branch("tauEtaAtEcalEntrance",      &_tauEtaAtEcalEntrance,      "tauEtaAtEcalEntrance/F");
    this -> _tree -> Branch("tauPhiAtEcalEntrance",      &_tauPhiAtEcalEntrance,      "tauPhiAtEcalEntrance/F");
    this -> _tree -> Branch("tauEtaAtEcalEntranceCheck", &_tauEtaAtEcalEntranceCheck, "tauEtaAtEcalEntranceCheck/F");
    this -> _tree -> Branch("muonPt",  &_muonPt,  "muonPt/F");
    this -> _tree -> Branch("muonEta", &_muonEta, "muonEta/F");
    this -> _tree -> Branch("muonPhi", &_muonPhi, "muonPhi/F");
    this -> _tree -> Branch("hltPt",  &_hltPt,  "hltPt/F");
    this -> _tree -> Branch("hltEta", &_hltEta, "hltEta/F");
    this -> _tree -> Branch("hltPhi", &_hltPhi, "hltPhi/F");
    this -> _tree -> Branch("l1tPt",  &_l1tPt,  "l1tPt/F");
    this -> _tree -> Branch("l1tEta", &_l1tEta, "l1tEta/F");
    this -> _tree -> Branch("l1tPhi", &_l1tPhi, "l1tPhi/F");
    this -> _tree -> Branch("l1tQual", &_l1tQual, "l1tQual/I");
    this -> _tree -> Branch("l1tIso", &_l1tIso, "l1tIso/I");
    this -> _tree -> Branch("hasTriggerMuonType", &_hasTriggerMuonType, "hasTriggerMuonType/O");
    this -> _tree -> Branch("hasTriggerTauType", &_hasTriggerTauType, "hasTriggerTauType/O");
    this -> _tree -> Branch("isMatched", &_isMatched, "isMatched/O");
    this -> _tree -> Branch("isOS", &_isOS, "isOS/O");
    this -> _tree -> Branch("foundJet", &_foundJet, "foundJet/I");
    this -> _tree -> Branch("Nvtx", &_Nvtx, "Nvtx/I");
    this -> _tree -> Branch("rho", &_rho, "rho/F");

    return;
}


void Ntuplizer::endJob()
{
    return;
}


void Ntuplizer::endRun(edm::Run const& iRun, edm::EventSetup const& iSetup)
{
    return;
}


void Ntuplizer::analyze(const edm::Event& iEvent, const edm::EventSetup& eSetup)
{
    this -> Initialize();

    _indexevents = iEvent.id().event();
    _runNumber = iEvent.id().run();
    _lumi = iEvent.luminosityBlock();

    // std::auto_ptr<pat::MuonRefVector> resultMuon(new pat::MuonRefVector);

    // search for the tag in the event
    edm::Handle<pat::MuonRefVector> muonHandle;
    edm::Handle<pat::TauRefVector>  tauHandle;
    edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjects;
    edm::Handle<edm::TriggerResults> triggerBits;
    edm::Handle<std::vector<reco::Vertex> >  vertexes;
    edm::Handle<double> rho;

    iEvent.getByToken(this -> _muonsTag, muonHandle);
    iEvent.getByToken(this -> _tauTag,   tauHandle);
    iEvent.getByToken(this -> _triggerObjects, triggerObjects);
    iEvent.getByToken(this -> _triggerBits, triggerBits);
    iEvent.getByToken(this -> _VtxTag,vertexes);
    iEvent.getByToken(this -> _rhoTag,rho);

//! TagAndProbe on HLT taus
    const edm::TriggerNames &names = iEvent.triggerNames(*triggerBits);
    const pat::TauRef tau = (*tauHandle)[0] ;
    const pat::MuonRef muon = (*muonHandle)[0] ;

    this -> _isOS = (muon -> charge() / tau -> charge() < 0) ? true : false;


    this -> _tauTriggerBitSet.reset();



    for (pat::TriggerObjectStandAlone  obj : *triggerObjects)
    {
        const float dR = deltaR (*tau, obj);
        if ( dR < 0.5)
        {
            this -> _isMatched = true;
            this -> _hasTriggerTauType = obj.hasTriggerObjectType(trigger::TriggerTau);
            this -> _hasTriggerMuonType = obj.hasTriggerObjectType(trigger::TriggerMuon);

            obj.unpackPathNames(names);
            const edm::TriggerNames::Strings& triggerNames = names.triggerNames();
            //Looking for the path
            unsigned int x = 0;
            bool foundTrigger = false;
            for (const tParameterSet& parameter : this -> _parameters)
            {
                if ((parameter.hltPathIndex >= 0)&&(obj.hasPathName(triggerNames[parameter.hltPathIndex], true, false)))
                {
                    foundTrigger = true;
                    //Path found, now looking for the label 1, if present in the parameter set
                    //std::cout << "==== FOUND PATH " << triggerNames[parameter.hltPathIndex] << " ====" << std::endl;
                    //Retrieving filter list for the event
                    const std::vector<std::string>& filters = (parameter.leg1 == 15)? (parameter.hltFilters1):(parameter.hltFilters2);
                    if (this -> hasFilters(obj, filters))
                    {
                        //std::cout << "#### FOUND TAU WITH HLT PATH " << x << " ####" << std::endl;
                        this -> _hltPt = obj.pt();
                        this -> _hltEta = obj.eta();
                        this -> _hltPhi = obj.phi();
                        this -> _tauTriggerBitSet[x] = true;
                        //std::cout << this -> _tauTriggerBitSet.to_string() << std::endl;
                    }
                }
                x++;
            }
            if (foundTrigger) this -> _foundJet++;
        }
    }


    //! TagAndProbe on L1T taus

    edm::Handle< BXVector<l1t::Tau> >  L1TauHandle;
    iEvent.getByToken(_L1TauTag, L1TauHandle);

    float minDR = 0.5; //Uncomment for new match algo

    for (l1t::TauBxCollection::const_iterator bx0TauIt = L1TauHandle->begin(0); bx0TauIt != L1TauHandle->end(0) ; bx0TauIt++)
    {
        const float dR = deltaR(*tau, *bx0TauIt);
        if (dR < minDR) //Uncomment for new match algo
        //if (dR < 0.5) //Uncomment for old match algo
        {
            minDR = dR; //Uncomment for new match algo
            const l1t::Tau& l1tTau = *bx0TauIt;
            this -> _l1tPt = l1tTau.pt();
            this -> _l1tEta = l1tTau.eta();
            this -> _l1tPhi = l1tTau.phi();
            this -> _l1tIso = l1tTau.hwIso();
            this -> _l1tQual = l1tTau.hwQual();
        }
    }

    this -> _tauPt = tau -> pt();
    this -> _tauEta = tau -> eta();
    this -> _tauPhi = tau -> phi();
    this -> _tauCharge = tau -> charge();
    this -> _tauDecayMode = tau -> decayMode();

    this -> _muonPt=muon->pt();
    this -> _muonEta=muon->eta();
    this -> _muonPhi=muon->phi();

    this -> _Nvtx = vertexes->size();
    this -> _rho = *rho;


    pair<float,float> etaphiAtEcalEntrance = getEtaPhiAtEcalEntrance(tau, eSetup);
    this -> _tauEtaAtEcalEntrance = etaphiAtEcalEntrance.first;
    this -> _tauPhiAtEcalEntrance = etaphiAtEcalEntrance.second;
    this -> _tauEtaAtEcalEntranceCheck = tau->etaAtEcalEntrance();

    // cout << "DEBUG    : " << tau->etaAtEcalEntrance() << " " << tau->pfEssential().etaAtEcalEntrance_ << " " << etaphiAtEcalEntrance.first  << endl;
    // cout << " ~~~>    : " << etaphiAtEcalEntrance.second  << endl;
    // cout << " ... cfr : " << tau->eta() << " " << tau->phi() << endl;
    // cout << " ??? was a PF tau? " << tau->isPFTau() << endl;
    // cout << "DEBUG: " << tau->phiAtECalEntrance() << " " << tau->etaAtECalEntrance() << endl;
    // cout << "DEBUG: " << tau->etaAtEcalEntrance() << " " << tau->pfEssential().etaAtEcalEntrance_ << " " << tau->pfEssential().phiAtEcalEntrance_  << endl;
    // cout << " ... cfr: " << tau->eta() << " " << tau->phi() << endl;
    //float deltaPt = this -> _hltPt - this -> _tauPt;
    //if (this -> _foundJet > 1 ) std::cout << "deltaPt: " << deltaPt << " con foundJet " << this -> _foundJet << " hltPt " << this -> _hltPt << endl;

    this -> _tauTriggerBits = this -> _tauTriggerBitSet.to_ulong();
    //std::cout << "++++++++++ FILL ++++++++++" << std::endl;
    this -> _tree -> Fill();

}

bool Ntuplizer::hasFilters(const pat::TriggerObjectStandAlone&  obj , const std::vector<std::string>& filtersToLookFor) {

    const std::vector<std::string>& eventLabels = obj.filterLabels();
    for (const std::string& filter : filtersToLookFor)
    {
        //Looking for matching filters
        bool found = false;
        for (const std::string& label : eventLabels)
        {
            //if (label == std::string("hltOverlapFilterIsoMu17MediumIsoPFTau40Reg"))
            if (label == filter)
            {

                //std::cout << "#### FOUND FILTER " << label << " == " << filter << " ####" << std::endl;
                found = true;
            }
        }
        if(!found) return false;
    }

    return true;
}

// function copied directly from PatTauProducer because only the eta positon is available in CMSSW_8_0_25 (2016 data taking)
// will get obsolete starting from 81X where phiAtEcalEntrance() and etaAtEcalEntrance() methods are implemented in pat::Tat
std::pair<float,float> Ntuplizer::getEtaPhiAtEcalEntrance(const pat::TauRef& tau, const edm::EventSetup &iSetup)
{
    float etaAtEcalEntrance = -999.;
    float phiAtEcalEntrance = -999.;

    // if( tau->isPFTau() ) {
    if (true) {
        // cout << "/// Entering in the getEtaPhiAtEcalEntrance function when isPFTau was " << tau->isPFTau() << endl;
        // edm::Handle<reco::PFTauCollection> pfTaus;
        // iEvent.getByToken(pfTauToken_, pfTaus);
        // reco::PFTauRef pfTauRef(pfTaus, idx);
        // pat::tau::TauPFEssential& aTauPFEssential = aTau.pfEssential_[0];
        // float ecalEnergy = 0;
        // float hcalEnergy = 0;
        float sumPhiTimesEnergy = 0.;
        float sumEtaTimesEnergy = 0.;
        float sumEnergy = 0.;
        // float leadChargedCandPt = -99;
        // float leadChargedCandEtaAtEcalEntrance = -99; 
        // const std::vector<reco::PFCandidatePtr>& signalCands = tau->signalPFCands();
        reco::CandidatePtrVector signalCands = tau->signalCands();

        // cout << "/// got the PF cands, their size is " << signalCands.size() << endl;

        // for(reco::CandidatePtrVector::const_iterator it = signalCands.begin(); it != signalCands.end(); ++it) {
        for (uint idxcand = 0; idxcand < signalCands.size(); ++idxcand)
        {


            // cout << "   ./// got a PF candidate" << endl;
            const reco::CandidatePtr& icand = signalCands[idxcand];
            // ecalEnergy += icand->ecalEnergy();
            // hcalEnergy += icand->hcalEnergy();
           
            math::XYZPoint pos;
            math::XYZTLorentzVector mom;

            // propagate this particle up to the ECAL entrance
            bool propagated = atECalEntrnce(iSetup, *icand, pos, mom);
            double candphiAtEcalEntrance = icand->phi();
            double candetaAtEcalEntrance = icand->eta();
            if( propagated )
            {
                candphiAtEcalEntrance = pos.Phi();
                candetaAtEcalEntrance = pos.Eta();
            }
  
            // sumPhiTimesEnergy += icand->positionAtECALEntrance().phi()*icand->energy();     
            // sumEtaTimesEnergy += icand->positionAtECALEntrance().eta()*icand->energy();
            sumPhiTimesEnergy += candphiAtEcalEntrance*icand->energy();     
            sumEtaTimesEnergy += candetaAtEcalEntrance*icand->energy();
            sumEnergy += icand->energy();    
            // const reco::Track* track = 0;
            // if ( icand->trackRef().isNonnull() ) track = icand->trackRef().get();
            // else if ( icand->muonRef().isNonnull() && icand->muonRef()->innerTrack().isNonnull()  ) track = icand->muonRef()->innerTrack().get();
            // else if ( icand->muonRef().isNonnull() && icand->muonRef()->globalTrack().isNonnull() ) track = icand->muonRef()->globalTrack().get();
            // else if ( icand->muonRef().isNonnull() && icand->muonRef()->outerTrack().isNonnull()  ) track = icand->muonRef()->outerTrack().get();
            // else if ( icand->gsfTrackRef().isNonnull() ) track = icand->gsfTrackRef().get();
            // if( track ) {
            //     if( track->pt() > leadChargedCandPt ) {
            //         leadChargedCandEtaAtEcalEntrance = icand->positionAtECALEntrance().eta();
            //         leadChargedCandPt = track->pt();
            //     }
            // }       
        }
        
        if (sumEnergy != 0.) {
            phiAtEcalEntrance = sumPhiTimesEnergy/sumEnergy;
            etaAtEcalEntrance = sumEtaTimesEnergy/sumEnergy;
        }
        else {
        phiAtEcalEntrance = -99.;
        etaAtEcalEntrance = -99.;
        }
    }

    return make_pair(etaAtEcalEntrance, phiAtEcalEntrance);
}

// --- track propagator, Michal Bluji courtesy, to get ECAL entrance position of a tau
//note that ~5GeV is kind of minimal Pt to reach ECal
//note should work but in orygianl code outerMomentum used raher than momentun (at vertex) which reduces extrapolation. Especially important for electrons which are bend more than other particles because of energy loss due to breamsthralung
bool Ntuplizer::atECalEntrnce(const edm::EventSetup &iSetup,
//           const pat::PackedCandidate &cand,
           const reco::Candidate &cand,
           math::XYZPoint &pos,
           math::XYZTLorentzVector &mom){

  double bField = 3.8;//hepefully Teslas are proper units (better to take it from event setup) 
  BaseParticlePropagator theParticle =
    BaseParticlePropagator(RawParticle(math::XYZTLorentzVector(cand.px(),
                                   cand.py(),
                                   cand.pz(),
                                   cand.energy()),
                                    math::XYZTLorentzVector(cand.vertex().x(),
                                   cand.vertex().y(),
                                   cand.vertex().z(),
                                   0.)),
               0.,0.,bField);
  theParticle.setCharge(cand.charge());

  theParticle.propagateToEcalEntrance(false);

  if(theParticle.getSuccess()!=0){
    pos = math::XYZPoint(theParticle.vertex());
    mom = math::XYZTLorentzVector(theParticle.momentum());
    return true;
  }
  else 
    return false;

  //return;
}


#include <FWCore/Framework/interface/MakerMacros.h>
DEFINE_FWK_MODULE(Ntuplizer);

#endif //NTUPLIZER_H
