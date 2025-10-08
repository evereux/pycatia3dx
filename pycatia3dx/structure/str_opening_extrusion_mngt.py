"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class StrOpeningExtrusionMngt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrOpeningExtrusionMngt
                | 
                | Object to manage Structure Opening's extrusion.
                | Role: To manage structure opening's extrusion.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def extrusion_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ExtrusionMode() As long
                |     Returns or Sets the extrusion mode of this Opening
                |     Legal values are:
                |     -1: Undefined extrusion mode
                |     1: Before forming extrusion mode
                |     2: After forming extrusion mode
                |     3: Removal extrusion mode
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in ExtrusionMode of the
                |              opening.
                |              
                | 
                |              Dim ObjStrOpeningExtrusionMngt As
                |              StrOpeningExtrusionMngt
                |              Set ObjStrOpeningExtrusionMngt = ObjStrOpening.StrOpeningExtrusionMngt
                |              lExtrusionMode = ObjStrOpeningExtrusionMngt.ExtrusionMode

        :return: int
        """

        return self.com_object.ExtrusionMode

    @extrusion_mode.setter
    def extrusion_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.ExtrusionMode = value

    def __repr__(self):
        return f'StrOpeningExtrusionMngt(name="{ self.name }")'
