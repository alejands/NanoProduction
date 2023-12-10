from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'TTto2L2Nu_Run3Summer22NanoAODv12-130X_DeepMET'
config.General.workArea = 'jobs'
config.General.transferLogs = True
config.General.instance = 'prod'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'deepmet_NanoAODv12_130X_cfg.py'
config.JobType.maxMemoryMB = 5000
config.JobType.numCores = 4

config.Data.inputDataset = '/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'
config.Data.outputDatasetTag = 'Run3Summer22NanoAODv12-130X_DeepMET'
config.Data.splitting = 'Automatic'
config.Data.totalUnits = 1200000
config.Data.outLFNDirBase = '/store/user/alejands/deepmet'

config.Site.storageSite = 'T3_US_CMU'
