"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class StrProfileCrv(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrProfileCrv
                | 
                | Object to manage Profile created with 1 curve
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Curve() As Reference
                |     Returns or Sets the Profile's curve.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the curve of the profile.
                |              
                | 
                |               Dim ObjStrProfileCrv As StrProfileCrv
                |               Set ObjStrProfileCrv = ObjSfdMember.StrProfileCrv
                |               Set RefCurve = ObjStrProfileCrv.Curve

        :return: Reference
        """

        return Reference(self.com_object.Curve)

    @curve.setter
    def curve(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Curve = value

    @property
    def reference(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Reference() As Reference
                |     Returns or Sets the curve's reference.
                |     Role Returns or Sets the curve's reference. When the profile is a stiffener
                |     on curve, or stiffener on free edge, you must set the delimited molded surface
                |     of the panel.
                | 
                |     See also:
                |         SfdPanel.GetDelimitedSupport
                |     Example:
                | 
                | 
                |              This example retrieves Reference of the profile.
                |              
                | 
                |               Set RefReference = ObjStrProfileCrv.Reference

        :return: Reference
        """

        return Reference(self.com_object.Reference)

    @reference.setter
    def reference(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Reference = value

    def get_curve_offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCurveOffset() As Parameter
                |     Returns the geodesic offset of the curve.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves Offset of the curve.
                |              
                | 
                |               Dim OffsetParm As Parameter
                |               Set OffsetParm = ObjStrProfile.GetCurveOffset

        :return: Parameter
        """
        return Parameter(self.com_object.GetCurveOffset())

    def __repr__(self):
        return f'StrProfileCrv(name="{ self.name }")'
