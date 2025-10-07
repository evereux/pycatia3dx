"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mode.reference import Reference
from pycatia3dx.part.surface_based_shape import SurfaceBasedShape


class SewSurface(SurfaceBasedShape):

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
                |                         CATPartIDLItf.SurfaceBasedShape
                |                             SewSurface
                | 
                | Represents the sewing operation.
                | It sews a shape using a sewing element, such as a surface or a
                | face
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def deviation(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Deviation() As double
                |     Sets or Gets the maximum deviation allowed for smoothing operation in
                |     sewing command. This value must be set in SI unit (m).
                | 
                |     Example: This example retrieves in DeviationValue the maximum deviation
                |     value for the Sewfeature.
                | 
                |      Dim DeviationValue As double
                |      Set DeviationValue = Sew.MaximumDeviationValue

        :return: float
        """

        return self.com_object.Deviation

    @deviation.setter
    def deviation(self, value: float):
        """
        :param float value:
        """

        self.com_object.Deviation = value

    @property
    def deviation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DeviationMode() As long
                |     Returns or sets the Deviation mode taken into account during Sew
                |     construction.
                |     Legal values:
                | 
                |     0
                |         Unknown Deviation mode.
                |     1
                |         None Deviation mode. Error thrown if maximum deviation exceeds CATIA
                |         resolution.
                |     2
                |         Automatic Deviation mode. Error thrown if maximum deviation exceeds 100
                |         times CATIA resolution.
                |     3
                |         Manual Deviation mode. Error thrown if maximum deviation exceeds input
                |         user deviation.
                | 
                |     Example:
                |         This example retrieves in oMode the Deviation mode for the Sew
                |         feature.
                | 
                |          Dim oMode
                |          Set oMode = Sew.DeviationMode

        :return: int
        """

        return self.com_object.DeviationMode

    @deviation_mode.setter
    def deviation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.DeviationMode = value

    @property
    def sewing_intersection_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SewingIntersectionMode() As CatSewingIntersectionMode
                |     Returns or sets the sewing mode . The sewing side is the side of the body
                |     kept after the sewing. A positive side refers to the same orientation than the
                |     sewing element normal vector.
                | 
                |     Example:
                |         The following example returns in sptSide the sewing side of the sew
                |         shape mySew, and then sets it to catPositiveSide:
                | 
                |          Set sptSide = mySew.SewingSide
                |          mySew.SewingSide = catPositiveSide

        :return: CatSewingIntersectionMode
        """

        return self.com_object.SewingIntersectionMode

    @sewing_intersection_mode.setter
    def sewing_intersection_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.SewingIntersectionMode = value

    @property
    def sewing_side(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SewingSide() As CatSplitSide
                |     Returns or sets the sewing side . The sewing side is the side of the body
                |     kept after the sewing. A positive side refers to the same orientation than the
                |     sewing element normal vector.
                | 
                |     Example:
                |         The following example returns in sptSide the sewing side of the sew
                |         shape mySew, and then sets it to catPositiveSide:
                | 
                |          Set sptSide = mySew.SewingSide
                |          mySew.SewingSide = catPositiveSide

        :return: CatSplitSide
        """

        return self.com_object.SewingSide

    @sewing_side.setter
    def sewing_side(self, value: int):
        """
        :param int value:
        """

        self.com_object.SewingSide = value

    def set_surface_support(self, i_support_surface: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSurfaceSupport(Reference iSupportSurface)
                |     Sets the surface support for surfacic sew surface.
                | 
                |     Parameters:
                | 
                |         iSupportSurface
                |             A Reference object to a surface (see Reference for more
                |             information)

        :param Reference i_support_surface:
        :return: None
        """
        return self.com_object.SetSurfaceSupport(i_support_surface.com_object)

    def set_volume_support(self, i_volume: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetVolumeSupport(Reference iVolume)
                |     Sets the volume support for volume sew surface.
                | 
                |     Parameters:
                | 
                |         iVolume
                |             A Reference object to a volume (see Reference for more
                |             information)
                | 
                |             Example:
                |                 The following example sets the volume support of SewSurface
                |                 firstSewSurface to volumeExtrude volume reference
                |                 :
                | 
                |                  firstSewSurface.SetVolumeSupport
                |                  volumeExtrudeRef

        :param Reference i_volume:
        :return: None
        """
        return self.com_object.SetVolumeSupport(i_volume.com_object)

    def __repr__(self):
        return f'SewSurface(name="{ self.name }")'
