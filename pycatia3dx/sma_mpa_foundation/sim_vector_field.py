"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimVectorField(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimVectorField
                | 
                | Represents the Vector Field object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def variation_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VariationType() As SimVectorFieldVariationType
                |     Returns or sets the variation type.

        :return: int
        """

        return self.com_object.VariationType

    @variation_type.setter
    def variation_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.VariationType = value

    def get_vector_components(self, o_x_comp: float, o_y_comp: float, o_z_comp: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetVectorComponents(double oXComp,double oYComp,double
                | oZComp)
                |     Retrieves the vector components.
                |     Only applicable when the variation type is set to
                |     SimVectorFieldUniform.
                | 
                |     Parameters:
                | 
                |         oXComp[out]
                |             X component of the vector. 
                |         oYComp[out]
                |             Y component of the vector. 
                |         oZComp[out]
                |             Z component of the vector.

        :param float o_x_comp:
        :param float o_y_comp:
        :param float o_z_comp:
        :return: None
        """
        return self.com_object.GetVectorComponents(o_x_comp, o_y_comp, o_z_comp)

    def set_vector_components(self, i_x_comp: float, i_y_comp: float, i_z_comp: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetVectorComponents(double iXComp,double iYComp,double
                | iZComp)
                |     Sets the vector components.
                |     Only applicable when the variation type is set to
                |     SimVectorFieldUniform.
                | 
                |     Parameters:
                | 
                |         iXComp[in]
                |             X component of the vector. 
                |         iYComp[in]
                |             Y component of the vector. 
                |         iZComp[in]
                |             Z component of the vector. 

        :param float i_x_comp:
        :param float i_y_comp:
        :param float i_z_comp:
        :return: None
        """
        return self.com_object.SetVectorComponents(i_x_comp, i_y_comp, i_z_comp)

    def __repr__(self):
        return f'SimVectorField(name="{ self.name }")'
