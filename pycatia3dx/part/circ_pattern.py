"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.int_param import IntParam
from pycatia3dx.mode.reference import Reference
from pycatia3dx.todo_part.angular_repartition import AngularRepartition
from pycatia3dx.todo_part.linear_repartition import LinearRepartition
from pycatia3dx.todo_part.pattern import Pattern


class CircPattern(Pattern):

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
                |                             CATPartIDLItf.Pattern
                |                                 CircPattern
                | 
                | Represents the circular pattern.
                | The shape is duplicated along concentric circles to build crowns. A linear
                | repartition object defines the duplication along radial directions, thus
                | determining the number of crowns. An angular repartition object defines the
                | duplication on the crowns.
                | 
                | See also:
                |     LinearRepartition, AngularRepartition
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def angular_direction_row(self) -> IntParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AngularDirectionRow() As IntParam (Read Only)
                |     Returns the position of the shape to be copied along the angular
                |     direction.
                | 
                |     Example:
                |         The following example returns in AngularDirPos the position of the
                |         shape to be copied along the angular direction.
                | 
                |          Set AngularDirPos = firstPattern.AngularDirectionRow

        :return: IntParam
        """

        return IntParam(self.com_object.AngularDirectionRow)

    @property
    def angular_repartition(self) -> AngularRepartition:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AngularRepartition() As AngularRepartition (Read
                | Only)
                |     Returns the angular repartition. The angular repartition is the repartition
                |     on a crown.
                | 
                |     Example:
                |         The following example returns in repartA the angular repartition of the
                |         circular pattern firstPattern:
                | 
                |          Set repartA = firstPattern.AngularRepartition

        :return: AngularRepartition
        """

        return AngularRepartition(self.com_object.AngularRepartition)

    @property
    def circular_pattern_parameters(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CircularPatternParameters() As
                | CatCircularPatternParameters
                |     Returns or sets the circular pattern parameters required to define the
                |     pattern. These parameters are used when reading the CATIAAngularRepartition
                |     properties.
                | 
                |     Example:
                |         The following example returns in parameters the circular pattern
                |         parameters of the firstPattern circular pattern, and then sets it to
                |         catCompleteCrown, so that only the number of instances is used to define the
                |         Pattern:
                | 
                |          Set parameters = firstPattern.CircularPatternParameters
                |          Set firstPattern.CircularPatternParameters = catCompleteCrown

        :return: CatCircularPatternParameters
        """

        return self.com_object.CircularPatternParameters

    @circular_pattern_parameters.setter
    def circular_pattern_parameters(self, value: int):
        """
        :param int value:
        """

        self.com_object.CircularPatternParameters = value

    @property
    def radial_alignment(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RadialAlignment() As boolean
                |     Returns or sets whether the copied shapes should be rotated or radial
                |     aligned with respect to the original one.
                |     True if the copied shapes are rotated.
                | 
                |     Example:
                |         The following example returns in alignedR the radial alignment of the
                |         circular pattern firstPattern, and then sets it to
                |         False:
                | 
                |          Set alignedR = firstPattern.RadialAlignment
                |          firstPattern.RadialAlignment = False

        :return: bool
        """

        return self.com_object.RadialAlignment

    @radial_alignment.setter
    def radial_alignment(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.RadialAlignment = value

    @property
    def radial_direction_row(self) -> IntParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RadialDirectionRow() As IntParam (Read Only)
                |     Returns the position of the shape to be copied along the radial
                |     direction.
                | 
                |     Example:
                |         The following example returns in RadialDirPos the position of the shape
                |         to be copied along the radial direction.
                | 
                |          Set RadialDirPos = firstPattern.RadialDirectionRow

        :return: IntParam
        """

        return IntParam(self.com_object.RadialDirectionRow)

    @property
    def radial_repartition(self) -> LinearRepartition:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RadialRepartition() As LinearRepartition (Read Only)
                |     Returns the radial repartition. The radial repartition is the repartition
                |     along a radius.
                | 
                |     Example:
                |         The following example returns in repartR the radial repartition of the
                |         circular pattern firstPattern:
                | 
                |          Set repartR = firstPattern.RadialRepartition

        :return: LinearRepartition
        """

        return LinearRepartition(self.com_object.RadialRepartition)

    @property
    def rotation_orientation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RotationOrientation() As boolean
                |     Returns or sets whether the shapes are copied clockwise on the crowns with
                |     respect to the rotation axis direction.
                |     True if the shapes are copied counterclockwise when the rotation axis
                |     direction goes towards you when you look at the crown.
                | 
                |     Example:
                |         The following example returns in alignedAxis whether the circular
                |         pattern firstPattern is built clockwise, and then sets it to
                |         True:
                | 
                |          alignedAxis = firstPattern.RotationOrientation
                |          firstPattern.RotationOrientation = True

        :return: bool
        """

        return self.com_object.RotationOrientation

    @rotation_orientation.setter
    def rotation_orientation(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.RotationOrientation = value

    def get_rotation_axis(self, io_rotation_axis: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetRotationAxis(CATSafeArrayVariant ioRotationAxis)
                |     Returns the rotation axis. The rotation axis is returned as an array
                |     containing the rotation axis vector components. Assume this array is
                |     oRotationAxis. It contains:
                | 
                |     oRotationAxis[0],oRotationAxis[1],oRotationAxis[2]
                |         The X, Y, and Z rotation axis vector components 
                | 
                |     Example:
                |         The following example returns in axisArray the rotation axis components
                |         of the circular pattern firstPattern:
                | 
                |          Call firstPattern.GetRotationAxis(axisArray)
                |          Set x = axisArray[0]
                |          Set y = axisArray[1]
                |          Set z = axisArray[2]

        :param tuple io_rotation_axis:
        :return: None
        """
        return self.com_object.GetRotationAxis(io_rotation_axis)

    def get_rotation_center(self, io_rotation_center: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetRotationCenter(CATSafeArrayVariant ioRotationCenter)
                |     Returns the rotation center if the user defined it. Returns E_FAIL if no
                |     rotation center has been defined The rotation center is returned as an array
                |     containing the rotation center coordinates. Assume this array is
                |     oRotationCenter. It contains:
                | 
                |     oRotationCenter[0],oRotationCenter[1],oRotationCenter[2]
                |         The X, Y, and Z rotation center coordinates 
                | 
                |     Example:
                |         The following example returns in centerArray the rotation center
                |         coordinates of the circular pattern firstPattern, and saves them in
                |         variables:
                | 
                |          Call firstPattern.GetRotationCenter(centerArray)
                |          x = centerArray[0]
                |          y = centerArray[1]
                |          z = centerArray[2]

        :param tuple io_rotation_center:
        :return: None
        """
        return self.com_object.GetRotationCenter(io_rotation_center)

    def get_stagger_pattern_choice(self, o_stagger_patt_choice: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetStaggerPatternChoice(boolean oStaggerPattChoice)
                |     Returns if user wants to have stagger pattern
                |     configuration.
                | 
                |     Parameters:
                | 
                |         oStaggerPattChoice[out]
                | 
                |             TRUE indicates Stagger pattern configuration.
                |             FALSE indicates conventional circular pattern configuration.

        :param bool o_stagger_patt_choice:
        :return: None
        """
        return self.com_object.GetStaggerPatternChoice(o_stagger_patt_choice)

    def get_stagger_step_value(self, o_stagger_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetStaggerStepValue(double oStaggerAngle)
                |     Returns the value of the Stagger angle.

        :param float o_stagger_angle:
        :return: None
        """
        return self.com_object.GetStaggerStepValue(o_stagger_angle)

    def set_instance_angular_spacing(self, i_instance_number: int, i_angular_spacing: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetInstanceAngularSpacing(long iInstanceNumber,double
                | iAngularSpacing)
                |     Sets the InstanceAngularSpacing.
                | 
                |     Parameters:
                | 
                |         iInstanceNumber
                |             The Instance Number 
                |         iAngularSpacing
                |             The Angular Spacing 
                | 
                |     Example:
                |         The following example sets the InstanceAngularSpacing of the circular
                |         pattern

        :param int i_instance_number:
        :param float i_angular_spacing:
        :return: None
        """
        return self.com_object.SetInstanceAngularSpacing(i_instance_number, i_angular_spacing)

    def set_rotation_axis(self, i_rotation_axis: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRotationAxis(Reference iRotationAxis)
                |     Sets the rotation axis.
                | 
                |     Parameters:
                | 
                |         iRotationAxis
                |             The rotation axis. It is passed as reference and can be valuated
                |             with a line, an edge or a plane reference: in this case the plane normal is
                |             taken into account.
                |             The following Boundary objects are supported: PlanarFace,
                |             CylindricalFace RectilinearTriDimFeatEdge and RectilinearBiDimFeatEdge.
                |             
                | 
                |     Example:
                |         The following example sets the rotation axis of the circular pattern
                |         firstPattern with the refLine1 reference:
                | 
                |          firstPattern.SetRotationAxis refLine1

        :param Reference i_rotation_axis:
        :return: None
        """
        return self.com_object.SetRotationAxis(i_rotation_axis.com_object)

    def set_rotation_center(self, i_rotation_center: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRotationCenter(Reference iRotationCenter)
                |     Sets the rotation center.
                | 
                |     Parameters:
                | 
                |         iRotationCenter
                |             The rotation center 
                | 
                |     Example:
                |         The following example sets the rotation center of the circular pattern
                |         firstPattern with point1Ref point:
                | 
                |          firstPattern.SetRotationCenter point1Ref

        :param Reference i_rotation_center:
        :return: None
        """
        return self.com_object.SetRotationCenter(i_rotation_center.com_object)

    def set_stagger_pattern_choice(self, i_stagger_patt_choice: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetStaggerPatternChoice(boolean iStaggerPattChoice)
                |     Sets the choice of creation of stagger pattern
                |     configuration.
                | 
                |     Parameters:
                | 
                |         iStaggerPattChoice[in]
                | 
                |             Legal values:
                |             TRUE indicates Stagger pattern configuration.
                |             FALSE indicates conventional circular pattern configuration.

        :param bool i_stagger_patt_choice:
        :return: None
        """
        return self.com_object.SetStaggerPatternChoice(i_stagger_patt_choice)

    def set_stagger_step_value(self, i_stagger_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetStaggerStepValue(double iStaggerAngle)
                |     Sets the value of the Stagger angle.

        :param float i_stagger_angle:
        :return: None
        """
        return self.com_object.SetStaggerStepValue(i_stagger_angle)

    def set_unequal_instance_number(self, i_instance_number: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetUnequalInstanceNumber(long iInstanceNumber)
                |     Sets the Instance Number.
                | 
                |     Parameters:
                | 
                |         iInstanceNumber
                |             The Instance Number 
                | 
                |     Example:
                |         The following example modifies the instance number for unequal angular
                |         spacing

        :param int i_instance_number:
        :return: None
        """
        return self.com_object.SetUnequalInstanceNumber(i_instance_number)

    def set_unequal_step(self, i_instance_number: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetUnequalStep(long iInstanceNumber)
                |     This method is deprecated Sets the UnequalStep.
                | 
                |     Parameters:
                | 
                |         iInstanceNumber
                |             The Instance Number 
                | 
                |     Example:
                |         The following example creates the number of pattern spacing objects in
                |         pattern object 

        :param int i_instance_number:
        :return: None
        """
        return self.com_object.SetUnequalStep(i_instance_number)

    def __repr__(self):
        return f'CircPattern(name="{ self.name }")'
