import ROOT, sys
from bin.tools import train

#### input variables to be used for training ###
variables = [

    'Jet1_trk02_tau1',
    'Jet1_trk02_tau2',
    'Jet1_trk02_tau3',
    'Jet1_trk02_tau32',
    'Jet1_trk02_tau21',
    'Jet1_trk02_tau31',
    'Jet1_trk02_SD_Corr_m',
    'Jet1_trk02_Corr_MetCorr_m',
]

#### define signal and background trees + selection to be applied ###

eospath = '/eos/experiment/fcc/hh/analyses/Zprime_tt/heppy_outputs/fcc_v02/'

bkgTree = eospath + 'pp_jj_lo/heppy.FCChhAnalyses.Zprime_tt.TreeProducer.TreeProducer_1/tree.root'
sigTree = eospath + 'pp_Zprime_20TeV_ttbar/heppy.FCChhAnalyses.Zprime_tt.TreeProducer.TreeProducer_1/tree.root'

cuts    = 'Jet1_trk02_Corr_MetCorr_pt > 7500. && Jet1_trk02_Corr_MetCorr_pt < 12500. && abs(Jet1_trk02_Corr_MetCorr_eta) < 2.5'

#### define MVA method ###

method = 'BDT'
nTrain = 5000
label = 'Zp_M_20TeV'


#### train the MVA ####
train(bkgTree, sigTree, variables, method, nTrain, label, cuts)


#### check the output with the TMVAGUI ####

outFileName = 'TMVA_{}_{}.root'.format(method, label)
ROOT.TMVA.TMVAGui(outFileName, label)
raw_input('Press Enter to continue...')
