import ROOT as r

Ana = ['thad', 'Whad']

path = {}
path['thad'] = '/eos/experiment/fcc/hh/analyses/W_top_vs_QCD_tagger/heppy_outputs/fcc_v02/TMVA_trainings/TMVA_BDT_thad_vs_QCD.root'
path['Whad'] = '/eos/experiment/fcc/hh/analyses/W_top_vs_QCD_tagger/heppy_outputs/fcc_v02/TMVA_trainings/TMVA_BDT_Whad_vs_QCD.root'

infile = {}
infile['thad'] = r.TFile.Open(path['thad'])
infile['Whad'] = r.TFile.Open(path['Whad'])

hist = {}
hist['thad'] = infile['thad'].Get('thad_vs_QCD/Method_BDT_thad_vs_QCD/BDT_thad_vs_QCD/MVA_BDT_thad_vs_QCD_trainingEffBvsS')
hist['Whad'] = infile['Whad'].Get('Whad_vs_QCD/Method_BDT_Whad_vs_QCD/BDT_Whad_vs_QCD/MVA_BDT_Whad_vs_QCD_trainingEffBvsS')

legend = {}
legend['thad'] = '#scale[1.3]{t_{ #scale[1.05]{had}} vs. QCD tagger}'
legend['Whad'] = '#scale[1.3]{W_{ #scale[1.05]{had}} vs. QCD tagger}'

color = {}
color['thad'] = r.kRed
color['Whad'] = r.kBlue

canvas = r.TCanvas(legend['thad'], legend['thad'], 600, 600)
canvas.SetLogy(True)
canvas.SetTicks(1,1)
canvas.SetLeftMargin(0.14)
canvas.SetRightMargin(0.08)
r.gStyle.SetOptStat(0)

leg = r.TLegend(0.35,0.12,0.9,0.3)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetLineColor(0)
leg.SetShadowColor(10)
leg.SetTextSize(0.035)
leg.SetTextFont(42)

############
for ana in Ana :
      hist[ana].SetLineWidth(3)
      hist[ana].SetLineColor(color[ana])
      leg.AddEntry(hist[ana],legend[ana],"l")
      
hist['thad'].GetYaxis().SetTitleOffset(1.45)
hist['thad'].GetXaxis().SetTitleOffset(1.15)
hist['thad'].SetTitle("")
hist['thad'].GetXaxis().SetTitle("Signal efficiency")
hist['thad'].GetYaxis().SetTitle("Background efficiency")
      
hist['thad'].SetMaximum(1.)
hist['thad'].SetMinimum(1.e-4)
hist['thad'].GetXaxis().SetRangeUser(0.2, 1.)

hist['thad'].Draw()
hist['Whad'].Draw("same")
leg.Draw("same")
      
Text = r.TLatex()
      
Text.SetNDC()
Text.SetTextAlign(31);
Text.SetTextSize(0.04)

leftText = 'Boosted topology'      
text = '#it{' + leftText +'}'
Text.DrawLatex(0.90, 0.92, text)
      
canvas.RedrawAxis()
canvas.GetFrame().SetBorderSize( 12 )
canvas.Modified()
canvas.Update()

canvas.Print('effQCD_vs_effWhadBlue_thadRed_log.pdf')

