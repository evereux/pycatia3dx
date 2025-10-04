"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_mapped_field_data import SimMappedFieldData
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_foundation.sim_space_time_field import SimSpaceTimeField


class SimScalarField(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimScalarField
                | 
                | Represents the Scalar Field object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def mapped_field_data(self) -> SimMappedFieldData:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MappedFieldData() As SimMappedFieldData (Read Only)
                |     Returns the mapped field data.

        :return: SimMappedFieldData
        """

        return SimMappedFieldData(self.com_object.MappedFieldData)

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
                |     Returns or sets the magnitude. Quantity: PRESSURE, units: N_m2

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
                | Property VariationType() As SimScalarFieldVariationType
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

    def __repr__(self):
        return f'SimScalarField(name="{ self.name }")'
