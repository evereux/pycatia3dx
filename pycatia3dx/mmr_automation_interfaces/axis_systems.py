#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.axis_system import AxisSystem
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class AxisSystems(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AxisSystems
                | 
                | A collection of all the AxisSystem objects contained in the
                | part.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self) -> AxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Add() As AxisSystem
                |     Creates a new AxisSystem and adds it to the AxisSystems
                |     collection.
                | 
                |     Returns:
                |         The created AxisSystem 
                |     Example:
                |         The following example creates a AxisSystem names NewAxisSystem in the
                |         AxisSystem collection of the rootPart part in the active 3D
                |         shape.
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set rootPart = editor.ActiveObject
                |          Set NewAxisSystem = rootPart.AxisSystems.Add()

        :return: AxisSystem
        """
        return AxisSystem(self.com_object.Add())

    def item(self, i_index: CATVariant) -> AxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Item(CATVariant iIndex) As AxisSystem
                |     Returns an Axis System using its index or its name from the AxisSystems
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the AxisSystem to retrieve from the
                |             collection of AxisSystems. As a numerics, this index is the rank of the
                |             AxisSystem in the collection. The index of the first AxisSystem in the
                |             collection is 1, and the index of the last AxisSystem is Count. As a string, it
                |             is the name you assigned to the AxisSystem using the AnyObject.Name property.
                |             
                | 
                |     Returns:
                |         The retrieved AxisSystem 
                |     Example:
                |         This example retrieves in ThisAxisSystem the fifth AxisSystem in the
                |         collection and in ThatAxisSystem the AxisSystem named MyAxisSystem in the
                |         AxisSystem collection of the active 3D shape.
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set rootPart = editor.ActiveObject
                |          Set AxisSystemColl = rootPart.AxisSystems
                |          Set ThisAxisSystem = AxisSystemColl.Item(5)
                |          Set ThatAxisSystem = AxisSystemColl.Item("MyAxisSystem")

        :param CATVariant i_index:
        :return: AxisSystem
        """
        return AxisSystem(self.com_object.Item(i_index))

    def __repr__(self):
        return f'AxisSystems(name="{ self.name }")'
