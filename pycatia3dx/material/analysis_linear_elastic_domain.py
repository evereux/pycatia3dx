"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.material.material_domain_content import MaterialDomainContent
from pycatia3dx.types.general import CATVariant


class AnalysisLinearElasticDomain(MaterialDomainContent):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMaterialIDLItf.MaterialDomainContent
                |                         AnalysisLinearElasticDomain
                | 
                | 
                | Deprecated:
                |     R417 ElFini domain removed please use SimMaterialDomain instead please use
                |     SimMaterialDomain instead Interface to access the Linear Elastic Domain
                |     properties and parameters.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def domain_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DomainType() As LinearElasticDomainType
                | 
                |     Deprecated:
                |         R417 ElFini domain removed please use SimMaterialDomain instead Gets
                |         the type of Linear Elastic Domain. 
                |     Parameters:
                | 
                |         oDomainType
                |             Returns the Type of Domain Domain_Isotropic : For Isotropic Domain Type Domain_Orthotropic2D : For Orthotropic-2D Domain Type Domain_Fiber : For Fiber Domain Type Domain_HoneyComb : For HoneyComb Domain Type Domain_Orthotropic3D : For Orthotropic-3D Domain Type This Method Returns E_FAIL one of these Types is not returned. 
                | 
                |     Example:
                | 
                |         : linearElasticDomain is the LinearElastic Domain Object oDomainType = linearElasticDomain.DomainType
                |          In this example, oDomainType is the output Type of Linear Elastic
                |          Domain

        :return: LinearElasticDomainType
        """

        return self.com_object.DomainType

    @domain_type.setter
    def domain_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.DomainType = value

    def domain_parameters_check(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub DomainParametersCheck()
                | 
                |     Deprecated:
                |         R417 ElFini domain removed please use SimMaterialDomain instead This
                |         API checks if all the Domain Parameter values obey the Material Property
                |         conditions as per their documentation. This API should be called after SET
                |         and/or PUT API for the following Domain Types are used in VB Script.
                |         Orthotropic-2D Fiber Orthotropic-3D

        :return: None
        """
        return self.com_object.DomainParametersCheck()

    def get_domain_parameter(self, i_param_name: str) -> CATVariant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetDomainParameter(CATBSTR iParamName) As CATVariant
                | 
                |     Deprecated:
                |         R417 ElFini domain removed please use SimMaterialDomain instead Gets
                |         the Value of Domain parameter. 
                |     Parameters:
                | 
                |         iParamName
                |             The name of the Parameter (physical type) The user should specify
                |             only the allowed Parameter Name based on the Type of Domain. The allowed
                |             Parameter Name for (Isotropic Domain) YOUNG_MODULUS POISSON_RATIO DENSITY
                |             YIELD_STRENGTH COEFFICIENT_OF_THERMAL_EXPANSION The allowed Parameter Name for
                |             (Orthotropic-2D Domain) YOUNG_MODULUS_X YOUNG_MODULUS_Y POISSON_RATIO_XY
                |             SHEAR_MODULUS_XY SHEAR_MODULUS_XZ SHEAR_MODULUS_YZ DENSITY
                |             TENSILE_STRESS_LIMIT_X COMPRESSIVE_STRESS_LIMIT_X TENSILE_STRESS_LIMIT_Y
                |             COMPRESSIVE_STRESS_LIMIT_Y SHEAR_STRESS_LIMIT_XY SHEAR_STRESS_LIMIT_XZ
                |             SHEAR_STRESS_LIMIT_YZ COEFFICIENT_OF_THERMAL_EXPANSION_X
                |             COEFFICIENT_OF_THERMAL_EXPANSION_Y The allowed Parameter Name for (Fiber
                |             Domain) YOUNG_MODULUS_X YOUNG_MODULUS_Y POISSON_RATIO_XY SHEAR_MODULUS_XY
                |             SHEAR_MODULUS_YZ DENSITY TENSILE_STRESS_LIMIT_X COMPRESSIVE_STRESS_LIMIT_X
                |             TENSILE_STRESS_LIMIT_Y COMPRESSIVE_STRESS_LIMIT_Y SHEAR_STRESS_LIMIT_XY
                |             SHEAR_STRESS_LIMIT_YZ COEFFICIENT_OF_THERMAL_EXPANSION_X
                |             COEFFICIENT_OF_THERMAL_EXPANSION_Y The allowed Parameter Name for (HoneyComb
                |             Domain) YOUNG_MODULUS_Z SHEAR_MODULUS_XZ SHEAR_MODULUS_YZ DENSITY
                |             TENSILE_STRESS_LIMIT_Z COMPRESSIVE_STRESS_LIMIT_Z SHEAR_STRESS_LIMIT_XZ
                |             SHEAR_STRESS_LIMIT_YZ COEFFICIENT_OF_THERMAL_EXPANSION_Z The allowed Parameter
                |             Name for (Orthotropic-3D Domain) YOUNG_MODULUS_X YOUNG_MODULUS_Y
                |             YOUNG_MODULUS_Z POISSON_RATIO_XY POISSON_RATIO_XZ POISSON_RATIO_YZ
                |             SHEAR_MODULUS_XY SHEAR_MODULUS_XZ SHEAR_MODULUS_YZ DENSITY
                |             TENSILE_STRESS_LIMIT_X COMPRESSIVE_STRESS_LIMIT_X TENSILE_STRESS_LIMIT_Y
                |             COMPRESSIVE_STRESS_LIMIT_Y TENSILE_STRESS_LIMIT_Z COMPRESSIVE_STRESS_LIMIT_Z
                |             SHEAR_STRESS_LIMIT_XY SHEAR_STRESS_LIMIT_XZ SHEAR_STRESS_LIMIT_YZ
                |             COEFFICIENT_OF_THERMAL_EXPANSION_X COEFFICIENT_OF_THERMAL_EXPANSION_Y
                |             COEFFICIENT_OF_THERMAL_EXPANSION_Z This Method Returns E_FAIL if Parameter Name
                |             is not one of the allowed Names for the particular Domain Type.
                |             
                |         oParamValue
                |             Returns the Value @param iParamName 
                | 
                |     Example:
                | 
                |         : linearElasticDomain is the LinearElastic Domain Object Set oParamValue = linearElasticDomain.GetDomainParameter ("YOUNG_MODULUS")
                |          In this example, oParamValue is the output value of the Parameter
                |          whose name is YOUNG_MODULUS.

        :param str i_param_name:
        :return: CATVariant
        """
        return self.com_object.GetDomainParameter(i_param_name)

    def set_domain_parameter(self, i_param_name: str, i_param_value: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetDomainParameter(CATBSTR iParamName,CATVariant
                | iParamValue)
                | 
                |     Deprecated:
                |         R417 ElFini domain removed please use SimMaterialDomain instead Sets
                |         the Value of Domain parameter. 
                |     Parameters:
                | 
                |         iParamName
                |             The name of the Parameter (physical type) The user should specify
                |             only the allowed Parameter Name based on the Type of Domain. The allowed
                |             Parameter Name for (Isotropic Domain) YOUNG_MODULUS POISSON_RATIO DENSITY
                |             YIELD_STRENGTH COEFFICIENT_OF_THERMAL_EXPANSION The allowed Parameter Name for
                |             (Orthotropic-2D Domain) YOUNG_MODULUS_X YOUNG_MODULUS_Y POISSON_RATIO_XY
                |             SHEAR_MODULUS_XY SHEAR_MODULUS_XZ SHEAR_MODULUS_YZ DENSITY
                |             TENSILE_STRESS_LIMIT_X COMPRESSIVE_STRESS_LIMIT_X TENSILE_STRESS_LIMIT_Y
                |             COMPRESSIVE_STRESS_LIMIT_Y SHEAR_STRESS_LIMIT_XY SHEAR_STRESS_LIMIT_XZ
                |             SHEAR_STRESS_LIMIT_YZ COEFFICIENT_OF_THERMAL_EXPANSION_X
                |             COEFFICIENT_OF_THERMAL_EXPANSION_Y The allowed Parameter Name for (Fiber
                |             Domain) YOUNG_MODULUS_X YOUNG_MODULUS_Y POISSON_RATIO_XY SHEAR_MODULUS_XY
                |             SHEAR_MODULUS_YZ DENSITY TENSILE_STRESS_LIMIT_X COMPRESSIVE_STRESS_LIMIT_X
                |             TENSILE_STRESS_LIMIT_Y COMPRESSIVE_STRESS_LIMIT_Y SHEAR_STRESS_LIMIT_XY
                |             SHEAR_STRESS_LIMIT_YZ COEFFICIENT_OF_THERMAL_EXPANSION_X
                |             COEFFICIENT_OF_THERMAL_EXPANSION_Y The allowed Parameter Name for (HoneyComb
                |             Domain) YOUNG_MODULUS_Z SHEAR_MODULUS_XZ SHEAR_MODULUS_YZ DENSITY
                |             TENSILE_STRESS_LIMIT_Z COMPRESSIVE_STRESS_LIMIT_Z SHEAR_STRESS_LIMIT_XZ
                |             SHEAR_STRESS_LIMIT_YZ COEFFICIENT_OF_THERMAL_EXPANSION_Z The allowed Parameter
                |             Name for (Orthotropic-3D Domain) YOUNG_MODULUS_X YOUNG_MODULUS_Y
                |             YOUNG_MODULUS_Z POISSON_RATIO_XY POISSON_RATIO_XZ POISSON_RATIO_YZ
                |             SHEAR_MODULUS_XY SHEAR_MODULUS_XZ SHEAR_MODULUS_YZ DENSITY
                |             TENSILE_STRESS_LIMIT_X COMPRESSIVE_STRESS_LIMIT_X TENSILE_STRESS_LIMIT_Y
                |             COMPRESSIVE_STRESS_LIMIT_Y TENSILE_STRESS_LIMIT_Z COMPRESSIVE_STRESS_LIMIT_Z
                |             SHEAR_STRESS_LIMIT_XY SHEAR_STRESS_LIMIT_XZ SHEAR_STRESS_LIMIT_YZ
                |             COEFFICIENT_OF_THERMAL_EXPANSION_X COEFFICIENT_OF_THERMAL_EXPANSION_Y
                |             COEFFICIENT_OF_THERMAL_EXPANSION_Z This Method Returns E_FAIL if Parameter Name
                |             is not one of the allowed Names for the particular Domain Type. This Method
                |             Returns E_FAIL if Poissons Ratio value is not within the required range for
                |             Isotropic Domain Type. 
                |         iParamValue
                |             The value of the Parameter to be set. 
                | 
                |     Example:
                | 
                |         : linearElasticDomain is the LinearElastic Domain Object Dim linearElasticDomain As MaterialDomainContent
                |          linearElasticDomain.SetDomainParameter "POISSON_RATIO_XY",
                |          0.4
                |          In this example, 0.4 value is set for the Paramater whose name is
                |          POISSON_RATIO_XY.

        :param str i_param_name:
        :param CATVariant i_param_value:
        :return: None
        """
        return self.com_object.SetDomainParameter(i_param_name, i_param_value)

    def __repr__(self):
        return f'AnalysisLinearElasticDomain(name="{self.name}")'
