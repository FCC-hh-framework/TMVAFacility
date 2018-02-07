import ROOT, sys
from bin.tools import train

#### input variables to be used for training ###
variables = [

    'Jet1_trk02_tau32',
    'Jet1_trk02_tau31',
    'Jet1_trk02_tau21',
    'Jet1_trk02_SD_Corr_m',
    'Jet1_trk02_SD_Corr_pt',
    'Jet2_trk02_tau32',
    'Jet2_trk02_tau31',
    'Jet2_trk02_tau21',
    'Jet2_trk02_SD_Corr_m',
    'Jet2_trk02_SD_Corr_pt',
    'missingET',
    'rapiditySeparation_trk02',
    'transverseMomentumAsymmetry_trk02',
]

#### define signal and background trees + selection to be applied ###

eospath = '/eos/experiment/fcc/hh/analyses/Zprime_tt/heppy_outputs/fcc_v02_mvaQCD/'

bkgTree = eospath + 'pp_jj_lo_filter_pTjet7_5TeV/heppy.FCChhAnalyses.Zprime_tt.TreeProducer.TreeProducer_1/tree.root'
sigTree = eospath + 'pp_Zprime_20TeV_ttbar_qcdBDTtrain/heppy.FCChhAnalyses.Zprime_tt.TreeProducer.TreeProducer_1/tree.root'

SIGcuts = ''
BKGcuts = 'Mj1j2_trk02>10000.'
cuts    = [SIGcuts,BKGcuts]

#### define MVA method ###

method = 'BDT'
#nTrain = 50000
nTrain = 0
label = 'Zp_M_20TeV'


#### train the MVA ####
train(bkgTree, sigTree, variables, method, nTrain, label, cuts)


#### check the output with the TMVAGUI ####

#outFileName = 'TMVA_{}_{}.root'.format(method, label)
#ROOT.TMVA.TMVAGui(outFileName, label)
#raw_input('Press Enter to continue...')
