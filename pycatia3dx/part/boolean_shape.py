"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.body import Body
from pycatia3dx.mmr_automation_interfaces.shape import Shape
from pycatia3dx.mode.reference import Reference


class BooleanShape(Shape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         BooleanShape
                | 
                | Represents the shapes based on boolean operations on other
                | shapes.
                | It is the base object for add, assemble, intersect, remove, and split
                | shapes.
                | 
                | See also:
                |     Add, Assemble, Intersect, Remove, Split, Trim
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def body(self) -> Body:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Body() As Body (Read Only)
                |     Returns the inserted body.

        :return: Body
        """

        return Body(self.com_object.Body)

    def set_operated_object(self, i_reference_object: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOperatedObject(Reference iReferenceObject)
                |     Modifies the Second Operand. input object to replace with Body or Volume

        :param Reference i_reference_object:
        :return: None
        """
        return self.com_object.SetOperatedObject(i_reference_object.com_object)

    def set_operating_volume(self, i_reference_object: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOperatingVolume(Reference iReferenceObject)
                |     Swaps the operands. Both the Operands must be Volume. This is available
                |     only for Volume Add and Volume UnionTrim Operations 

        :param Reference i_reference_object:
        :return: None
        """
        return self.com_object.SetOperatingVolume(i_reference_object.com_object)

    def __repr__(self):
        return f'BooleanShape(name="{ self.name }")'
