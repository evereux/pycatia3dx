"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SpotDrOperation(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SpotDrOperation

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_cartesian_target(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCartesianTarget() As CATSafeArrayVariant
                |     Gets the Robot Cartesian target of the specified motion
                |     group.
                | 
                |     Parameters:
                | 
                |         oMathTransformation
                |             The absolute Transformation. Array of double containing 12 elements
                |             9 rotational vector and u translational vector
                |             Matrix= a11 a12 a13 Vector= u1
                |             a21 a22 a23 u2
                |             a31 a32 a33 u3
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             Cartesian target successfully set
                |         E_FAIL
                |             Cartesian target could not be set successfully

        :return: tuple
        """
        return self.com_object.GetCartesianTarget()

    def get_pattern_pos(self, osp_pattern_pos: AnyObject, osp_pattern_pos_owner: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPatternPos(AnyObject ospPatternPos,AnyObject
                | ospPatternPosOwner)
                |     Gets the Pattern Position link
                | 
                |     Example:
                | 
                |            
                |      Gets the Pattern Position link
                |        
                | 
                | 
                |       
                |      Parameters:
                | 
                |       
                | 
                |             
                | 
                | 
                |             
                |          ospPatternPos
                | 
                |            
                |                   The Pattern Position
                |                
                |              
                |                 
                |          ospPatternPosOwner
                | 
                |            
                |                   The Pattern Position Owner (product Occ in Root
                |                   context)
                |                
                |              
                | 
                | 
                |       
                |      Returns: 
                |      
                |       
                |                S_OK = Success.
                |               E_FAIL = Error

        :param AnyObject osp_pattern_pos:
        :param AnyObject osp_pattern_pos_owner:
        :return: None
        """
        return self.com_object.GetPatternPos(osp_pattern_pos.com_object, osp_pattern_pos_owner.com_object)

    def set_cartesian_target(self, i_math_transformation: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCartesianTarget(CATSafeArrayVariant
                | iMathTransformation)
                |     Sets the Robot Cartesian target of the specified motion
                |     group.
                | 
                |     Parameters:
                | 
                |         iMathTransformation
                |             The absolute Transformation. Array of double containing 12 elements
                |             9 rotational vector and u translational vector
                |             Matrix= a11 a12 a13 Vector= u1
                |             a21 a22 a23 u2
                |             a31 a32 a33 u3
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             Cartesian target successfully set
                |         E_FAIL
                |             Cartesian target could not be set successfully

        :param tuple i_math_transformation:
        :return: None
        """
        return self.com_object.SetCartesianTarget(i_math_transformation)

    def set_pattern_pos(self, ip_pattern_pos: AnyObject, ip_pattern_pos_owner: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPatternPos(AnyObject ipPatternPos,AnyObject
                | ipPatternPosOwner)
                |     Sets the Pattern Position link
                | 
                |     Example:
                |      Sets the Pattern Position link
                |
                |      Parameters:
                |          ipPatternPos
                |                   The Pattern Position
                |          ipPatternPosOwner
                |                   The Pattern Position Owner (product Occ in Root
                |                   context)
                |      Returns:
                |               S_OK = Success.
                |               E_FAIL = Error

        :param AnyObject ip_pattern_pos:
        :param AnyObject ip_pattern_pos_owner:
        :return: None
        """
        return self.com_object.SetPatternPos(ip_pattern_pos.com_object, ip_pattern_pos_owner.com_object)

    def __repr__(self):
        return f'SpotDrOperation(name="{ self.name }")'
