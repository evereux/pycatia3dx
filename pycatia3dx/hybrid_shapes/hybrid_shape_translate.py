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


class HybridShapeTranslate(HybridShape):

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
                |                         HybridShapeTranslate
                | 
                | Represents the hybrid shape translate feature object.
                | Role: To access the data of the hybrid shape translate feature object. This
                | data includes:
                | 
                |     The element to translate
                |     The translation direction
                |     The translation distance and its value
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
                | 
                | Use the CATIAHybridShapeFactory to create HybridShapeFeature
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def coord_x_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CoordXValue() As double
                |     Returns or sets the translate X coordinate value.

        :return: float
        """

        return self.com_object.CoordXValue

    @coord_x_value.setter
    def coord_x_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.CoordXValue = value

    @property
    def coord_y_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CoordYValue() As double
                |     Returns or sets the translate Y coordinate value.

        :return: float
        """

        return self.com_object.CoordYValue

    @coord_y_value.setter
    def coord_y_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.CoordYValue = value

    @property
    def coord_z_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CoordZValue() As double
                |     Returns or sets the translate Z coordinate value.

        :return: float
        """

        return self.com_object.CoordZValue

    @coord_z_value.setter
    def coord_z_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.CoordZValue = value

    @property
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Direction() As HybridShapeDirection
                |     Returns or sets the translate direction.
                | 
                |     Example
                |         This example retrieves in Dir the translation direction for the
                |         Translate hybrid shape feature.
                | 
                |          Dim Dir As CATIAHybridShapeDirection
                |          Set Dir=Translate.Direction

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
    def distance(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Distance() As Length (Read Only)
                |     Returns the translate distance.

        :return: Length
        """

        return Length(self.com_object.Distance)

    @property
    def distance_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property DistanceValue() As double
                |     Returns or sets the translate distance value.
                | 
                |     Example
                |         This example retrieves in DistVal the translation distance value for
                |         the Translate hybrid shape feature.
                | 
                |          Dim DistVal As double
                |          Set DistVal =Translate.DistanceValue

        :return: float
        """

        return self.com_object.DistanceValue

    @distance_value.setter
    def distance_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.DistanceValue = value

    @property
    def elem_to_translate(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ElemToTranslate() As Reference
                |     Returns or sets the element to translate.
                | 
                |     Example
                |         This example retrieves in Element the element to be translated for the
                |         Translate hybrid shape feature.
                | 
                |          Dim Element As Reference
                |          Set Element=Translate.ElemToTranslate

        :return: Reference
        """

        return Reference(self.com_object.ElemToTranslate)

    @elem_to_translate.setter
    def elem_to_translate(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ElemToTranslate = value

    @property
    def first_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstPoint() As Reference
                |     Returns or sets the first point defining the translation.

        :return: Reference
        """

        return Reference(self.com_object.FirstPoint)

    @first_point.setter
    def first_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstPoint = value

    @property
    def ref_axis_system(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RefAxisSystem() As Reference
                |     Returns or Sets the reference Axis System for Translate
                |     feature.
                |     This data is not mandatory, if element is null, the absolute axis system is
                |     taken.
                |     When an element is given, X, Y and Z are considered in this Axis system.
                |     
                | Example
                | :
                |     This example retrieves in oRefAxis the reference Axis System for Translate
                |     feature.
                | 
                |      Dim oRefAxis As CATIAReference
                |      Set oRefAxis  = Translate.RefAxisSystem

        :return: Reference
        """

        return Reference(self.com_object.RefAxisSystem)

    @ref_axis_system.setter
    def ref_axis_system(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.RefAxisSystem = value

    @property
    def second_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondPoint() As Reference
                |     Returns or sets the second point defining the translation.

        :return: Reference
        """

        return Reference(self.com_object.SecondPoint)

    @second_point.setter
    def second_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondPoint = value

    @property
    def vector_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property VectorType() As long
                |     Returns or sets the way the translation vector is defined.
                | 
                |         0= Direction + distance
                |         1= point + points
                |         2= coordinates
                |         3= Unknown type

        :return: int
        """

        return self.com_object.VectorType

    @vector_type.setter
    def vector_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.VectorType = value

    @property
    def volume_result(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property VolumeResult() As boolean
                |     Returns or sets the volume result.
                |     Legal values: True if the result of translation is required as volume
                |     (option is effective only in case of volumes,requires GSO License) and False if
                |     it is needed as surface .
                | 
                |     Example:
                | 
                |          This example sets that the result of
                |          the hybShpTranslate hybrid shape translate is volume.
                |          
                | 
                |          hybShpTranslate.VolumeResult = True

        :return: bool
        """

        return self.com_object.VolumeResult

    @volume_result.setter
    def volume_result(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.VolumeResult = value

    def get_creation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetCreationMode() As long
                |     Gets the creation mode.
                |     Legal values:
                | 
                |     0
                |         CATGSMTransfoModeUnset. Default behavior: creation mode by default for
                |         all features, modification mode for axis system
                |     1
                |         CATGSMTransfoModeCreation. Creation mode. 
                |     2
                |         CATGSMTransfoModeModification. Modification mode. 
                | 
                | Example:
                |     This example retrieves in oCreation the creation mode for the
                |     hybShpTranslate hybrid shape feature.
                | 
                |      oCreation = hybShpTranslate.GetCreationMode

        :return: int
        """
        return self.com_object.GetCreationMode()

    def set_creation_mode(self, i_creation: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetCreationMode(boolean iCreation)
                |     Sets the creation mode(creation or modification).
                |     Legal values: True if the result is a creation feature and False if the
                |     result is a modification feature.
                | 
                |     Example:
                | 
                |          This example sets that the mode of
                |          the hybShpTranslate hybrid shape translate to
                |          creation
                |          
                | 
                |          hybShpTranslate.SetCreationMode True

        :param bool i_creation:
        :return: None
        """
        return self.com_object.SetCreationMode(i_creation)

    def __repr__(self):
        return f'HybridShapeTranslate(name="{ self.name }")'
