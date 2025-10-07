"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.shape import Shape
from pycatia3dx.mode.reference import Reference
from pycatia3dx.sketcher.sketch import Sketch


class SketchBasedShape(Shape):

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
                |                         SketchBasedShape
                | 
                | Represents the shapes based on sketched 2D geometry.
                | It is the base object for prisms, holes, revolutions, stiffeners, and
                | sweeps.
                | 
                | See also:
                |     Prism, Hole, Revolution, Stiffener, Sweep
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def sketch(self) -> Sketch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Sketch() As Sketch (Read Only)
                |     Returns the sketch the shape is based on.
                | 
                |     Example:
                |         The following example returns the sketch a pad named firstPad is based
                |         on:
                | 
                |          Set sketchPad = firstPad.Sketch

        :return: Sketch
        """

        return Sketch(self.com_object.Sketch)

    def set_profile_element(self, i_profile_element: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetProfileElement(Reference iProfileElement)
                |     Returns or sets a profile element. 

        :param Reference i_profile_element:
        :return: None
        """
        return self.com_object.SetProfileElement(i_profile_element.com_object)

    def __repr__(self):
        return f'SketchBasedShape(name="{ self.name }")'
