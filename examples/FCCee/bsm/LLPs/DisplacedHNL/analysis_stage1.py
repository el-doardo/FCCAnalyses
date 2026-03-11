## ## espoto ## ##
# 	Sto per implementare lo studio dei jet per segnali a stati finali mujj 
# 	Inizio cercando di estrarre il muone a pt più alta dalla collezione di particelle:
# 	la classe RecoMuon_Lead sarà composta dal solo muone estratto, la classe della
#	collezione di particelle dalle quali manca il muone leading è JetParticles .
# 	Do le JetParticles in pasto alle funzioni che clusterizzano le RecoParticles
#	impostando l'algoritmo Dhuram kt esclusivo con Nj=2. 
#	Aggiungo il filtro per pt del muone lead > 20GeV
#
#	Sto Andando alla ricerca della ricostruzione del displaced vertex nella speranza di lavorare bene coi jet :/

import ROOT

#Mandatory: List of processes

processList = {
        #'p8_ee_Zee_ecm91':{'fraction':0.01}, ## ## secondo il paper lui non serve, ma sono curioso 	## ## fraction limit sperimentato: 1
        #'p8_ee_Zmumu_ecm91':{'fraction':0.01},		## ## fraction limit sperimentato: 0.25
        #'p8_ee_Ztautau_ecm91':{'fraction':0.01},	## ## fraction limit sperimentato: 0.25
        #'p8_ee_Zbb_ecm91':{'fraction':0.01},		## ## fraction limit sperimentato: 0.1
        #'p8_ee_Zcc_ecm91':{'fraction':0.01},		## ## fraction limit sperimentato: 0.1
        #'p8_ee_Zud_ecm91':{'fraction':0.01},		## ## fraction limit sperimentato: 0.5 forse alzabile
        #'p8_ee_Zss_ecm91':{'fraction':0.01},		## ## fraction limit sperimentato: 0.5 forrse alzabile

	## ##
	
		#"HNL_1.04e-8_10gev":{},
		#"HNL_1.04e-8_70gev":{},
		#"HNL_4e-10_20gev":{},
		#"HNL_4e-10_80gev":{},	
		"HNL_6.67e-10_30gev":{},
		"HNL_8.35e-9_40gev":{},
		#"HNL_2.27e-9_20gev":{},
		#"HNL_2.27e-9_50gev":{},
		#"HNL_3.17e-11_30gev":{},
		#"HNL_3.17e-11_60gev":{},

	
	
		"numujj":{},
}

processList_ = {

        #centrally-produced backgrounds
        #'p8_ee_Zee_ecm91':{'chunks':100},
        #'p8_ee_Zmumu_ecm91':{'chunks':100},
        #'p8_ee_Ztautau_ecm91':{'chunks':100},
        #'p8_ee_Zbb_ecm91':{'chunks':100},
        #'p8_ee_Zcc_ecm91':{'chunks':100},
        #'p8_ee_Zud_ecm91':{'chunks':100},
        #'p8_ee_Zss_ecm91':{'chunks':100},

		"HNL_1.04e-8_10gev":{},
		"HNL_1.04e-8_20gev":{},
		"HNL_1.04e-8_30gev":{},
		"HNL_1.04e-8_40gev":{},
		"HNL_1.04e-8_50gev":{},
		"HNL_1.04e-8_60gev":{},
		"HNL_1.04e-8_70gev":{},
		"HNL_1.04e-8_80gev":{},
		"HNL_1.04e-8_90gev":{},

		"HNL_4e-10_10gev":{},
		"HNL_4e-10_20gev":{},
		"HNL_4e-10_30gev":{},
		"HNL_4e-10_40gev":{},
		"HNL_4e-10_50gev":{},
		"HNL_4e-10_60gev":{},
		"HNL_4e-10_70gev":{},
		"HNL_4e-10_80gev":{},
		"HNL_4e-10_90gev":{},

		"HNL_6.67e-10_10gev":{},
		"HNL_6.67e-10_20gev":{},
		"HNL_6.67e-10_30gev":{},
		"HNL_6.67e-10_40gev":{},
		"HNL_6.67e-10_50gev":{},
		"HNL_6.67e-10_60gev":{},
		"HNL_6.67e-10_70gev":{},
		"HNL_6.67e-10_80gev":{},
		"HNL_6.67e-10_90gev":{},

		"HNL_8.35e-9_10gev":{},
		"HNL_8.35e-9_20gev":{},
		"HNL_8.35e-9_30gev":{},
		"HNL_8.35e-9_40gev":{},
		"HNL_8.35e-9_50gev":{},
		"HNL_8.35e-9_60gev":{},
		"HNL_8.35e-9_70gev":{},
		"HNL_8.35e-9_80gev":{},
		"HNL_8.35e-9_90gev":{},

		"HNL_2.27e-9_10gev":{},
		"HNL_2.27e-9_20gev":{},
		"HNL_2.27e-9_30gev":{},
		"HNL_2.27e-9_40gev":{},
		"HNL_2.27e-9_50gev":{},
		"HNL_2.27e-9_60gev":{},
		"HNL_2.27e-9_70gev":{},
		"HNL_2.27e-9_80gev":{},
		"HNL_2.27e-9_90gev":{},

		"HNL_3.17e-11_10gev":{},
		"HNL_3.17e-11_20gev":{},
		"HNL_3.17e-11_30gev":{},
		"HNL_3.17e-11_40gev":{},
		"HNL_3.17e-11_50gev":{},
		"HNL_3.17e-11_60gev":{},
		"HNL_3.17e-11_70gev":{},
		"HNL_3.17e-11_80gev":{},
		"HNL_3.17e-11_90gev":{},

        
}

#Production tag. This points to the yaml files for getting sample statistics
#Mandatory when running over EDM4Hep centrally produced events
#Comment out when running over privately produced events
#prodTag     = "FCCee/winter2023/IDEA/"

#Input directory
#Comment out when running over centrally produced events
#Mandatory when running over privately produced events

inputDir = "/eos/user/e/espoto/FCC_2jet_z_pole/FCCAnalysis/hadronized_signals"

# additional/costom C++ functions, defined in header files (optional)
includePaths = ["functions.h"]

#Optional: output directory, default is local dir
#outputDir = "output_stage1/"
outputDir = "/eos/user/e/espoto/FCC_2jet_z_pole/FCCAnalysis/stage1_reco/"

### necessary to run on HTCondor ###
eosType = "eosuser"

#Optional: ncpus, default is 4
nCPUS = 10

#Optional running on HTCondor, default is False
#runBatch = True

#Optional batch queue name when running on HTCondor, default is workday
batchQueue = "workday"

#Optional computing account when running on HTCondor, default is group_u_FCC.local_gen
compGroup = "group_u_FCC.local_gen"

#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():
        def analysers(df):

                df2 = (df

                #Access the various objects and their properties with the following syntax: .Define("<your_variable>", "<accessor_fct (name_object)>")
		#This will create a column in the RDataFrame named <your_variable> and filled with the return value of the <accessor_fct> for the given collection/object 
		#Accessor functions are the functions found in the C++ analyzers code that return a certain variable, e.g. <namespace>::get_n(object) returns the number 
		#of these objects in the event and <namespace>::get_pt(object) returns the pt of the object. Here you can pick between two namespaces to access either
		#reconstructed (namespace = ReconstructedParticle) or MC-level objects (namespace = MCParticle). 
		#For the name of the object, in principle the names of the EDM4HEP collections are used - photons, muons and electrons are an exception, see below

		#OVERVIEW: Accessing different objects and counting them
               

                # Following code is written specifically for the HNL study
                ####################################################################################################
                .Alias("Particle0", "Particle#0.index")
                .Alias("Particle1", "Particle#1.index")
                .Alias("MCRecoAssociations0", "MCRecoAssociations#0.index")
                .Alias("MCRecoAssociations1", "MCRecoAssociations#1.index")

                .Define("GenTau",   "FCCAnalyses::MCParticle::sel_pdgID(15, true)(Particle)")
                .Define("GenPion",   "FCCAnalyses::MCParticle::sel_pdgID(211, true)(Particle)")
                .Define("GenKL",   "FCCAnalyses::MCParticle::sel_pdgID(130, true)(Particle)")
                .Define("GenKplus",   "FCCAnalyses::MCParticle::sel_pdgID(321, true)(Particle)")

                .Define("n_GenTaus",      "FCCAnalyses::MCParticle::get_n(GenTau)")
                .Define("n_GenPions",      "FCCAnalyses::MCParticle::get_n(GenPion)")
                .Define("n_GenKLs",      "FCCAnalyses::MCParticle::get_n(GenKL)")
                .Define("n_GenKpluss",      "FCCAnalyses::MCParticle::get_n(GenKplus)")

                #.Filter("n_GenTaus>0")
                #.Filter("n_GenPions>0 || n_GenKLs>0 || n_GenKpluss>0")

                .Define("GenPion_e", "if (n_GenPions>0) return FCCAnalyses::MCParticle::get_e(GenPion); else return FCCAnalyses::MCParticle::get_genStatus(GenPion);")
                .Define("GenKL_e", "if (n_GenKLs>0) return FCCAnalyses::MCParticle::get_e(GenKL); else return FCCAnalyses::MCParticle::get_genStatus(GenKL);")
                .Define("GenTau_e", "if (n_GenTaus>0) return FCCAnalyses::MCParticle::get_e(GenTau); else return FCCAnalyses::MCParticle::get_genStatus(GenTau);")
                .Define("GenKplus_e", "if (n_GenKpluss>0) return FCCAnalyses::MCParticle::get_e(GenKplus); else return FCCAnalyses::MCParticle::get_genStatus(GenKplus);")
                
                .Define("GenPion_pt", "if (n_GenPions>0) return FCCAnalyses::MCParticle::get_pt(GenPion); else return FCCAnalyses::MCParticle::get_genStatus(GenPion);")
                .Define("GenKL_pt", "if (n_GenKLs>0) return FCCAnalyses::MCParticle::get_pt(GenKL); else return FCCAnalyses::MCParticle::get_genStatus(GenKL);")
                .Define("GenTau_pt", "if (n_GenTaus>0) return FCCAnalyses::MCParticle::get_pt(GenTau); else return FCCAnalyses::MCParticle::get_genStatus(GenTau);")
                .Define("GenKplus_pt", "if (n_GenKpluss>0) return FCCAnalyses::MCParticle::get_pt(GenKplus); else return FCCAnalyses::MCParticle::get_genStatus(GenKplus);")
 
                #all final state gen electrons and positrons
                .Define("GenElectron_PID", "FCCAnalyses::MCParticle::sel_pdgID(11, true)(Particle)")
                .Define("FSGenElectron", "FCCAnalyses::MCParticle::sel_genStatus(1)(GenElectron_PID)") #gen status==1 means final state particle (FS)
                .Define("n_FSGenElectron", "FCCAnalyses::MCParticle::get_n(FSGenElectron)")
                #put in dummy values below if there aren't any FSGenElectrons, to avoid seg fault
                .Define("FSGenElectron_e", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_e(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
                .Define("FSGenElectron_p", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_p(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
                .Define("FSGenElectron_pt", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_pt(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
                .Define("FSGenElectron_px", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_px(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
                .Define("FSGenElectron_py", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_py(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
                .Define("FSGenElectron_pz", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_pz(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
                .Define("FSGenElectron_eta", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_eta(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
                .Define("FSGenElectron_theta", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_theta(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
                .Define("FSGenElectron_phi", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_phi(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
                .Define("FSGenElectron_charge", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_charge(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")

                .Define("FSGenElectron_vertex_x", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_vertex_x( FSGenElectron ); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
                .Define("FSGenElectron_vertex_y", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_vertex_y( FSGenElectron ); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
                .Define("FSGenElectron_vertex_z", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_vertex_z( FSGenElectron ); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
                
                #all final state gen Muons
                .Define("GenMuon_PID", "FCCAnalyses::MCParticle::sel_pdgID(13, true)(Particle)")
                .Define("FSGenMuon", "FCCAnalyses::MCParticle::sel_genStatus(1)(GenMuon_PID)") #gen status==1 means final state particle (FS)
                .Define("n_FSGenMuon", "FCCAnalyses::MCParticle::get_n(FSGenMuon)")
                #put in dummy values below if there aren't any FSGenMuons, to avoid seg fault
                .Define("FSGenMuon_e", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_e(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
                .Define("FSGenMuon_p", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_p(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
                .Define("FSGenMuon_pt", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_pt(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
                .Define("FSGenMuon_px", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_px(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
                .Define("FSGenMuon_py", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_py(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
                .Define("FSGenMuon_pz", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_pz(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
                .Define("FSGenMuon_eta", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_eta(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
                .Define("FSGenMuon_theta", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_theta(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
                .Define("FSGenMuon_phi", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_phi(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
                .Define("FSGenMuon_charge", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_charge(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")

                .Define("FSGenMuon_vertex_x", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_vertex_x( FSGenMuon ); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
                .Define("FSGenMuon_vertex_y", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_vertex_y( FSGenMuon ); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
                .Define("FSGenMuon_vertex_z", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_vertex_z( FSGenMuon ); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")

                ### merging electrons and muons ###
                .Define("FSGenLepton", "FCCAnalyses::MCParticle::mergeParticles(FSGenElectron, FSGenMuon)") 
                .Define("n_FSGenLepton", "FCCAnalyses::MCParticle::get_n(FSGenLepton)")
                #put in dummy values below if there aren't any FSGenMuons, to avoid seg fault
                .Define("FSGenLepton_e", "FCCAnalyses::MCParticle::get_e(FSGenLepton)")
                .Define("FSGenLepton_p", "FCCAnalyses::MCParticle::get_p(FSGenLepton)")
                .Define("FSGenLepton_pt", "FCCAnalyses::MCParticle::get_pt(FSGenLepton)")
                .Define("FSGenLepton_px", "FCCAnalyses::MCParticle::get_px(FSGenLepton)")
                .Define("FSGenLepton_py", "FCCAnalyses::MCParticle::get_py(FSGenLepton)")
                .Define("FSGenLepton_pz", "FCCAnalyses::MCParticle::get_pz(FSGenLepton)")
                .Define("FSGenLepton_eta", "FCCAnalyses::MCParticle::get_eta(FSGenLepton)")
                .Define("FSGenLepton_theta", "FCCAnalyses::MCParticle::get_theta(FSGenLepton)")
                .Define("FSGenLepton_phi", "FCCAnalyses::MCParticle::get_phi(FSGenLepton)")
                .Define("FSGenLepton_charge", "FCCAnalyses::MCParticle::get_charge(FSGenLepton)")
                .Define("FSGenLepton_time", "FCCAnalyses::MCParticle::get_time(FSGenLepton)") #creation time in s

                .Define("FSGenLepton_vertex_x", "FCCAnalyses::MCParticle::get_vertex_x(FSGenLepton)")
                .Define("FSGenLepton_vertex_y", "FCCAnalyses::MCParticle::get_vertex_y(FSGenLepton)")
                .Define("FSGenLepton_vertex_z", "FCCAnalyses::MCParticle::get_vertex_z(FSGenLepton)")

                .Define("FSGenLepton_e_led",     " if (n_FSGenLepton>1) return FSGenLepton_e.at(0); else return float(-1000.);")
                .Define("FSGenLepton_p_led",     " if (n_FSGenLepton>1) return FSGenLepton_p.at(0); else return float(-1000.);")
                .Define("FSGenLepton_pt_led",    " if (n_FSGenLepton>1) return FSGenLepton_pt.at(0); else return float(-1000.);")
                .Define("FSGenLepton_px_led",    " if (n_FSGenLepton>1) return FSGenLepton_px.at(0); else return float(-1000.);")
                .Define("FSGenLepton_py_led",     " if (n_FSGenLepton>1) return FSGenLepton_py.at(0); else return float(-1000.);")
                .Define("FSGenLepton_pz_led",     " if (n_FSGenLepton>1) return FSGenLepton_pz.at(0); else return float(-1000.);")
		.Define("FSGenLepton_eta_led",    " if (n_FSGenLepton>1) return FSGenLepton_eta.at(0); else return float(-1000.);") #pseudorapidity eta
                .Define("FSGenLepton_theta_led",  " if (n_FSGenLepton>1) return FSGenLepton_theta.at(0); else return float(-1000.);")
		.Define("FSGenLepton_phi_led",    " if (n_FSGenLepton>1) return FSGenLepton_phi.at(0); else return float(-1000.);") #polar angle in the transverse plane phi
                .Define("FSGenLepton_charge_led", " if (n_FSGenLepton>1) return FSGenLepton_charge.at(0); else return float(-1000.);")

                .Define("FSGenLepton_e_sub",     " if (n_FSGenLepton>1) return FSGenLepton_e.at(1); else return float(-1000.);")
                .Define("FSGenLepton_p_sub",     " if (n_FSGenLepton>1) return FSGenLepton_p.at(1); else return float(-1000.);")
                .Define("FSGenLepton_pt_sub",    " if (n_FSGenLepton>1) return FSGenLepton_pt.at(1); else return float(-1000.);")
                .Define("FSGenLepton_px_sub",    " if (n_FSGenLepton>1) return FSGenLepton_px.at(1); else return float(-1000.);")
                .Define("FSGenLepton_py_sub",     " if (n_FSGenLepton>1) return FSGenLepton_py.at(1); else return float(-1000.);")
                .Define("FSGenLepton_pz_sub",     " if (n_FSGenLepton>1) return FSGenLepton_pz.at(1); else return float(-1000.);")
		.Define("FSGenLepton_eta_sub",    " if (n_FSGenLepton>1) return FSGenLepton_eta.at(1); else return float(-1000.);") #pseudorapidity eta
                .Define("FSGenLepton_theta_sub",  " if (n_FSGenLepton>1) return FSGenLepton_theta.at(1); else return float(-1000.);")
		.Define("FSGenLepton_phi_sub",    " if (n_FSGenLepton>1) return FSGenLepton_phi.at(1); else return float(-1000.);") #polar angle in the transverse plane phi
                .Define("FSGenLepton_charge_sub", " if (n_FSGenLepton>1) return FSGenLepton_charge.at(1); else return float(-1000.);")

                # Finding the Lxy of the HNL
                ### both leptons have the same vertex decaying from Z or W so when there are no electrons use one of the muons, when there are at least one electron use that ###
                # Definition: Lxy = math.sqrt( (branchGenPtcl.At(daut1).X)**2 + (branchGenPtcl.At(daut1).Y)**2 )
                .Define("FSGen_Lxy", "return sqrt(FSGenLepton_vertex_x*FSGenLepton_vertex_x + FSGenLepton_vertex_y*FSGenLepton_vertex_y)")
                # Finding the Lxyz of the HNL
                .Define("FSGen_Lxyz", "return sqrt(FSGenLepton_vertex_x*FSGenLepton_vertex_x + FSGenLepton_vertex_y*FSGenLepton_vertex_y + FSGenLepton_vertex_z*FSGenLepton_vertex_z)")
                
                #all final state gen neutrinos and anti-neutrinos
                .Define("GenNeutrino_PID", "FCCAnalyses::MCParticle::sel_pdgID(12, true)(Particle)")
                .Define("FSGenNeutrino", "FCCAnalyses::MCParticle::sel_genStatus(1)(GenNeutrino_PID)") #gen status==1 means final state particle (FS)
                .Define("n_FSGenNeutrino", "FCCAnalyses::MCParticle::get_n(FSGenNeutrino)")
                .Define("FSGenNeutrino_e", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_e(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
                .Define("FSGenNeutrino_p", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_p(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
                .Define("FSGenNeutrino_pt", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_pt(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
                .Define("FSGenNeutrino_px", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_px(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
                .Define("FSGenNeutrino_py", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_py(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
                .Define("FSGenNeutrino_pz", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_pz(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
                .Define("FSGenNeutrino_eta", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_eta(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
                .Define("FSGenNeutrino_theta", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_theta(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
                .Define("FSGenNeutrino_phi", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_phi(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
                .Define("FSGenNeutrino_charge", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_charge(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")

                #all final state gen photons
                .Define("GenPhoton_PID", "FCCAnalyses::MCParticle::sel_pdgID(22, false)(Particle)")
                .Define("FSGenPhoton", "FCCAnalyses::MCParticle::sel_genStatus(1)(GenPhoton_PID)") #gen status==1 means final state particle (FS)
                .Define("n_FSGenPhoton", "FCCAnalyses::MCParticle::get_n(FSGenPhoton)")
                .Define("FSGenPhoton_e", "FCCAnalyses::MCParticle::get_e(FSGenPhoton)")
                .Define("FSGenPhoton_p", "FCCAnalyses::MCParticle::get_p(FSGenPhoton)")
                .Define("FSGenPhoton_pt", "FCCAnalyses::MCParticle::get_pt(FSGenPhoton)")
                .Define("FSGenPhoton_px", "FCCAnalyses::MCParticle::get_px(FSGenPhoton)")
                .Define("FSGenPhoton_py", "FCCAnalyses::MCParticle::get_py(FSGenPhoton)")
                .Define("FSGenPhoton_pz", "FCCAnalyses::MCParticle::get_pz(FSGenPhoton)")
                .Define("FSGenPhoton_eta", "FCCAnalyses::MCParticle::get_eta(FSGenPhoton)")
                .Define("FSGenPhoton_theta", "FCCAnalyses::MCParticle::get_theta(FSGenPhoton)")
                .Define("FSGenPhoton_phi", "FCCAnalyses::MCParticle::get_phi(FSGenPhoton)")
                .Define("FSGenPhoton_charge", "FCCAnalyses::MCParticle::get_charge(FSGenPhoton)")

                ### Gen HNLs, merged the two ###
                .Define("GenN1_PID", "FCCAnalyses::MCParticle::sel_pdgID(9900012, true)(Particle)") #true to include charge conjugate
                .Define("GenN2_PID", "FCCAnalyses::MCParticle::sel_pdgID(9900014, true)(Particle)") #true to include charge conjugate
                .Define("GenN", "FCCAnalyses::MCParticle::mergeParticles(GenN1_PID, GenN2_PID)") 
                .Define("GenN_status", "FCCAnalyses::MCParticle::get_genStatus(GenN)") 
                .Define("n_GenN", "FCCAnalyses::MCParticle::get_n(GenN)")
                .Define("GenN_e", "FCCAnalyses::MCParticle::get_e(GenN)")
                .Define("GenN_p", "FCCAnalyses::MCParticle::get_p(GenN)")
                .Define("GenN_mass", "FCCAnalyses::MCParticle::get_mass(GenN)")

                ### definetly overkill for this study, gets the associated daugthers and then their vertex ###
                .Define("GenN1_indices", "MCParticle::get_indices( 9900012, {}, false, true, true, true) ( Particle, Particle1)" )
                .Define("GenN2_indices", "MCParticle::get_indices( 9900014, {}, false, true, true, true) ( Particle, Particle1)" )
                .Define("GenN1_dec", "FCCAnalyses::MCParticle::get_list_of_stable_particles_from_decay(GenN1_indices[0], Particle, Particle1)")
                .Define("GenN2_dec", "FCCAnalyses::MCParticle::get_list_of_stable_particles_from_decay(GenN2_indices[0], Particle, Particle1)")
                .Define("GenN_d1", "if (GenN1_dec.size()>0) return MCParticle::sel_byIndex(GenN1_dec.at(0), Particle); else return MCParticle::sel_byIndex(GenN2_dec.at(0), Particle);")

                .Define("GenN_vertex_x",    "return MCParticle::get_vertex_x({GenN_d1})")
                .Define("GenN_vertex_y",    "return MCParticle::get_vertex_y({GenN_d1})")
                .Define("GenN_vertex_z",    "return MCParticle::get_vertex_z({GenN_d1})")
                .Define("GenN_Lxyz", "return sqrt(GenN_vertex_x*GenN_vertex_x + GenN_vertex_y*GenN_vertex_y + GenN_vertex_z*GenN_vertex_z)") #in mm
                
                ### use the time of creation fo the leptons to get the lifetime of the HNL ###
                .Define("GenN_tau", "return (FSGenLepton_time * GenN_e.at(0) / GenN_mass.at(0)) ") #tau of HNLs in s
        
                # ee invariant mass
                .Define("FSGen_TwoLeptons_energy", "if (n_FSGenLepton>1) return (FSGenLepton_e.at(0) + FSGenLepton_e.at(1)); else return float(-1.);")
                .Define("FSGen_TwoLeptons_px", "if (n_FSGenLepton>1) return (FSGenLepton_px.at(0) + FSGenLepton_px.at(1)); else return float(-1.);")
                .Define("FSGen_TwoLeptons_py", "if (n_FSGenLepton>1) return (FSGenLepton_py.at(0) + FSGenLepton_py.at(1)); else return float(-1.);")
                .Define("FSGen_TwoLeptons_pz", "if (n_FSGenLepton>1) return (FSGenLepton_pz.at(0) + FSGenLepton_pz.at(1)); else return float(-1.);")
                .Define("FSGen_invMass", "if (n_FSGenLepton>1) return sqrt(FSGen_TwoLeptons_energy*FSGen_TwoLeptons_energy - FSGen_TwoLeptons_px*FSGen_TwoLeptons_px - FSGen_TwoLeptons_py*FSGen_TwoLeptons_py - FSGen_TwoLeptons_pz*FSGen_TwoLeptons_pz ); else return float(-1.);")

                # MC event primary vertex
                .Define("MC_PrimaryVertex",  "FCCAnalyses::MCParticle::get_EventPrimaryVertex(21)( Particle )" )
                

                .Define("FSGenParticles", "FCCAnalyses::MCParticle::sel_genStatus(1)(Particle)")
                .Define("DecGenParticles", "FCCAnalyses::MCParticle::sel_genStatus(2)(Particle)")
                .Define("GenParticles_PID", "FCCAnalyses::MCParticle::get_pdg(Particle)")
                .Define("FSGenParticles_PID", "FCCAnalyses::MCParticle::get_pdg(FSGenParticles)")
                .Define("DecGenParticles_PID", "FCCAnalyses::MCParticle::get_pdg(DecGenParticles)")

                ################### Reconstructed particles #####################
                .Define("n_RecoTracks","ReconstructedParticle2Track::getTK_n(EFlowTrack_1)")

                #JETS
                ### count how many jets are in the event in total to check, it doesn't work with this method on reclustered jets, only on the edm4hep collections Jet ###
		.Define("n_RecoJets", "ReconstructedParticle::get_n(Jet)") 
                #SIMPLE VARIABLES: Access the basic kinematic variables of the (selected) jets, works analogously for electrons, muons
		.Define("RecoJet_e",      "ReconstructedParticle::get_e(Jet)")
                .Define("RecoJet_p",      "ReconstructedParticle::get_p(Jet)") #momentum p
                .Define("RecoJet_pt",      "ReconstructedParticle::get_pt(Jet)") #transverse momentum pt
                .Define("RecoJet_px",      "ReconstructedParticle::get_px(Jet)")
                .Define("RecoJet_py",      "ReconstructedParticle::get_py(Jet)")
                .Define("RecoJet_pz",      "ReconstructedParticle::get_pz(Jet)")
		.Define("RecoJet_eta",     "ReconstructedParticle::get_eta(Jet)") #pseudorapidity eta
                .Define("RecoJet_theta",   "ReconstructedParticle::get_theta(Jet)")
		.Define("RecoJet_phi",     "ReconstructedParticle::get_phi(Jet)") #polar angle in the transverse plane phi
                .Define("RecoJet_charge",  "ReconstructedParticle::get_charge(Jet)")
                .Define("RecoJetTrack_absD0", "return abs(ReconstructedParticle2Track::getRP2TRK_D0(Jet,EFlowTrack_1))")
                .Define("RecoJetTrack_absZ0", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0(Jet,EFlowTrack_1))")
                .Define("RecoJetTrack_absD0sig", "return abs(ReconstructedParticle2Track::getRP2TRK_D0_sig(Jet,EFlowTrack_1))") #significance
                .Define("RecoJetTrack_absZ0sig", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0_sig(Jet,EFlowTrack_1))")
                .Define("RecoJetTrack_D0cov", "ReconstructedParticle2Track::getRP2TRK_D0_cov(Jet,EFlowTrack_1)") #variance (not sigma)
                .Define("RecoJetTrack_Z0cov", "ReconstructedParticle2Track::getRP2TRK_Z0_cov(Jet,EFlowTrack_1)")

		#PHOTONS
		.Alias("Photon0", "Photon#0.index") 
		.Define("RecoPhotons",  "ReconstructedParticle::get(Photon0, ReconstructedParticles)")
		.Define("n_RecoPhotons",  "ReconstructedParticle::get_n(RecoPhotons)") #count how many photons are in the event in total
                .Define("RecoPhoton_e",      "ReconstructedParticle::get_e(RecoPhotons)")
                .Define("RecoPhoton_p",      "ReconstructedParticle::get_p(RecoPhotons)")
                .Define("RecoPhoton_pt",      "ReconstructedParticle::get_pt(RecoPhotons)")
                .Define("RecoPhoton_px",      "ReconstructedParticle::get_px(RecoPhotons)")
                .Define("RecoPhoton_py",      "ReconstructedParticle::get_py(RecoPhotons)")
                .Define("RecoPhoton_pz",      "ReconstructedParticle::get_pz(RecoPhotons)")
		.Define("RecoPhoton_eta",     "ReconstructedParticle::get_eta(RecoPhotons)") #pseudorapidity eta
                .Define("RecoPhoton_theta",   "ReconstructedParticle::get_theta(RecoPhotons)")
		.Define("RecoPhoton_phi",     "ReconstructedParticle::get_phi(RecoPhotons)") #polar angle in the transverse plane phi
                .Define("RecoPhoton_charge",  "ReconstructedParticle::get_charge(RecoPhotons)")

                #NEUTRAL HADRONS
                #.Define("Candidates", "ReconstructedParticle::remove(ReconstructedParticles, RecoPhotons)") #does not work well, there are more "photons" than expected at e<2 Gev(no efficiency) that are not in Photons but in RecoParticle so they are kept here
                .Define("NeutralHadrons_cand",   "ReconstructedParticles[ReconstructedParticles.type != 22 && ReconstructedParticles.energy > 2]") #this instead excludes all photons with type 22, type 0 is charged particles and then type 130 is K0 that we are interested in, pi0 always decay in gamma-gamma
                .Define("NeutralHadrons",       "ReconstructedParticle::sel_charge(0, true) (NeutralHadrons_cand)")
                .Define("n_NeutralHadrons",  "ReconstructedParticle::get_n(NeutralHadrons)") #count how many photons are in the event in total
                .Define("NeutralHadrons_e",      "ReconstructedParticle::get_e(NeutralHadrons)")
                .Define("NeutralHadrons_p",      "ReconstructedParticle::get_p(NeutralHadrons)")
                .Define("NeutralHadrons_pt",      "ReconstructedParticle::get_pt(NeutralHadrons)")
                .Define("NeutralHadrons_px",      "ReconstructedParticle::get_px(NeutralHadrons)")
                .Define("NeutralHadrons_py",      "ReconstructedParticle::get_py(NeutralHadrons)")
                .Define("NeutralHadrons_pz",      "ReconstructedParticle::get_pz(NeutralHadrons)")
		.Define("NeutralHadrons_eta",     "ReconstructedParticle::get_eta(NeutralHadrons)") #pseudorapidity eta
                .Define("NeutralHadrons_theta",   "ReconstructedParticle::get_theta(NeutralHadrons)")
		.Define("NeutralHadrons_phi",     "ReconstructedParticle::get_phi(NeutralHadrons)") #polar angle in the transverse plane phi
                .Define("NeutralHadrons_charge",  "ReconstructedParticle::get_charge(NeutralHadrons)")
                .Define("NeutralHadrons_mass",  "ReconstructedParticle::get_mass(NeutralHadrons)")

		#ELECTRONS 
		.Alias("Electron0", "Electron#0.index")
		.Define("RecoElectrons",  "ReconstructedParticle::get(Electron0, ReconstructedParticles)")
		.Define("n_RecoElectrons",  "ReconstructedParticle::get_n(RecoElectrons)") #count how many electrons are in the event in total
                .Define("RecoElectron_e",      "ReconstructedParticle::get_e(RecoElectrons)")
                .Define("RecoElectron_p",      "ReconstructedParticle::get_p(RecoElectrons)")
                .Define("RecoElectron_pt",      "ReconstructedParticle::get_pt(RecoElectrons)")
                .Define("RecoElectron_px",      "ReconstructedParticle::get_px(RecoElectrons)")
                .Define("RecoElectron_py",      "ReconstructedParticle::get_py(RecoElectrons)")
                .Define("RecoElectron_pz",      "ReconstructedParticle::get_pz(RecoElectrons)")
		.Define("RecoElectron_eta",     "ReconstructedParticle::get_eta(RecoElectrons)") #pseudorapidity eta
                .Define("RecoElectron_theta",   "ReconstructedParticle::get_theta(RecoElectrons)")
		.Define("RecoElectron_phi",     "ReconstructedParticle::get_phi(RecoElectrons)") #polar angle in the transverse plane phi
                .Define("RecoElectron_charge",  "ReconstructedParticle::get_charge(RecoElectrons)")
                .Define("RecoElectronTrack_absD0", "return abs(ReconstructedParticle2Track::getRP2TRK_D0(RecoElectrons,EFlowTrack_1))")
                .Define("RecoElectronTrack_absZ0", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0(RecoElectrons,EFlowTrack_1))")
                .Define("RecoElectronTrack_absD0sig", "return abs(ReconstructedParticle2Track::getRP2TRK_D0_sig(RecoElectrons,EFlowTrack_1))") #significance
                .Define("RecoElectronTrack_absZ0sig", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0_sig(RecoElectrons,EFlowTrack_1))")
                .Define("RecoElectronTrack_D0cov", "ReconstructedParticle2Track::getRP2TRK_D0_cov(RecoElectrons,EFlowTrack_1)") #variance (not sigma)
                .Define("RecoElectronTrack_Z0cov", "ReconstructedParticle2Track::getRP2TRK_Z0_cov(RecoElectrons,EFlowTrack_1)")

                # MUONS
		.Alias("Muon0", "Muon#0.index")
		.Define("RecoMuons",  "ReconstructedParticle::get(Muon0, ReconstructedParticles)")
		.Define("n_RecoMuons",  "ReconstructedParticle::get_n(RecoMuons)") #count how many muons are in the event in total
                .Define("RecoMuon_e",      "ReconstructedParticle::get_e(RecoMuons)")
                .Define("RecoMuon_p",      "ReconstructedParticle::get_p(RecoMuons)")
                .Define("RecoMuon_pt",      "ReconstructedParticle::get_pt(RecoMuons)")
                .Define("RecoMuon_px",      "ReconstructedParticle::get_px(RecoMuons)")
                .Define("RecoMuon_py",      "ReconstructedParticle::get_py(RecoMuons)")
                .Define("RecoMuon_pz",      "ReconstructedParticle::get_pz(RecoMuons)")
		.Define("RecoMuon_eta",     "ReconstructedParticle::get_eta(RecoMuons)") #pseudorapidity eta
                .Define("RecoMuon_theta",   "ReconstructedParticle::get_theta(RecoMuons)")
		.Define("RecoMuon_phi",     "ReconstructedParticle::get_phi(RecoMuons)") #polar angle in the transverse plane phi
                .Define("RecoMuon_charge",  "ReconstructedParticle::get_charge(RecoMuons)")
                .Define("RecoMuonTrack_absD0", "return abs(ReconstructedParticle2Track::getRP2TRK_D0(RecoMuons,EFlowTrack_1))")
                .Define("RecoMuonTrack_absZ0", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0(RecoMuons,EFlowTrack_1))")
                .Define("RecoMuonTrack_absD0sig", "return abs(ReconstructedParticle2Track::getRP2TRK_D0_sig(RecoMuons,EFlowTrack_1))") #significance
                .Define("RecoMuonTrack_absZ0sig", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0_sig(RecoMuons,EFlowTrack_1))")
                .Define("RecoMuonTrack_D0cov", "ReconstructedParticle2Track::getRP2TRK_D0_cov(RecoMuons,EFlowTrack_1)") #variance (not sigma)
                .Define("RecoMuonTrack_Z0cov", "ReconstructedParticle2Track::getRP2TRK_Z0_cov(RecoMuons,EFlowTrack_1)")

                ### building variables for the two leptons final state ###
                .Define("RecoLeptons", "ReconstructedParticle::merge(RecoElectrons, RecoMuons)")
                .Define("n_RecoLeptons",  "ReconstructedParticle::get_n(RecoLeptons)") 
                .Define("Reco_e",      "ReconstructedParticle::get_e(RecoLeptons)")
                .Define("Reco_p",      "ReconstructedParticle::get_p(RecoLeptons)")
                .Define("Reco_pt",      "ReconstructedParticle::get_pt(RecoLeptons)")
                .Define("Reco_px",      "ReconstructedParticle::get_px(RecoLeptons)")
                .Define("Reco_py",      "ReconstructedParticle::get_py(RecoLeptons)")
                .Define("Reco_pz",      "ReconstructedParticle::get_pz(RecoLeptons)")
		.Define("Reco_eta",     "ReconstructedParticle::get_eta(RecoLeptons)") #pseudorapidity eta
                .Define("Reco_theta",   "ReconstructedParticle::get_theta(RecoLeptons)")
		.Define("Reco_phi",     "ReconstructedParticle::get_phi(RecoLeptons)") #polar angle in the transverse plane phi
                .Define("Reco_charge",  "ReconstructedParticle::get_charge(RecoLeptons)")
                .Define("RecoTrack_absD0", "return abs(ReconstructedParticle2Track::getRP2TRK_D0(RecoLeptons,EFlowTrack_1))")
                .Define("RecoTrack_absZ0", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0(RecoLeptons,EFlowTrack_1))")
                .Define("RecoTrack_absD0sig", "return abs(ReconstructedParticle2Track::getRP2TRK_D0_sig(RecoLeptons,EFlowTrack_1))") #significance
                .Define("RecoTrack_absZ0sig", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0_sig(RecoLeptons,EFlowTrack_1))")
                .Define("RecoTrack_D0cov", "ReconstructedParticle2Track::getRP2TRK_D0_cov(RecoLeptons,EFlowTrack_1)") #variance (not sigma)
                .Define("RecoTrack_Z0cov", "ReconstructedParticle2Track::getRP2TRK_Z0_cov(RecoLeptons,EFlowTrack_1)")

                .Define("RecoLepton_lead",     "FCCAnalyses::ZHfunctions::get_leading(RecoLeptons);")
                .Define("Reco_e_lead",      "ReconstructedParticle::get_e(RecoLepton_lead)")
                .Define("Reco_p_lead",      "ReconstructedParticle::get_p(RecoLepton_lead)")
                .Define("Reco_pt_lead",      "ReconstructedParticle::get_pt(RecoLepton_lead)")
                .Define("Reco_px_lead",      "ReconstructedParticle::get_px(RecoLepton_lead)")
                .Define("Reco_py_lead",      "ReconstructedParticle::get_py(RecoLepton_lead)")
                .Define("Reco_pz_lead",      "ReconstructedParticle::get_pz(RecoLepton_lead)")
		.Define("Reco_eta_lead",     "ReconstructedParticle::get_eta(RecoLepton_lead)") #pseudorapidity eta
                .Define("Reco_theta_lead",   "ReconstructedParticle::get_theta(RecoLepton_lead)")
		.Define("Reco_phi_lead",     "ReconstructedParticle::get_phi(RecoLepton_lead)") #polar angle in the transverse plane phi
                .Define("Reco_charge_lead",  "ReconstructedParticle::get_charge(RecoLepton_lead)")
                .Define("RecoTrack_absD0_lead", "return abs(ReconstructedParticle2Track::getRP2TRK_D0(RecoLepton_lead,EFlowTrack_1))")
                .Define("RecoTrack_absZ0_lead", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0(RecoLepton_lead,EFlowTrack_1))")
                .Define("RecoTrack_absD0sig_lead", "return abs(ReconstructedParticle2Track::getRP2TRK_D0_sig(RecoLepton_lead,EFlowTrack_1))") #significance
                .Define("RecoTrack_absZ0sig_lead", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0_sig(RecoLepton_lead,EFlowTrack_1))")
                .Define("RecoTrack_D0cov_lead", "ReconstructedParticle2Track::getRP2TRK_D0_cov(RecoLepton_lead,EFlowTrack_1)") #variance (not sigma)
                .Define("RecoTrack_Z0cov_lead", "ReconstructedParticle2Track::getRP2TRK_Z0_cov(RecoLepton_lead,EFlowTrack_1)")

                .Define("RecoLepton_sub",     "FCCAnalyses::ZHfunctions::get_subleading(RecoLeptons);")
                .Define("Reco_e_sub",      "ReconstructedParticle::get_e(RecoLepton_sub)")
                .Define("Reco_p_sub",      "ReconstructedParticle::get_p(RecoLepton_sub)")
                .Define("Reco_pt_sub",      "ReconstructedParticle::get_pt(RecoLepton_sub)")
                .Define("Reco_px_sub",      "ReconstructedParticle::get_px(RecoLepton_sub)")
                .Define("Reco_py_sub",      "ReconstructedParticle::get_py(RecoLepton_sub)")
                .Define("Reco_pz_sub",      "ReconstructedParticle::get_pz(RecoLepton_sub)")
                .Define("Reco_eta_sub",     "ReconstructedParticle::get_eta(RecoLepton_sub)") #pseudorapidity eta
                .Define("Reco_theta_sub",   "ReconstructedParticle::get_theta(RecoLepton_sub)")
                .Define("Reco_phi_sub",     "ReconstructedParticle::get_phi(RecoLepton_sub)") #polar angle in the transverse plane phi
                .Define("Reco_charge_sub",  "ReconstructedParticle::get_charge(RecoLepton_sub)")
                .Define("RecoTrack_absD0_sub", "return abs(ReconstructedParticle2Track::getRP2TRK_D0(RecoLepton_sub,EFlowTrack_1))")
                .Define("RecoTrack_absZ0_sub", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0(RecoLepton_sub,EFlowTrack_1))")
                .Define("RecoTrack_absD0sig_sub", "return abs(ReconstructedParticle2Track::getRP2TRK_D0_sig(RecoLepton_sub,EFlowTrack_1))") #significance
                .Define("RecoTrack_absZ0sig_sub", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0_sig(RecoLepton_sub,EFlowTrack_1))")
                .Define("RecoTrack_D0cov_sub", "ReconstructedParticle2Track::getRP2TRK_D0_cov(RecoLepton_sub,EFlowTrack_1)") #variance (not sigma)
                .Define("RecoTrack_Z0cov_sub", "ReconstructedParticle2Track::getRP2TRK_Z0_cov(RecoLepton_sub,EFlowTrack_1)")

                ### cosine between two leptons ###
                .Define("Reco_TwoLeptons_p", "if (n_RecoLeptons>1) return (Reco_px.at(0)*Reco_px.at(1) + Reco_py.at(0)*Reco_py.at(1) + Reco_pz.at(0)*Reco_pz.at(1)); else return float(-2.);")
                .Define("Reco_cos", "if (n_RecoLeptons>1) return (Reco_TwoLeptons_p/(Reco_p.at(0)*Reco_p.at(1))); else return float(-2.);")

                ### angular distance between two leptons ###
                .Define("Reco_DR","if (n_RecoLeptons>1) return myUtils::deltaR(Reco_phi.at(0), Reco_phi.at(1), Reco_eta.at(0), Reco_eta.at(1)); else return float(-1.);")
			

			#################################################################################################################################################
			#################################################################################################################################################
			#################################################################################################################################################
			## ## Da qui inserisco il grosso blocco riadattato da analysis_SV.py
			## ## estraggo il muone a maggior pt
			
				.Define("RecoMuon_lead", "FCCAnalyses::ZHfunctions::get_leading_pt(RecoMuons);") ## ## definisco get_leading_pt basandomi su get_leading
				.Define("RecoMuon_lead_pt", "ReconstructedParticle::get_pt(RecoMuon_lead) ") ## ## Pt del muone lead
				.Define("RecoMuon_lead_e", "ReconstructedParticle::get_e(RecoMuon_lead) ") ## ## Pt del muone lead
				.Define("RecoMuon_lead_Track_absD0", "return abs(ReconstructedParticle2Track::getRP2TRK_D0(RecoMuon_lead,EFlowTrack_1))")
				#.Define("RecoMuon_lead_Track", "ReconstructedParticle2Track::getRP2TRK(RecoMuon_lead,EFlowTrack_1)") ## ## inserisco questa traccia in get_VertexData per ottenere un oggetto sul quale poter fare il taglio al chi2
				#.Define("RecoDecayVertexObjectMuon_lead",   "VertexFitterSimple::VertexFitter_Tk( 0, RecoMuon_lead_Track)" ) ### reconstructing a vertex withour any request n=0 ###
				#.Define("RecoDecayVertexObjectMuon_lead",   "VertexFitterSimple::VertexFitter_Tk( 0, RecoMuon_lead_Track, EFlowTrack_1 )" ) ## ## provo a usare questo invece di quello sopra (non è cambiato nulla)
                # .Define("RecoDecayVertexMuon_lead",  "VertexingUtils::get_VertexData( RecoDecayVertexObjectMuon_lead )") ## ## se tutto va bene userò il chi2 da questo oggetto, ne ho definito uno omonimo più avanti.

							# number of tracks
               .Define("ntracks","ReconstructedParticle2Track::getTK_n(EFlowTrack_1)")


               #####
               # determime the primary (and secondary) tracks without using the MC-matching:

	       # Select the tracks that are reconstructed  as primaries
               .Define("RecoedPrimaryTracks",  "VertexFitterSimple::get_PrimaryTracks( EFlowTrack_1, true, 4.5, 20e-3, 300, 0., 0., 0.)")

               .Define("n_RecoedPrimaryTracks",  "ReconstructedParticle2Track::getTK_n( RecoedPrimaryTracks )")
               # the final primary vertex :
               .Define("PrimaryVertexObject",   "VertexFitterSimple::VertexFitter_Tk ( 1, RecoedPrimaryTracks, true, 4.5, 20e-3, 300) ")
               .Define("PrimaryVertex",   "VertexingUtils::get_VertexData( PrimaryVertexObject )")

               # the secondary tracks
               .Define("SecondaryTracks",   "VertexFitterSimple::get_NonPrimaryTracks( EFlowTrack_1,  RecoedPrimaryTracks )")
               .Define("n_SecondaryTracks",  "ReconstructedParticle2Track::getTK_n( SecondaryTracks )" )

               # which of the tracks are primary according to the reco algprithm (boolean)
               .Define("IsPrimary_based_on_reco",  "VertexFitterSimple::IsPrimary_forTracks( EFlowTrack_1,  RecoedPrimaryTracks )")

               # jet clustering (ee-kt) before reconstructing SVs in event
				.Define("JetsParticles", "ReconstructedParticle::remove(ReconstructedParticles, RecoMuon_lead)")
               .Define("RP_px",  "ReconstructedParticle::get_px(JetsParticles)") ## ## Sto usando JetsParticles invece di ReconstructedParticles
               .Define("RP_py",  "ReconstructedParticle::get_py(JetsParticles)")
               .Define("RP_pz",  "ReconstructedParticle::get_pz(JetsParticles)")
               .Define("RP_e",   "ReconstructedParticle::get_e(JetsParticles)")
               #build psedo-jets with the Reconstructed final particles
               .Define("pseudo_jets", "JetClusteringUtils::set_pseudoJets(RP_px, RP_py, RP_pz, RP_e)")
               #run jet clustering with all reco particles. ee_kt_algorithm, exclusive clustering, exactly 2 jets, E-scheme
               .Define("FCCAnalysesJets_ee_kt", "JetClustering::clustering_ee_kt(2, 2, 1, 0)(pseudo_jets)")
               #get the jets out of the structure
               .Define("jets_ee_kt", "JetClusteringUtils::get_pseudoJets(FCCAnalysesJets_ee_kt)")
               #get the jet constituents out of the structure
	       		.Define("jetconstituents_ee_kt", "JetClusteringUtils::get_constituents(FCCAnalysesJets_ee_kt)")


	       # finding SVs in jets 
               .Define("SV_jet", "VertexFinderLCFIPlus::get_SV_jets(ReconstructedParticles, EFlowTrack_1, PrimaryVertexObject, IsPrimary_based_on_reco, jets_ee_kt, jetconstituents_ee_kt)") ## posso provare a inserire JetsParticles al posto di ReconstructedParticles 
               # finding SVs in the event (two interfaces)
	       #.Define("SV_evt1", "VertexFinderLCFIPlus::get_SV_event(ReconstructedParticles, EFlowTrack_1, PrimaryVertexObject, IsPrimary_based_on_reco)")
               #.Define("SV_evt2", "VertexFinderLCFIPlus::get_SV_event(SecondaryTracks, EFlowTrack_1, PrimaryVertexObject)")

	       # multiplicity
               #.Define("SV_evt2_n","VertexingUtils::get_n_SV(SV_evt2)")
               #.Define("SV_evt1_n","VertexingUtils::get_n_SV(SV_evt1)")
	       		.Define("SV_jet_n", "VertexingUtils::get_n_SV(SV_jet)")
               # vertex position
               .Define("SV_jet_position",  "VertexingUtils::get_position_SV( SV_jet )")
               #.Define("SV_evt1_position", "VertexingUtils::get_position_SV( SV_evt1 )")
               #.Define("SV_evt2_position", "VertexingUtils::get_position_SV( SV_evt2 )")

               # more SV properties
               .Define("sv_mass",    "VertexingUtils::get_invM(SV_jet)") # SV mass
               # .Define("sv_p",       "VertexingUtils::get_pMag_SV(SV_jet)") # SV momentum (magnitude)
               # .Define("sv_ntracks", "VertexingUtils::get_VertexNtrk(SV_jet)") # SV daughters (no of tracks)
               .Define("sv_chi2",    "VertexingUtils::get_chi2_SV(SV_jet)") # SV chi2 (not normalised)
               .Define("sv_normchi2","VertexingUtils::get_norm_chi2_SV(SV_jet)") # SV chi2 (normalised)
               # .Define("sv_ndf",     "VertexingUtils::get_nDOF_SV(SV_jet)") # SV no of DOF
               # .Define("sv_theta",   "VertexingUtils::get_theta_SV(SV_jet)") # SV polar angle (theta)
               # .Define("sv_phi",     "VertexingUtils::get_phi_SV(SV_jet)") # SV azimuthal angle (phi)

#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################
			
                ### Jet clustering with different algorithm, only on non leptons ###
                ### https://github.com/HEP-FCC/FCCAnalyses/blob/master/addons/FastJet/JetClustering.h ###
                #.Define("JetsParticles", "ReconstructedParticle::remove(ReconstructedParticles, RecoLeptons)") ## ## modifico questa riga
				## ##.Define("JetsParticles", "ReconstructedParticle::remove(ReconstructedParticles, RecoMuon_lead)")
                ## ##.Define("RP_px", "ReconstructedParticle::get_px(JetsParticles) ")
                ## ##.Define("RP_py", "ReconstructedParticle::get_py(JetsParticles) ")
                ## ##.Define("RP_pz", "ReconstructedParticle::get_pz(JetsParticles) ")
                ## ### build pseudo jets with the RP, using the interface that takes px,py,pz,E
                ## ##.Define("pseudo_jets",  "JetClusteringUtils::set_pseudoJets(RP_px, RP_py, RP_pz, RP_e)" )
                ## ##### Durham algo, exclusive clustering (first number 2) N_jets=0 (second number), E-scheme=0 (third and forth numbers) ###
                ## ##.Define( "FCCAnalysesJets_ee_kt",  "JetClustering::clustering_ee_kt(2, 2, 1, 0)(pseudo_jets)" ) ## ## exclusive
				## ###.Define( "FCCAnalysesJets_ee_kt",  "JetClustering::clustering_ee_kt(0, 5, 1, 0)(pseudo_jets)" ) ## ## inclusive
                ## ##.Define("jets_ee_kt",  "JetClusteringUtils::get_pseudoJets( FCCAnalysesJets_ee_kt )")
                ## ##### get the number of jets in a workaround way, anyway is exactly zero for exclusive clustering ###
                ## ##.Define("jets_e",  "JetClusteringUtils::get_e(jets_ee_kt)")
				## ##.Define("jets_pt",  "JetClusteringUtils::get_pt(jets_ee_kt)")
				## ##.Define("jets_p",  "JetClusteringUtils::get_p(jets_ee_kt)")
				## ##.Define("jets_px",  "JetClusteringUtils::get_px(jets_ee_kt)")
				## ##.Define("jets_py",  "JetClusteringUtils::get_py(jets_ee_kt)")
				## ##.Define("jets_pz",  "JetClusteringUtils::get_pz(jets_ee_kt)")
				## ##.Define("jets_m",  "JetClusteringUtils::get_m(jets_ee_kt)")
				## ##.Define("jets_eta",  "JetClusteringUtils::get_eta(jets_ee_kt)")
				## ##.Define("jets_ph",  "JetClusteringUtils::get_phi(jets_ee_kt)")
				## ##.Define("jets_phi_std",  "JetClusteringUtils::get_phi_std(jets_ee_kt)")
				## ##.Define("jets_theta",  "JetClusteringUtils::get_theta(jets_ee_kt)")
                ## ##.Define("n_jets", "jets_e.size()")

                ### Durham algo, exclusive clustering (first number 2, 3 for exclusive up to n) N_jets=0 (second number), E-scheme=0 (third and forth numbers) ###
                .Define( "FCCAnalysesJets_ee_kt_excl",  "JetClustering::clustering_ee_kt(3, 2, 1, 0)(pseudo_jets)" )
                .Define("jets_ee_kt_excl",  "JetClusteringUtils::get_pseudoJets( FCCAnalysesJets_ee_kt_excl )")
                ### get the number of jets in a workaround way, anyway is exactly zero for exclusive clustering ###
                .Define("jets_e_excl",  "JetClusteringUtils::get_e(jets_ee_kt_excl)")
                .Define("n_jets_excl", "jets_e_excl.size()")

                .Define("FCCAnalysesJets_antikt", "JetClustering::clustering_antikt(0.4, 0, 1., 0, 0)(pseudo_jets)")
                .Define("antikt_jets", "JetClusteringUtils::get_pseudoJets(FCCAnalysesJets_antikt)")
                .Define("antikt_jets_sel", "FCCAnalyses::ZHfunctions::sel_e(5., antikt_jets)")
                .Define("antikt_jets_e", "JetClusteringUtils::get_e(antikt_jets_sel)")
                .Define("n_antikt_jets", "antikt_jets_e.size()")

                .Define("FCCAnalysesJets_antikt10", "JetClustering::clustering_antikt(0.4, 0, 10., 0, 0)(pseudo_jets)")
                .Define("antikt_jets10", "JetClusteringUtils::get_pseudoJets(FCCAnalysesJets_antikt10)")
                .Define("jets_antikt_px10", "JetClusteringUtils::get_px(antikt_jets10)")
                .Define("n_antikt_jets10", "jets_antikt_px10.size()")
                
                ### not useful in this case as the primary track code runs by looking at the chi2 of vertex, taking out the tracks making it larger until there is only one track ###
                ### so there will always be one primary track even if they should both be secondary but the code doesn't handle that and we have both secondary in principle ###
				
				## ## Blocchi per vertex (controllare i valori input in get_PrimaryTracks(...)
                .Define("PrimaryTracks",  "VertexFitterSimple::get_PrimaryTracks( EFlowTrack_1, true, 4.5, 20e-3, 300, 0., 0., 0.)") 
                .Define("PrimaryVertexObject", "VertexFitterSimple::VertexFitter_Tk(1, PrimaryTracks, true, 4.5, 20e-3, 300)")
                .Define("n_PrimaryTracks",  "ReconstructedParticle2Track::getTK_n( PrimaryTracks )")
                .Define("SecondaryTracks",   "VertexFitterSimple::get_NonPrimaryTracks( EFlowTrack_1, PrimaryTracks )")
                .Define("n_SecondaryTracks",  "ReconstructedParticle2Track::getTK_n( SecondaryTracks )" )
			
                .Define("RecoDecayVertexMuon_lead",  "VertexingUtils::get_VertexData( PrimaryVertexObject )") ## ## da decoomentare il precedente RecoDecayVertexMuon_lead

               ### reconstruct the reco decay vertex using the reco'ed tracks from electrons and muons ###
				## ## tolgo questo blocco perché dovrebbe essere buono per la precedente versione dello studio
                #.Define("RecoElectronTracks",   "ReconstructedParticle2Track::getRP2TRK( RecoElectrons, EFlowTrack_1)") ### EFlowTrack_1 contains all tracks, selecting a subset associated with certain particles ###
                #.Define("RecoMuonTracks",   "ReconstructedParticle2Track::getRP2TRK( RecoMuons, EFlowTrack_1)")
                #.Define("RecoLeptonTracks",   "ReconstructedTrack::Merge( RecoElectronTracks, RecoMuonTracks)") ### merges two tracks collections ###
                
                #.Define("RecoDecayVertexObjectLepton",   "VertexFitterSimple::VertexFitter_Tk( 0, RecoLeptonTracks)" ) ### reconstructing a vertex withour any request n=0 ###
                #.Define("RecoDecayVertexLepton",  "VertexingUtils::get_VertexData( RecoDecayVertexObjectLepton )")

                #.Define("Reco_Lxyz","return sqrt(RecoDecayVertexLepton.position.x*RecoDecayVertexLepton.position.x + RecoDecayVertexLepton.position.y*RecoDecayVertexLepton.position.y + RecoDecayVertexLepton.position.z*RecoDecayVertexLepton.position.z);")
                #.Define("Reco_Lxy","return sqrt(RecoDecayVertexLepton.position.x*RecoDecayVertexLepton.position.x + RecoDecayVertexLepton.position.y*RecoDecayVertexLepton.position.y);")

				## ## inserisco un blocco modificato pensato per i jet:
				#.Define("RecoMuon_lead_Track",   "ReconstructedParticle2Track::getRP2TRK( RecoMuon_lead, EFlowTrack_1)")
				#.Define("RecoDecayVertexObjectMuon_lead",   "VertexFitterSimple::VertexFitter_Tk( 0, RecoMuon_lead_Track, PrimaryTracks )" )
				#.Define("RecoDecayVertexMuon_lead",  "VertexingUtils::get_VertexData( RecoDecayVertexObjectMuon_lead )")

                #.Define("Reco_Lxyz","return sqrt(RecoDecayVertexMuon_lead.position.x*RecoDecayVertexMuon_lead.position.x + RecoDecayVertexMuon_lead.position.y*RecoDecayVertexMuon_lead.position.y + RecoDecayVertexMuon_lead.position.z*RecoDecayVertexMuon_lead.position.z);")
                #.Define("Reco_Lxy","return sqrt(RecoDecayVertexMuon_lead.position.x*RecoDecayVertexMuon_lead.position.x + RecoDecayVertexMuon_lead.position.y*RecoDecayVertexMuon_lead.position.y);")
			
                ### https://github.com/HEP-FCC/FCCAnalyses/blob/d39a711a703244ee2902f5d2191ad1e2367363ac/examples/FCCee/vertex/validation_tkParam.py#L115 ###
                #.Define("RecoTracks_noLeptons",   "ReconstructedTrack::Remove( RecoLeptonTracks, EFlowTrack_1)")
                #.Define("n_noLeptonTracks",  "ReconstructedParticle2Track::getTK_n( RecoTracks_noLeptons )" )
                #.Define("noLep_e",      "ReconstructedParticle::get_e(JetsParticles)")
                #.Define("noLep_p",      "ReconstructedParticle::get_p(JetsParticles)")
                #.Define("noLep_pt",      "ReconstructedParticle::get_pt(JetsParticles)")
                #.Define("noLep_px",      "ReconstructedParticle::get_px(JetsParticles)")
                #.Define("noLep_py",      "ReconstructedParticle::get_py(JetsParticles)")
                #.Define("noLep_pz",      "ReconstructedParticle::get_pz(JetsParticles)")
				#.Define("noLep_eta",     "ReconstructedParticle::get_eta(JetsParticles)") #pseudorapidity eta
                #.Define("noLep_theta",   "ReconstructedParticle::get_theta(JetsParticles)")
				#.Define("noLep_phi",     "ReconstructedParticle::get_phi(JetsParticles)") #polar angle in the transverse plane phi
                #.Define("noLep_charge",  "ReconstructedParticle::get_charge(JetsParticles)")
                #.Define("RecoTracknoLep_absD0", "return abs(ReconstructedParticle2Track::getRP2TRK_D0(JetsParticles,EFlowTrack_1))")
                #.Define("RecoTracknoLep_absZ0", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0(JetsParticles,EFlowTrack_1))")
                #.Define("RecoTracknoLep_absD0sig", "return abs(ReconstructedParticle2Track::getRP2TRK_D0_sig(JetsParticles,EFlowTrack_1))") #significance
                #.Define("RecoTracknoLep_absZ0sig", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0_sig(JetsParticles,EFlowTrack_1))")
                #.Define("RecoTracknoLep_D0cov", "ReconstructedParticle2Track::getRP2TRK_D0_cov(JetsParticles,EFlowTrack_1)") #variance (not sigma)
                #.Define("RecoTracknoLep_Z0cov", "ReconstructedParticle2Track::getRP2TRK_Z0_cov(JetsParticles,EFlowTrack_1)")
               
                ### LCFIPlus algorithm for vertexing ###
                #find the DVs
            	#.Define("RecoDVs", "VertexFinderLCFIPlus::get_SV_event(RecoMuon_lead, EFlowTrack_1, PrimaryVertexObject, true, 9., 40., 5.)")
				#.Define("RecoDVs", "VertexFinderLCFIPlus::get_SV_jets(ReconstructedParticles, EFlowTrack_1, PrimaryVertexObject, true, pseudo_jets, 10)") ## ## l'ho scritto io, ma non so usarlo
                #find number of DVs
                #.Define("n_RecoDVs", "VertexingUtils::get_n_SV(RecoDVs)")
                #.Define("DV_Lxyz", "VertexingUtils::get_d3d_SV(RecoDVs, PrimaryVertexObject)")

                #EVENTWIDE VARIABLES: Access quantities that exist only once per event, such as the missing energy (despite the name, the MissingET collection contains the total missing energy)
		.Define("RecoMissingEnergy_e", "ReconstructedParticle::get_e(MissingET)")
		.Define("RecoMissingEnergy_p", "ReconstructedParticle::get_p(MissingET)")
		.Define("RecoMissingEnergy_pt", "ReconstructedParticle::get_pt(MissingET)")
		.Define("RecoMissingEnergy_px", "ReconstructedParticle::get_px(MissingET)") #x-component of RecoMissingEnergy
		.Define("RecoMissingEnergy_py", "ReconstructedParticle::get_py(MissingET)") #y-component of RecoMissingEnergy
		.Define("RecoMissingEnergy_pz", "ReconstructedParticle::get_pz(MissingET)") #z-component of RecoMissingEnergy
		.Define("RecoMissingEnergy_eta", "ReconstructedParticle::get_eta(MissingET)")
		.Define("RecoMissingEnergy_theta", "ReconstructedParticle::get_theta(MissingET)")
		.Define("RecoMissingEnergy_phi", "ReconstructedParticle::get_phi(MissingET)") #angle of RecoMissingEnergy

                # different definition of missing energy from fccanalysis classes instead of edm4hep
                .Define("RecoEmiss", "FCCAnalyses::ZHfunctions::missingEnergy(91.188, ReconstructedParticles)") #ecm 
                .Define("RecoEmiss_px",  "RecoEmiss[0].momentum.x")
                .Define("RecoEmiss_py",  "RecoEmiss[0].momentum.y")
                .Define("RecoEmiss_pz",  "RecoEmiss[0].momentum.z")
                .Define("RecoEmiss_pt",  "return sqrt(RecoEmiss_px*RecoEmiss_px + RecoEmiss_py*RecoEmiss_py)")
                .Define("RecoEmiss_p",  "return sqrt(RecoEmiss_px*RecoEmiss_px + RecoEmiss_py*RecoEmiss_py + RecoEmiss_pz*RecoEmiss_pz)")
                .Define("RecoEmiss_e",   "RecoEmiss[0].energy")

                ### dilepton invariant mass ###
                .Define("Reco_TwoLeptons_energy", "if (n_RecoLeptons>1) return (Reco_e.at(0) + Reco_e.at(1)); else return float(-1.);")
                .Define("Reco_TwoLeptons_px", "if (n_RecoLeptons>1) return (Reco_px.at(0) + Reco_px.at(1)); else return float(-1.);")
                .Define("Reco_TwoLeptons_py", "if (n_RecoLeptons>1) return (Reco_py.at(0) + Reco_py.at(1)); else return float(-1.);")
                .Define("Reco_TwoLeptons_pz", "if (n_RecoLeptons>1) return (Reco_pz.at(0) + Reco_pz.at(1)); else return float(-1.);")
                .Define("Reco_invMass", "if (n_RecoLeptons>1) return sqrt(Reco_TwoLeptons_energy*Reco_TwoLeptons_energy - Reco_TwoLeptons_px*Reco_TwoLeptons_px - Reco_TwoLeptons_py*Reco_TwoLeptons_py - Reco_TwoLeptons_pz*Reco_TwoLeptons_pz ); else return float(-1.);")

                .Define('RecoMC_PID', "ReconstructedParticle2MC::getRP2MC_pdg(MCRecoAssociations0,MCRecoAssociations1,ReconstructedParticles,Particle)")

                #### FILTERS APPLIED TO ALL THE EVENTS ####
                ### minimal selection for hnls final state
                #.Filter("n_RecoPhotons==0 && n_RecoLeptons==2 && ((Reco_charge.at(0)==1 && Reco_charge.at(1)==-1) || (Reco_charge.at(0)==-1 && Reco_charge.at(1)==1))") ## ## lui va via
                ### generator selection on llnunu background that needs to be applied consinstently to the others
                #.Filter("Reco_pt.at(0) > 1 && Reco_pt.at(1) > 1 && RecoEmiss_pt > 5")
				.Filter("n_RecoMuons > 0 && RecoMuon_pt.at(0) > 10")
				.Filter("n_jets>0")

               )
                return df2

        def output():
                branchList = [
                        ######## Monte-Carlo particles #######
                        "n_FSGenElectron",
                        "n_FSGenMuon",
                        "n_FSGenLepton",
                        "n_FSGenPhoton",
                        #"n_GenN",  ## ## decommentato da me
                        #"n_FSGenNeutrino", ## ## decommentato da me
						#"FSGenTotal_e", ## ## prova per energia totale

                        "GenParticles_PID",

                        #"n_GenTaus",
                        #"n_GenPions",
                        #"n_GenKLs",
                        #"n_GenKpluss",

                        #"GenPion_e",
                        #"GenTau_e",
                        #"GenKL_e",
                        #"GenKplus_e",

                        #"GenPion_pt",
                        #"GenTau_pt",
                        #"GenKL_pt",
                        #"GenKplus_pt",

                        #"FSGenLepton_e",  ## ## decommentato da me
                        #"FSGenLepton_p",## ## decommentato da me
                        #"FSGenLepton_pt",## ## decommentato da me
                        #"FSGenLepton_px",## ## decommentato da me
                        #"FSGenLepton_py",## ## decommentato da me
                        #"FSGenLepton_pz",## ## decommentato da me
                        #"FSGenLepton_eta",## ## decommentato da me
                        #"FSGenLepton_theta",## ## decommentato da me
                        #"FSGenLepton_phi",## ## decommentato da me
                        #"FSGenLepton_charge",## ## decommentato da me
                        #"FSGenLepton_time",## ## decommentato da me
                        #"FSGenLepton_vertex_x",## ## decommentato da me
                        #"FSGenLepton_vertex_y",## ## decommentato da me
                        #"FSGenLepton_vertex_z",## ## decommentato da me

						#"FSGenElectron_e",  ## ## decommentato da me
                        #"FSGenElectron_p",## ## decommentato da me
                        #"FSGenElectron_pt",## ## decommentato da me
                        #"FSGenElectron_px",## ## decommentato da me
                        #"FSGenElectron_py",## ## decommentato da me
                        #"FSGenElectron_pz",## ## decommentato da me
                        #"FSGenElectron_eta",## ## decommentato da me
                        #"FSGenElectron_theta",## ## decommentato da me
                        #"FSGenElectron_phi",## ## decommentato da me
                        #"FSGenElectron_charge",## ## decommentato da me
                        #"FSGenElectron_time",## ## decommentato da me
                        #"FSGenElectron_vertex_x",## ## decommentato da me
                        #"FSGenElectron_vertex_y",## ## decommentato da me
                        #"FSGenElectron_vertex_z",## ## decommentato da me

						#"FSGenMuon_e",  ## ## decommentato da me
                        #"FSGenMuon_p",## ## decommentato da me
                        #"FSGenMuon_pt",## ## decommentato da me
                        #"FSGenMuon_px",## ## decommentato da me
                        #"FSGenMuon_py",## ## decommentato da me
                        #"FSGenMuon_pz",## ## decommentato da me
                        #"FSGenMuon_eta",## ## decommentato da me
                        #"FSGenMuon_theta",## ## decommentato da me
                        #"FSGenMuon_phi",## ## decommentato da me
                        #"FSGenMuon_charge",## ## decommentato da me
                        #"FSGenMuon_time",## ## decommentato da me
                        #"FSGenMuon_vertex_x",## ## decommentato da me
                        #"FSGenMuon_vertex_y",## ## decommentato da me
                        #"FSGenMuon_vertex_z",## ## decommentato da me

						#"FSGenNeutrino_e",  ## ## decommentato da me
                        #"FSGenNeutrino_p",## ## decommentato da me
                        #"FSGenNeutrino_pt",## ## decommentato da me
                        #"FSGenNeutrino_px",## ## decommentato da me
                        #"FSGenNeutrino_py",## ## decommentato da me
                        #"FSGenNeutrino_pz",## ## decommentato da me
                        #"FSGenNeutrino_eta",## ## decommentato da me
                        #"FSGenNeutrino_theta",## ## decommentato da me
                        #"FSGenNeutrino_phi",## ## decommentato da me

                        #"FSGenLepton_e_led",## ## decommentato da me
                        #"FSGenLepton_p_led",## ## decommentato da me
                        #"FSGenLepton_pt_led",## ## decommentato da me
                        #"FSGenLepton_px_led",## ## decommentato da me
                        #"FSGenLepton_py_led",## ## decommentato da me
                        #"FSGenLepton_pz_led",## ## decommentato da me
                        #"FSGenLepton_eta_led",## ## decommentato da me
                        #"FSGenLepton_theta_led",## ## decommentato da me
                        #"FSGenLepton_phi_led",## ## decommentato da me
                        #"FSGenLepton_charge_led",## ## decommentato da me

                        #"FSGenLepton_e_sub",## ## decommentato da me
                        #"FSGenLepton_p_sub",## ## decommentato da me
                        #"FSGenLepton_pt_sub",## ## decommentato da me
                        #"FSGenLepton_px_sub",## ## decommentato da me
                        #"FSGenLepton_py_sub",## ## decommentato da me
                        #"FSGenLepton_pz_sub",## ## decommentato da me
                        #"FSGenLepton_eta_sub",## ## decommentato da me
                        #"FSGenLepton_theta_sub",## ## decommentato da me
                        #"FSGenLepton_phi_sub",## ## decommentato da me
                        #"FSGenLepton_charge_sub",## ## decommentato da me

                        #"FSGen_Lxy",## ## decommentato da me
                        #"FSGen_Lxyz",## ## decommentato da me
                        #"FSGen_invMass",## ## decommentato da me
                        #"GenN_Lxyz",## ## decommentato da me
                        #"GenN_tau",## ## decommentato da me
                        #"GenN_mass",## ## decommentato da me
                        #"GenN_e",## ## decommentato da me
                        #"GenN_p",## ## decommentato da me


                        #"FSGenPhoton_e",
                        #"FSGenPhoton_p",
                        #"FSGenPhoton_pt",
                        #"FSGenPhoton_px",
                        #"FSGenPhoton_py",
                        #"FSGenPhoton_pz",
                        #"FSGenPhoton_eta",
                        #"FSGenPhoton_theta",
                        #"FSGenPhoton_phi",
                        #"FSGenPhoton_charge",

                        ######## Reconstructed particles #######
                       	#"n_RecoTracks",
                        #"n_noLeptonTracks",
                        #"n_PrimaryTracks",
                        #"n_SecondaryTracks",

                        #"n_jets",
                        #"n_jets_excl",
                        #"n_antikt_jets",
                        #"n_antikt_jets10",
                        #"n_RecoJets",
						

                        "n_RecoPhotons",
                        "n_RecoElectrons",
                        "n_RecoMuons",
                        "n_RecoLeptons",

                        #"RecoJet_e",
                        #"RecoJet_p",
                        #"RecoJet_pt",
                        #"RecoJet_px",
                        #"RecoJet_py",
                        #"RecoJet_pz",
                        #"RecoJet_eta",
                        #"RecoJet_theta",
                        #"RecoJet_phi",
                        #"RecoJet_charge",
                        #"RecoJetTrack_absD0",
                        #"RecoJetTrack_absZ0",
                        #"RecoJetTrack_absD0sig",
                        #"RecoJetTrack_absZ0sig",
                        #"RecoJetTrack_D0cov",
                        #"RecoJetTrack_Z0cov",

                        #"RecoPhoton_e",
                        #"RecoPhoton_p",
                        #"RecoPhoton_pt",
                        #"RecoPhoton_px",
                        #"RecoPhoton_py",
                        #"RecoPhoton_pz",
                        #"RecoPhoton_eta",
                        #"RecoPhoton_theta",
                        #"RecoPhoton_phi",
                        #"RecoPhoton_charge",

                        "RecoElectron_e",## ## decommentato da me
                        "RecoElectron_p",## ## decommentato da me
                        "RecoElectron_pt",## ## decommentato da me
                        "RecoElectron_px",## ## decommentato da me
                        "RecoElectron_py",## ## decommentato da me
                        "RecoElectron_pz",## ## decommentato da me
                        "RecoElectron_eta",## ## decommentato da me
                        "RecoElectron_theta",## ## decommentato da me
                        "RecoElectron_phi",## ## decommentato da me
                        "RecoElectron_charge",## ## decommentato da me
                        "RecoElectronTrack_absD0",## ## decommentato da me
                        #"RecoElectronTrack_absZ0",
                        #"RecoElectronTrack_absD0sig",
                        #"RecoElectronTrack_absZ0sig",
                        #"RecoElectronTrack_D0cov",
                        #"RecoElectronTrack_Z0cov",

                        "n_NeutralHadrons",
                        "NeutralHadrons_e",
                        "NeutralHadrons_p",
                        "NeutralHadrons_pt",
                        "NeutralHadrons_px",
                        "NeutralHadrons_py",
                        "NeutralHadrons_pz",
                        "NeutralHadrons_eta",
                        "NeutralHadrons_theta",
                        "NeutralHadrons_phi",
                        "NeutralHadrons_charge",
                        "NeutralHadrons_mass",

                        "RecoMissingEnergy_e",
                        "RecoMissingEnergy_p",
                        "RecoMissingEnergy_pt",
                        "RecoMissingEnergy_px",
                        "RecoMissingEnergy_py",
                        "RecoMissingEnergy_pz",
                        "RecoMissingEnergy_eta",
                        "RecoMissingEnergy_theta",
                        "RecoMissingEnergy_phi",

                        "RecoEmiss_px",
                        "RecoEmiss_py",
                        "RecoEmiss_pz",
                        "RecoEmiss_pt",
                        "RecoEmiss_p",
                        "RecoEmiss_e",

                        "Reco_e",
                        "Reco_p",
                        "Reco_pt",
                        "Reco_px",
                        "Reco_py",
                        "Reco_pz",
                        "Reco_eta",
                        "Reco_theta",
                        "Reco_phi",
                        "Reco_charge",
                        "RecoTrack_absD0",
                        "RecoTrack_absZ0",
                        "RecoTrack_absD0sig",
                        "RecoTrack_absZ0sig",
                        "RecoTrack_D0cov",
                        "RecoTrack_Z0cov",

                        "Reco_e_lead",
                        "Reco_p_lead",
                        "Reco_pt_lead",
                        "Reco_px_lead",
                        "Reco_py_lead",
                        "Reco_pz_lead",
                        "Reco_eta_lead",
                        "Reco_theta_lead",
                        "Reco_phi_lead",
                        "Reco_charge_lead",
                        "RecoTrack_absD0_lead",
                        "RecoTrack_absZ0_lead",
                        "RecoTrack_absD0sig_lead",
                        "RecoTrack_absZ0sig_lead",
                        "RecoTrack_D0cov_lead",
                        "RecoTrack_Z0cov_lead",

                        "Reco_e_sub",
                        "Reco_p_sub",
                        "Reco_pt_sub",
                        "Reco_px_sub",
                        "Reco_py_sub",
                        "Reco_pz_sub",
                        "Reco_eta_sub",
                        "Reco_theta_sub",
                        "Reco_phi_sub",
                        "Reco_charge_sub",
                        "RecoTrack_absD0_sub",
                        "RecoTrack_absZ0_sub",
                        "RecoTrack_absD0sig_sub",
                        "RecoTrack_absZ0sig_sub",
                        "RecoTrack_D0cov_sub",
                        "RecoTrack_Z0cov_sub",

                        #"RecoDecayVertexLepton",
                        #"Reco_Lxy",
                        #"Reco_Lxyz",
                        "Reco_invMass",
                        "Reco_cos",
                        "Reco_DR",

                        #"n_RecoDVs",
                        #"DV_Lxyz", 
                        #"DV_Lxyz_sig",

                        #"RecoMC_PID",
                        
                        #"noLep_e",
                        #"noLep_p",   
                        #"noLep_pt",   
                        #"noLep_px",   
                        #"noLep_py",   
                        #"noLep_pz",    
		        #"noLep_eta",   
                        #"noLep_theta",
	                #"noLep_phi",  
                        #"noLep_charge", 
                        #"RecoTracknoLep_absD0", 
                        #"RecoTracknoLep_absZ0", 
                        #"RecoTracknoLep_absD0sig", 
                        #"RecoTracknoLep_absZ0sig", 
                        #"RecoTracknoLep_D0cov", 
                        #"RecoTracknoLep_Z0cov",
					"jets_e",
					"jets_pt",
					"n_jets",
               		#"n_PrimaryTracks",
	                #"n_SecondaryTracks",
					"RecoMuon_lead_pt",
					"RecoMuon_lead_e",
					"RecoMuon_lead_Track_absD0",
					"RecoDecayVertexMuon_lead",
					
					########################################
					########   JET   #######################
					########################################
					  #  primary vertex and primary tracks w/o any MC-matching :
                		'IsPrimary_based_on_reco',
                		'PrimaryVertex',

                		# vector of SV vertex objects
                		'SV_jet',
                		#'SV_evt1',
                		#'SV_evt2',

                		# SV multiplicity
               			 #'SV_evt1_n',
                		#'SV_evt2_n',
                		'SV_jet_n',

                		# SV position
                		'SV_jet_position',
                		#'SV_evt1_position',
						#'SV_evt2_position',

                		# more SV variables
                		'sv_mass',
                		# 'sv_p',
                		# 'sv_ntracks',
                		'sv_chi2',
                		'sv_normchi2',
                		# 'sv_ndf',
	        			# 'sv_theta',
                		# 'sv_phi',

		]

                return branchList
