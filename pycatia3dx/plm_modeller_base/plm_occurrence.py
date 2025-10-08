"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity
from pycatia3dx.system.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia3dx.plm_modeller_base.plm_occurrences import PLMOccurrences


class PLMOccurrence(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMOccurrence
                | 
                | Represents a PLM Product Occurrence object.
                | Enables to retrieve a PLM Entity (Instance/Reference) and a PLM Occurrences
                | collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def plm_entity(self) -> PLMEntity:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PLMEntity() As PLMEntity (Read Only)
                |     Returns the Instance or Reference Product Model object.
                |     Role: This method retrieves the corresponding PLM Product Instance if
                |     calling object is an instance or the PLM Product Reference if it is a
                |     reference.

        :return: PLMEntity
        """

        return PLMEntity(self.com_object.PLMEntity)

    @property
    def plm_occurrences(self) -> 'PLMOccurrences':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PLMOccurrences() As PLMOccurrences (Read Only)
                |     Returns the PLM Product Occurrences collection.
                |     Role: This method returns the Product Occurrences collection directly
                |     aggregated within this object.

        :return: PLMOccurrences
        """
        from pycatia3dx.plm_modeller_base.plm_occurrences import PLMOccurrences
        return PLMOccurrences(self.com_object.PLMOccurrences)

    def __repr__(self):
        return f'PlmOccurrence(name="{self.name}")'
