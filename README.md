# TauTagAndProbe
Set of tools to evaluate tau trigger performance on T&amp;P

### Install instructions
```
cmsrel CMSSW_9_2_5_patch2
cd CMSSW_9_2_5_patch2/src
cmsenv
git clone https://github.com/davignon/TauTagAndProbe
scram b -j4
```

Run test.py to produce ntuples including offline taus + various online quantities

### Running on Monte Carlo for HLT
Simply switch the flag isMC accordingly in test.py
It is important to use T&P mu-tau selections as the efficiency is computed using the tau leg of the mu+tau paths.

### Running on Monte Carlo for L1
For Monte Carlo (MC), we implemented a truth matching rather than a Tag & Probe technique which would dramatically and artificially decrease the available statistics.
The MC-specific producers are in two parts:

1. To get the unpacked L1 quantities and the reco information, use:
```
cmsRun test_noTagAndProbe_multipleTaus.py
```
This runs on MiniAOD and will write ntuples that are referred as "offline".
A wrapper for this is: ```submitOnTier3_multipleTaus.py```, where you can specify the name of the dataset to run on, the global tag, etc.

2. To re-emulate the L1 objects with a specific config, you have to run on RAW, and use:
```
cmsRun reEmulL1_MC_L1Only.py
```
The correspond wrapper is: ```submitOnTier3_reEmulL1_MC.py```, where you can specify the name of the dataset to run on, the global tag, etc. Also be mindful that you can specify the emulator version to be run in reEmulL1_MC_L1Only.py by specifying the correct:
```
process.load("L1Trigger.L1TCalorimeter.caloStage2Params_2017_vX_X_XXX_cfi")
```

### Ntuples content
The Ntuple produced that way contain basic tau offline quantities (kinematics, DM, various discriminators) + bits corresponding to various HLT triggers (tauTriggerBits variable) + L1-HLT specific variables (for expert user).

The events stored pass basic mu+tauh T&P selections (OS requirement not applied for filter! isOS variable stored in Ntuple).

The tree triggerNames has the name of all the HLT paths included in the tauTriggerBits variable.

This can be checked for instance with
```
triggerNames->Scan("triggerNames","","colsize=100")
*******************************************************************************************************************
*    Row   *                                                                                         triggerNames *
*******************************************************************************************************************
*        0 *                                                 HLT_IsoMu24_eta2p1_LooseChargedIsoPFTau20_SingleL1_v *
*        1 *                                         HLT_IsoMu24_eta2p1_LooseChargedIsoPFTau20_TightID_SingleL1_v *
*        2 *                                                HLT_IsoMu24_eta2p1_MediumChargedIsoPFTau20_SingleL1_v *
*        3 *                                        HLT_IsoMu24_eta2p1_MediumChargedIsoPFTau20_TightID_SingleL1_v *
*        4 *                                                 HLT_IsoMu24_eta2p1_TightChargedIsoPFTau20_SingleL1_v *
*        5 *                                         HLT_IsoMu24_eta2p1_TightChargedIsoPFTau20_TightID_SingleL1_v *
...
```
The Row of the path correspond to the bit number in the tauTriggerBits variable.

In the example presented here, the decision of the MediumChargedIsoPFTau20 leg can be checked for instance by requiring (tauTriggerBits>>2)&1 (matching with tag muon + offline tau of 0.5 included).


### Plotting: mostly turn-ons
Any basic check can be performed using those Ntuples (efficiency vs pT, eta-phi...) using custom code developed by the user.

A more fancy package is available to produce turn-on plots with CB fits.

For this, the Ntuples must first be converted using the script test/convertTreeForFitting.py (blame RooFit for not being able to deal with custom boolean cuts).

The package for plotting is available in test/fitter/ (to be compiled with make).

The CB fit can be run using a as an example test/fitter/hlt_turnOn_fitter.par (includes example for L1 and HLT turnons w/ subtraction of SS mu+tauh events to take into account contamination from fake taus using bkgSubW weight).

To be launched with
```
./fit.exe run/hlt_turnOn_fitter.par
```
The "Michelangelo" turn-on plot can then be produced adapting the script test/fitter/results/plot_turnOn_Data_vs_MC.py

### Resolutions:
UNDER DEVELOPMENT


