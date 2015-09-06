import FWCore.ParameterSet.Config as cms

process = cms.Process("MillePedeFileConverter")

process.load("FWCore.MessageService.MessageLogger_cfi")

# This is just a test configuration. It should not be loaded directly in any
# other configuration.
# The filenames below are just suggestions.
# To get all info about this module, type:
# edmPluginHelp -p MillePedeFileConverter

# Using the normal standard messagelogger, with its standard configuration,
# but setting the category of messages to MillePedeFileActions
process.MessageLogger = process.MessageLogger.clone(
        categories = cms.untracked.vstring('MillePedeFileActions'),
        )

# Limit our test to 5 events (we work on run level anyway)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(5) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        "file:step1.root"
    )
)

# Loading the autogenerated millePedeFileConverter_cfi:
from Alignment.MillePedeAlignmentAlgorithm.millePedeFileConverter_cfi import millePedeFileConverter
process.testMillePedeFileConverter = millePedeFileConverter.clone()

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)

process.p = cms.Path(process.testMillePedeFileConverter)

process.e = cms.EndPath(process.out)