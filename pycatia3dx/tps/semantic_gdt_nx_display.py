"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.semantic_gdt_common_zone import SemanticGDTCommonZone


class SemanticGDTNxDisplay(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SemanticGDTNxDisplay
                | 
                | Interface to distinguish Collection of features from Separate features
                | GDT.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def instance_count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InstanceCount() As long (Read Only)
                |     Gets count of instances.

        :return: int
        """

        return self.com_object.InstanceCount

    def common_zone(self) -> SemanticGDTCommonZone:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CommonZone() As SemanticGDTCommonZone
                |     Gets the GDT on the Common Zone interface to access CZ modifier
                |     information. Method is only returning a valid object if ISO Standard is
                |     applied.
                | 
                |     Parameters:
                | 
                |         oCommonZone
                |             Common Zone related information.

        :return: SemanticGDTCommonZone
        """
        return SemanticGDTCommonZone(self.com_object.CommonZone())

    def is_a_collection(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsACollection() As boolean
                |     Checks if GDT is Collection of Features. In ISO Standard, GDT may have a CZ
                |     modifier on tolerance value.
                | 
                |     Parameters:
                | 
                |         oIsColl
                | 
                |                 TRUE: The GDT is applied on several elements considered as a
                |                 collection
                |                 FALSE: The GDT is not applied with a collection consideration.
                |                 It must be a separate.

        :return: bool
        """
        return self.com_object.IsACollection()

    def is_a_separate(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsASeparate() As boolean
                |     Checks if GDT is Separate Features. In ASME Standard this is indicated with
                |     the "INDIVIDUALLY" text linked to the GDT.
                | 
                |     Parameters:
                | 
                |         oIsSeparate
                | 
                |                 TRUE: The GDT is applied on several elements as many separate
                |                 specifications.
                |                 FALSE: The GDT is not applied with a separate consideration. It
                |                 must be a collection.

        :return: bool
        """
        return self.com_object.IsASeparate()

    def __repr__(self):
        return f'SemanticGdtNxDisplay(name="{ self.name }")'
