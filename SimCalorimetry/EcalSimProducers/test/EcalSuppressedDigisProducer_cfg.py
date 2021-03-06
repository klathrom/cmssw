import FWCore.ParameterSet.Config as cms

process = cms.Process("testECALDigi")
#Geometry
#
process.load("Geometry.CMSCommonData.cmsSimIdealGeometryXML_cfi")

process.load("SimGeneral.MixingModule.mixNoPU_cfi")

process.load("CalibCalorimetry.Configuration.Ecal_FakeConditions_cff")

process.load("Geometry.CaloEventSetup.CaloGeometry_cff")

process.load("SimCalorimetry.Configuration.ecalDigiSequence_cff")

process.Timing = cms.Service("Timing")

process.MessageLogger = cms.Service("MessageLogger",
    #    untracked vstring categories = { "EcalShape","EcalCoder","EcalDigi" }
    #    untracked vstring debugModules = {"ecaldigi"}
    cout = cms.untracked.PSet(
        #      untracked string threshold = "DEBUG" 
        #      untracked PSet DEBUG = { untracked int32 limit = 0 }
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(-1)
        )
    ),
    destinations = cms.untracked.vstring('cout')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)
process.source = cms.Source("PoolSource",
    debugFlag = cms.untracked.bool(True),
    debugVebosity = cms.untracked.uint32(10),
    fileNames = cms.untracked.vstring('file:simevent.root')
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('digis.root')
)

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    moduleSeeds = cms.PSet(
        simEcalUnsuppressedDigis = cms.untracked.uint32(12345)
    )
)

process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")

process.p = cms.Path(process.mix*process.randomEngineStateProducer*process.ecalDigiSequence)
process.fine = cms.EndPath(process.out)

