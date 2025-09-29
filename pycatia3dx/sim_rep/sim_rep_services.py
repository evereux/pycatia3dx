"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.product_structure_client.vpm_rep_reference import VPMRepReference


class SimRepServices(Service):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         SimRepServices
                | 
                | Represents the service associated to the representation
                | reference.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def duplicate_rep(self, i_rep_to_duplicate: VPMRepReference, i_dup_string: str, i_mcx_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DuplicateRep(VPMRepReference iRepToDuplicate,CATBSTR
                | iDupString,SimMCXDuplicateMode iMCXMode)
                |     Duplicates a simulation model representation reference.
                | 
                |     Parameters:
                | 
                |         iRepToDuplicate
                |             The representation reference to duplicate. 
                |         iDupString
                |             The duplication string. 
                |         iMCXMode
                |             The connection duplication mode.

        :param VPMRepReference i_rep_to_duplicate:
        :param str i_dup_string:
        :param int i_mcx_mode:
        :return: None
        """
        return self.com_object.DuplicateRep(i_rep_to_duplicate.com_object, i_dup_string, i_mcx_mode)

    def is_loaded(self, i_rep_reference: VPMRepReference) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsLoaded(VPMRepReference iRepReference) As boolean
                |     Asks if the representation reference is loaded or not.
                | 
                |     Parameters:
                | 
                |         iRepReference
                |             Representation reference to be checked. 
                | 
                |     Returns:
                |         True: the represenation reference is loaded.
                |         False: the represenation reference is not loaded.

        :param VPMRepReference i_rep_reference:
        :return: bool
        """
        return self.com_object.IsLoaded(i_rep_reference.com_object)

    def load_rep(self, i_rep_reference: VPMRepReference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub LoadRep(VPMRepReference iRepReference)
                |     Loads a Representation Reference in Design mode.
                | 
                |     Parameters:
                | 
                |         iRepReference
                |             The representation reference to load in design mode.

        :param VPMRepReference i_rep_reference:
        :return: None
        """
        return self.com_object.LoadRep(i_rep_reference.com_object)

    def unload_rep(self, i_rep_reference: VPMRepReference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub UnloadRep(VPMRepReference iRepReference)
                |     Unloads a Representation Reference .
                | 
                |     Parameters:
                | 
                |         iRepReference
                |             The representation reference to unload. 
                | 
                | 
                | Copyright © 1999-2024, Dassault Systèmes. All rights reserved.

        :param VPMRepReference i_rep_reference:
        :return: None
        """
        return self.com_object.UnloadRep(i_rep_reference.com_object)

    def __repr__(self):
        return f'SimRepServices(name="{self.name}")'
