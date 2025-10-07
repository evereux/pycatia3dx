"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.str.str_adv_panel import StrAdvPanel
from pycatia3dx.str.str_break import StrBreak
from pycatia3dx.str.str_category_mngt import StrCategoryMngt
from pycatia3dx.str.str_openings import StrOpenings
from pycatia3dx.str.str_openings_mgr import StrOpeningsMgr
from pycatia3dx.str.str_panel_limit_mngt import StrPanelLimitMngt
from pycatia3dx.str.str_panel_surf import StrPanelSurf
from pycatia3dx.str.str_plate_extrusion_mngt import StrPlateExtrusionMngt
from pycatia3dx.str.str_slots import StrSlots


class StructurePlate(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StructurePlate
                | 
                | Object to manage the Structure Plate object.
                | Role: Allows accessing and setting of Plate's data.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def panel_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PanelType() As CATStrPanelMode
                |     Returns the Panel's type.
                |     values:
                |     catStrPanelModeUndefined: Undefined
                |     catStrPanelModeSurf: Panel defined by a surface

        :return: CATStrPanelMode
        """

        return self.com_object.PanelType

    @panel_type.setter
    def panel_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.PanelType = value

    @property
    def str_adv_panel(self) -> StrAdvPanel:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrAdvPanel() As StrAdvPanel (Read Only)
                |     Returns the StrAdvPanel object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in ObjStrAdvPanel the StrAdvPanel
                |              object
                |              of the StrPlate
                |              
                | 
                |              Set ObjStrAdvPanel = ObjStrPlate.StrAdvPanel

        :return: StrAdvPanel
        """

        return StrAdvPanel(self.com_object.StrAdvPanel)

    @property
    def str_break(self) -> StrBreak:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrBreak() As StrBreak (Read Only)
                |     Returns the StrBreak object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in ObjStrBreak the StrBreak
                |              object
                |              of the StrPlate
                |              
                | 
                |              Set ObjStrBreak = ObjStrPlate.StrBreak

        :return: StrBreak
        """

        return StrBreak(self.com_object.StrBreak)

    @property
    def str_category_mngt(self) -> StrCategoryMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrCategoryMngt() As StrCategoryMngt (Read Only)
                |     Returns the StrCategoryMngt object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in ObjStrCategoryMngt the StrCategoryMngt
                |              object
                |              of the StrPlate
                |              
                | 
                |              Set ObjStrCategoryMngt = ObjStrPlate.StrCategoryMngt

        :return: StrCategoryMngt
        """

        return StrCategoryMngt(self.com_object.StrCategoryMngt)

    @property
    def str_openings_mgr(self) -> StrOpeningsMgr:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrOpeningsMgr() As StrOpeningsMgr (Read Only)
                |     Returns the StrOpeningsMgr object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in ObjStrOpeningsMgr the StrOpeningsMgr
                |              object
                |              of the StrPlate
                |              
                | 
                |              Set ObjStrOpeningsMgr = ObjStrPlate.StrOpeningsMgr

        :return: StrOpeningsMgr
        """

        return StrOpeningsMgr(self.com_object.StrOpeningsMgr)

    @property
    def str_panel_limit_mngt(self) -> StrPanelLimitMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrPanelLimitMngt() As StrPanelLimitMngt (Read Only)
                |     Returns the StrPanelLimitMngt object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in ObjStrPanelLimitMngt the
                |              StrPanelLimitMngt object
                |              of the StrPlate
                |              
                | 
                |              Set ObjStrPanelLimitMngt = ObjStrPlate.StrPanelLimitMngt

        :return: StrPanelLimitMngt
        """

        return StrPanelLimitMngt(self.com_object.StrPanelLimitMngt)

    @property
    def str_panel_surf(self) -> StrPanelSurf:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrPanelSurf() As StrPanelSurf (Read Only)
                |     Returns the StrPanelSurf object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in ObjStrPanelSurf the StrPanelLimitMngt
                |              object
                |              of the StrPlate
                |              
                | 
                |              Set ObjStrPanelSurf = ObjStrPlate.StrPanelSurf

        :return: StrPanelSurf
        """

        return StrPanelSurf(self.com_object.StrPanelSurf)

    @property
    def str_plate_extrusion_mngt(self) -> StrPlateExtrusionMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrPlateExtrusionMngt() As StrPlateExtrusionMngt (Read
                | Only)
                |     Returns the StrPlateExtrusionMngt object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in ObjStrPlateExtrusionMngt the
                |              StrPlateExtrusionMngt object
                |              of the StrPlate
                |              
                | 
                |              Set ObjStrPlateExtrusionMngt = ObjStrPlate.StrPlateExtrusionMngt

        :return: StrPlateExtrusionMngt
        """

        return StrPlateExtrusionMngt(self.com_object.StrPlateExtrusionMngt)

    @property
    def str_slots(self) -> StrSlots:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrSlots() As StrSlots (Read Only)
                |     Returns the Slots that are inside this object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the StrSlots object.
                |              
                | 
                |               Dim ListOfSlots As StrSlots
                |               Set ListOfSlots = ObjSddPanel.StrSlots

        :return: StrSlots
        """

        return StrSlots(self.com_object.StrSlots)

    def get_canonic_support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCanonicSupport() As Reference
                |     Returns the Canonical MoldedSurface of this plate.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves CanonicSupport of the
                |              plate.
                |              
                | 
                |              Set RefCanonicSupport = ObjSfdPanel.GetCanonicSupport

        :return: Reference
        """
        return Reference(self.com_object.GetCanonicSupport())

    def get_delimited_support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDelimitedSupport() As Reference
                |     Returns the delimited MoldedSurface of this Plate.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves DelimitedSupport of the
                |              plate.
                |              
                | 
                |              Set RefDelimitedSupport = ObjSfdPanel.GetDelimitedSupport

        :return: Reference
        """
        return Reference(self.com_object.GetDelimitedSupport())

    def get_openings(self, i_type: int) -> StrOpenings:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOpenings(long iType) As StrOpenings
                |     Returns the list of Openings that are inside this object.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of Opening you want to retrieve:
                |             - 0: All
                |             - 1: Openings piercing the Plates inside the
                |             OpeningPlateSet
                |             - 2: Openings piercing the Plates and interrupting the Profiles
                |             inside the OpeningPlateProfileSet
                |             - 3: Openings piercing the Profile inside the OpeningProfileSet
                |             
                | 
                |     Example:
                | 
                |          
                | 
                |              This example retrieves all type of Openings
                |              
                | 
                |              Dim ObjStrOpenings As StrOpenings
                |              Set ObjStrOpenings = ObjSddPlate.GetOpenings(0)

        :param int i_type:
        :return: StrOpenings
        """
        return StrOpenings(self.com_object.GetOpenings(i_type))

    def __repr__(self):
        return f'StructurePlate(name="{ self.name }")'
