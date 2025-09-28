"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeDevelop(HybridShape):

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
                |                         HybridShapeDevelop
                | 
                | Represents the hybrid shape develop feature object.
                | Role: To access the data of the hybrid shape develop feature object. This data
                | includes:
                | 
                |     The developing mode
                |     The positining mode used for the 2D wire
                |     The 2D wire to be developed
                |     The positioning transformation
                |     The support revolution surface on which the development is
                |     operated
                |     The point designated as the origin of the planar 2D wire
                |     The direction corresponding to the first axis of the planar axis system
                |     related to the planar 2D wire
                |     The development origin on the support surface
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeDevelop
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Mode() As long
                |     Returns or sets the developing mode.
                |     Legal values:
                | 
                |     CATGSMDevelopMethod_DevDev
                |         Develop / develop algorithm
                |     CATGSMDevelopMethod_DevProj
                |         Develop / project algorithm

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
    def mode_pos(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ModePos() As long
                |     Returns or sets the positioning mode used for the 2D wire.
                |     Legal values:
                | 
                |     CATGSMPositionMode_NoneOrPositioned
                |         No positioning 
                |     CATGSMPositionMode_ExplicitSweep
                |     CATGSMPositionMode_Develop
                |         The 2D wire is to be moved from its initial position

        :return: int
        """

        return self.com_object.ModePos

    @mode_pos.setter
    def mode_pos(self, value: int):
        """
        :param int value:
        """

        self.com_object.ModePos = value

    @property
    def plane_axis_direction(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property PlaneAxisDirection() As Reference
                |     Returns or sets the direction corresponding to the first axis of the planar
                |     axis system related to the planar 2D wire.
                |     Sub-element(s) supported (see Boundary object): RectilinearTriDimFeatEdge,
                |     BiDimFeatEdge or RectilinearMonoDimFeatEdge.

        :return: Reference
        """

        return Reference(self.com_object.PlaneAxisDirection)

    @plane_axis_direction.setter
    def plane_axis_direction(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.PlaneAxisDirection = value

    @property
    def plane_axis_origin(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property PlaneAxisOrigin() As Reference
                |     Returns or sets the point designated as the origin of the planar 2D
                |     wire.
                |     Sub-element(s) supported (see Boundary object): Vertex.

        :return: Reference
        """

        return Reference(self.com_object.PlaneAxisOrigin)

    @plane_axis_origin.setter
    def plane_axis_origin(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.PlaneAxisOrigin = value

    @property
    def point_on_support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property PointOnSupport() As Reference
                |     Returns or sets the development origin on the support
                |     surface.
                |     Sub-element(s) supported (see Boundary object): Vertex.

        :return: Reference
        """

        return Reference(self.com_object.PointOnSupport)

    @point_on_support.setter
    def point_on_support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.PointOnSupport = value

    @property
    def positioned_wire(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property PositionedWire() As Reference
                |     Returns or sets the positioning transformation.
                |     Role: To retrieve or set the positioning transformation associated to the
                |     develop feature and which result corresponds to the positioned 2D wire.

        :return: Reference
        """

        return Reference(self.com_object.PositionedWire)

    @positioned_wire.setter
    def positioned_wire(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.PositionedWire = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Support() As Reference
                |     Returns or sets the support revolution surface on which the development is
                |     operated.
                |     Sub-element(s) supported (see Boundary object): Face.

        :return: Reference
        """

        return Reference(self.com_object.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Support = value

    @property
    def wire_to_develop(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property WireToDevelop() As Reference
                |     Returns or sets the 2D wire to be developed.
                |     Sub-element(s) supported (see Boundary object): TriDimFeatEdge or
                |     BiDimFeatEdge.

        :return: Reference
        """

        return Reference(self.com_object.WireToDevelop)

    @wire_to_develop.setter
    def wire_to_develop(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.WireToDevelop = value

    def get_plane_axis_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPlaneAxisAngle() As Angle
                |     Retrieves the rotation angle.
                |     Role: The rotation angle is expressed in the planar coordinate system
                |     related to the 2D planar wire from its default position.
                | 
                |     Returns:
                |         The rotation value

        :return: Angle
        """
        return Angle(self.com_object.GetPlaneAxisAngle())

    def get_plane_axis_coord(self, i_coor_idx: int) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPlaneAxisCoord(long iCoorIdx) As Length
                |     Retrieves the translation coordinates.
                |     Role: The translation coordinates are expressed with respect to the planar
                |     coordinate system related to the 2D planar wire from its default position.
                |     GetPlaneAxisCoord retrieves one coordinate at a time.
                | 
                |     Parameters:
                | 
                |         iCoorIdx
                |             The coordinate index
                |             Legal values
                |             : 1 for X and 2 for Y 
                | 
                |     Returns:
                |         The coordinate value

        :param int i_coor_idx:
        :return: Length
        """
        return Length(self.com_object.GetPlaneAxisCoord(i_coor_idx))

    def get_plane_axis_swap_axes(self, ii: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPlaneAxisSwapAxes(long ii) As long
                |     Retrieves the inversion axes from their previous
                |     definitions.
                | 
                |     Parameters:
                | 
                |         iI
                |             == NOT USED YET == Must always be set to 0 
                | 
                |     Returns:
                |         The inversion value
                |         Legal values:
                | 
                |         CATGSMAxisInversionMode_None
                |             No axis inverted 
                |         CATGSMAxisInversionMode_X
                |             Only the X axis is inverted
                |         CATGSMAxisInversionMode_Y
                |             Only the Y axis is inverted
                |         CATGSMAxisInversionMode_Both
                |             Both axes are inverted

        :param int ii:
        :return: int
        """
        return self.com_object.GetPlaneAxisSwapAxes(ii)

    def set_plane_axis_angle(self, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPlaneAxisAngle(double iAngle)
                |     Sets the rotation angle.
                |     Role: The rotation angle is expressed in the planar coordinate system
                |     related to the 2D planar wire from its default position.
                | 
                |     Parameters:
                | 
                |         iAngle
                |             The rotation angle value.

        :param float i_angle:
        :return: None
        """
        return self.com_object.SetPlaneAxisAngle(i_angle)

    def set_plane_axis_coord(self, i_coor_idx: int, i_coord_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPlaneAxisCoord(long iCoorIdx,double iCoordValue)
                |     Sets the translation coordinates.
                |     Role: The translation coordinates are expressed with respect to the planar
                |     coordinate system related to the 2D planar wire from its default position.
                |     SetPlaneAxisCoord sets one coordinate at a time.
                | 
                |     Parameters:
                | 
                |         iCoorIdx
                |             The coordinate index
                |             Legal values
                |             : 1 for X and 2 for Y 
                |         iCoordValue
                |             The coordinate value

        :param int i_coor_idx:
        :param float i_coord_value:
        :return: None
        """
        return self.com_object.SetPlaneAxisCoord(i_coor_idx, i_coord_value)

    def set_plane_axis_swap_axes(self, i_idx: int, i_inversion_value: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPlaneAxisSwapAxes(long iIdx,long iInversionValue)
                |     Sets the inversion axes from their previous definitions.
                | 
                |     Parameters:
                | 
                |         iIdx
                |             == NOT USED YET == Must always be set to 0 
                |         iInversionValue
                |             The inversion value
                |             Legal values:
                | 
                |             CATGSMAxisInversionMode_None
                |                 No axis inverted 
                |             CATGSMAxisInversionMode_X
                |                 Only the X axis is inverted
                |             CATGSMAxisInversionMode_Y
                |                 Only the Y axis is inverted
                |             CATGSMAxisInversionMode_Both
                |                 Both axes are inverted

        :param int i_idx:
        :param int i_inversion_value:
        :return: None
        """
        return self.com_object.SetPlaneAxisSwapAxes(i_idx, i_inversion_value)

    def __repr__(self):
        return f'HybridShapeDevelop(name="{ self.name }")'
