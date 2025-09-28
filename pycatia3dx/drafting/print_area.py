"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class PrintArea(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PrintArea
                | 
                | Manages print area of drawing sheet.
                | 
                | This interface is obtained from DrawingSheet.PrintArea method.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def activation_state(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ActivationState(boolean iActivated)
                |     Activates or deactivates the print area.
                | 
                |     Parameters:
                | 
                |         in
                |             boolean iActivated [in] The activation state of the print area
                |             (TRUE means activated, FALSE means deactivated). 
                | 
                |     Returns:
                |         Un HRESULT
                | 
                |         S_OK
                |             The activation state could be valuated. 
                |         E_FAIL
                |             No activation or deactivation possible.

        :return: bool
        """

        return self.com_object.ActivationState

    @activation_state.setter
    def activation_state(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ActivationState = value

    @property
    def area_height(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AreaHeigth(double iHeigth)
                |     Valuates the heigth of the print area.
                | 
                |     Parameters:
                | 
                |         in
                |             double iHeigth [in] The heigth of the print area. The value must be
                |             strictly positive. 
                | 
                |     Returns:
                |         Un HRESULT
                | 
                |         S_OK
                |         E_FAIL

        :return: bool
        """

        return self.com_object.AreaHeight

    @area_height.setter
    def area_height(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AreaHeight = value

    @property
    def area_low_x(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AreaLowX(double iX)
                |     Valuates the low x coordinate of the print area.
                | 
                |     Parameters:
                | 
                |         in
                |             double iX [in] The low x coordinate. 
                | 
                |     Returns:
                |         Un HRESULT
                | 
                |         S_OK
                |         E_FAIL

        :return: bool
        """

        return self.com_object.AreaLowX

    @area_low_x.setter
    def area_low_x(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AreaLowX = value

    @property
    def area_low_y(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AreaLowY(double iY)
                |     Valuates the low y coordinate of the print area.
                | 
                |     Parameters:
                | 
                |         in
                |             double iY [in] The low y coordinate. 
                | 
                |     Returns:
                |         Un HRESULT
                | 
                |         S_OK
                |         E_FAIL

        :return: bool
        """

        return self.com_object.AreaLowY

    @area_low_y.setter
    def area_low_y(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AreaLowY = value

    @property
    def area_width(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AreaWidth(double iWidth)
                |     Valuates the width of the print area.
                | 
                |     Parameters:
                | 
                |         in
                |             double iWidth [in] The width of the print area. The value must be
                |             strictly positive. 
                | 
                |     Returns:
                |         Un HRESULT
                | 
                |         S_OK
                |         E_FAIL

        :return: bool
        """

        return self.com_object.AreaWidth

    @area_width.setter
    def area_width(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AreaWidth = value

    def get_area(self, o_x: float, o_y: float, o_width: float, o_height: float, o_activated: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetArea(double oX,double oY,double oWidth,double oHeigth,boolean
                | oActivated)
                |     Gets the printing area defined on an object. Also communicates the
                |     activation state of the printing area. 
                | All the values are given in mm.
                | 
                | Parameters:
                | 
                |     out
                |         double oX [out] The low x coordinate of the area. 
                |     out
                |         double oY [out] The low y coordinate of the area. 
                |     out
                |         double oWidth [out] The width of the area. 
                |     out
                |         double oHeigth [out] The heigth of the area. 
                |     out
                |         boolean oActivated [out] The activation state of the print area (TRUE
                |         means activated, FALSE means deactivated). 
                | 
                | Returns:
                |     Un HRESULT
                | 
                |     S_OK
                |         The print area was succesfully retrieved. 
                |     E_FAIL
                |         No print area could be retrived.

        :param float o_x:
        :param float o_y:
        :param float o_width:
        :param float o_height:
        :param bool o_activated:
        :return: None
        """
        return self.com_object.GetArea(o_x, o_y, o_width, o_height, o_activated)

    def set_area(self, i_x: float, i_y: float, i_width: float, i_height: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetArea(double iX,double iY,double iWidth,double iHeigth)
                |     Sets a set of coordinates to define a rectangle print area.
                |     
                | All the values are given in mm.
                | 
                | Parameters:
                | 
                |     in
                |         double iX [in] The low x coordinate of the area. 
                |     in
                |         double iY [in] The low y coordinate of the area. 
                |     in
                |         double iWidth [in] The width of the area. The value must be strictly
                |         positive. 
                |     in
                |         double iHeigth [in] The heigth of the area. The value must be strictly
                |         positive. 
                | 
                | Returns:
                |     Un HRESULT
                | 
                |     S_OK
                |         The print area was successfully defined. 
                |     E_FAIL
                |         No print area could be defined.

        :param float i_x:
        :param float i_y:
        :param float i_width:
        :param float i_height:
        :return: None
        """
        return self.com_object.SetArea(i_x, i_y, i_width, i_height)

    def __repr__(self):
        return f'PrintArea(name="{ self.name }")'
