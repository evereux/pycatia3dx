#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.shape import Shape
from pycatia3dx.mode.move import Move


class Solid(Shape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         Solid
                | 
                | Represents an imported solid object.
                | Role: the imported solid is a solid obtained from copy/paste with link or
                | design in context.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def move(self) -> Move:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Move() As Move (Read Only)
                |     Returns the move object of the solid.
                |     Role: The move object is aggregated by the solid object and itself
                |     aggregates a movable object to which you can apply a move transformation by
                |     means of an isometry matrix. It moves the solid according to this
                |     isometry.
                | 
                |     Example:
                | 
                |          This example retrieves the move object EngineMoveObject for
                |          the
                |          Engine product.
                |          
                | 
                |          Dim EngineMoveObject As Move
                |          Set EngineMoveObject = Engine.Move
                |          
                | 
                | 
                |          
                |          
                | 
                |     See also:
                |         Move

        :return: Move
        """

        return Move(self.com_object.Move)

    def __repr__(self):
        return f'Solid(name="{ self.name }")'
