"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.todo_part.boolean_shape import BooleanShape


class Intersect(BooleanShape):

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
                |                         CATPartIDLItf.BooleanShape
                |                             Intersect
                | 
                | Represents the intersect boolean operation.
                | It is performed between a body and the current shape.
                | 
                | Example
                | 
                | The following example shows how to create a new shape by intersecting two
                | existing pads Pad1 and Pad2, created in two different bodies Body1 and Body2
                | respectively, using the existing shape factory named
                | shapeFactory.
                | 
                |  ' Make Pad1 the current shape
                |  CATIA.ActiveDocument.Part.CurrentShape = Pad1
                |  ' 
                |  ' Create the intersection between Pad1 and Body2 
                |  Set NewShape      = shapeFactory.AddNewIntersect(Body2)

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'Intersect(name="{ self.name }")'
