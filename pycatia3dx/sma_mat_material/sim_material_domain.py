"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.material.material_domain_content import MaterialDomainContent
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mat_material.sim_material_behaviors import SimMaterialBehaviors
from pycatia3dx.sma_mat_material.sim_material_options import SimMaterialOptions


class SimMaterialDomain(MaterialDomainContent):

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
                |                         SimMaterialDomain
                | 
                | Represents the Simulation Material Domain object.
                | 
                | Example:
                |     Given a MaterialDomains object, you can create and retrieve a
                |     SimMaterialDomain object as following:
                | 
                |      Dim MyMaterialDomains As MaterialDomains
                |      ...
                |      Dim MyMaterialDomain As MaterialDomain
                |      MyMaterialDomains.Add "dsc_matref_rep_SmaOptions",
                |      MyMaterialDomain
                | 
                |      Dim MySimulationDomain As SimMaterialDomain
                |      Set MySimulationDomain = MyMaterialDomain.MaterialDomainContent
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def behaviors(self) -> SimMaterialBehaviors:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Behaviors() As SimMaterialBehaviors (Read Only)
                |     Retrieves a collection of all behaviors in the material domain.

        :return: SimMaterialBehaviors
        """

        return SimMaterialBehaviors(self.com_object.Behaviors)

    @property
    def default_behavior(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DefaultBehavior() As CATBaseDispatch
                |     Default material behavior on a simulation domain.

        :return: AnyObject
        """

        return AnyObject(self.com_object.DefaultBehavior)

    @default_behavior.setter
    def default_behavior(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.DefaultBehavior = value

    @property
    def material(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Material() As CATBaseDispatch (Read Only)
                |     Retrieves material reference of simulation domain.

        :return: AnyObject
        """

        return AnyObject(self.com_object.Material)

    @property
    def options(self) -> SimMaterialOptions:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Options() As SimMaterialOptions (Read Only)
                |     Retrieves a collection of all material options in the material domain.

        :return: SimMaterialOptions
        """

        return SimMaterialOptions(self.com_object.Options)

    def duplicate_and_add_material_option(self, ip_mat_option_source: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DuplicateAndAddMaterialOption(CATBaseDispatch ipMatOptionSource) As
                | CATBaseDispatch
                |     Duplicates and adds a material option in a simulation
                |     domain.
                | 
                |     Parameters:
                | 
                |         ispMatOptionSource
                |             Material option to be duplicated. 
                | 
                |     Returns:
                |         Duplicated material option.

        :param AnyObject ip_mat_option_source:
        :return: AnyObject
        """
        return self.com_object.DuplicateAndAddMaterialOption(ip_mat_option_source.com_object)

    def sync_all_behaviors(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SyncAllBehaviors()
                |     Synchronises all material behaviors. This should be done after
                |     modifications to individual material options and behaviors within a material
                |     domain are completed and before the material domain is used elsewhere. It is
                |     not necessary to sync the material domain after each modification to a material
                |     domain or behavior 

        :return: None
        """
        return self.com_object.SyncAllBehaviors()

    def __repr__(self):
        return f'SimMaterialDomain(name="{ self.name }")'
