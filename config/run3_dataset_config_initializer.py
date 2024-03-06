import copy
import os

year = '2022'; pre_post = 'pre'; lumi = "9739"
# year = '2022'; pre_post = 'post'; lumi = "27787"
# year = '2023'; pre_post = 'pre'; lumi = "19884"
# year = '2023'; pre_post = 'post'; lumi = "9959"

base_processes = {'data':     {'data_tau': [],
                               'data_mu': [],
                               'data_ele': [],
                               'data_phh': []},
                  'dy':       {'dy': []},
                  'others':   {'ewk': [],
                               'multiboson': [],
                               'singletop': [],
                               'ttx': [],
                               'wjets': []},
                   'singleh': {'fusionh': [],
                               'vh': []},
                   'ttbar':   {'ttbar' : []},
                   'qqhh':    {'VBFHHto2B2Tau_CV-1_C2V-1_C3-1': [],
                               'VBFHHto2B2Tau_CV-1_C2V-1_C3-2': [],
                               'VBFHHto2B2Tau_CV-1_C2V-2_C3-1': [],
                               'VBFHHto2B2Tau_CV-1p74_C2V-1p37_C3-14p4': [],
                               'VBFHHto2B2Tau_CV-m0p012_C2V-0p030_C3-10p2': [],
                               'VBFHHto2B2Tau_CV-m0p758_C2V-1p44_C3-m19p3': [],
                               'VBFHHto2B2Tau_CV-m0p962_C2V-0p959_C3-m1p43': [],
                               'VBFHHto2B2Tau_CV-m1p21_C2V-1p94_C3-m0p94': [],
                               'VBFHHto2B2Tau_CV-m1p60_C2V-2p72_C3-m1p36': [],
                               'VBFHHto2B2Tau_CV-m1p83_C2V-3p57_C3-m3p39': [],
                               'VBFHHto2B2Tau_CV-m2p12_C2V-3p87_C3-m5p96': []},
                    'gghh':    {'GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00': [],
                                'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00': [],
                                'GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00': [],
                                'GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00': [],
                                'GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00': [],
                                'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p10': [],
                                'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p35': [],
                                'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-3p00': [],
                                'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-m2p00': []}
                 }
                          
processes = {'2022': {'pre':  copy.deepcopy(base_processes),
                      'post': copy.deepcopy(base_processes)
                     },
             '2023': {'pre':  copy.deepcopy(base_processes),
                      'post': copy.deepcopy(base_processes)
                     }
            }

# new stadard color palette
#
# color  RGB             HEX
violet = [150,  74, 139] #964A8B
cyan   = [87,  144, 252] #5790FC
orange = [248, 156,  32] #F89C20
red    = [228,  37,  54] #E42536
grey   = [156, 156, 161] #9C9CA1
purple = [122,  33, 221] #7A21DD
black  = [  0,   0,   0] #000000

colors = {'data' : black,
          'data_tau': black,
          'data_mu': black,
          'data_ele': black,
          'data_phh': black,
          'dy': purple,
          'ttbar': red,
          'singleh': orange,
          'fusionh': orange,
          'vh': orange,
          'others': grey,
          'ewk': grey,
          'multiboson': grey,
          'singletop': grey,
          'ttx': grey,
          'wjets': grey,
          'qqhh': cyan,
          'VBFHHto2B2Tau_CV-1_C2V-1_C3-1': cyan,
          'VBFHHto2B2Tau_CV-1_C2V-1_C3-2': cyan,
          'VBFHHto2B2Tau_CV-1_C2V-2_C3-1': cyan,
          'VBFHHto2B2Tau_CV-1p74_C2V-1p37_C3-14p4': cyan,
          'VBFHHto2B2Tau_CV-m0p012_C2V-0p030_C3-10p2': cyan,
          'VBFHHto2B2Tau_CV-m0p758_C2V-1p44_C3-m19p3': cyan,
          'VBFHHto2B2Tau_CV-m0p962_C2V-0p959_C3-m1p43': cyan,
          'VBFHHto2B2Tau_CV-m1p21_C2V-1p94_C3-m0p94': cyan,
          'VBFHHto2B2Tau_CV-m1p60_C2V-2p72_C3-m1p36': cyan,
          'VBFHHto2B2Tau_CV-m1p83_C2V-3p57_C3-m3p39': cyan,
          'VBFHHto2B2Tau_CV-m2p12_C2V-3p87_C3-m5p96': cyan,
          'gghh': black,
          'GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00': black,
          'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00': black,
          'GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00': black,
          'GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00': black,
          'GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00': black,
          'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p10': black,
          'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p35': black,
          'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-3p00': black,
          'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-m2p00': black
         }

# STRUCTURE
# processes['YEAR']['PRE/POST']['PROCESS'].append(['DAS_STRING', 'NAME', 'TAGS'])

################################################################################################################################################################################################################################################################################################
# DATA

processes['2022']['pre']['data']['data_tau'].append(['/Tau/Run2022B-22Sep2023-v1/NANOAOD', 'Tau_2022B', 'NanoAODv12'])
processes['2022']['pre']['data']['data_tau'].append(['/Tau/Run2022C-22Sep2023-v1/NANOAOD', 'Tau_2022C', 'NanoAODv12'])
processes['2022']['pre']['data']['data_tau'].append(['/Tau/Run2022D-22Sep2023-v1/NANOAOD', 'Tau_2022D', 'NanoAODv12'])
processes['2022']['pre']['data']['data_mu'].append(['/SingleMuon/Run2022B-22Sep2023-v1/NANOAOD', 'SingleMuon_2022B', 'NanoAODv12'])
processes['2022']['pre']['data']['data_mu'].append(['/SingleMuon/Run2022C-22Sep2023-v1/NANOAOD', 'SingleMuon_2022C', 'NanoAODv12'])
processes['2022']['pre']['data']['data_mu'].append(['/Muon/Run2022D-22Sep2023-v1/NANOAOD', 'Muon_2022D', 'NanoAODv12'])
processes['2022']['pre']['data']['data_ele'].append(['/EGamma/Run2022B-22Sep2023-v2/NANOAOD', 'EGamma_2022B', 'NanoAODv12'])
processes['2022']['pre']['data']['data_ele'].append(['/EGamma/Run2022C-22Sep2023-v1/NANOAOD', 'EGamma_2022C', 'NanoAODv12'])
processes['2022']['pre']['data']['data_ele'].append(['/EGamma/Run2022D-22Sep2023-v1/NANOAOD', 'EGamma_2022D', 'NanoAODv12'])

processes['2022']['post']['data']['data_tau'].append(['/Tau/Run2022E-22Sep2023-v1/NANOAOD', 'Tau_2022E', 'NanoAODv12'])
processes['2022']['post']['data']['data_tau'].append(['/Tau/Run2022F-22Sep2023-v1/NANOAOD', 'Tau_2022F', 'NanoAODv12'])
processes['2022']['post']['data']['data_tau'].append(['/Tau/Run2022G-22Sep2023-v1/NANOAOD', 'Tau_2022G', 'NanoAODv12'])
processes['2022']['post']['data']['data_mu'].append(['/Muon/Run2022E-22Sep2023-v1/NANOAOD', 'Muon_2022E', 'NanoAODv12'])
processes['2022']['post']['data']['data_mu'].append(['/Muon/Run2022F-22Sep2023-v2/NANOAOD', 'Muon_2022F', 'NanoAODv12'])
processes['2022']['post']['data']['data_mu'].append(['/Muon/Run2022G-22Sep2023-v1/NANOAOD', 'Muon_2022G', 'NanoAODv12'])
processes['2022']['post']['data']['data_ele'].append(['/EGamma/Run2022E-22Sep2023-v1/NANOAOD', 'EGamma_2022E', 'NanoAODv12'])
processes['2022']['post']['data']['data_ele'].append(['/EGamma/Run2022F-22Sep2023-v1/NANOAOD', 'EGamma_2022F', 'NanoAODv12'])
processes['2022']['post']['data']['data_ele'].append(['/EGamma/Run2022G-22Sep2023-v2/NANOAOD', 'EGamma_2022G', 'NanoAODv12'])

processes['2023']['pre']['data']['data_tau'].append(['/Tau/Run2023B-22Sep2023-v1/NANOAOD', 'Tau_Run2023B', 'NanoAODv12'])
processes['2023']['pre']['data']['data_tau'].append(['/Tau/Run2023C-22Sep2023_v1-v2/NANOAOD', 'Tau_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_tau'].append(['/Tau/Run2023C-22Sep2023_v2-v1/NANOAOD', 'Tau_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_tau'].append(['/Tau/Run2023C-22Sep2023_v3-v1/NANOAOD', 'Tau_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_tau'].append(['/Tau/Run2023C-22Sep2023_v4-v1/NANOAOD', 'Tau_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_mu'].append(['/Muon0/Run2023B-22Sep2023-v1/NANOAOD', 'Muon0_Run2023B', 'NanoAODv12'])
processes['2023']['pre']['data']['data_mu'].append(['/Muon1/Run2023B-22Sep2023-v1/NANOAOD', 'Muon1_Run2023B', 'NanoAODv12'])
processes['2023']['pre']['data']['data_mu'].append(['/Muon0/Run2023C-22Sep2023_v1-v1/NANOAOD', 'Muon0_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_mu'].append(['/Muon0/Run2023C-22Sep2023_v2-v1/NANOAOD', 'Muon0_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_mu'].append(['/Muon0/Run2023C-22Sep2023_v3-v1/NANOAOD', 'Muon0_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_mu'].append(['/Muon0/Run2023C-22Sep2023_v4-v1/NANOAOD', 'Muon0_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_mu'].append(['/Muon1/Run2023C-22Sep2023_v1-v1/NANOAOD', 'Muon1_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_mu'].append(['/Muon1/Run2023C-22Sep2023_v2-v1/NANOAOD', 'Muon1_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_mu'].append(['/Muon1/Run2023C-22Sep2023_v3-v1/NANOAOD', 'Muon1_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_mu'].append(['/Muon1/Run2023C-22Sep2023_v4-v1/NANOAOD', 'Muon1_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_ele'].append(['/EGamma0/Run2023B-22Sep2023-v1/NANOAOD', 'EGamma0_Run2023B', 'NanoAODv12'])
processes['2023']['pre']['data']['data_ele'].append(['/EGamma0/Run2023B-22Sep2023-v1/NANOAOD', 'EGamma0_Run2023B', 'NanoAODv12'])
processes['2023']['pre']['data']['data_ele'].append(['/EGamma0/Run2023C-22Sep2023_v1-v1/NANOAOD', 'EGamma0_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_ele'].append(['/EGamma0/Run2023C-22Sep2023_v2-v1/NANOAOD', 'EGamma0_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_ele'].append(['/EGamma0/Run2023C-22Sep2023_v3-v1/NANOAOD', 'EGamma0_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_ele'].append(['/EGamma0/Run2023C-22Sep2023_v4-v1/NANOAOD', 'EGamma0_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_ele'].append(['/EGamma1/Run2023C-22Sep2023_v1-v1/NANOAOD', 'EGamma1_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_ele'].append(['/EGamma1/Run2023C-22Sep2023_v2-v1/NANOAOD', 'EGamma1_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_ele'].append(['/EGamma1/Run2023C-22Sep2023_v3-v1/NANOAOD', 'EGamma1_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_ele'].append(['/EGamma1/Run2023C-22Sep2023_v4-v1/NANOAOD', 'EGamma1_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_ele'].append(['/ParkingHH/Run2023C-22Sep2023_v3-v1/NANOAOD', 'ParkingHH_Run2023C', 'NanoAODv12'])
processes['2023']['pre']['data']['data_ele'].append(['/ParkingHH/Run2023C-22Sep2023_v4-v1/NANOAOD', 'ParkingHH_Run2023C', 'NanoAODv12'])

processes['2023']['post']['data']['data_tau'].append(['/Tau/Run2023D-22Sep2023_v1-v1/NANOAOD', 'Tau_Run2023D', 'NanoAODv12'])
processes['2023']['post']['data']['data_tau'].append(['/Tau/Run2023D-22Sep2023_v2-v1/NANOAOD', 'Tau_Run2023D', 'NanoAODv12'])
processes['2023']['post']['data']['data_mu'].append(['/Muon0/Run2023D-22Sep2023_v1-v1/NANOAOD', 'Muon0_Run2023D', 'NanoAODv12'])
processes['2023']['post']['data']['data_mu'].append(['/Muon0/Run2023D-22Sep2023_v2-v1/NANOAOD', 'Muon0_Run2023D', 'NanoAODv12'])
processes['2023']['post']['data']['data_mu'].append(['/Muon1/Run2023D-22Sep2023_v1-v1/NANOAOD', 'Muon1_Run2023D', 'NanoAODv12'])
processes['2023']['post']['data']['data_mu'].append(['/Muon1/Run2023D-22Sep2023_v2-v1/NANOAOD', 'Muon1_Run2023D', 'NanoAODv12'])
processes['2023']['post']['data']['data_ele'].append(['/EGamma0/Run2023D-22Sep2023_v1-v1/NANOAOD', 'EGamma0_Run2023D', 'NanoAODv12'])
processes['2023']['post']['data']['data_ele'].append(['/EGamma0/Run2023D-22Sep2023_v2-v1/NANOAOD', 'EGamma0_Run2023D', 'NanoAODv12'])
processes['2023']['post']['data']['data_ele'].append(['/EGamma1/Run2023D-22Sep2023_v1-v1/NANOAOD', 'EGamma1_Run2023D', 'NanoAODv12'])
processes['2023']['post']['data']['data_ele'].append(['/EGamma1/Run2023D-22Sep2023_v2-v1/NANOAOD', 'EGamma1_Run2023D', 'NanoAODv12'])
processes['2023']['post']['data']['data_phh'].append(['/ParkingHH/Run2023D-22Sep2023_v1-v1/NANOAOD', 'ParkingHH_Run2023D', 'NanoAODv12'])
processes['2023']['post']['data']['data_phh'].append(['/ParkingHH/Run2023D-22Sep2023_v2-v1/NANOAOD', 'ParkingHH_Run2023D', 'NanoAODv12'])

################################################################################################################################################################################################################################################################################################
# DY

processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'DYto2L-2Jets_MLL-10to50', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-10to50_ext1', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'DYto2L-2Jets_MLL-50', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_ext1', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'DYto2L-2Jets_MLL-50_0J', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'DYto2L-2Jets_MLL-50_1J', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'DYto2L-2Jets_MLL-50_2J', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-40to100_1J', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-40to100_2J', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-100to200_1J', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-100to200_2J', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-200to400_1J', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-200to400_2J', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-400to600_1J', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-400to600_2J', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-600_1J', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-600_2J', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-4Jets_MLL-10to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'DYto2L-4Jets_MLL-10to50', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'DYto2L-4Jets_MLL-50', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'DYto2L-4Jets_MLL-50_ext1', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-4Jets_MLL-50_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'DYto2L-4Jets_MLL-50_1J', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-4Jets_MLL-50_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'DYto2L-4Jets_MLL-50_2J', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-4Jets_MLL-50_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'DYto2L-4Jets_MLL-50_3J', 'NanoAODv12'])
processes['2022']['pre']['dy']['dy'].append(['/DYto2L-4Jets_MLL-50_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'DYto2L-4Jets_MLL-50_4J', 'NanoAODv12'])

processes['2022']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'DYto2L-2Jets_MLL-10to50', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM', 'DYto2L-2Jets_MLL-10to50_ext1', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'DYto2L-2Jets_MLL-50', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_ext1', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'DYto2L-2Jets_MLL-50_0J', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'DYto2L-2Jets_MLL-50_1J', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'DYto2L-2Jets_MLL-50_2J', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-40to100_1J', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-100to200_1J', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-100to200_2J', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-200to400_1J', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-200to400_2J', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-400to600_1J', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-400to600_2J', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-600_1J', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-600_2J', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'DYto2L-4Jets_MLL-50', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM', 'DYto2L-4Jets_MLL-50_ext1', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-4Jets_MLL-50_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'DYto2L-4Jets_MLL-50_1J', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-4Jets_MLL-50_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'DYto2L-4Jets_MLL-50_2J', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-4Jets_MLL-50_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'DYto2L-4Jets_MLL-50_3J', 'NanoAODv12'])
processes['2022']['post']['dy']['dy'].append(['/DYto2L-4Jets_MLL-50_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'DYto2L-4Jets_MLL-50_4J', 'NanoAODv12'])

processes['2023']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50', 'NanoAODv12'])
processes['2023']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-40to100_1J', 'NanoAODv12'])
processes['2023']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-40to100_2J', 'NanoAODv12'])
processes['2023']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-100to200_1J', 'NanoAODv12'])
processes['2023']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-100to200_2J', 'NanoAODv12'])
processes['2023']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-200to400_1J', 'NanoAODv12'])
processes['2023']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-200to400_2J', 'NanoAODv12'])
processes['2023']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-400to600_1J', 'NanoAODv12'])
processes['2023']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-400to600_2J', 'NanoAODv12'])
processes['2023']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-600_1J', 'NanoAODv12'])
processes['2023']['pre']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-600_2J', 'NanoAODv12'])
processes['2023']['pre']['dy']['dy'].append(['/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM', 'DYto2L-4Jets_MLL-50', 'NanoAODv12'])

processes['2023']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM', 'DYto2L-2Jets_MLL-50', 'NanoAODv12'])
processes['2023']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-40to100_1J', 'NanoAODv12'])
processes['2023']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-40to100_2J', 'NanoAODv12'])
processes['2023']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-100to200_1J', 'NanoAODv12'])
processes['2023']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-100to200_2J', 'NanoAODv12'])
processes['2023']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-200to400_1J', 'NanoAODv12'])
processes['2023']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-200to400_2J', 'NanoAODv12'])
processes['2023']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-400to600_1J', 'NanoAODv12'])
processes['2023']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-400to600_2J', 'NanoAODv12'])
processes['2023']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-600_1J', 'NanoAODv12'])
processes['2023']['post']['dy']['dy'].append(['/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM', 'DYto2L-2Jets_MLL-50_PTLL-600_2J', 'NanoAODv12'])
processes['2023']['post']['dy']['dy'].append(['/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM', 'DYto2L-4Jets_MLL-50', 'NanoAODv12'])

################################################################################################################################################################################################################################################################################################
# EWK

# processes['2022']['pre']['ewk'].append(['', '', 'NanoAODv12'])
# processes['2022']['post']['ewk'].append(['', '', 'NanoAODv12'])

################################################################################################################################################################################################################################################################################################
# W+JETS

processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'WtoLNu-2Jets', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'WtoLNu-2Jets_1J', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'WtoLNu-2Jets_2J', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-40to100_1J', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-40to100_2J', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-100to200_1J', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-100to200_2J', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-200to400_1J', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-200to400_2J', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-400to600_1J', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-400to600_2J', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-600_1J', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-600_2J', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'WtoLNu-4Jets', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'WtoLNu-4Jets_ext1', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-4Jets_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'WtoLNu-4Jets_1J', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-4Jets_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM', 'WtoLNu-4Jets_2J', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-4Jets_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'WtoLNu-4Jets_3J', 'NanoAODv12'])
processes['2022']['pre']['others']['wjets'].append(['/WtoLNu-4Jets_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'WtoLNu-4Jets_4J', 'NanoAODv12'])

processes['2022']['post']['others']['wjets'].append(['/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'WtoLNu-2Jets', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM', 'WtoLNu-2Jets_0J', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'WtoLNu-2Jets_1J', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'WtoLNu-2Jets_2J', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-40to100_1J', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-40to100_2J', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-100to200_1J', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-200to400_1J', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-400to600_1J', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-400to600_2J', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-600_1J', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-2Jets_PTLNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM', 'WtoLNu-2Jets_PTLNu-600_2J', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'WtoLNu-4Jets', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM', 'WtoLNu-4Jets_ext1', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-4Jets_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'WtoLNu-4Jets_1J', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-4Jets_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'WtoLNu-4Jets_2J', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-4Jets_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'WtoLNu-4Jets_3J', 'NanoAODv12'])
processes['2022']['post']['others']['wjets'].append(['/WtoLNu-4Jets_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'WtoLNu-4Jets_4J', 'NanoAODv12'])

processes['2023']['pre']['others']['wjets'].append(['/WtoLNu-4Jets_MLNu-120to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v5/NANOAODSIM', 'WtoLNu-4Jets_MLNu-120to200', 'NanoAODv12'])
processes['2023']['pre']['others']['wjets'].append(['/WtoLNu-4Jets_MLNu-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v5/NANOAODSIM', 'WtoLNu-4Jets_MLNu-200to400', 'NanoAODv12'])
processes['2023']['pre']['others']['wjets'].append(['/WtoLNu-4Jets_MLNu-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v4/NANOAODSIM', 'WtoLNu-4Jets_MLNu-400to800', 'NanoAODv12'])
processes['2023']['pre']['others']['wjets'].append(['/WtoLNu-4Jets_MLNu-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v4/NANOAODSIM', 'WtoLNu-4Jets_MLNu-800to1500', 'NanoAODv12'])
processes['2023']['pre']['others']['wjets'].append(['/WtoLNu-4Jets_MLNu-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM', 'WtoLNu-4Jets_MLNu-1500to2500', 'NanoAODv12'])
processes['2023']['pre']['others']['wjets'].append(['/WtoLNu-4Jets_MLNu-2500to4000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v5/NANOAODSIM', 'WtoLNu-4Jets_MLNu-2500to4000', 'NanoAODv12'])
processes['2023']['pre']['others']['wjets'].append(['/WtoLNu-4Jets_MLNu-4000to6000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v5/NANOAODSIM', 'WtoLNu-4Jets_MLNu-4000to6000', 'NanoAODv12'])
processes['2023']['pre']['others']['wjets'].append(['/WtoLNu-4Jets_MLNu-6000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v4/NANOAODSIM', 'WtoLNu-4Jets_MLNu-6000', 'NanoAODv12'])

processes['2023']['post']['others']['wjets'].append(['/WtoLNu-4Jets_MLNu-120to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM', 'WtoLNu-4Jets_MLNu-120to200', 'NanoAODv12'])
processes['2023']['post']['others']['wjets'].append(['/WtoLNu-4Jets_MLNu-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM', 'WtoLNu-4Jets_MLNu-200to400', 'NanoAODv12'])
processes['2023']['post']['others']['wjets'].append(['/WtoLNu-4Jets_MLNu-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v5/NANOAODSIM', 'WtoLNu-4Jets_MLNu-400to800', 'NanoAODv12'])
processes['2023']['post']['others']['wjets'].append(['/WtoLNu-4Jets_MLNu-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM', 'WtoLNu-4Jets_MLNu-800to1500', 'NanoAODv12'])
processes['2023']['post']['others']['wjets'].append(['/WtoLNu-4Jets_MLNu-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM', 'WtoLNu-4Jets_MLNu-1500to2500', 'NanoAODv12'])
processes['2023']['post']['others']['wjets'].append(['/WtoLNu-4Jets_MLNu-2500to4000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v5/NANOAODSIM', 'WtoLNu-4Jets_MLNu-2500to4000', 'NanoAODv12'])
processes['2023']['post']['others']['wjets'].append(['/WtoLNu-4Jets_MLNu-4000to6000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM', 'WtoLNu-4Jets_MLNu-4000to6000', 'NanoAODv12'])
processes['2023']['post']['others']['wjets'].append(['/WtoLNu-4Jets_MLNu-6000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v5/NANOAODSIM', 'WtoLNu-4Jets_MLNu-6000', 'NanoAODv12'])

################################################################################################################################################################################################################################################################################################
# TT

processes['2022']['pre']['ttbar']['ttbar'].append(['/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TTto2L2Nu', 'NanoAODv12'])
processes['2022']['pre']['ttbar']['ttbar'].append(['/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'TTto2L2Nu_ext1', 'NanoAODv12'])
processes['2022']['pre']['ttbar']['ttbar'].append(['/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TTtoLNu2Q', 'NanoAODv12'])
processes['2022']['pre']['ttbar']['ttbar'].append(['/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'TTtoLNu2Q_ext1', 'NanoAODv12'])
processes['2022']['pre']['ttbar']['ttbar'].append(['/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TTto4Q', 'NanoAODv12'])
processes['2022']['pre']['ttbar']['ttbar'].append(['/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'TTto4Q_ext1', 'NanoAODv12'])

processes['2022']['post']['ttbar']['ttbar'].append(['/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'TTto2L2Nu', 'NanoAODv12'])
processes['2022']['post']['ttbar']['ttbar'].append(['/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM', 'TTto2L2Nu_ext1', 'NanoAODv12'])
processes['2022']['post']['ttbar']['ttbar'].append(['/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'TTtoLNu2Q', 'NanoAODv12'])
processes['2022']['post']['ttbar']['ttbar'].append(['/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM', 'TTtoLNu2Q_ext1', 'NanoAODv12'])
processes['2022']['post']['ttbar']['ttbar'].append(['/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'TTto4Q', 'NanoAODv12'])
processes['2022']['post']['ttbar']['ttbar'].append(['/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM', 'TTto4Q_ext1', 'NanoAODv12'])

processes['2023']['pre']['ttbar']['ttbar'].append(['/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM', 'TTto2L2Nu', 'NanoAODv12'])
processes['2023']['pre']['ttbar']['ttbar'].append(['/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM', 'TTtoLNu2Q', 'NanoAODv12'])
processes['2023']['pre']['ttbar']['ttbar'].append(['/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM', 'TTto4Q', 'NanoAODv12'])

processes['2023']['post']['ttbar']['ttbar'].append(['/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM', 'TTto2L2Nu', 'NanoAODv12'])
processes['2023']['post']['ttbar']['ttbar'].append(['/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM', 'TTtoLNu2Q', 'NanoAODv12'])
processes['2023']['post']['ttbar']['ttbar'].append(['/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM', 'TTto4Q', 'NanoAODv12'])

################################################################################################################################################################################################################################################################################################
# TT+X

processes['2022']['pre']['others']['ttx'].append(['/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM', 'TTHto2B', 'NanoAODv12'])
processes['2022']['pre']['others']['ttx'].append(['/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM', 'TTHtoNon2B', 'NanoAODv12'])
processes['2022']['pre']['others']['ttx'].append(['/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TTWH', 'NanoAODv12'])
processes['2022']['pre']['others']['ttx'].append(['/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TTWW', 'NanoAODv12'])
processes['2022']['pre']['others']['ttx'].append(['/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TTZH', 'NanoAODv12'])
processes['2022']['pre']['others']['ttx'].append(['/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TTZZ', 'NanoAODv12'])

processes['2022']['post']['others']['ttx'].append(['/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM', 'TTHto2B', 'NanoAODv12'])
processes['2022']['post']['others']['ttx'].append(['/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'TTHtoNon2B', 'NanoAODv12'])
processes['2022']['post']['others']['ttx'].append(['/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'TTWH', 'NanoAODv12'])
processes['2022']['post']['others']['ttx'].append(['/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'TTWW', 'NanoAODv12'])
processes['2022']['post']['others']['ttx'].append(['/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM', 'TTZH', 'NanoAODv12'])
processes['2022']['post']['others']['ttx'].append(['/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM', 'TTZZ', 'NanoAODv12'])

################################################################################################################################################################################################################################################################################################
# SINGLE T

processes['2022']['pre']['others']['singletop'].append(['/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TWminusto2L2Nu', 'NanoAODv12'])
processes['2022']['pre']['others']['singletop'].append(['/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'TWminusto2L2Nu_ext1', 'NanoAODv12'])
processes['2022']['pre']['others']['singletop'].append(['/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TWminustoLNu2Q', 'NanoAODv12'])
processes['2022']['pre']['others']['singletop'].append(['/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'TWminustoLNu2Q_ext1', 'NanoAODv12'])
processes['2022']['pre']['others']['singletop'].append(['/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TWminusto4Q', 'NanoAODv12'])
processes['2022']['pre']['others']['singletop'].append(['/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'TWminusto4Q_ext1', 'NanoAODv12'])
processes['2022']['pre']['others']['singletop'].append(['/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TbarWplusto2L2Nu', 'NanoAODv12'])
processes['2022']['pre']['others']['singletop'].append(['/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'TbarWplusto2L2Nu_ext1', 'NanoAODv12'])
processes['2022']['pre']['others']['singletop'].append(['/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TbarWplustoLNu2Q', 'NanoAODv12'])
processes['2022']['pre']['others']['singletop'].append(['/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'TbarWplustoLNu2Q_ext1', 'NanoAODv12'])
processes['2022']['pre']['others']['singletop'].append(['/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TbarWplusto4Q', 'NanoAODv12'])
processes['2022']['pre']['others']['singletop'].append(['/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'TbarWplusto4Q_ext1', 'NanoAODv12'])
processes['2022']['pre']['others']['singletop'].append(['/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TBbarQ_t-channel', 'NanoAODv12'])
processes['2022']['pre']['others']['singletop'].append(['/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TbarBQ_t-channel', 'NanoAODv12'])
processes['2022']['pre']['others']['singletop'].append(['/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TBbartoLplusNuBbar-s-channel', 'NanoAODv12'])
processes['2022']['pre']['others']['singletop'].append(['/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'TbarBtoLminusNuB-s-channel', 'NanoAODv12'])

processes['2022']['post']['others']['singletop'].append(['/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','TWminusto2L2Nu', 'NanoAODv12'])
processes['2022']['post']['others']['singletop'].append(['/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM','TWminusto2L2Nu_ext1', 'NanoAODv12'])
processes['2022']['post']['others']['singletop'].append(['/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','TWminustoLNu2Q', 'NanoAODv12'])
processes['2022']['post']['others']['singletop'].append(['/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM','TWminustoLNu2Q_ext1', 'NanoAODv12'])
processes['2022']['post']['others']['singletop'].append(['/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','TWminusto4Q', 'NanoAODv12'])
processes['2022']['post']['others']['singletop'].append(['/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM','TWminusto4Q_ext1', 'NanoAODv12'])
processes['2022']['post']['others']['singletop'].append(['/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','TbarWplusto2L2Nu', 'NanoAODv12'])
processes['2022']['post']['others']['singletop'].append(['/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM','TbarWplusto2L2Nu_ext1', 'NanoAODv12'])
processes['2022']['post']['others']['singletop'].append(['/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','TbarWplustoLNu2Q', 'NanoAODv12'])
processes['2022']['post']['others']['singletop'].append(['/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM','TbarWplustoLNu2Q_ext1', 'NanoAODv12'])
processes['2022']['post']['others']['singletop'].append(['/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','TbarWplusto4Q', 'NanoAODv12'])
processes['2022']['post']['others']['singletop'].append(['/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM','TbarWplusto4Q_ext1', 'NanoAODv12'])
processes['2022']['post']['others']['singletop'].append(['/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','TBbarQ_t-channel', 'NanoAODv12'])
processes['2022']['post']['others']['singletop'].append(['/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','TbarBQ_t-channel', 'NanoAODv12'])
processes['2022']['post']['others']['singletop'].append(['/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','TBbartoLplusNuBbar-s-channel', 'NanoAODv12'])
processes['2022']['post']['others']['singletop'].append(['/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','TbarBtoLminusNuB-s-channel', 'NanoAODv12'])

processes['2023']['pre']['others']['singletop'].append(['/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM', 'TWminusto2L2Nu', 'NanoAODv12'])
processes['2023']['pre']['others']['singletop'].append(['/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM', 'TWminustoLNu2Q', 'NanoAODv12'])
processes['2023']['pre']['others']['singletop'].append(['/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM', 'TWminusto4Q', 'NanoAODv12'])

processes['2023']['post']['others']['singletop'].append(['/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM', 'TWminusto2L2Nu', 'NanoAODv12'])
processes['2023']['post']['others']['singletop'].append(['/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM', 'TWminustoLNu2Q', 'NanoAODv12'])
processes['2023']['post']['others']['singletop'].append(['/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM', 'TWminusto4Q', 'NanoAODv12'])

################################################################################################################################################################################################################################################################################################
# MULTI-BOSON

processes['2022']['pre']['others']['multiboson'].append(['/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'WWto2L2Nu', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'WWto2L2Nu_ext1', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'WWtoLNu2Q', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'WWtoLNu2Q_ext1', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'WWto4Q', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'WWto4Q_ext1', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/ZZto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'ZZto2L2Nu', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/ZZto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'ZZto2L2Nu_ext1', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'ZZto2L2Q', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'ZZto2L2Q_ext1', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/ZZto2Nu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'ZZto2Nu2Q', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/ZZto2Nu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'ZZto2Nu2Q_ext1', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'ZZto4L', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'ZZto4L_ext1', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'WWW', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'WWZ', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'WZZ', 'NanoAODv12'])
processes['2022']['pre']['others']['multiboson'].append(['/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'ZZZ', 'NanoAODv12'])

processes['2022']['post']['others']['multiboson'].append(['/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'WWto2L2Nu', 'NanoAODv12'])
processes['2022']['post']['others']['multiboson'].append(['/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM', 'WWto2L2Nu_ext1', 'NanoAODv12'])
processes['2022']['post']['others']['multiboson'].append(['/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'WWtoLNu2Q', 'NanoAODv12'])
processes['2022']['post']['others']['multiboson'].append(['/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM', 'WWtoLNu2Q_ext1', 'NanoAODv12'])
processes['2022']['post']['others']['multiboson'].append(['/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'WWto4Q', 'NanoAODv12'])
processes['2022']['post']['others']['multiboson'].append(['/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM', 'WWto4Q_ext1', 'NanoAODv12'])
processes['2022']['post']['others']['multiboson'].append(['/ZZto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'ZZto2L2Nu', 'NanoAODv12'])
processes['2022']['post']['others']['multiboson'].append(['/ZZto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM', 'ZZto2L2Nu_ext1', 'NanoAODv12'])
processes['2022']['post']['others']['multiboson'].append(['/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'ZZto2L2Q', 'NanoAODv12'])
processes['2022']['post']['others']['multiboson'].append(['/ZZto2Nu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'ZZto2Nu2Q', 'NanoAODv12'])
processes['2022']['post']['others']['multiboson'].append(['/ZZto2Nu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM', 'ZZto2Nu2Q_ext1', 'NanoAODv12'])
processes['2022']['post']['others']['multiboson'].append(['/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'ZZto4L', 'NanoAODv12'])
processes['2022']['post']['others']['multiboson'].append(['/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM', 'ZZto4L_ext1', 'NanoAODv12'])
processes['2022']['post']['others']['multiboson'].append(['/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'WWW', 'NanoAODv12'])
processes['2022']['post']['others']['multiboson'].append(['/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'WWZ', 'NanoAODv12'])
processes['2022']['post']['others']['multiboson'].append(['/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'WZZ', 'NanoAODv12'])
processes['2022']['post']['others']['multiboson'].append(['/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'ZZZ', 'NanoAODv12'])

processes['2023']['pre']['others']['multiboson'].append(['/WW_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM', 'WW', 'NanoAODv12'])
processes['2023']['pre']['others']['multiboson'].append(['/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM', 'WWtoLNu2Q', 'NanoAODv12'])
processes['2023']['pre']['others']['multiboson'].append(['/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM', 'ZZ', 'NanoAODv12'])
processes['2023']['pre']['others']['multiboson'].append(['/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM', 'WWW', 'NanoAODv12'])
processes['2023']['pre']['others']['multiboson'].append(['/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM', 'WWZ', 'NanoAODv12'])
processes['2023']['pre']['others']['multiboson'].append(['/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM', 'WZZ', 'NanoAODv12'])
processes['2023']['pre']['others']['multiboson'].append(['/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM', 'ZZZ', 'NanoAODv12'])

processes['2023']['post']['others']['multiboson'].append(['/WW_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM', 'WW', 'NanoAODv12'])
processes['2023']['post']['others']['multiboson'].append(['/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM', 'WWtoLNu2Q', 'NanoAODv12'])
processes['2023']['post']['others']['multiboson'].append(['/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM', 'WWto4Q', 'NanoAODv12'])
processes['2023']['post']['others']['multiboson'].append(['/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM', 'ZZ', 'NanoAODv12'])
processes['2023']['post']['others']['multiboson'].append(['/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM', 'WWW', 'NanoAODv12'])
processes['2023']['post']['others']['multiboson'].append(['/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM', 'WWZ', 'NanoAODv12'])
processes['2023']['post']['others']['multiboson'].append(['/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM', 'WZZ', 'NanoAODv12'])
processes['2023']['post']['others']['multiboson'].append(['/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM', 'ZZZ', 'NanoAODv12'])

################################################################################################################################################################################################################################################################################################
# VH

processes['2022']['pre']['singleh']['vh'].append(['/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'ZH_Hto2B_Zto2L', 'NanoAODv12'])
processes['2022']['pre']['singleh']['vh'].append(['/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'ZH_Hto2B_Zto2L_ext1', 'NanoAODv12'])
processes['2022']['pre']['singleh']['vh'].append(['/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'ZH_Hto2B_Zto2Q', 'NanoAODv12'])
processes['2022']['pre']['singleh']['vh'].append(['/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM', 'ZH_Hto2B_Zto2Q_ext1', 'NanoAODv12'])
processes['2022']['pre']['singleh']['vh'].append(['/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'WminusH_Hto2B_Wto2Q', 'NanoAODv12'])
processes['2022']['pre']['singleh']['vh'].append(['/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'WminusH_Hto2B_Wto2Q_ext1', 'NanoAODv12'])
processes['2022']['pre']['singleh']['vh'].append(['/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'WminusH_Hto2B_WtoLNu', 'NanoAODv12'])
processes['2022']['pre']['singleh']['vh'].append(['/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'WminusH_Hto2B_WtoLNu_ext1', 'NanoAODv12'])
processes['2022']['pre']['singleh']['vh'].append(['/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'WplusH_Hto2B_Wto2Q', 'NanoAODv12'])
processes['2022']['pre']['singleh']['vh'].append(['/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'WplusH_Hto2B_Wto2Q_ext1', 'NanoAODv12'])
processes['2022']['pre']['singleh']['vh'].append(['/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'WplusH_Hto2B_WtoLNu', 'NanoAODv12'])
processes['2022']['pre']['singleh']['vh'].append(['/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM', 'WplusH_Hto2B_WtoLNu_ext1', 'NanoAODv12'])
processes['2022']['pre']['singleh']['vh'].append(['/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'ggZH_Hto2B_Zto2L', 'NanoAODv12'])
processes['2022']['pre']['singleh']['vh'].append(['/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM', 'ggZH_Hto2B_Zto2L_ext1', 'NanoAODv12'])
processes['2022']['pre']['singleh']['vh'].append(['/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'ggZH_Hto2B_Zto2Q', 'NanoAODv12'])
processes['2022']['pre']['singleh']['vh'].append(['/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM', 'ggZH_Hto2B_Zto2Q_ext1', 'NanoAODv12'])

processes['2022']['post']['singleh']['vh'].append(['/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','ZH_Hto2B_Zto2L', 'NanoAODv12'])
processes['2022']['post']['singleh']['vh'].append(['/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM','ZH_Hto2B_Zto2L_ext1', 'NanoAODv12'])
processes['2022']['post']['singleh']['vh'].append(['/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','ZH_Hto2B_Zto2Q', 'NanoAODv12'])
processes['2022']['post']['singleh']['vh'].append(['/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','WminusH_Hto2B_Wto2Q', 'NanoAODv12'])
processes['2022']['post']['singleh']['vh'].append(['/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM','WminusH_Hto2B_Wto2Q_ext1', 'NanoAODv12'])
processes['2022']['post']['singleh']['vh'].append(['/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','WminusH_Hto2B_WtoLNu', 'NanoAODv12'])
processes['2022']['post']['singleh']['vh'].append(['/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM','WminusH_Hto2B_WtoLNu_ext1', 'NanoAODv12'])
processes['2022']['post']['singleh']['vh'].append(['/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','WplusH_Hto2B_Wto2Q', 'NanoAODv12'])
processes['2022']['post']['singleh']['vh'].append(['/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM','WplusH_Hto2B_Wto2Q_ext1', 'NanoAODv12'])
processes['2022']['post']['singleh']['vh'].append(['/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','WplusH_Hto2B_WtoLNu', 'NanoAODv12'])
processes['2022']['post']['singleh']['vh'].append(['/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM','WplusH_Hto2B_WtoLNu_ext1', 'NanoAODv12'])
processes['2022']['post']['singleh']['vh'].append(['/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','ggZH_Hto2B_Zto2L', 'NanoAODv12'])
processes['2022']['post']['singleh']['vh'].append(['/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM','ggZH_Hto2B_Zto2L_ext1', 'NanoAODv12'])
processes['2022']['post']['singleh']['vh'].append(['/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','ggZH_Hto2B_Zto2Q', 'NanoAODv12'])
processes['2022']['post']['singleh']['vh'].append(['/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM','ggZH_Hto2B_Zto2Q_ext1', 'NanoAODv12'])

################################################################################################################################################################################################################################################################################################
# SINGLE H

processes['2022']['pre']['singleh']['fusionh'].append(['/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM','GluGluHToTauTau', 'NanoAODv12'])
processes['2022']['pre']['singleh']['fusionh'].append(['/GluGluHto2B_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM','GluGluHto2B', 'NanoAODv12'])
processes['2022']['pre']['singleh']['fusionh'].append(['/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM','VBFHToTauTau', 'NanoAODv12'])
processes['2022']['pre']['singleh']['fusionh'].append(['/VBFHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM','VBFHto2B', 'NanoAODv12'])

processes['2022']['post']['singleh']['fusionh'].append(['/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson70KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','GluGluHToTauTau', 'NanoAODv12'])
processes['2022']['post']['singleh']['fusionh'].append(['/GluGluHto2B_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','GluGluHto2B', 'NanoAODv12'])
processes['2022']['post']['singleh']['fusionh'].append(['/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson70KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM','VBFHToTauTau', 'NanoAODv12'])
processes['2022']['post']['singleh']['fusionh'].append(['/VBFHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM','VBFHto2B', 'NanoAODv12'])

processes['2023']['post']['singleh']['fusionh'].append(['/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM', 'GluGluHToTauTau', 'NanoAODv12'])
processes['2023']['post']['singleh']['fusionh'].append(['/GluGluHToBB_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM', 'GluGluHToBB', 'NanoAODv12'])
processes['2023']['post']['singleh']['fusionh'].append(['/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM', 'VBFHToTauTau', 'NanoAODv12'])
processes['2023']['post']['singleh']['fusionh'].append(['/VBFHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-KeepRAW_130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM', 'VBFHto2B', 'NanoAODv12'])

################################################################################################################################################################################################################################################################################################
# NON-RESONANT SIGNALS

processes['2022']['pre']['qqhh']['VBFHHto2B2Tau_CV-1_C2V-1_C3-1'].append(['/VBFHHto2B2Tau_CV-1_C2V-1_C3-1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-1_C2V-1_C3-1', 'NanoAODv12'])
processes['2022']['pre']['qqhh']['VBFHHto2B2Tau_CV-1_C2V-1_C3-2'].append(['/VBFHHto2B2Tau_CV-1_C2V-1_C3-2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-1_C2V-1_C3-2', 'NanoAODv12'])
processes['2022']['pre']['qqhh']['VBFHHto2B2Tau_CV-1_C2V-2_C3-1'].append(['/VBFHHto2B2Tau_CV-1_C2V-2_C3-1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-1_C2V-2_C3-1', 'NanoAODv12'])
processes['2022']['pre']['qqhh']['VBFHHto2B2Tau_CV-1p74_C2V-1p37_C3-14p4'].append(['/VBFHHto2B2Tau_CV-1p74_C2V-1p37_C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-1p74_C2V-1p37_C3-14p4', 'NanoAODv12'])
processes['2022']['pre']['qqhh']['VBFHHto2B2Tau_CV-m0p012_C2V-0p030_C3-10p2'].append(['/VBFHHto2B2Tau_CV-m0p012_C2V-0p030_C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-m0p012_C2V-0p030_C3-10p2', 'NanoAODv12'])
processes['2022']['pre']['qqhh']['VBFHHto2B2Tau_CV-m0p758_C2V-1p44_C3-m19p3'].append(['/VBFHHto2B2Tau_CV-m0p758_C2V-1p44_C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-m0p758_C2V-1p44_C3-m19p3', 'NanoAODv12'])
processes['2022']['pre']['qqhh']['VBFHHto2B2Tau_CV-m0p962_C2V-0p959_C3-m1p43'].append(['/VBFHHto2B2Tau_CV-m0p962_C2V-0p959_C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-m0p962_C2V-0p959_C3-m1p43', 'NanoAODv12'])
processes['2022']['pre']['qqhh']['VBFHHto2B2Tau_CV-m1p21_C2V-1p94_C3-m0p94'].append(['/VBFHHto2B2Tau_CV-m1p21_C2V-1p94_C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-m1p21_C2V-1p94_C3-m0p94', 'NanoAODv12'])
processes['2022']['pre']['qqhh']['VBFHHto2B2Tau_CV-m1p60_C2V-2p72_C3-m1p36'].append(['/VBFHHto2B2Tau_CV-m1p60_C2V-2p72_C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-m1p60_C2V-2p72_C3-m1p36', 'NanoAODv12'])
processes['2022']['pre']['qqhh']['VBFHHto2B2Tau_CV-m1p83_C2V-3p57_C3-m3p39'].append(['/VBFHHto2B2Tau_CV-m1p83_C2V-3p57_C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-m1p83_C2V-3p57_C3-m3p39', 'NanoAODv12'])
processes['2022']['pre']['qqhh']['VBFHHto2B2Tau_CV-m2p12_C2V-3p87_C3-m5p96'].append(['/VBFHHto2B2Tau_CV-m2p12_C2V-3p87_C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-m2p12_C2V-3p87_C3-m5p96', 'NanoAODv12'])
processes['2022']['pre']['gghh']['GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00'].append(['/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00', 'NanoAODv12'])
processes['2022']['pre']['gghh']['GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00'].append(['/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00', 'NanoAODv12'])
processes['2022']['pre']['gghh']['GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00'].append(['/GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00', 'NanoAODv12'])
processes['2022']['pre']['gghh']['GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00'].append(['/GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00', 'NanoAODv12'])
processes['2022']['pre']['gghh']['GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00'].append(['/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00', 'NanoAODv12'])
processes['2022']['pre']['gghh']['GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p10'].append(['/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p10_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p10', 'NanoAODv12'])
processes['2022']['pre']['gghh']['GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p35'].append(['/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p35_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p35', 'NanoAODv12'])
processes['2022']['pre']['gghh']['GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-3p00'].append(['/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-3p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-3p00', 'NanoAODv12'])
processes['2022']['pre']['gghh']['GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-m2p00'].append(['/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-m2p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-m2p00', 'NanoAODv12'])

processes['2022']['post']['qqhh']['VBFHHto2B2Tau_CV-1_C2V-1_C3-1'].append(['/VBFHHto2B2Tau_CV-1_C2V-1_C3-1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-1_C2V-1_C3-1', 'NanoAODv12'])
processes['2022']['post']['qqhh']['VBFHHto2B2Tau_CV-1_C2V-1_C3-1'].append(['/VBFHHto2B2Tau_CV-1_C2V-1_C3-1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-Poisson70KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-1_C2V-1_C3-1', 'NanoAODv12'])
processes['2022']['post']['qqhh']['VBFHHto2B2Tau_CV-1_C2V-1_C3-2'].append(['/VBFHHto2B2Tau_CV-1_C2V-1_C3-2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-1_C2V-1_C3-2', 'NanoAODv12'])
processes['2022']['post']['qqhh']['VBFHHto2B2Tau_CV-1_C2V-2_C3-1'].append(['/VBFHHto2B2Tau_CV-1_C2V-2_C3-1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-1_C2V-2_C3-1', 'NanoAODv12'])
processes['2022']['post']['qqhh']['VBFHHto2B2Tau_CV-1p74_C2V-1p37_C3-14p4'].append(['/VBFHHto2B2Tau_CV-1p74_C2V-1p37_C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-1p74_C2V-1p37_C3-14p4', 'NanoAODv12'])
processes['2022']['post']['qqhh']['VBFHHto2B2Tau_CV-m0p012_C2V-0p030_C3-10p2'].append(['/VBFHHto2B2Tau_CV-m0p012_C2V-0p030_C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-m0p012_C2V-0p030_C3-10p2', 'NanoAODv12'])
processes['2022']['post']['qqhh']['VBFHHto2B2Tau_CV-m0p758_C2V-1p44_C3-m19p3'].append(['/VBFHHto2B2Tau_CV-m0p758_C2V-1p44_C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-m0p758_C2V-1p44_C3-m19p3', 'NanoAODv12'])
processes['2022']['post']['qqhh']['VBFHHto2B2Tau_CV-m0p962_C2V-0p959_C3-m1p43'].append(['/VBFHHto2B2Tau_CV-m0p962_C2V-0p959_C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-m0p962_C2V-0p959_C3-m1p43', 'NanoAODv12'])
processes['2022']['post']['qqhh']['VBFHHto2B2Tau_CV-m1p21_C2V-1p94_C3-m0p94'].append(['/VBFHHto2B2Tau_CV-m1p21_C2V-1p94_C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-m1p21_C2V-1p94_C3-m0p94', 'NanoAODv12'])
processes['2022']['post']['qqhh']['VBFHHto2B2Tau_CV-m1p60_C2V-2p72_C3-m1p36'].append(['/VBFHHto2B2Tau_CV-m1p60_C2V-2p72_C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-m1p60_C2V-2p72_C3-m1p36', 'NanoAODv12'])
processes['2022']['post']['qqhh']['VBFHHto2B2Tau_CV-m1p83_C2V-3p57_C3-m3p39'].append(['/VBFHHto2B2Tau_CV-m1p83_C2V-3p57_C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-m1p83_C2V-3p57_C3-m3p39', 'NanoAODv12'])
processes['2022']['post']['qqhh']['VBFHHto2B2Tau_CV-m2p12_C2V-3p87_C3-m5p96'].append(['/VBFHHto2B2Tau_CV-m2p12_C2V-3p87_C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'VBFHHto2B2Tau_CV-m2p12_C2V-3p87_C3-m5p96', 'NanoAODv12'])
processes['2022']['post']['gghh']['GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00'].append(['/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00', 'NanoAODv12'])
processes['2022']['post']['gghh']['GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00'].append(['/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00', 'NanoAODv12'])
processes['2022']['post']['gghh']['GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00'].append(['/GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00', 'NanoAODv12'])
processes['2022']['post']['gghh']['GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00'].append(['/GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00', 'NanoAODv12'])
processes['2022']['post']['gghh']['GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00'].append(['/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00', 'NanoAODv12'])
processes['2022']['post']['gghh']['GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p10'].append(['/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p10_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p10', 'NanoAODv12'])
processes['2022']['post']['gghh']['GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p35'].append(['/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p35_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p35', 'NanoAODv12'])
processes['2022']['post']['gghh']['GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-3p00'].append(['/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-3p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-3p00', 'NanoAODv12'])
processes['2022']['post']['gghh']['GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-m2p00'].append(['/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-m2p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM', 'GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-m2p00', 'NanoAODv12'])

################################################################################################################################################################################################################################################################################################
# RESONANT SIGNALS

# processes['2022']['pre']['hhbbtautau_resonant'].append(['', '', 'NanoAODv12'])
# processes['2022']['post']['hhbbtautau_resonant'].append(['', '', 'NanoAODv12'])

################################################################################################################################################################################################################################################################################################
################################################################################################################################################################################################################################################################################################
# HERE WE ACTUALLY DO SOMETHING

issue = ''
if year == '2022': issue = 'EE'
if year == '2023': issue = 'BPix'

file_path = 'run3_dataset_'+year+'_'+pre_post+issue+'.py'
os.system('rm '+file_path)
os.system('touch '+file_path)

with open(file_path, 'a') as f:
    f.write('from analysis_tools import ObjectCollection, Category, Process, Dataset, Feature, Systematic\n')
    f.write('from analysis_tools.utils import DotDict\n')
    f.write('from analysis_tools.utils import join_root_selection as jrs\n')
    f.write('from plotting_tools import Label\n')
    f.write('from collections import OrderedDict\n\n')
    f.write('from cmt.config.base_config import Config as cmt_base_config\n\n')

    f.write('class Datasets_'+year+'_'+pre_post+issue+'(cmt_base_config):\n')
    f.write('\tdef __init__(self, *args, **kwargs):\n')
    f.write('\t\tsuper(Datasets_'+year+'_'+pre_post+issue+', self).__init__(*args, **kwargs)\n\n')
    f.write('\tdef add_datasets(self):\n')
    f.write('\t\tdatasets = [\n')
      
    for proc_group in processes[year][pre_post]:
        # if 'data' not in proc_group: break

        for proc in processes[year][pre_post][proc_group].keys():
            for das in processes[year][pre_post][proc_group][proc]:
                if len(das) == 0: continue

                f.write('\t\t\tDataset("'+das[1]+'",\n')
                f.write('\t\t\t\t\tdataset="'+das[0]+'",\n')
                f.write('\t\t\t\t\tprocess=self.processes.get("'+das[1]+'"),\n')
                if 'data' in proc_group: f.write('\t\t\t\t\trunEra="'+das[1][-1]+'",\n')
                else:                    f.write('\t\t\t\t\txs=1.0,\n')
                
                f.write('\t\t\t\t\ttags=["'+das[2]+'"]),\n\n')
    
    f.write('\t\t]\n')
    f.write('\t\treturn ObjectCollection(datasets)\n')


print('File run3_dataset_'+year+'_'+pre_post+issue+'.py successfully produced')
print('Please add the following lines to the base_config in order to have processes succesfully initialized')

for proc_group in processes[year][pre_post]:
    # if 'data' not in proc_group: break

    string = '\nProcess("'+proc_group+'", Label("'+proc_group+'"), color=('+str(colors[proc_group][0])+', '+str(colors[proc_group][1])+', '+str(colors[proc_group][2])+')'

    if 'data' in proc_group:
        string = string + ', isData=True),'
    elif 'HHto2B2Tau' in proc_group:
        string = string + ', isSignal=True),'
    else:
        string = string + '),'

    print(string)

    for proc in processes[year][pre_post][proc_group].keys():
        for das in processes[year][pre_post][proc_group][proc]:
            if len(das) == 0: continue

            string = 'Process("'+das[1]+'", Label("'+das[1]+'"), color=('+str(colors[proc][0])+', '+str(colors[proc][1])+', '+str(colors[proc][2])+'), parent_process="'+proc_group+'"'

            if 'data' in proc:
                string = string + ', isData=True),'
            elif 'HHto2B2Tau' in proc:
                string = string + ', isSignal=True),'
            else:
                string = string + '),'

            print(string)