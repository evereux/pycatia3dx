#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_body import HybridBody
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class HybridBodies(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     HybridBodies
                | 
                | A collection of the HybridBody objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=HybridBody)
        self.com_object = com_object

    def add(self) -> HybridBody:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Add() As HybridBody
                |     Creates a new hybrid body and adds it to the HybridBodies collection. This
                |     body becomes the current one
                | 
                |     Returns:
                |         The created body 
                |     Example:
                |         The following example creates a body named newHybridBody in the hybrid
                |         body collection of the rootPart part in the 3D shape. NewPartBody becomes the
                |         current body.
                | 
                |          Set newHybridBody = rootPart.HybridBodies.Add

        :return: HybridBody
        """
        return HybridBody(self.com_object.Add())

    def item(self, i_index: CATVariant) -> HybridBody:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Item(CATVariant iIndex) As HybridBody
                |     Returns a body using its index or its name from the Bodies
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the hybrid body to retrieve from the
                |             collection of hybrid bodies. As a numerics, this index is the rank of the
                |             hybrid body in the collection. The index of the first hybrid body in the
                |             collection is 1, and the index of the last hybrid body is Count. As a string,
                |             it is the name you assigned to the hybrid body using the AnyObject.Name
                |             property. 
                | 
                |     Returns:
                |         The retrieved hybrid body 
                |     Example:
                |         This example retrieves in ThisHybridBody the fifth hybrid body in the
                |         collection and in ThatHybridBody the hybrid body named MyHybridBody in the
                |         hybrid body collection of the 3D shape.
                | 
                |          Set hybridBodyColl = rootPart.HybridBodies
                |          Set ThisHybridBody = hybridBodyColl.Item(5)
                |          Set ThatHybridBody = hybridBodyColl.Item("MyHybridBody")

        :param CATVariant i_index:
        :return: HybridBody
        """
        return HybridBody(self.com_object.Item(i_index))

    def __repr__(self):
        return f'HybridBodies(name="{self.name}")'
