import ROOT
from array import array
import os, sys

def train(bkgTree, sigTree, discriList, MVAmethod, nTraining, label, cuts):
    
    file_proc1 = ROOT.TFile(bkgTree)    
    file_proc2 = ROOT.TFile(sigTree)   

    tree_proc1 = file_proc1.Get('events')
    tree_proc2 = file_proc2.Get('events')

    Nproc1 = float(tree_proc1.GetEntries())
    Nproc2 = float(tree_proc2.GetEntries())

    proc1_weight = 1/Nproc1
    proc2_weight = 1/Nproc2

    MVA_fileName = 'TMVA_'+MVAmethod+'_'+label+'.root'
    file_MVA = ROOT.TFile(MVA_fileName,'recreate')

    print 'Will write MVA info in ', MVA_fileName 

    factory = ROOT.TMVA.Factory(MVAmethod, file_MVA)
   
    dataloader = ROOT.TMVA.DataLoader(label);
   
    for discriVar in discriList :
        dataloader.AddVariable(discriVar)

    dataloader.AddSignalTree(tree_proc2, proc2_weight)
    dataloader.AddBackgroundTree(tree_proc1, proc1_weight)
   
    # add cuts here eventually
    
    sigcut = ROOT.TCut(cuts)
    bkgcut = ROOT.TCut(cuts)

    dataloader.PrepareTrainingAndTestTree( ROOT.TCut( sigcut ), ROOT.TCut( bkgcut ),
                                      ':'.join([ 'nTrain_Signal={}'.format(nTraining),     # Number of signal events used, 0 = ALL
                                               'nTrain_Background={}'.format(nTraining), # Number of background events, 0 = ALL
                                               'nTest_Signal={}'.format(nTraining),     # Number of signal events used, 0 = ALL
                                               'nTest_Background={}'.format(nTraining), # Number of background events, 0 = ALL
                                               'SplitMode=Random',    # How are events chosen to be used for either training or testing
                                               'NormMode=NumEvents',  # Integral of datasets is given by number of events
                                                                      #   (could e.g. also be sum of weights or simply defined to be 1)
                                               '!V'                   # Don't print everything (i.e. not verbose) 
                                               ]))
    BDTcfg = '!H:!V:NTrees=4000:MaxDepth=4:BoostType=AdaBoost:AdaBoostBeta=0.5:SeparationType=GiniIndex:nCuts=20:PruneMethod=NoPruning'
    MLPcfg = 'H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:!UseRegulator'

    if MVAmethod == 'BDT':
        factory.BookMethod(dataloader, ROOT.TMVA.Types.kBDT, 'BDT_'+label,BDTcfg)
    elif MVAmethod == 'MLP':
        factory.BookMethod(dataloader, ROOT.TMVA.Types.kMLP, 'N_Nmin1_'+label, MLPcfg)
    elif MVAmethod == 'CUT':
        factory.BookMethod(dataloader, ROOT.TMVA.Types.kCuts, 'MC_'+label, '!H:!V:FitMethod=MC:EffSel:SampleSize=8000000:VarProp=FSmart')
    elif MVAmethod == 'ALL':
        factory.BookMethod(dataloader, ROOT.TMVA.Types.kBDT, 'BDT_'+label,BDTcfg)
        factory.BookMethod(dataloader, ROOT.TMVA.Types.kMLP, 'MLP_'+label, MLPcfg)
        #factory.BookMethod(dataloader, ROOT.TMVA.Types.kCuts, 'MC_'+label, '!H:!V:FitMethod=MC:EffSel:SampleSize=8000000:VarProp=FSmart')
  
      
    else :
        print 'MVA method must be BDT, MLP, CUT or ALL.'
        sys.exit()

    factory.TrainAllMethods()
    factory.TestAllMethods()
    factory.EvaluateAllMethods()
    file_MVA.Close()
