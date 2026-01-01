from enum import IntEnum


class LinearElasticDomainType(IntEnum):
    Domain_Isotropic = 0
    Domain_Orthotropic2D = 1
    Domain_Fiber = 2
    Domain_HoneyComb = 3
    Domain_Orthotropic3D = 4
