import ROOT

# global parameters
intLumi        = 150.0e+06 #in pb-1

###If scaleSig=0 or scaleBack=0, we don't apply any additional scaling, on top of the normalization to cross section and integrated luminosity, as defined in finalSel.py
###If scaleSig or scaleBack is not defined, plots will be normalized to 1
#scaleSig       = 0.
#scaleBack      = 0.
ana_tex        = "e^{+}e^{-} #rightarrow N_{1,2} #nu, N_{1,2} #rightarrow ll#nu"
delphesVersion = '3.4.2'
energy         = 125
collider       = 'FCC-ee'
inputDir       = '/eos/user/e/espoto/H_pole/FCCAnalyses/gen/final_gen/'
outdir         = '/eos/user/e/espoto/H_pole/FCCAnalyses/gen/plots_gen/'
formats        = ['png']
#formats        = ['pdf']
#yaxis          = ['lin','log']
yaxis          = ['log']
stacksig       = ['nostack']
stackbkg       = ['stack']
#legendCoord    = [0.68,0.76,0.96,0.88]
#plotStatUnc    = True ### to include statistical uncertainty ###
splitLeg       = True ### to split legend for backgrounds and signals ###

variables = [

    #gen variables
    #"FSGenMissing_e", ## ## definito da me in stage1
	#"FSGenMissing_pt", ## ## definito da me in stage1
	#"FSGenMissing_e_nu",
    "n_FSGenElectron",
    "n_FSGenMuon",
    "n_FSGenLepton",
    "n_GenN",
    #"n_FSGenPhoton",
    "n_FSGenNeutrino",

    "FSGenElectron_e",     ## ## just a note: following two group of raws are defined in stage1, but no hint in final
    #"FSGenElectron_p",
    "FSGenElectron_pt",
    #"FSGenElectron_pz",
    "FSGenElectron_eta",
    #"FSGenElectron_theta",
    "FSGenElectron_phi",
    #"FSGenElectron_vertex_x",
    #"FSGenElectron_vertex_y",
    #"FSGenElectron_vertex_z",
    #"FSGenElectron_vertex_x_prompt",
    #"FSGenElectron_vertex_y_prompt",
    #"FSGenElectron_vertex_z_prompt",

    "FSGenMuon_e",
    #"FSGenMuon_p",
    "FSGenMuon_pt",
    #"FSGenMuon_pz",
    "FSGenMuon_eta",
    #"FSGenMuon_theta",
    "FSGenMuon_phi",
    #"FSGenMuon_vertex_x",
    #"FSGenMuon_vertex_y",
    #"FSGenMuon_vertex_z",
    #"FSGenMuon_vertex_x_prompt",
    #"FSGenMuon_vertex_y_prompt",
    #"FSGenMuon_vertex_z_prompt",

    "FSGenLepton_e",   
    #"FSGenLepton_p",
    "FSGenLepton_pt",
    #"FSGenLepton_pz",
    "FSGenLepton_eta",
    #"FSGenLepton_theta",
    "FSGenLepton_phi",
    #"FSGenLepton_vertex_x",
    #"FSGenLepton_vertex_y",
    #"FSGenLepton_vertex_z",
    #"FSGenLepton_vertex_x_prompt",
    #"FSGenLepton_vertex_y_prompt",
    #"FSGenLepton_vertex_z_prompt",

    "FSGenNeutrino_e",
    #"FSGenNeutrino_p",
    "FSGenNeutrino_pt",
    #"FSGenNeutrino_pz",
    "FSGenNeutrino_eta",
    #"FSGenNeutrino_theta",
    "FSGenNeutrino_phi",

    #"FSGenPhoton_e",
    #"FSGenPhoton_p",
    #"FSGenPhoton_pt",
    #"FSGenPhoton_pz",
    #"FSGenPhoton_eta",
    #"FSGenPhoton_theta",
    #"FSGenPhoton_phi",

    "FSGen_Lxy",
    "FSGen_Lxyz",
    "GenN_Lxyz",
    ## ##"FSGen_Lxyz_prompt",
    "FSGen_invMass",

    "GenN_mass",
    "GenN_e",
    "GenN_p",
    ## ## "GenN_time", ## ## no hint of it in final nor stage1
    #"GenN_tau",
    ## ## "GenN_txyz", ## ## no hint of it in final nor stage1
    ## ## "GenN_Lxyz_tau", ## ## no hint of it in final nor stage1
    ## ## "GenN_Lxyz_time",# # ## no hint of it in final nor stage1

    #reco variables
    ## ##"n_RecoTracks",
    ## ##"n_PrimaryTracks",
    ## ##"n_SecondaryTracks",
    ## ##"n_RecoJets",
    ## ##"n_RecoPhotons",
    ## ##"n_RecoElectrons",
    ## ##"n_RecoMuons",
    ## ##"n_RecoLeptons",

    #"jets_e",
    #"RecoJet_e",
    #"RecoJet_p",
    #"RecoJet_pt",
    #"RecoJet_pz",
    #"RecoJet_eta",
    #"RecoJet_theta",
    #"RecoJet_phi",
    #"RecoJet_charge",
    #"RecoJetTrack_absD0",
    #"RecoJetTrack_absD0_prompt",
    #"RecoJetTrack_absZ0",
    #"RecoJetTrack_absZ0_prompt",
    #"RecoJetTrack_absD0sig",
    #"RecoJetTrack_absD0sig_prompt",
    #"RecoJetTrack_absZ0sig",
    #"RecoJetTrack_absZ0sig_prompt",
    #"RecoJetTrack_D0cov",
    #"RecoJetTrack_Z0cov",

    ## ##"RecoElectron_e",
    ## ##"RecoElectron_p",
    ## ##"RecoElectron_pt",
    ## ##"RecoElectron_px",
    ## ##"RecoElectron_py",
    ## ##"RecoElectron_pz",
    ## ##"RecoElectron_eta",
    ## ##"RecoElectron_theta",
    ## ##"RecoElectron_phi",

    ## ##"RecoElectronTrack_absD0",
    ## ##"RecoElectronTrack_absD0_prompt",
    #"RecoElectronTrack_absZ0",
    #"RecoElectronTrack_absZ0_prompt",
    #"RecoElectronTrack_absD0sig",
    #"RecoElectronTrack_absD0sig_med",
    #"RecoElectronTrack_absD0sig_prompt",
    #"RecoElectronTrack_absZ0sig",
    #"RecoElectronTrack_absZ0sig_prompt",
    #"RecoElectronTrack_D0cov",
    #"RecoElectronTrack_Z0cov",

    ## ##"Reco_e",
    ## ##"Reco_p",
    ## ##"Reco_pt",
    ## ##"Reco_px",
    ## ##"Reco_py",
    ## ##"Reco_pz",
    ## ##"Reco_eta",
    ## ##"Reco_theta",
    ## ##"Reco_phi",

    ## ##"RecoTrack_absD0_prompt",
    ## ##"RecoTrack_absZ0_prompt",
    ## ##"RecoTrack_absD0_med",
    ## ##"RecoTrack_absZ0_med",
    ## ##"RecoTrack_absD0",
    ## ##"RecoTrack_absZ0",
    ## ##"RecoTrack_absD0sig",
    ## ##"RecoTrack_absD0sig_med",
    ## ##"RecoTrack_absD0sig_prompt",
    ## ##"RecoTrack_absZ0sig",
    ## ##"RecoTrack_absZ0sig_med",
    ## ##"RecoTrack_absZ0sig_prompt",
    ## ##"RecoTrack_D0cov",
    ## ##"RecoTrack_Z0cov",

    ## ##"Reco_DecayVertexLepton_x",       
    ## ##"Reco_DecayVertexLepton_y",          
    ## ##"Reco_DecayVertexLepton_z",          
    ## ##"Reco_DecayVertexLepton_x_prompt",   
    ## ##"Reco_DecayVertexLepton_y_prompt",    
    ## ##"Reco_DecayVertexLepton_z_prompt",    
    ## ##"Reco_DecayVertexLepton_chi2",    
    ## ##"Reco_DecayVertexLepton_probability", 

    ## ##"Reco_Lxy",
    ## ##"Reco_Lxy_prompt",
    ## ##"Reco_Lxyz",
    ## ##"Reco_Lxyz_prompt",
    
    ## ##"Reco_invMass",
    ## ##"Reco_cos",
    ## ##"Reco_DR",

    ## ##"RecoMissingEnergy_e",
    ## ##"RecoMissingEnergy_p",
    ## ##"RecoMissingEnergy_pt",
    ## ##"RecoMissingEnergy_px",
    ## ##"RecoMissingEnergy_py",
    ## ##"RecoMissingEnergy_pz",
    ## ##"RecoMissingEnergy_eta",
    ## ##"RecoMissingEnergy_theta",
    ## ##"RecoMissingEnergy_phi",

    #"RecoPhoton_e",
    #"RecoPhoton_p",
    #"RecoPhoton_pt",
    #"RecoPhoton_pz",
    #"RecoPhoton_eta",
    #"RecoPhoton_theta",
    #"RecoPhoton_phi",
    #"RecoPhoton_charge",
    
]

    
#Dictionary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['HNL']  = [
    "selReco",
]

extralabel = {}
extralabel['selReco'] = "Before selection"

colors = {}

colors['HNL_1.04e-8_30gev'] = ROOT.kWhite ## ## mod edo
#colors['HNL_4e-8_10gev'] = ROOT.kCyan-7 ## ## mod edo
colors['HNL_1.04e-8_60gev'] = ROOT.kAzure+5
colors['HNL_1.04e-8_90gev'] = ROOT.kBlue-7
colors['HNL_1.04e-8_110gev'] = ROOT.kOrange-2
colors['HNL_1.04e-8_120gev'] = ROOT.kOrange+8
colors['HNL_4e-12_50gev'] = ROOT.kBlue-4
colors['HNL_6.67e-8_60gev'] = ROOT.kRed-4
colors['HNL_4e-8_60gev'] = ROOT.kBlue-4
colors['HNL_2.86e-9_70gev'] = ROOT.kRed+2
colors['HNL_2.86e-8_80gev'] = ROOT.kBlue+2

colors['HNL'] = ROOT.kWhite

#colors['HNL_2.86e-12_30gev'] = ROOT.kAzure+6
#colors['HNL_2.86e-7_30gev'] = ROOT.kOrange+1
#colors['HNL_4e-12_50gev'] = ROOT.kBlue-4
#colors['HNL_2.86e-9_70gev'] = ROOT.kRed-4
#colors['HNL_6.67e-8_60gev'] = ROOT.kRed-4


colors['Zbb'] = 48
colors['Zcc'] = 44
colors['Zud'] = 41
colors['Ztautau'] = 34
colors['Zee'] = 29
colors['Zmumu'] = 32
colors['Zss'] = 20
colors['emununu'] = 40
colors['tatanunu'] = 38

#colors['Zbb'] = ROOT.kRed-4
#colors['Zcc'] = ROOT.kOrange-3
#colors['Zud'] = ROOT.kYellow-4
#colors['Ztautau'] = ROOT.kGreen-3
#colors['Zee'] = ROOT.kCyan-3
#colors['Zmumu'] = ROOT.kBlue-7
#colors['Zss'] = ROOT.kViolet-4

plots = {}
plots['HNL'] = {'signal':{
                    #'HNL_4e-8_10gev':['HNL_4e-8_10gev'], ## ## mod edo: 8_10gev -> 10_20gev
                    #'HNL_1.33e-9_20gev':['HNL_1.33e-9_20gev'],
                    #'HNL_2.86e-12_30gev':['HNL_2.86e-12_30gev'],
                    #'HNL_2.86e-7_30gev':['HNL_2.86e-7_30gev'],
                    #'HNL_5e-12_40gev':['HNL_5e-12_40gev'],
                    #'HNL_4e-12_50gev':['HNL_4e-12_50gev'],
                    #'HNL_6.67e-8_60gev':['HNL_6.67e-8_60gev'],
                    #'HNL_4e-8_60gev':['HNL_4e-8_60gev'],
                    #'HNL_2.86e-9_70gev':['HNL_2.86e-9_70gev'],
                    #'HNL_2.86e-8_80gev':['HNL_2.86e-8_80gev'],

					'HNL_1.04e-8_30gev':['HNL_1.04e-8_30gev'], ## ## this is also going to be a dummy background
					'HNL_1.04e-8_60gev':['HNL_1.04e-8_60gev'],
					'HNL_1.04e-8_90gev':['HNL_1.04e-8_90gev'],
					'HNL_1.04e-8_110gev':['HNL_1.04e-8_110gev'],
					'HNL_1.04e-8_120gev':['HNL_1.04e-8_120gev'],
	
					#"HNL_4e-10_30gev":{},
					#"HNL_4e-10_60gev":{},
					#"HNL_4e-10_90gev":{},
					#"HNL_4e-10_110gev":{},
					#"HNL_4e-10_120gev":{},
	
					#"HNL_6.67e-10_30gev":{},
					#"HNL_6.67e-10_60gev":{},
					#"HNL_6.67e-10_90gev":{},
					#"HNL_6.67e-10_110gev":{},
					#"HNL_6.67e-10_120gev":{},

					#"HNL_8.35e-9_30gev":{},
					#"HNL_8.35e-9_60gev":{},
					#"HNL_8.35e-9_90gev":{},
					#"HNL_8.35e-9_110gev":{},
					#"HNL_8.35e-9_120gev":{},
		
					#"HNL_2.27e-9_30gev":{},
					#"HNL_2.27e-9_60gev":{},
					#"HNL_2.27e-9_90gev":{},
					#"HNL_2.27e-9_110gev":{},
					#"HNL_2.27e-9_120gev":{},

					#"HNL_3.17e-11_30gev":{},
					#"HNL_3.17e-11_60gev":{},
					#"HNL_3.17e-11_90gev":{},
					#"HNL_3.17e-11_110gev":{},
					#"HNL_3.17e-11_120gev":{},
                },
                'backgrounds':{
					'HNL_1.04e-8_30gev':['HNL_1.04e-8_30gev'],
                    #'HNL_4e-10_20gev':['HNL_4e-10_20gev']
                    #'HNL':['HNL_2.86e-12_30gev'], ### impossible to plot without both signals and backgrounds, choose one signal and make it white ### 
                    #'Zud': ['p8_ee_Zud_ecm91'],
                    #'Zss':['p8_ee_Zss_ecm91'],
                    #'Zcc': ['p8_ee_Zcc_ecm91'],
                    #'Zbb':['p8_ee_Zbb_ecm91'],
                    #'Zee':['p8_ee_Zee_ecm91'],
                    #'Zmumu': ['p8_ee_Zmumu_ecm91'],
                    #'Ztautau': ['p8_ee_Ztautau_ecm91'],
                    #'tatanunu': ['tatanunu'],
                    #'emununu': ['emununu'],
                },
                }

legend = {}

legend['HNL_1.04e-8_30gev'] = 'U^{2}=1.04e-8, M_{N}=30 GeV' ## mod edo
#legend['HNL_4e-8_10gev'] = 'U^{2}=4e-8, M_{N}=10 GeV' ## ## mod edo
legend['HNL_1.04e-8_60gev'] = 'U^{2}=1.04e-8, M_{N}=60 GeV'
legend['HNL_1.04e-8_90gev'] = 'U^{2}=1.04e-8, M_{N}=90 GeV'
legend['HNL_1.04e-8_110gev'] = 'U^{2}=1.04e-8, M_{N}=110 GeV'
legend['HNL_1.04e-8_120gev'] = 'U^{2}=1.04e-8, M_{N}=120 GeV'
legend['HNL_4e-12_50gev'] = 'U^{2}=4e-12, M_{N}=50 GeV'
legend['HNL_6.67e-8_60gev'] = 'U^{2}=6.67e-8, M_{N}=60 GeV'
legend['HNL_4e-8_60gev'] = 'U^{2}=4e-8, M_{N}=60 GeV'
legend['HNL_2.86e-9_70gev'] = 'U^{2}=2.86e-9, M_{N}=70 GeV'
legend['HNL_2.86e-8_80gev'] = 'U^{2}=2.86e-8, M_{N}=80 GeV'

legend['HNL'] = ''

legend['Zud'] = 'Z #rightarrow ud'
legend['Zss'] = 'Z #rightarrow ss'
legend['Zbb'] = 'Z #rightarrow bb'
legend['Zcc'] = 'Z #rightarrow cc'
legend['Zee'] = 'Z #rightarrow ee'
legend['Zmumu'] = 'Z #rightarrow #mu#mu'
legend['Ztautau'] = 'Z #rightarrow #tau#tau'
legend['emununu'] = 'e#mu#nu#nu'
legend['tatanunu'] = '#tau#tau#nu#nu'
