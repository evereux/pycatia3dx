from enum import IntEnum


class SimGeneralVectorFieldVariationType(IntEnum):
    SimGeneralVectorFieldUniform = 0
    SimGeneralVectorFieldMappedSpatialData = 1
    SimGeneralVectorFieldSpaceTimeData = 2
    SimGeneralVectorFieldUserDefined = 3
    SimGeneralVectorFieldVariableData = 4
    SimGeneralVectorFieldExternalFieldData = 5


class SimInitializationServiceSimulationMethod(IntEnum):
    SimInitializationServiceStructuralMechanics = 0
    SimInitializationServiceThermalMechanics = 1
    SimInitializationServiceThermalStructuralMechanics = 2
    SimInitializationServiceEssentialStructuralMechanics = 3
    SimInitializationServiceEssentialThermalMechanics = 4
    SimInitializationServiceEssentialThermalStructuralMechanics = 5
    SimInitializationServiceLinearDynamics = 6
    SimInitializationServiceStructuralValidation = 7
    SimInitializationServiceFrequencyValidation = 8
    SimInitializationServiceThermalValidation = 9
    SimInitializationServiceThermalStructuralValidation = 10


class SimScalarFieldVariationType(IntEnum):
    SimScalarFieldUniform = 0
    SimScalarFieldMappedSpatialData = 1
    SimScalarFieldSpaceTimeData = 2
    SimScalarFieldUserDefined = 3


class SimSymmetricTensorFieldVariationType(IntEnum):
    SimSymmetricTensorFieldUniform = 0
    SimSymmetricTensorFieldMappedSpatialData = 1
    SimSymmetricTensorFieldSpaceTimeData = 2
    SimSymmetricTensorFieldUserDefined = 3
    SimSymmetricTensorFieldExternalFieldData = 4


class SimVectorFieldVariationType(IntEnum):
    SimVectorFieldUniform = 0
    SimVectorFieldUserDefined = 1
