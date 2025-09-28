#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.boundary import Boundary
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class HybridShapes(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     HybridShapes
                | 
                | The collection of the HybridShapes making up a body.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_boundary(self, i_label: str) -> Boundary:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetBoundary(CATBSTR iLabel) As Boundary
                |     Returns a boundary using its label.
                | 
                |     Parameters:
                | 
                |         iLabel
                |             Identification of the Boundary object. See Reference.DisplayName.
                |             
                | 
                |     Returns:
                |         The retrieved boundary

        :param str i_label:
        :return: Boundary
        """
        return Boundary(self.com_object.GetBoundary(i_label))

    def item(self, i_index: CATVariant) -> HybridShape:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Item(CATVariant iIndex) As HybridShape
                |     Returns a HybridShape using its index or its name from the HybridShapes
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the HybridShape to retrieve from the
                |             collection of HybridShapes. As a numerics, this index is the rank of the
                |             HybridShape in the collection. The index of the first HybridShape in the
                |             collection is 1, and the index of the last HybridShape is Collection.Count. As
                |             a string, it is the name you assigned to the HybridShape using the
                |             AnyObject.Name property. 
                | 
                |     Returns:
                |         The retrieved HybridShape 
                |     Example:
                |         This example retrieves in ThisHybridShape the third HybridShape, and in
                |         ThatHybridShape the HybridShape named MyHybridShape in the HybridShape
                |         collection of the active 3D shape.
                | 
                |          Set Editor = CATIA.ActiveEditor
                |          Set Part = Editor.ActiveObject
                |          Set ThisHybridShape = Part.HybridShapes.Item(3)
                |          Set ThatHybridShape = Part.HybridShapes.Item("MyHybridShape")

        :param CATVariant i_index:
        :return: HybridShape
        """
        return HybridShape(self.com_object.Item(i_index))

    def __repr__(self):
        return f'HybridShapes(name="{ self.name }")'
