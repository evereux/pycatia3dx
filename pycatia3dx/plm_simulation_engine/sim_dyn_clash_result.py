"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimDynClashResult(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SIMDynClashResult
                | 
                | Represents the simulation dynamic clash results.
                | These results can be retrieved through
                | SIMDynClashServices.RetrieveResults.
                | Note: the rest of the documentation will use the following
                | variable.
                | 
                |      Dim MyDynClashResult As SIMDynClashResult
                | 
                | 
                | See also:
                |     SIMDynClashServices
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def clash_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ClashType() As long (Read Only)
                |     Indicates if there is any clash to report.
                | 
                |     Example:
                | 
                |      Dim bClashType As Boolean
                |      bClashType = MyDynClash.ClashType

        :return: int
        """

        return self.com_object.ClashType

    def get_colliding_part(self, i_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCollidingPart(long iIndex) As AnyObject
                |     Indicates if the colliding part. There are 2 of them
                | 
                |     Example:
                | 
                |      Dim MyPart1
                |      Dim MyPart2
                |      MyPart1 = MyDynClashResult.GetCollidingPart(1)
                |      MyPart2 = MyDynClashResult.GetCollidingPart(2)

        :param int i_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetCollidingPart(i_index))

    def get_parameter(self, i_parameter_id: str) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameter(CATBSTR iParameterID) As double
                |     Indicates if the colliding part. There are 2 of them
                | 
                |     Example:
                | 
                |      Dim MyValue As Double
                |      MyValue = MyDynClashResult.GetParameter("PENETRATION")

        :param str i_parameter_id:
        :return: float
        """
        return self.com_object.GetParameter(i_parameter_id)

    def __repr__(self):
        return f'SimDynClashResult(name="{ self.name }")'
