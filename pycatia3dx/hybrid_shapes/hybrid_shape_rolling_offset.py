"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeRollingOffset(HybridShape):

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
                |                         HybridShapeRollingOffset
                | 
                | The RollingOffset feature
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def offset(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Offset() As Length (Read Only)
                |     Role: To get_Offset on the object.
                | 
                |     Parameters:
                | 
                |         oOffset
                |             offset value return value for CATScript applications, with
                |             (IDLRETVAL) function type 
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

        return Length(self.com_object.Offset)

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Support() As Reference
                |     Role: To manage the support on the object.
                | 
                |     Parameters:
                | 
                |         iSupport
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

        return Reference(self.com_object.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Support = value

    def get_curve(self, i_pos: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func getCurve(long iPos) As Reference
                |     Role: To get_Curve on the object.
                | 
                |     Parameters:
                | 
                |         iPos
                |             Position 
                | 
                |     See also:
                |         long
                |     Parameters:
                | 
                |         oCurve
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

        :param int i_pos:
        :return: Reference
        """
        return Reference(self.com_object.getCurve(i_pos))

    def get_nb_curve(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func getNbCurve() As long
                |     Role: To get_NbCurve on the object.
                | 
                |     Parameters:
                | 
                |         CurvesNb
                |             Number of curves 
                | 
                |     See also:
                |         long
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: int
        """
        return self.com_object.getNbCurve()

    def get_offset(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func getOffset() As double
                |     Role: To getOffset on the object.
                | 
                |     Parameters:
                | 
                |         oOffset
                |             offset value 
                | 
                |     See also:
                |         double
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: float
        """
        return self.com_object.getOffset()

    def put_curve(self, i_curve: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub putCurve(Reference iCurve)
                |     Role: To add or remove a curve on the object.
                | 
                |     Parameters:
                | 
                |         iCurve
                |             Curve to Add/Remove if not present in the list, or to remove.
                |             
                | 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :param Reference i_curve:
        :return: None
        """
        return self.com_object.putCurve(i_curve.com_object)

    def put_offset(self, i_offset: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub putOffset(double iOffset)
                |     Role: To put_Offset on the object.
                | 
                |     Parameters:
                | 
                |         iOffset
                |             offset value 
                | 
                |     See also:
                |         double
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :param float i_offset:
        :return: None
        """
        return self.com_object.putOffset(i_offset)

    def __repr__(self):
        return f'HybridShapeRollingOffset(name="{ self.name }")'
