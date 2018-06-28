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

eospath = '/eos/experiment/fcc/hh/analyses/W_top_vs_QCD_tagger/heppy_outputs/fcc_v02/'

bkgTree = eospath + 'p8_pp_jj_lo_tagger/heppy.FCChhAnalyses.W_top_vs_QCD_tagger.TreeProducer.TreeProducer_1/tree_jetlist.root'
sigTree = eospath + 'p8_pp_Zprime_20TeV_ttbar_tagger/heppy.FCChhAnalyses.W_top_vs_QCD_tagger.TreeProducer.TreeProducer_1/tree_jetlist.root'

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
