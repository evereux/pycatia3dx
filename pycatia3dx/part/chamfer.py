"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mode.reference import Reference
from pycatia3dx.mode.references import References
from pycatia3dx.todo_part.dress_up_shape import DressUpShape


class Chamfer(DressUpShape):

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
                |                         CATPartIDLItf.DressUpShape
                |                             Chamfer
                | 
                | Represents the chamfer shape.
                | A chamfer is made up of a list of geometrical elements to process, such as
                | faces, and is defined using a couple of parameters, such as two lengthes, or a
                | length and an angle.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Angle() As Angle (Read Only)
                |     Returns the chamfer angle. This is valid only if the chamfer is defined
                |     using a length and an angle, that is if the chamfer definition mode
                |     CatChamferMode is set to catLengthAngleChamfer.
                | 
                |     Example:
                |         The following example returns in angle the angle of the firstChamfer
                |         chamfer:
                | 
                |          Set angle = firstChamfer.Angle

        :return: Angle
        """

        return Angle(self.com_object.Angle)

    @property
    def elements_to_chamfer(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ElementsToChamfer() As References (Read Only)
                |     Returns the collection of geometrical elements to be
                |     chamfered.
                | 
                |     Example:
                |         The following example returns in list the list of elements of the
                |         firstChamfer chamfer:
                | 
                |          Set list = firstChamfer.ElementsToChamfer

        :return: References
        """

        return References(self.com_object.ElementsToChamfer)

    @property
    def length1(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Length1() As Length (Read Only)
                |     Returns the chamfer first length. This is the first length if the chamfer
                |     is defined by two lengthes, or the chamfer if the chamfer is defined by a
                |     length and an angle.
                | 
                |     Example:
                |         The following example returns in length1 the first length of the
                |         firstChamfer chamfer:
                | 
                |          Set length1 = firstChamfer.Length1

        :return: Length
        """

        return Length(self.com_object.Length1)

    @property
    def length2(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Length2() As Length (Read Only)
                |     Returns the chamfer second length. This is valid only if the chamfer is
                |     defined using two lengthes, that is if the chamfer definition mode
                |     CatChamferMode is set to catTwoLengthChamfer.
                | 
                |     Example:
                |         The following example returns in length2 the second length of the
                |         firstChamfer chamfer:
                | 
                |          Set length2 = firstChamfer.Length2

        :return: Length
        """

        return Length(self.com_object.Length2)

    @property
    def mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Mode() As CatChamferMode
                |     Returns or sets the chamfer definition mode. The chamfer definition mode
                |     enables the chamfer to be defined using either two lengthes or a length and an
                |     angle.
                | 
                |     Example:
                |         The following example returns in mode how the parameters of the
                |         firstChamfer chamfer are defined, and then sets it to
                |         catTwoLengthChamfer:
                | 
                |          Set mode = firstChamfer.Mode
                |          firstChamfer.Mode = catTwoLengthChamfer

        :return: CatChamferMode
        """

        return self.com_object.Mode

    @mode.setter
    def mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.Mode = value

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Orientation() As CatChamferOrientation
                |     Returns or sets the chamfer orientation.
                | 
                |     Example:
                |         The following example returns in orient the orientation mode of the
                |         firstChamfer chamfer, and then sets it to
                |         catReverseChamfer:
                | 
                |          Set orient = firstChamfer.Orientation
                |          firstChamfer.Orientation = catReverseChamfer

        :return: CatChamferOrientation
        """

        return self.com_object.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.Orientation = value

    @property
    def propagation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Propagation() As CatChamferPropagation
                |     Returns or sets the propagation mode of the geometrical elements to be
                |     chamfered.
                | 
                |     Example:
                |         The following example returns in prop the propagation mode of the
                |         firstChamfer chamfer, and then sets it to
                |         catMinimalChamfer:
                | 
                |          Set prop = firstChamfer.Propagation
                |          firstChamfer.Propagation = catMinimalChamfer

        :return: CatChamferPropagation
        """

        return self.com_object.Propagation

    @propagation.setter
    def propagation(self, value: int):
        """
        :param int value:
        """

        self.com_object.Propagation = value

    def add_element_to_chamfer(self, i_element_to_chamfer: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddElementToChamfer(Reference iElementToChamfer)
                |     Adds a new geometrical element to be chamfered.
                | 
                |     Parameters:
                | 
                |         iElementToChamfer
                |             The new element to be chamfered
                |             The following Boundary object is supported: TriDimFeatEdge.
                |             
                | 
                |     Example:
                |         The following example adds the new element element to be chamfered for
                |         the firstChamfer chamfer:
                | 
                |          firstChamfer.AddElementToChamfer(element)

        :param Reference i_element_to_chamfer:
        :return: None
        """
        return self.com_object.AddElementToChamfer(i_element_to_chamfer.com_object)

    def withdraw_element_to_chamfer(self, i_element_to_withdraw: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub WithdrawElementToChamfer(Reference iElementToWithdraw)
                |     Withdraws a geometrical element from those to be
                |     chamfered.
                | 
                |     Parameters:
                | 
                |         iElementToWithdraw
                |             The existing element to withdraw
                |             The following Boundary object is supported: TriDimFeatEdge.
                |             
                | 
                |     Example:
                |         The following example withdraws an existing element element to be
                |         chamfered from the firstChamfer chamfer:
                | 
                |          firstChamfer.WithdrawElementToChamfer(element)

        :param Reference i_element_to_withdraw:
        :return: None
        """
        return self.com_object.WithdrawElementToChamfer(i_element_to_withdraw.com_object)

    def __repr__(self):
        return f'Chamfer(name="{ self.name }")'
