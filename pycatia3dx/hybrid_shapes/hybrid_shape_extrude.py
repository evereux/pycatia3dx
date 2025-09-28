"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeExtrude(HybridShape):

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
                |                         HybridShapeExtrude
                | 
                | The Extrude feature : an Extrude is made up of a face to process and one Extrude parameter.
                | Role: To access the data of the hybrid shape extrude feature
                | object.
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def begin_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property BeginOffset() As Length (Read Only)
                |     Role: To get_BeginOffset on the object. For surface extrude, if limit type
                |     is upto, this offset value is not used. In case of Volume Extrude, if the up-to
                |     element is specified, this will act as offset value from the upto
                |     element.
                | 
                |     Parameters:
                | 
                |         oExtrude
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Length
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: Length
        """

        return Length(self.com_object.BeginOffset)

    @property
    def context(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Context() As long
                |     Returns or sets the context on Extrude feature.
                |     Legal values:
                | 
                |         0 This option creates surface of extrusion.
                |         1 This option creates volume of extrusion.
                | 
                | 
                |     Note: Setting volume result requires GSO License.
                | 
                |     Example:
                |         This example retrieves in oContext the context for the Extrude1 hybrid
                |         shape feature.
                | 
                |          Dim oContext
                |          Set oContext = Extrude1.Context

        :return: int
        """

        return self.com_object.Context

    @context.setter
    def context(self, value: int):
        """
        :param int value:
        """

        self.com_object.Context = value

    @property
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Direction() As HybridShapeDirection
                |     Role: To get_Direction on the object.
                | 
                |     Parameters:
                | 
                |         oDir
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         HybridShapeDirection
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.Direction)

    @direction.setter
    def direction(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.Direction = value

    @property
    def end_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property EndOffset() As Length (Read Only)
                |     Role: To get_EndOffset on the object. For surface extrude, if limit type is
                |     upto, this offset value is not used. In case of Volume Extrude, if the up-to
                |     element is specified, this will act as offset value from the upto
                |     element.
                | 
                |     Parameters:
                | 
                |         oExtrude
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Length
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: Length
        """

        return Length(self.com_object.EndOffset)

    @property
    def extruded_object(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ExtrudedObject() As Reference
                |     Role: To get_ExtrudedObject on the object.
                | 
                |     Parameters:
                | 
                |         oFaceToExtrude
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Reference
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: Reference
        """

        return Reference(self.com_object.ExtrudedObject)

    @extruded_object.setter
    def extruded_object(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ExtrudedObject = value

    @property
    def first_limit_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstLimitType() As long
                |     Returns or sets the First limit type.
                |     Legal values:
                | 
                |     0
                |         Unknown Limit type.
                |     1
                |         Limit type is Dimension. It implies that limit is defined by
                |         length
                |     2
                |         Limit type is UptoElement. It implies that limit is defined by a
                |         geometrical element
                | 
                | Example:
                |     This example retrieves in oLim1Type the first limit type for the Extrude
                |     hybrid shape feature.
                | 
                |      Dim oLim1Type
                |      Set oLim1Type = Extrude.FirstLimitType

        :return: int
        """

        return self.com_object.FirstLimitType

    @first_limit_type.setter
    def first_limit_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.FirstLimitType = value

    @property
    def first_upto_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstUptoElement() As Reference
                |     Returns or sets the First up-to element used to limit
                |     extrusion.
                | 
                |     Example:
                |         This example retrieves in Lim1Elem the First up-to element for the
                |         Extrude hybrid shape feature.
                | 
                |          Dim Lim1Elem As Reference 
                |          Set Lim1Elem = Extrude.FirstUptoElement

        :return: Reference
        """

        return Reference(self.com_object.FirstUptoElement)

    @first_upto_element.setter
    def first_upto_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstUptoElement = value

    @property
    def orientation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Orientation(boolean iOrientation)
                |     Gets or sets orientation of the extrude. Orientation = TRUE : The natural orientation is taken. = FALSE : The opposite orientation is taken This example retrieves in IsInverted orientation of the extrude for the Extrude hybrid shape feature.
                | 
                |      Dim IsInverted As boolean
                |      IsInverted = Extrude.Orientation

        :return: bool
        """

        return self.com_object.Orientation

    @orientation.setter
    def orientation(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Orientation = value

    @property
    def second_limit_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondLimitType() As long
                |     Returns or sets the Second limit type.
                |     Legal values:
                | 
                |     0
                |         Unknown Limit type.
                |     1
                |         Limit type is Dimension. It implies that limit is defined by
                |         length
                |     2
                |         Limit type is UptoElement. It implies that limit is defined by a
                |         geometrical element
                | 
                | Example:
                |     This example retrieves in oLim2Type the second limit type for the Extrude
                |     hybrid shape feature.
                | 
                |      Dim oLim2Type
                |      Set oLim2Type = Extrude.SecondLimitType

        :return: int
        """

        return self.com_object.SecondLimitType

    @second_limit_type.setter
    def second_limit_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SecondLimitType = value

    @property
    def second_upto_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondUptoElement() As Reference
                |     Returns or sets the Second up-to element used to limit
                |     extrusion.
                | 
                |     Example:
                |         This example retrieves in Lim2Elem the Second up-to element for the
                |         Extrude hybrid shape feature.
                | 
                |          Dim Lim2Elem As Reference 
                |          Set Lim2Elem = Extrude.SecondUptoElement

        :return: Reference
        """

        return Reference(self.com_object.SecondUptoElement)

    @second_upto_element.setter
    def second_upto_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondUptoElement = value

    @property
    def symmetrical_extension(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SymmetricalExtension() As boolean
                |     Returns or Sets the Symmetrical Extension of Extrude (Limit 2 = -Limit 1).
                | 
                |     Parameters:
                | 
                |         iSym
                |             Symetry flag

        :return: bool
        """

        return self.com_object.SymmetricalExtension

    @symmetrical_extension.setter
    def symmetrical_extension(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SymmetricalExtension = value

    def __repr__(self):
        return f'HybridShapeExtrude(name="{ self.name }")'
