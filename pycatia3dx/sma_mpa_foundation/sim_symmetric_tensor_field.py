"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_foundation.sim_space_time_field import SimSpaceTimeField


class SimSymmetricTensorField(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSymmetricTensorField
                | 
                | Represents the Symmetric Tensor Field object.
    
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
    def variation_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VariationType() As
                | SimSymmetricTensorFieldVariationType
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

    def get_uniform_tensor_components(self, o_comp11: float, o_comp22: float, o_comp33: float, o_comp12: float, o_comp13: float, o_comp23: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetUniformTensorComponents(double oComp11,double oComp22,double
                | oComp33,double oComp12,double oComp13,double oComp23)
                |     Retrieves the symmetric tensor components.
                | 
                |     Parameters:
                | 
                |         oComp11[out]
                |             The 11 component of the tensor. 
                |         oComp22[out]
                |             The 22 component of the tensor. 
                |         oComp33[out]
                |             The 33 component of the tensor. 
                |         oComp12[out]
                |             The 12 component of the tensor. 
                |         oComp13[out]
                |             The 13 component of the tensor. 
                |         oComp23[out]
                |             The 23 component of the tensor. 
                | 
                |     Returns:
                |         S_OK if successful.

        :param float o_comp11:
        :param float o_comp22:
        :param float o_comp33:
        :param float o_comp12:
        :param float o_comp13:
        :param float o_comp23:
        :return: None
        """
        return self.com_object.GetUniformTensorComponents(o_comp11, o_comp22, o_comp33, o_comp12, o_comp13, o_comp23)

    def set_uniform_tensor_components(self, i_comp11: float, i_comp22: float, i_comp33: float, i_comp12: float, i_comp13: float, i_comp23: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetUniformTensorComponents(double iComp11,double iComp22,double
                | iComp33,double iComp12,double iComp13,double iComp23)
                |     Sets the symmetric tensor components.
                | 
                |     Parameters:
                | 
                |         iComp11[in]
                |             The 11 component of the tensor. 
                |         iComp22[in]
                |             The 22 component of the tensor. 
                |         iComp33[in]
                |             The 33 component of the tensor. 
                |         iComp12[in]
                |             The 12 component of the tensor. 
                |         iComp13[in]
                |             The 13 component of the tensor. 
                |         iComp23[in]
                |             The 23 component of the tensor. 
                | 
                |     Returns:
                |         S_OK if successful. 

        :param float i_comp11:
        :param float i_comp22:
        :param float i_comp33:
        :param float i_comp12:
        :param float i_comp13:
        :param float i_comp23:
        :return: None
        """
        return self.com_object.SetUniformTensorComponents(i_comp11, i_comp22, i_comp33, i_comp12, i_comp13, i_comp23)

    def __repr__(self):
        return f'SimSymmetricTensorField(name="{ self.name }")'
