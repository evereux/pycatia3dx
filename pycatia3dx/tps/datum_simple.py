"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia3dx.system.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia3dx.tps.annotations import Annotations


class DatumSimple(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DatumSimple
                | 
                | Interface for Simple Datum TPS (datum entity).
                | TPS for Technological Product Specifications.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def label(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Label() As CATBSTR
                |     Retrieves or sets Label.

        :return: str
        """

        return self.com_object.Label

    @label.setter
    def label(self, value: str):
        """
        :param str value:
        """

        self.com_object.Label = value

    @property
    def targets(self) -> 'Annotations':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Targets() As Annotations (Read Only)
                |     Retrieves a CATITPSList to read the list of datum target. All objects of
                |     the list adhere to CATITPSDatumTarget. 

        :return: Annotations
        """
        from pycatia3dx.tps.annotations import Annotations
        return Annotations(self.com_object.Targets)

    def __repr__(self):
        return f'DatumSimple(name="{self.name}")'
