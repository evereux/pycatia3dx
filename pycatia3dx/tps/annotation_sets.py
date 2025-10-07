"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class AnnotationSets(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AnnotationSets
                | 
                | Interface for collection of Annotations' Set
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As AnyObject
                |     Retrieve a set.

        :param CATVariant i_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.Item(i_index))

    def load_annotation_sets_list(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub LoadAnnotationSetsList()
                |     Loads the Annotation Sets list. This method is very useful when a cgr
                |     document containing Annotation Set is inserted in the product, because the
                |     Annotation Set is not automatically loaded If the Annotation Set is already
                |     loaded nothing happens. 

        :return: None
        """
        return self.com_object.LoadAnnotationSetsList()

    def __repr__(self):
        return f'AnnotationSets(name="{ self.name }")'
