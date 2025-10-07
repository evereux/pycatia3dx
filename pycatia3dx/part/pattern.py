"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.part.transformation_shape import TransformationShape
from pycatia3dx.system.any_object import AnyObject


class Pattern(TransformationShape):

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
                |                         CATPartIDLItf.TransformationShape
                |                             Pattern
                | 
                | Represents the pattern shape.
                | It is the base object for rectangular and circular patterns. A pattern shape is
                | a set of copies of the same shape. The copy is done according to linear and
                | angular repartitions.
                | 
                | See also:
                |     CircPattern, RectPattern, Repartition, LinearRepartition,
                |     AngularRepartition
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def item_to_copy(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ItemToCopy() As AnyObject
                |     Returns or sets the shape to be copied.
                | 
                |     Example:
                |         The following example returns in shape the copied shape of the pattern
                |         firstPattern, and then sets it to pad1:
                | 
                |          Set shape = firstPattern.ItemToCopy
                |          firstPattern.ItemToCopy = pad1

        :return: AnyObject
        """

        return AnyObject(self.com_object.ItemToCopy)

    @item_to_copy.setter
    def item_to_copy(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.ItemToCopy = value

    @property
    def rotation_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RotationAngle() As Angle (Read Only)
                |     Returns the pattern global rotation angle. The rotation is applied to the
                |     whole pattern, but not to the shapes themselves. The shape to be copied is used
                |     as the rotation center.
                | 
                |     Example:
                |         The following example returns in globAng the rotation of pattern
                |         firstPattern:
                | 
                |          Set globAng = firstPattern.RotationAngle

        :return: Angle
        """

        return Angle(self.com_object.RotationAngle)

    def activate_position(self, i_pos_u: int, i_pos_v: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ActivatePosition(long iPosU,long iPosV)
                |     Allows user to activate an instance of the pattern.
                | 
                |     Parameters:
                | 
                |         iPosU
                |             The position of the instance in the U direction 
                |         iPosV
                |             The position of the instance in the V direction

        :param int i_pos_u:
        :param int i_pos_v:
        :return: None
        """
        return self.com_object.ActivatePosition(i_pos_u, i_pos_v)

    def desactivate_position(self, i_pos_u: int, i_pos_v: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DesactivatePosition(long iPosU,long iPosV)
                |     Allows user to desactivate an instance of the pattern.
                | 
                |     Parameters:
                | 
                |         iPosU
                |             The position of the instance in the U direction 
                |         iPosV
                |             The position of the instance in the V direction 

        :param int i_pos_u:
        :param int i_pos_v:
        :return: None
        """
        return self.com_object.DesactivatePosition(i_pos_u, i_pos_v)

    def __repr__(self):
        return f'Pattern(name="{ self.name }")'
