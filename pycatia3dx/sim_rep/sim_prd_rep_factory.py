"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.product_structure_client.vpm_rep_reference import VPMRepReference
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class SimPrdRepFactory(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimPrdRepFactory
                | 
                | Represents the service to create simulation product
                | representations.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_prd_rep(self, i_rep_type: str) -> VPMRepReference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreatePrdRep(CATBSTR iRepType) As VPMRepReference
                |     Creates a simulation product representation.
                | 
                |     Parameters:
                | 
                |         iRepType:
                |             The type of representation to create.
                |             Legal values: "FEM", "XRep", or "AbstractionShape"
                |             
                | 
                |     Returns:
                |         The created simulation product representation.

        :param str i_rep_type:
        :return: VPMRepReference
        """
        return VPMRepReference(self.com_object.CreatePrdRep(i_rep_type))

    def __repr__(self):
        return f'SimPrdRepFactory()'
