"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.tps.annotation import Annotation
from pycatia3dx.types.general import CATVariant


class Annotations(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Annotations
                | 
                | Interface for collection of TPS objects CATIAAnnotation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_annot: Annotation) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Add(Annotation iAnnot)
                |     Add an Annotation.

        :param Annotation i_annot:
        :return: None
        """
        return self.com_object.Add(i_annot.com_object)

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As AnyObject
                |     Retrieves an Annotation managing by CATIAAnnotation. Deprecated method:
                |     Item method is replaced by Item2 has.

        :param CATVariant i_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.Item(i_index))

    def item2(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item2(CATVariant iIndex) As AnyObject
                |     Retrieve an Annotation using interface CATIAAnnotation2 

        :param CATVariant i_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.Item2(i_index))

    def __repr__(self):
        return f'Annotations(name="{ self.name }")'
