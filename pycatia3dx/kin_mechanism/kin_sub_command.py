"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.kin_mechanism.kin_command import KinCommand
from pycatia3dx.kin_mechanism.kin_mechanism import KinMechanism
from pycatia3dx.product_structure_client.vpm_occurrence import VPMOccurrence


class KinSubCommand(KinCommand):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATKinMechanismIDLItf.KinCommand
                |                         KinSubCommand
                | 
                | The interface to access a CATIAKinSubCommand.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def sub_mechanism(self) -> KinMechanism:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SubMechanism() As KinMechanism (Read Only)
                |     Returns the sub mechanism owner of the kinematics sub command. An empty
                |     value means that the command is directly under the macro mechanism
                |     it-self
                | 
                |     Parameters:
                | 
                |         oSubMechanism

        :return: KinMechanism
        """

        return KinMechanism(self.com_object.SubMechanism)

    @property
    def sub_mechanism_product_occurrence(self) -> VPMOccurrence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SubMechanismProductOccurrence() As VPMOccurrence (Read
                | Only)
                |     Returns the VPMOccurrence owner of the sub mechanism. An empty value means
                |     that the command is directly under the macro mechanism
                |     it-self
                | 
                |     Parameters:
                | 
                |         oSubMechanismProdOcc

        :return: VPMOccurrence
        """

        return VPMOccurrence(self.com_object.SubMechanismProductOccurrence)

    def __repr__(self):
        return f'KinSubCommand(name="{self.name}")'
