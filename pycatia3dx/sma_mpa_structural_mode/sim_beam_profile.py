"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimBeamProfile(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimBeamProfile
                | 
                | Represents the Beam Profile object.
                | 
                | Example:
                |     Given a SimBehaviors object, you can create a SimBeamProfile as
                |     following:
                | 
                |      Dim MyBehaviors As SimBehaviors
                |      ...
                |      Dim MyBeamProfile As SimBeamProfile
                |      Set MyBeamProfile = MyBehaviors.Add("SimBeamProfile")
                |      
                | 
                |     Given a SimBehaviors object, you can retrieve a SimBeamProfile named "Beam
                |     Profile.1" as following:
                | 
                |      Dim MyBehaviors As SimBehaviors
                |      ...
                |      Dim MyBeamProfile As SimBeamProfile
                |      Set MyBeamProfile = MyBehaviors.Item("Beam Profile.1")
                |      
                | 
                | Example in Python:
                |     Given a SimBehaviors object myBehaviors, you can create a SimBeamProfile as
                |     following:
                | 
                |      ...
                |      myBeamProfile = myBehaviors.Add("SimBeamProfile")
                |      
                | 
                |     Given a SimBehaviors object myBehaviors, you can retrieve a SimBeamProfile
                |     named "Beam Profile.1" as following:
                | 
                |      ...
                |      myBeamProfile = myBehaviors.Item("Beam Profile.1")
                |      
                | 
                | See also:
                |     SimBehaviors
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def parameters(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Parameters() As CATSafeArrayVariant
                |     Returns or sets the list of beam profile parameters. The possible values
                |     are:
                | 
                |         Box : {Width(a), Height(b), Thickness(t1), Thickness(t2), Thickness(t3), Thickness(t4)}
                |         Circular : {Radius(r)}
                |         General : {Area, I11, I12, I22, J, GammaO, GammaW}
                |         Hex : {Radius(r), Thickness(t)}
                |         I_Beam : {Offset(l), Height(h), Width(b1), Width(b2), Thickness(t1), Thickness(t2), Thickness(t3)}
                |         L_Beam : {Width(a), Height(b), Thickness(t1), Thickness(t2)}
                |         Pipe : {Radius(r), Thickness(t)}
                |         Rectangular : {Base(a), Height(b)}
                |         Trapezoid : {Width(a), Height(b), Width(c), Height(d)}
                |         T_Beam : {Width(b), Height(h), Length(l), Thickness(t1), Thickness(t2)}
                |         Channel : {Width(w), Height(h), Flange thickness1(t1), Web thickness2(t2), Reference offset(o)}
                |         Hat : {Length(l), Height(h), Width(b), Width(b1), Width(b2), Thickness(t1), Thickness(t2), Thickness(t3)}
                | 
                |     Parameter Quantity Unit
                |     Area AREA m2
                |     I11, I12, I22, J and GammaO INERTIA m4
                |     GammaW WARPING_COEFFICIENT m6
                |     All other parameters LENGTH m

        :return: tuple
        """

        return self.com_object.Parameters

    @parameters.setter
    def parameters(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.Parameters = value

    @property
    def shape(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Shape() As SimBeamProfileShape
                |     Returns or sets the shape of the beam profile.

        :return: int
        """

        return self.com_object.Shape

    @shape.setter
    def shape(self, value: int):
        """
        :param int value:
        """

        self.com_object.Shape = value

    def get_shear_center(self, o_shear_center_x_value: float, o_shear_center_y_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetShearCenter(double oShearCenterXValue,double
                | oShearCenterYValue)
                |     Retrieves the values of the shear center for beam profile. Shear center can
                |     be specified only for general shape beam profile.
                | 
                |     Parameters:
                | 
                |         oShearCenterXValue
                |             [out] The shear center in local x-direction of beam profile which
                |             is used for the beam section. Quantity: LENGTH, units: m
                |             
                |         oShearCenterYValue
                |             [out] The shear center in local y-direction of beam profile which
                |             is used for the beam section. Quantity: LENGTH, units: m
                |             
                | 
                |     Returns:
                |         S_OK if successful.

        :param float o_shear_center_x_value:
        :param float o_shear_center_y_value:
        :return: None
        """
        return self.com_object.GetShearCenter(o_shear_center_x_value, o_shear_center_y_value)

    def set_shear_center(self, i_shear_center_x_value: float, i_shear_center_y_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetShearCenter(double iShearCenterXValue,double
                | iShearCenterYValue)
                |     Sets the values of the shear center for beam profile. Shear center can be
                |     specified only for general shape beam profile.
                | 
                |     Parameters:
                | 
                |         iShearCenterXValue
                |             [in] The shear center in local x-direction of beam profile which
                |             should be used for the beam section. Quantity: LENGTH, units: m
                |             
                |         iShearCenterYValue
                |             [in] The shear center in local y-direction of beam profile which
                |             should be used for the beam section. Quantity: LENGTH, units: m
                |             
                | 
                |     Returns:
                |         S_OK if successful. 

        :param float i_shear_center_x_value:
        :param float i_shear_center_y_value:
        :return: None
        """
        return self.com_object.SetShearCenter(i_shear_center_x_value, i_shear_center_y_value)

    def __repr__(self):
        return f'SimBeamProfile(name="{ self.name }")'
