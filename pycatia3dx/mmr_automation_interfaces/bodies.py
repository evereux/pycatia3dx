#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.body import Body
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class Bodies(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Bodies
                | 
                | A collection of all the Body objects contained in the part.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self) -> Body:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Add() As Body
                |     Creates a new body and adds it to the Bodies collection. This body becomes
                |     the current one
                | 
                |     Returns:
                |         The created body 
                |     Example:
                |         The following example creates a body named NewBody in the body
                |         collection of the rootPart part in the active 3D shape. NewBody becomes the
                |         current body in the 3D shape.
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set rootPart = editor.ActiveObject
                |          Set NewBody = rootPart.Bodies.Add

        :return: Body
        """
        return Body(self.com_object.Add())

    def item(self, i_index: CATVariant) -> Body:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Item(CATVariant iIndex) As Body
                |     Returns a body using its index or its name from the Bodies
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the body to retrieve from the collection
                |             of bodies. As a numerics, this index is the rank of the body in the collection.
                |             The index of the first body in the collection is 1, and the index of the last
                |             body is Count. As a string, it is the name you assigned to the body using the
                |             AnyObject.Name property. 
                | 
                |     Returns:
                |         The retrieved body 
                |     Example:
                |         This example retrieves in ThisBody the fifth body in the collection and
                |         in ThatBody the body named MyBody in the body collection of the active 3D
                |         shape.
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set rootPart = editor.ActiveObject
                |          Set BodyColl = rootPart.Bodies
                |          Set ThisBody = BodyColl.Item(5)
                |          Set ThatBody = BodyColl.Item("MyBody")

        :param CATVariant i_index:
        :return: Body
        """
        return Body(self.com_object.Item(i_index))

    def __repr__(self):
        return f'Bodies(name="{self.name}")'
