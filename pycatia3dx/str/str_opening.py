"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.str.str_category_mngt import StrCategoryMngt
from pycatia3dx.str.str_opening_3d_object import StrOpening3DObject
from pycatia3dx.str.str_opening_extrusion_mngt import StrOpeningExtrusionMngt
from pycatia3dx.str.str_opening_limit_dimensions_mngt import StrOpeningLimitDimensionsMngt
from pycatia3dx.str.str_opening_output_profile import StrOpeningOutputProfile
from pycatia3dx.str.str_opening_standard import StrOpeningStandard


class StrOpening(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrOpening
                | 
                | Object to define a Structure Opening.
                | The list of interfaces involved into the Opening are: -
                | CATIAStrOpeningOutputProfile / 3DObject / Standard: for the creation
                | mode
                | Role: Allows accessing and setting of Opening's data.
                | 
                | See also:
                |     StrOpenings
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def opening_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OpeningType() As CATStrOpeningMode
                |     Returns or Sets Opening's type. Legal Values: - catStrOpeningModeUndefined : undefined opening. - catStrOpeningMode3DObject : opening creation using other mode. - catStrOpeningModeOutputProfile : opening creation using sketch. - catStrOpeningModeStandard : Standard opening mode.
                | 
                |     Example:
                | 
                | 
                |              This example sets OpeningType of the SfdOpening to the Sketch
                |              mode.
                |              
                | 
                |              ObjStrOpening.OpeningType = catStrOpeningModeOutputProfile

        :return: CATStrOpeningMode
        """

        return self.com_object.OpeningType

    @opening_type.setter
    def opening_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.OpeningType = value

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
                |              This example retrieves the StrCategoryMngt
                |              object.
                |              
                | 
                |              Dim ObjStrOpening As StrOpening
                |              Set ObjStrOpening = ObjStrOpenings.Add
                |              Set ObjStrCategoryMngt = ObjStrOpening.StrCategoryMngt

        :return: StrCategoryMngt
        """

        return StrCategoryMngt(self.com_object.StrCategoryMngt)

    @property
    def str_opening_3d_object(self) -> StrOpening3DObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrOpening3DObject() As StrOpening3DObject (Read
                | Only)
                |     Returns the StrOpening3DObject object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the StrOpening3DObject
                |              object.
                |              
                | 
                |              Set ObjStrOpening3DObject = ObjStrOpening.StrOpening3DObject

        :return: StrOpening3DObject
        """

        return StrOpening3DObject(self.com_object.StrOpening3DObject)

    @property
    def str_opening_extrusion_mngt(self) -> StrOpeningExtrusionMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrOpeningExtrusionMngt() As StrOpeningExtrusionMngt (Read
                | Only)
                |     Returns the StrOpeningExtrusionMngt object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the StrOpeningExtrusionMngt
                |              object.
                |              
                | 
                |              Set ObjStrOpeningExtrusionMngt = ObjStrOpening.StrOpeningExtrusionMngt

        :return: StrOpeningExtrusionMngt
        """

        return StrOpeningExtrusionMngt(self.com_object.StrOpeningExtrusionMngt)

    @property
    def str_opening_limit_dimensions_mngt(self) -> StrOpeningLimitDimensionsMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrOpeningLimitDimensionsMngt() As StrOpeningLimitDimensionsMngt (Read
                | Only)
                |     Returns the StrOpeningLimitDimensionsMngt object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the StrOpeningLimitDimensionsMngt
                |              object.
                |              
                | 
                |              Set ObjStrOpeningLimitDimensionsMngt = ObjStrOpening.StrOpeningLimitDimensionsMngt

        :return: StrOpeningLimitDimensionsMngt
        """

        return StrOpeningLimitDimensionsMngt(self.com_object.StrOpeningLimitDimensionsMngt)

    @property
    def str_opening_output_profile(self) -> StrOpeningOutputProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrOpeningOutputProfile() As StrOpeningOutputProfile (Read
                | Only)
                |     Returns the StrOpeningOutputProfile object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the StrOpeningOutputProfile
                |              object.
                |              
                | 
                |              Set ObjStrOpeningOutputProfile = ObjStrOpening.StrOpeningOutputProfile

        :return: StrOpeningOutputProfile
        """

        return StrOpeningOutputProfile(self.com_object.StrOpeningOutputProfile)

    @property
    def str_opening_standard(self) -> StrOpeningStandard:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrOpeningStandard() As StrOpeningStandard (Read
                | Only)
                |     Returns the StrOpeningStandard object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the StrOpeningStandard
                |              object.
                |              
                | 
                |              Set ObjStrOpeningStandard = ObjStrOpening.StrOpeningStandard

        :return: StrOpeningStandard
        """

        return StrOpeningStandard(self.com_object.StrOpeningStandard)

    def __repr__(self):
        return f'StrOpening(name="{ self.name }")'
