"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mat_material.sim_material_option import SimMaterialOption
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimMaterialOptions(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimMaterialOptions
                | 
                | Represents the collection of material options.
                | 
                | Example:
                |     Given a SimMaterialDomain object you can retrieve a SimMaterialOptions
                |     collection as following:
                | 
                |      Dim MyMaterialDomain As SimMaterialDomain
                |      ...
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      Set MyMaterialOptions = MyMaterialDomain.Options
                |      
                | 
                | See also:
                |     SimMaterialDomain
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SimMaterialOption)
        self.com_object = com_object

    def add(self, i_type: str) -> SimMaterialOption:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iType) As CATBaseDispatch
                |     Creates a new material option in a simulation domain.
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of the material option.
                | 
                |                 SimIsotropicConductivity for conductivity.
                |                 SimDensity for Density.
                |                 SimElasticity for Elastic.
                |                 SimExpansion for Expansion.
                |                 SimGasketMembraneElastic for Gasket Membrane
                |                 Elastic.
                |                 SimGasketThicknessBehavior for Gasket Thickness
                |                 Behavior.
                |                 SimGasketTransverseShearElastic for Gasket Transverse Shear
                |                 Elastic.
                |                 SimHashinDamage for Hashin Damage.
                |                 SimPlasticity for Plastic.
                |                 SMAMatCastIronPlasticity for Cast Iron
                |                 Plasticity.
                |                 SMAMatDamping for Damping.
                |                 SMAMatBulkModulus for Bulk Modulus.
                |                 SMAMatSpecificHeat for Specific Heat.
                |                 SMAMatInelasticHeatFraction for Inelastic Heat
                |                 Fraction.
                |                 SMAMatLatentHeat for Latent Heat.
                |                 SMAMatVolumetricDrag for Volumetric Drag.
                |                 SMAMatAcousticAbsorption for Acoustic Absorption.
                |                 
                | 
                |     Returns:
                |         Created material option.

        :param str i_type:
        :return: SimMaterialOption
        """
        return SimMaterialOption(self.com_object.Add(i_type))

    def item(self, i_index: CATVariant) -> SimMaterialOption:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a material option object.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the material option. 
                | 
                |     Returns:
                |         The material option object.

        :param CATVariant i_index:
        :return: SimMaterialOption
        """
        return SimMaterialOption(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a material option object.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the material option to be removed. 

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SimMaterialOptions(name="{self.name}")'
