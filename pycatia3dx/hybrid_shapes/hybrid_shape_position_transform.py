"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapePositionTransform(HybridShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         HybridShapePositionTransfo
                | 
                | Represents the hybrid shape position transformation feature
                | object.
                | Role: To access the data of the hybrid shape position transformation feature
                | object. This data includes:
                | 
                |     The positioning mode
                |     The profile to be positioned
                |     The initila and target planes
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapePositionTransfo
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def initial_direction_computation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property InitialDirectionComputationMode() As long
                |     Gets or sets the computation mode of the X axis (or direction) of the
                |     initial axis system.
                | 
                |     Parameters:
                | 
                |         oDirCompMode
                |             computation mode = 0 : no X axis specified = 1 : the X axis is implicitly the tangent of the profile at the origin(the origin then HAS to be on the profile). = 2 : the X axis is specified by a direction by SetPositionDirection(1,UserInputDirection).

        :return: int
        """

        return self.com_object.InitialDirectionComputationMode

    @initial_direction_computation_mode.setter
    def initial_direction_computation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.InitialDirectionComputationMode = value

    @property
    def mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Mode() As long
                |     Returns or sets the positioning mode.
                |     Legal values:
                | 
                |     CATGSMPositionMode_NoneOrPositioned
                |         No positioning
                |     CATGSMPositionMode_ExplicitSweep
                |         The explicit profile is to be moved from its initial plane to the first
                |         sweep plane
                |     CATGSMPositionMode_Develop

        :return: int
        """

        return self.com_object.Mode

    @mode.setter
    def mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.Mode = value

    @property
    def profile(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Profile() As Reference
                |     Returns or sets the profile to be positioned.

        :return: Reference
        """

        return Reference(self.com_object.Profile)

    @profile.setter
    def profile(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Profile = value

    def get_nb_pos_angle(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetNbPosAngle() As long
                |     Gets the number of numerical positioning parameters : first axis direction angles.
                | 
                |     Parameters:
                | 
                |         oI
                |             Number of parameters

        :return: int
        """
        return self.com_object.GetNbPosAngle()

    def get_nb_pos_coord(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetNbPosCoord() As long
                |     Gets the number of numerical positioning parameters : origin planar coordinates.
                | 
                |     Parameters:
                | 
                |         oI
                |             Number of parameters

        :return: int
        """
        return self.com_object.GetNbPosCoord()

    def get_pos_angle(self, i_i: int) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPosAngle(long iI) As Angle
                |     Returns angles of both initial and target coordinate systems from default
                |     positions.
                | 
                |     Parameters:
                | 
                |         iI
                |             The index of numerical positioning angles in initial (value 1) or
                |             target (value 2) axis system. 
                |         oAngle
                |             The angle value.

        :param int i_i:
        :return: Angle
        """
        return Angle(self.com_object.GetPosAngle(i_i))

    def get_pos_coord(self, ii: int) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPosCoord(long ii) As Length
                |     Returns translation coordinates if both initial and target coordinate
                |     systems from default positions.
                | 
                |     Parameters:
                | 
                |         iI
                |             The iIndex of numerical positioning coordinates in initial (value 1
                |             or 2) or target (value 3 or 4) coordinate system. 
                |         oCoordinate
                |             The coordinate value

        :param int ii:
        :return: Length
        """
        return Length(self.com_object.GetPosCoord(ii))

    def get_pos_point(self, ii: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPosPoint(long ii) As Reference
                |     Returns the points designated as the origins of the initial and target
                |     planes.
                | 
                |     Parameters:
                | 
                |         iI
                |             The plane index: 1 for initial one, 2 for target one
                |             
                |         oElem
                |             The origin point

        :param int ii:
        :return: Reference
        """
        return Reference(self.com_object.GetPosPoint(ii))

    def get_pos_swap_axes(self, ii: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPosSwapAxes(long ii) As long
                |     Returns axis inversion from previous definitions for both initial and
                |     target planes.
                | 
                |     Parameters:
                | 
                |         iI
                |             The coordinate system index: 1 for initial one, 2 for target one
                |             
                |         oInversion
                |             The inversion value:
                | 
                |             CATGSMAxisInversionMode_None
                |                 No axis inverted
                |             CATGSMAxisInversionMode_X
                |                 Only the X axis iq inverted
                |             CATGSMAxisInversionMode_Y
                |                 Only the Y axis is inverted
                |             CATGSMAxisInversionMode_Both
                |                 Both axes inverted

        :param int ii:
        :return: int
        """
        return self.com_object.GetPosSwapAxes(ii)

    def get_position_direction(self, i_i: int) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPositionDirection(long iI) As HybridShapeDirection
                |     Returns the positioning directions.
                |     The positioning direction can be initial or target plane X-axis
                |     direction.
                | 
                |     Parameters:
                | 
                |         iI
                |             The plane index: 1 for initial one, 2 for target one
                |             
                |         oElem
                |             The direction element

        :param int i_i:
        :return: HybridShapeDirection
        """
        return HybridShapeDirection(self.com_object.GetPositionDirection(i_i))

    def remove_all_pos_angle(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveAllPosAngle()
                |     Removes all numerical positioning parameters : first axis direction angles.

        :return: None
        """
        return self.com_object.RemoveAllPosAngle()

    def remove_all_pos_coord(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveAllPosCoord()
                |     Removes all numerical positioning parameters : origin planar coordinates.

        :return: None
        """
        return self.com_object.RemoveAllPosCoord()

    def set_pos_angle(self, i_i: int, i_angle: Angle) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPosAngle(long iI,Angle iAngle)
                |     Sets angles of both initial and target coordinate systems.
                | 
                |     Parameters:
                | 
                |         iI
                |             The index of numerical positioning angles in initial (value 1) or
                |             target (value 2) axis system. 
                |         iAngle
                |             The angle value.

        :param int i_i:
        :param Angle i_angle:
        :return: None
        """
        return self.com_object.SetPosAngle(i_i, i_angle.com_object)

    def set_pos_coord(self, i_i: int, i_coordinate: Length) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPosCoord(long iI,Length iCoordinate)
                |     Sets translation coordinates of both initial and target coordinate
                |     systems.
                | 
                |     Parameters:
                | 
                |         iI
                |             The iIndex of numerical positioning coordinates in initial (value 1
                |             or 2) or target (value 3 or 4) coordinate system. 
                |         iCoordinate
                |             The coordinate value

        :param int i_i:
        :param Length i_coordinate:
        :return: None
        """
        return self.com_object.SetPosCoord(i_i, i_coordinate.com_object)

    def set_pos_point(self, i_i: int, i_elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPosPoint(long iI,Reference iElem)
                |     Sets the points designated as the origins of the initial and target
                |     planes.
                | 
                |     Parameters:
                | 
                |         iI
                |             The plane index: 1 for initial one, 2 for target one
                |             
                |         iElem
                |             The origin point

        :param int i_i:
        :param Reference i_elem:
        :return: None
        """
        return self.com_object.SetPosPoint(i_i, i_elem.com_object)

    def set_pos_swap_axes(self, ii: int, i_inversion: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPosSwapAxes(long ii,long iInversion)
                |     Sets axis inversion from previous definitions for both initial and target
                |     planes.
                | 
                |     Parameters:
                | 
                |         iI
                |             The coordinate system index: 1 for initial one, 2 for target one
                |             
                |         iInversion
                |             The inversion value:
                | 
                |             CATGSMAxisInversionMode_None
                |                 No axis inverted
                |             CATGSMAxisInversionMode_X
                |                 Only the X axis iq inverted
                |             CATGSMAxisInversionMode_Y
                |                 Only the Y axis is inverted
                |             CATGSMAxisInversionMode_Both
                |                 Both axes inverted

        :param int ii:
        :param int i_inversion:
        :return: None
        """
        return self.com_object.SetPosSwapAxes(ii, i_inversion)

    def set_position_direction(self, i_i: int, i_elem: HybridShapeDirection) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPositionDirection(long iI,HybridShapeDirection iElem)
                |     Sets the positioning directions.
                |     The positioning direction can be initial or target plane X-axis
                |     direction.
                | 
                |     Parameters:
                | 
                |         iI
                |             The plane index: 1 for initial one, 2 for target one
                |             
                |         iElem
                |             The direction element

        :param int i_i:
        :param HybridShapeDirection i_elem:
        :return: None
        """
        return self.com_object.SetPositionDirection(i_i, i_elem.com_object)

    def __repr__(self):
        return f'HybridShapePositionTransfo(name="{ self.name }")'
