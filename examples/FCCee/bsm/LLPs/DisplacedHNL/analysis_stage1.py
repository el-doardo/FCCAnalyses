## ## espoto ## ##
# 	
# 	Spero che questo branch rimanga pulito e ordinato.
# 	Questo è il principale proposito con il quale 
#	è stato creato
# 	
## ## ## ## ## ## ## ## ## ##	


import ROOT

#Mandatory: List of processes

processList = {

	## ## ## ## ## ## ## ## ## ## ## ## #
	#	Backgrounds centrally produced	#
	## ## ## ## ## ## ## ## ## ## ## ## #
	
        #'p8_ee_Zee_ecm91':{'fraction':0.01}, 		## ## secondo il paper lui non serve, ma sono curioso 	## ## fraction limit sperimentato: 1
        #'p8_ee_Zmumu_ecm91':{'fraction':0.01},		## ## fraction limit sperimentato: 0.25
        #'p8_ee_Ztautau_ecm91':{'fraction':0.01},	## ## fraction limit sperimentato: 0.25
        #'p8_ee_Zbb_ecm91':{'fraction':0.01},		## ## fraction limit sperimentato: 0.1
        #'p8_ee_Zcc_ecm91':{'fraction':0.01},		## ## fraction limit sperimentato: 0.1
        #'p8_ee_Zud_ecm91':{'fraction':0.01},		## ## fraction limit sperimentato: 0.5 forse alzabile
        #'p8_ee_Zss_ecm91':{'fraction':0.01},		## ## fraction limit sperimentato: 0.5 forrse alzabile

	## ## ## ## ## ## ## ## ## ## ## ## #
	#	Backgrounds locally produced	#
	## ## ## ## ## ## ## ## ## ## ## ## #

		"numujj":{},
	

	## ## ## ## ## ## ## ## #
	#	Segnali di HNLs		#
	## ## ## ## ## ## ## ##	#
	
		"HNL_1.04e-8_10gev":{},
		"HNL_1.04e-8_70gev":{},
		"HNL_4e-10_20gev":{},
		"HNL_4e-10_80gev":{},	
		"HNL_6.67e-10_30gev":{},
		"HNL_8.35e-9_40gev":{},
		"HNL_2.27e-9_20gev":{},
		"HNL_2.27e-9_50gev":{},
		"HNL_3.17e-11_30gev":{},
		"HNL_3.17e-11_60gev":{},
	
}

processList_ = {


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
#inputDir = "/eos/experiment/fcc/ee/generation/DelphesEvents/winter2023/IDEA/"
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
				.Alias("Muon0", "Muon#0.index")


                ################### Reconstructed particles #####################
                .Define("n_RecoTracks","ReconstructedParticle2Track::getTK_n(EFlowTrack_1)")
					   
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


				## ## estraggo il muone a maggior pt
				.Define("RecoMuon_lead", "FCCAnalyses::ZHfunctions::get_leading_pt(RecoMuons);") ## ## definisco get_leading_pt basandomi su get_leading
				.Define("RecoMuon_lead_pt", "ReconstructedParticle::get_pt(RecoMuon_lead) ") ## ## Pt del muone lead
				.Define("RecoMuon_lead_e", "ReconstructedParticle::get_e(RecoMuon_lead) ") ## ## Pt del muone lead
				.Define("RecoMuon_lead_Track_absD0", "return abs(ReconstructedParticle2Track::getRP2TRK_D0(RecoMuon_lead,EFlowTrack_1))") ## ## Lui potrebbe andar via


				## ## ## ## #
				#	JET		#
				## ## ## ## #
					   
                ### Jet clustering with different algorithm, only on non leptons ###
                ### https://github.com/HEP-FCC/FCCAnalyses/blob/master/addons/FastJet/JetClustering.h ###
					   
				.Define("JetsParticles", "ReconstructedParticle::remove(ReconstructedParticles, RecoMuon_lead)")
                .Define("RP_px", "ReconstructedParticle::get_px(JetsParticles) ")
                .Define("RP_py", "ReconstructedParticle::get_py(JetsParticles) ")
                .Define("RP_pz", "ReconstructedParticle::get_pz(JetsParticles) ")
                .Define("RP_e", "ReconstructedParticle::get_e(JetsParticles) ")
					   
                # build pseudo jets with the RP, using the interface that takes px,py,pz,E
                .Define("pseudo_jets",  "JetClusteringUtils::set_pseudoJets(RP_px, RP_py, RP_pz, RP_e)" )
					   
                ### Durham algo, exclusive clustering (first number 2) N_jets=0 (second number), E-scheme=0 (third and forth numbers) ###
                .Define( "FCCAnalysesJets_ee_kt",  "JetClustering::clustering_ee_kt(2, 2, 1, 0)(pseudo_jets)" ) ## ## exclusive
				#.Define( "FCCAnalysesJets_ee_kt",  "JetClustering::clustering_ee_kt(0, 5, 1, 0)(pseudo_jets)" ) ## ## inclusive
					   
                .Define("jets_ee_kt",  "JetClusteringUtils::get_pseudoJets( FCCAnalysesJets_ee_kt )")
                ### get the number of jets in a workaround way, anyway is exactly zero for exclusive clustering ###
                .Define("jets_e",  "JetClusteringUtils::get_e(jets_ee_kt)")
				.Define("jets_pt",  "JetClusteringUtils::get_pt(jets_ee_kt)")
				.Define("jets_p",  "JetClusteringUtils::get_p(jets_ee_kt)")
				.Define("jets_px",  "JetClusteringUtils::get_px(jets_ee_kt)")
				.Define("jets_py",  "JetClusteringUtils::get_py(jets_ee_kt)")
				.Define("jets_pz",  "JetClusteringUtils::get_pz(jets_ee_kt)")
				.Define("jets_m",  "JetClusteringUtils::get_m(jets_ee_kt)")
				.Define("jets_eta",  "JetClusteringUtils::get_eta(jets_ee_kt)")
				.Define("jets_ph",  "JetClusteringUtils::get_phi(jets_ee_kt)")
				.Define("jets_phi_std",  "JetClusteringUtils::get_phi_std(jets_ee_kt)")
				.Define("jets_theta",  "JetClusteringUtils::get_theta(jets_ee_kt)")
                .Define("n_jets", "jets_e.size()")

                
                ### not useful in this case as the primary track code runs by looking at the chi2 of vertex, taking out the tracks making it larger until there is only one track ###
                ### so there will always be one primary track even if they should both be secondary but the code doesn't handle that and we have both secondary in principle ###
				
				## ## Questa parte va capita
                .Define("PrimaryTracks",  "VertexFitterSimple::get_PrimaryTracks( EFlowTrack_1, true, 4.5, 20e-3, 300, 0., 0., 0.)") 
                .Define("PrimaryVertexObject", "VertexFitterSimple::VertexFitter_Tk(1, PrimaryTracks, true, 4.5, 20e-3, 300)")
                .Define("n_PrimaryTracks",  "ReconstructedParticle2Track::getTK_n( PrimaryTracks )")
                .Define("SecondaryTracks",   "VertexFitterSimple::get_NonPrimaryTracks( EFlowTrack_1, PrimaryTracks )")
                .Define("n_SecondaryTracks",  "ReconstructedParticle2Track::getTK_n( SecondaryTracks )" )
				.Define("RecoDecayVertexMuon_lead",  "VertexingUtils::get_VertexData( PrimaryVertexObject )")
				
				## ## Posso controllare se questi funzionano, forse hanno senso
                .Define("Reco_Lxyz","return sqrt(RecoDecayVertexMuon_lead.position.x*RecoDecayVertexMuon_lead.position.x + RecoDecayVertexMuon_lead.position.y*RecoDecayVertexMuon_lead.position.y + RecoDecayVertexMuon_lead.position.z*RecoDecayVertexMuon_lead.position.z);")
                .Define("Reco_Lxy","return sqrt(RecoDecayVertexMuon_lead.position.x*RecoDecayVertexMuon_lead.position.x + RecoDecayVertexMuon_lead.position.y*RecoDecayVertexMuon_lead.position.y);")

                ### https://github.com/HEP-FCC/FCCAnalyses/blob/d39a711a703244ee2902f5d2191ad1e2367363ac/examples/FCCee/vertex/validation_tkParam.py#L115 ###
                
               	## ## Questi potrebbero essere utili
                ### LCFIPlus algorithm for vertexing ###
                #find the DVs
                #.Define("RecoDVs", "VertexFinderLCFIPlus::get_SV_event(RecoLeptonTracks, EFlowTrack_1, PrimaryVertexObject, true, 9., 40., 5.)")
                #find number of DVs
                #.Define("n_RecoDVs", "VertexingUtils::get_n_SV(RecoDVs)")
                #.Define("DV_Lxyz", "VertexingUtils::get_d3d_SV(RecoDVs, PrimaryVertexObject)")


				## ## ## ## ## ## ###
				#	Missing Energy	#
				## ## ## ## ## ## ###
					   
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
                        

                        ######## Reconstructed particles #######
                       	"n_RecoTracks",
                        "n_PrimaryTracks",
                        "n_SecondaryTracks",

                        "n_jets",
						"jets_e",
						"jets_pt",

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

					
                        "Reco_Lxy",
                        "Reco_Lxyz",

                        #"n_RecoDVs",
                        #"DV_Lxyz", 
                        #"DV_Lxyz_sig",

                        
						"RecoMuon_lead_pt",
						"RecoMuon_lead_e",
						"RecoMuon_lead_Track_absD0",
						"RecoDecayVertexMuon_lead",

		]

                return branchList
