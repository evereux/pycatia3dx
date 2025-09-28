"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape


class Plane(HybridShape):

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
                |                         Plane
                | 
                | Represents the hybrid shape Plane feature object.
                | Role: Declare hybrid shape Plane root feature object. All interfaces for
                | different type of Plane derives HybridShapePlane.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapePlane
                | objects.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_first_axis(self, o_first_axis: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetFirstAxis(CATSafeArrayVariant oFirstAxis)
                |     Returns the coordinates of the first plane axis.
                | 
                |     Parameters:
                | 
                |         oFirstAxis[0]
                |             The X Coordinate of the first plane axis 
                |         oFirstAxis[1]
                |             The Y Coordinate of the first plane axis 
                |         oFirstAxis[2]
                |             The Z Coordinate of the first plane axis 
                | 
                |     See also:
                |         HybridShapeFactory

        :param tuple o_first_axis:
        :return: None
        """
        return self.com_object.GetFirstAxis(o_first_axis)

    def get_origin(self, o_origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetOrigin(CATSafeArrayVariant oOrigin)
                |     Returns the origin of the plane.
                | 
                |     Parameters:
                | 
                |         oOrigin[0]
                |             The X Coordinate of the plane origin 
                |         oOrigin[1]
                |             The Y Coordinate of the plane origin 
                |         oOrigin[2]
                |             The Z Coordinate of the plane origin 
                | 
                |     See also:
                |         HybridShapeFactory

        :param tuple o_origin:
        :return: None
        """
        return self.com_object.GetOrigin(o_origin)

    def get_position(self, o_x: float, o_y: float, o_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetPosition(double oX,double oY,double oZ)
                |     Gets the position where the plane is displayed.
                | 
                |     Parameters:
                | 
                |         oX
                |             X coordinates 
                |         oY
                |             Y coordinates 
                |         oZ
                |             Z coordinates 
                | 
                |     Returns:
                |         S_OK if the position has been set before, E_FAIL else.

        :param float o_x:
        :param float o_y:
        :param float o_z:
        :return: None
        """
        return self.com_object.GetPosition(o_x, o_y, o_z)

    def get_second_axis(self, o_second_axis: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetSecondAxis(CATSafeArrayVariant oSecondAxis)
                |     Returns the coordinates of the second plane axis.
                | 
                |     Parameters:
                | 
                |         oSecondAxis[0]
                |             The X Coordinate of the second plane axis 
                |         oSecondAxis[1]
                |             The Y Coordinate of the second plane axis 
                |         oSecondAxis[2]
                |             The Z Coordinate of the second plane axis 
                | 
                |     See also:
                |         HybridShapeFactory

        :param tuple o_second_axis:
        :return: None
        """
        return self.com_object.GetSecondAxis(o_second_axis)

    def is_a_ref_plane(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func IsARefPlane() As long
                |     Queries whether the plane is a reference plane (fixed axis
                |     plane).
                | 
                |     Returns:
                |         0 when the plane is a reference plane, 1 else.

        :return: int
        """
        return self.com_object.IsARefPlane()

    def put_first_axis(self, i_first_axis: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub PutFirstAxis(CATSafeArrayVariant iFirstAxis)
                |     Sets the first axis. The first plane axis must be a point-direction
                |     line.
                |     Note: This method can only be used on CATIAHybridShapePlane2Lines
                |     feature
                | 
                |     Parameters:
                | 
                |         iFirstAxis[0]
                |             The X Coordinate of the first plane axis 
                |         iFirstAxis[1]
                |             The Y Coordinate of the first plane axis 
                |         iFirstAxis[2]
                |             The Z Coordinate of the first plane axis 
                | 
                |     See also:
                |         HybridShapeFactory

        :param tuple i_first_axis:
        :return: None
        """
        return self.com_object.PutFirstAxis(i_first_axis)

    def put_origin(self, i_origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub PutOrigin(CATSafeArrayVariant iOrigin)
                |     Sets the origin of the plane.
                |     Note: This method can only be used on CATIAHybridShapePlane2Lines
                |     feature
                | 
                |     Parameters:
                | 
                |         iOrigin[0]
                |             The X Coordinate of the plane origin 
                |         iOrigin[1]
                |             The Y Coordinate of the plane origin 
                |         iOrigin[2]
                |             The Z Coordinate of the plane origin 
                | 
                |     See also:
                |         HybridShapeFactory

        :param tuple i_origin:
        :return: None
        """
        return self.com_object.PutOrigin(i_origin)

    def put_second_axis(self, i_second_axis: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub PutSecondAxis(CATSafeArrayVariant iSecondAxis)
                |     Sets the coordinates of the second plane axis. The second plane axis must
                |     be a point-direction line
                |     Note: This method can only be used on CATIAHybridShapePlane2Lines
                |     feature
                | 
                |     Parameters:
                | 
                |         iSecondAxis[0]
                |             The X Coordinate of the second plane axis 
                |         iSecondAxis[1]
                |             The Y Coordinate of the second plane axis 
                |         iSecondAxis[2]
                |             The Z Coordinate of the second plane axis 
                | 
                |     See also:
                |         HybridShapeFactory

        :param tuple i_second_axis:
        :return: None
        """
        return self.com_object.PutSecondAxis(i_second_axis)

    def remove_position(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemovePosition()
                |     Removes reference position of a plane.
                |     Note: When removed, the plane is displayed at its default position.

        :return: None
        """
        return self.com_object.RemovePosition()

    def set_position(self, i_x: float, i_y: float, i_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPosition(double iX,double iY,double iZ)
                |     Sets the position where the plane is displayed.
                | 
                |     Parameters:
                | 
                |         iX
                |             X coordinates 
                |         iY
                |             Y coordinates 
                |         iZ
                |             Z coordinates

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :return: None
        """
        return self.com_object.SetPosition(i_x, i_y, i_z)

    def __repr__(self):
        return f'Plane(name="{ self.name }")'
