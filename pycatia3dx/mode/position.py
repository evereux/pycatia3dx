"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2020 on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.move import Move


class Position(Move):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfModelInterfaces.Move
                |                         Position
                | 
                | Interface to manage object position.
                | Role:The position object is the 3D-axis system associated with an object. This
                | interface provides methods to retrieve or set the relative or absolute position
                | of the item, in the coordinate space of the context.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_abs_components(self, o_axis_components_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub GetAbsComponents(CATSafeArrayVariant oAxisComponentsArray)
                |     Returns the object's position in a global context. This returns the 3D-axis
                |     system associated with the object.
                | 
                |     Parameters:
                | 
                |         oAxisComponentsArray
                |             The array used to store the twelve components retrieved from the
                |             objet's position. The first nine represent successively the components of the
                |             x-axis, y-axis, and z-axis. The last three represent the coordinates of the
                |             origin point. 
                | 
                |     Example:
                | 
                |          This example retrieves in oAxisComponentsArray
                |          the 3D-axis system components from 
                |          the Position object associated with MyObject:
                |          
                | 
                |          Dim oAxisComponentsArray ( 11 )
                |          MyObject.Position.GetAbsComponents
                |          oAxisComponentsArray

        :param tuple o_axis_components_array:
        :return: None
        """
        return self.com_object.GetAbsComponents(o_axis_components_array)

    def get_components(self, o_axis_components_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub GetComponents(CATSafeArrayVariant oAxisComponentsArray)
                |     Returns relative object's position. This returns the 3D-axis system
                |     associated with the object.
                | 
                |     Parameters:
                | 
                |         oAxisComponentsArray
                |             The array used to store the twelve components retrieved from the
                |             objet's position. The first nine represent successively the components of the
                |             x-axis, y-axis, and z-axis. The last three represent the coordinates of the
                |             origin point. 
                | 
                |     Example:
                | 
                |          This example retrieves in oAxisComponentsArray
                |          the 3D-axis system components from 
                |          the Position object associated with MyObject:
                |          
                | 
                |          Dim oAxisComponentsArray ( 11 )
                |          MyObject.Position.GetComponents oAxisComponentsArray

        :param tuple o_axis_components_array:
        :return: None
        """
        return self.com_object.GetComponents(o_axis_components_array)

    def set_abs_components(self, i_axis_components_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetAbsComponents(CATSafeArrayVariant iAxisComponentsArray)
                |     Sets the object's position in an absolute 3D-coordinates space (global
                |     context). This sets the 3D-axis system associated with the
                |     object.
                | 
                |     Parameters:
                | 
                |         iAxisComponentsArray
                |             The array initialized with the components to set to the object's
                |             position. The first nine represent successively the components of the x-axis,
                |             y-axis, and z-axis. The last three represent the coordinates of the origin
                |             point. 
                | 
                |     Example:
                | 
                |          This example sets the 3D-axis system components stored
                |          in
                |          iAxisComponentsArray to
                |          the Position object associated with MyObject:
                |          
                | 
                |          Dim iAxisComponentsArray( 11 )
                |          ' x axis components
                |          iAxisComponentsArray( 0 )  = 1.000
                |          iAxisComponentsArray( 1 )  = 0
                |          iAxisComponentsArray( 2 )  = 0.707
                |          ' y axis components
                |          iAxisComponentsArray( 3 )  = 0
                |          iAxisComponentsArray( 4 )  = 0
                |          iAxisComponentsArray( 5 )  = 0.707
                |          ' z axis components
                |          iAxisComponentsArray( 6 )  = 0
                |          iAxisComponentsArray( 7 )  = -0.707
                |          iAxisComponentsArray( 8 )  = 0.707
                |          ' origin point coordinates
                |          iAxisComponentsArray( 9 )  = 1.000
                |          iAxisComponentsArray( 10 ) = 2.000
                |          iAxisComponentsArray( 11 ) = 3.000
                |          MyObject.Position.SetAbsComponents
                |          iAxisComponentsArray

        :param tuple i_axis_components_array:
        :return: None
        """
        return self.com_object.SetAbsComponents(i_axis_components_array)

    def set_components(self, i_axis_components_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetComponents(CATSafeArrayVariant iAxisComponentsArray)
                |     Sets the relative object's position. This sets the 3D-axis system
                |     associated with the object.
                | 
                |     Parameters:
                | 
                |         iAxisComponentsArray
                |             The array initialized with the components to set to the object's
                |             position. The first nine represent successively the components of the x-axis,
                |             y-axis, and z-axis. The last three represent the coordinates of the origin
                |             point. 
                | 
                |     Example:
                | 
                |          This example sets the 3D-axis system components stored
                |          in
                |          iAxisComponentsArray to
                |          the Position object associated with MyObject:
                |          
                | 
                |          Dim iAxisComponentsArray( 11 )
                |          ' x axis components
                |          iAxisComponentsArray( 0 )  = 1.000
                |          iAxisComponentsArray( 1 )  = 0
                |          iAxisComponentsArray( 2 )  = 0.707
                |          ' y axis components
                |          iAxisComponentsArray( 3 )  = 0
                |          iAxisComponentsArray( 4 )  = 0
                |          iAxisComponentsArray( 5 )  = 0.707
                |          ' z axis components
                |          iAxisComponentsArray( 6 )  = 0
                |          iAxisComponentsArray( 7 )  = -0.707
                |          iAxisComponentsArray( 8 )  = 0.707
                |          ' origin point coordinates
                |          iAxisComponentsArray( 9 )  = 1.000
                |          iAxisComponentsArray( 10 ) = 2.000
                |          iAxisComponentsArray( 11 ) = 3.000
                |          MyObject.Position.SetComponents iAxisComponentsArray

        :param tuple i_axis_components_array:
        :return: None
        """
        return self.com_object.SetComponents(i_axis_components_array)

    def __repr__(self):
        return f'Position(name="{self.name}")'
