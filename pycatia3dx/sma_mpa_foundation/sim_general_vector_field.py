"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_foundation.sim_space_time_field import SimSpaceTimeField


class SimGeneralVectorField(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimGeneralVectorField
                | 
                | Represents the General Vector Field object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def space_time_field_data(self) -> SimSpaceTimeField:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpaceTimeFieldData() As SimSpaceTimeField (Read Only)
                |     Returns the space time field data.

        :return: SimSpaceTimeField
        """

        return SimSpaceTimeField(self.com_object.SpaceTimeFieldData)

    @property
    def uniform_magnitude(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UniformMagnitude() As double
                |     Returns or sets the uniform magnitude.

        :return: float
        """

        return self.com_object.UniformMagnitude

    @uniform_magnitude.setter
    def uniform_magnitude(self, value: float):
        """
        :param float value:
        """

        self.com_object.UniformMagnitude = value

    @property
    def variation_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VariationType() As SimGeneralVectorFieldVariationType
                |     Returns or sets the variation type.

        :return: SimGeneralVectorFieldVariationType
        """

        return self.com_object.VariationType

    @variation_type.setter
    def variation_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.VariationType = value

    def get_unit_vector_components(self, o_x_comp: float, o_y_comp: float, o_z_comp: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetUnitVectorComponents(double oXComp,double oYComp,double
                | oZComp)
                |     Retrieves the unit vector components.
                |     Only applicable when the variation type is set to
                |     SimGeneralVectorFieldUniform.
                | 
                |     Parameters:
                | 
                |         oXComp[out]
                |             X component of the general vector. 
                |         oYComp[out]
                |             Y component of the general vector. 
                |         oZComp[out]
                |             Z component of the general vector.

        :param float o_x_comp:
        :param float o_y_comp:
        :param float o_z_comp:
        :return: None
        """
        return self.com_object.GetUnitVectorComponents(o_x_comp, o_y_comp, o_z_comp)

    def set_unit_vector_components(self, i_x_comp: float, i_y_comp: float, i_z_comp: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetUnitVectorComponents(double iXComp,double iYComp,double
                | iZComp)
                |     Sets the unit vector components.
                |     Only applicable when the variation type is set to
                |     SimGeneralVectorFieldUniform.
                | 
                |     Parameters:
                | 
                |         iXComp[in]
                |             X component of the general vector. 
                |         iYComp[in]
                |             Y component of the general vector. 
                |         iZComp[in]
                |             Z component of the general vector. 

        :param float i_x_comp:
        :param float i_y_comp:
        :param float i_z_comp:
        :return: None
        """
        return self.com_object.SetUnitVectorComponents(i_x_comp, i_y_comp, i_z_comp)

    def __repr__(self):
        return f'SimGeneralVectorField(name="{ self.name }")'
