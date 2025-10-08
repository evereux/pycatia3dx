"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class StrPosSupportFace(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrPosSupportFace
                | 
                | Object to manage the specification of which face of an object to use for
                | positioning.
                | This interface is used, for example, to set and get the support face for a
                | Standard Opening Positioning Strategy.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def role(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Role() As CATBSTR (Read Only)
                |     Returns the role of this parameter. The role is specific to the element
                |     from which this interface was retrieved.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the role of the parameter.
                |              
                | 
                |              Dim ObjStrStandardPosStrategyParameters As
                |              StrStandardPosStrategyParameters
                |              Set ObjStrStandardPosStrategyParameters = ObjStrOpeningsMgr.GetStandardPositioningStrategyParms(StdPosStrategyName)
                |              Dim ObjStrPosSupportFace As StrPosSupportFace
                |              Set ObjStrPosSupportFace = ObjStrStandardPosStrategyParameters.Item(1)
                |              If (TypeName(ObjStrPosSupportFace) = "StrPosSupportFace") Then
                |                  StrRole = ObjStrPosSupportFace.Role
                |              End If

        :return: str
        """

        return self.com_object.Role

    def get_face_side(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFaceSide() As long
                |     Returns the nominal side of a plate-like object to use as a
                |     support.
                |     RoleThe Plate-like object is any object that has parallel main faces, where
                |     one face is considered the control surface (the "molded" side), and the
                |     thickness to the other face is much smaller than the face dimensions. This
                |     other main face is the "thrown" side, since it is in the direction of the
                |     material throw direction.
                |     legal values:
                |     -1 : undefined
                |     0 : molded surface side
                |     1 : material side
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the nominal face side.
                |              
                | 
                |              FaceSide = ObjStrPosSupportFace.GetFaceSide

        :return: int
        """
        return self.com_object.GetFaceSide()

    def set_face_side(self, i_face_side: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFaceSide(long iFaceSide)
                |     Sets the nominal side of a plate-like object to use as a
                |     support.
                | 
                |     Parameters:
                | 
                |         iFaceSide
                |             The nominal face side (molded side or thrown side). legal
                |             values:
                |             -1 : undefined
                |             0 : molded surface side
                |             1 : material side 
                | 
                |     Example:
                | 
                | 
                |              This example sets the nominal face side.
                |              
                | 
                |              ObjStrPosSupportFace.SetFaceSide 1

        :param int i_face_side:
        :return: None
        """
        return self.com_object.SetFaceSide(i_face_side)

    def __repr__(self):
        return f'StrPosSupportFace(name="{ self.name }")'
