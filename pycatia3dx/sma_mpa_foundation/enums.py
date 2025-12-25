from enum import Enum


class SimGeneralVectorFieldVariationType(Enum):
    SimGeneralVectorFieldUserDefined = 0
    SimGeneralVectorFieldVariableData = 1
    SimGeneralVectorFieldUniform = 2
    SimGeneralVectorFieldExternalFieldData = 3
    SimGeneralVectorFieldSpaceTimeData = 4
    SimGeneralVectorFieldMappedSpatialData = 5


class SimInitializationServiceSimulationMethod(Enum):
    SimInitializationServiceThermalMechanics = 0
    SimInitializationServiceThermalValidation = 1
    SimInitializationServiceLinearDynamics = 2
    SimInitializationServiceEssentialThermalStructuralMechanics = 3
    SimInitializationServiceEssentialStructuralMechanics = 4
    SimInitializationServiceStructuralMechanics = 5
    SimInitializationServiceEssentialThermalMechanics = 6
    SimInitializationServiceStructuralValidation = 7
    SimInitializationServiceThermalStructuralValidation = 8
    SimInitializationServiceFrequencyValidation = 9
    SimInitializationServiceThermalStructuralMechanics = 10


class SimScalarFieldVariationType(Enum):
    SimScalarFieldSpaceTimeData = 0
    SimScalarFieldMappedSpatialData = 1
    SimScalarFieldUserDefined = 2
    SimScalarFieldUniform = 3


class SimSymmetricTensorFieldVariationType(Enum):
    SimSymmetricTensorFieldExternalFieldData = 0
    SimSymmetricTensorFieldUniform = 1
    SimSymmetricTensorFieldSpaceTimeData = 2
    SimSymmetricTensorFieldUserDefined = 3
    SimSymmetricTensorFieldMappedSpatialData = 4


class SimVectorFieldVariationType(Enum):
    SimVectorFieldUniform = 0
    SimVectorFieldUserDefined = 1


