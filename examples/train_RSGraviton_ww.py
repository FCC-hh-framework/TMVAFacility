import ROOT, sys
from bin.tools import train

#### input variables to be used for training ###
variables = [

    'Jet1_trk02_tau32',
    'Jet1_trk02_tau31',
    'Jet1_trk02_tau21',
    'Jet1_trk02_SD_Corr_m',
    'Jet1_trk02_SD_Corr_pt',
    'Jet1_Flow15',
    'Jet1_Flow25',
    'Jet1_Flow35',
    'Jet1_Flow45',
    'Jet1_Flow55',
    'Jet2_trk02_tau32',
    'Jet2_trk02_tau31',
    'Jet2_trk02_tau21',
    'Jet2_trk02_SD_Corr_m',
    'Jet2_trk02_SD_Corr_pt',
    'Jet2_Flow15',
    'Jet2_Flow25',
    'Jet2_Flow35',
    'Jet2_Flow45',
    'Jet2_Flow55',
    'rapiditySeparation_trk02',
    'transverseMomentumAsymmetry_trk02',
]

#### define signal and background trees + selection to be applied ###

eospath = '/eos/experiment/fcc/hh/analyses/RSGraviton_ww/heppy_outputs/fcc_v02_mvaQCD_jetflow0.2/'

bkgTree = eospath + 'pp_jj_lo_filter_pTjet7_5TeV/heppy.FCChhAnalyses.RSGraviton_ww.TreeProducer.TreeProducer_1/tree.root'
sigTree = eospath + 'pp_RSGraviton_20TeV_ww_qcdBDTtrain/heppy.FCChhAnalyses.RSGraviton_ww.TreeProducer.TreeProducer_1/tree.root'

SIGcuts = ''
BKGcuts = 'Mj1j2_trk02>10000.'
cuts    = [SIGcuts,BKGcuts]

#### define MVA method ###

method = 'BDT'
#nTrain = 50000
nTrain = 0
label = 'RSGraviton_ww_M_20TeV'


#### train the MVA ####
train(bkgTree, sigTree, variables, method, nTrain, label, cuts)


#### check the output with the TMVAGUI ####

#outFileName = 'TMVA_{}_{}.root'.format(method, label)
#ROOT.TMVA.TMVAGui(outFileName, label)
#raw_input('Press Enter to continue...')
