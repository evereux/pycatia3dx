"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_connector_dampings import SimConnectorDampings
from pycatia3dx.sma_mpa_structural_mode.sim_connector_elasticities import SimConnectorElasticities


class SimConnectorBehavior(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimConnectorBehavior
                | 
                | Represents the Connector Behavior object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def connector_dampings(self) -> SimConnectorDampings:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConnectorDampings() As SimConnectorDampings (Read
                | Only)
                |     Returns the list of connector dampings. Each member of the list will adhere
                |     to SMAMpaConnectorDamping interface.

        :return: SimConnectorDampings
        """

        return SimConnectorDampings(self.com_object.ConnectorDampings)

    @property
    def connector_elasticities(self) -> SimConnectorElasticities:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConnectorElasticities() As SimConnectorElasticities (Read
                | Only)
                |     Returns the connector elasticities. Each member of the list will adhere to
                |     SMAIMpaConnectorElasticity interface.

        :return: SimConnectorElasticities
        """

        return SimConnectorElasticities(self.com_object.ConnectorElasticities)

    def get_reference_length(self, i_degree_of_freedom: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetReferenceLength(SimDof iDegreeOfFreedom) As double
                |     Retrieves the reference length for a specific degree of
                |     freedom.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom
                |             [in] The degree of freedom. 
                | 
                |     Returns:
                |         The reference length.

        :param int i_degree_of_freedom:
        :return: float
        """
        return self.com_object.GetReferenceLength(i_degree_of_freedom)

    def get_reference_length_flag(self, i_degree_of_freedom: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetReferenceLengthFlag(SimDof iDegreeOfFreedom) As
                | boolean
                |     Retrieves the flag which determines if a reference length is active on a
                |     particular degree of freedom.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom
                |             [in] The degree of freedom. 
                |         oReferenceLengthFlag[out]
                |             The reference length flag. TRUE : the reference length is active, FALSE : the reference length is not active.

        :param int i_degree_of_freedom:
        :return: bool
        """
        return self.com_object.GetReferenceLengthFlag(i_degree_of_freedom)

    def set_reference_length(self, i_degree_of_freedom: int, i_reference_length: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetReferenceLength(SimDof iDegreeOfFreedom,double
                | iReferenceLength)
                |     Sets the reference length for a specific degree of
                |     freedom.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom
                |             [in] The degree of freedom. 
                |         iReferenceLength
                |             [in] The reference length.

        :param int i_degree_of_freedom:
        :param float i_reference_length:
        :return: None
        """
        return self.com_object.SetReferenceLength(i_degree_of_freedom, i_reference_length)

    def set_reference_length_flag(self, i_degree_of_freedom: int, i_reference_length_flag: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetReferenceLengthFlag(SimDof iDegreeOfFreedom,boolean
                | iReferenceLengthFlag)
                |     Set the flag which determines if a reference length is active on a
                |     particular degree of freedom.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom
                |             [in] The degree of freedom. 
                |         iReferenceLengthFlag[in]
                |             The reference length flag. TRUE : the reference length is active, FALSE : the reference length is not active. 

        :param int i_degree_of_freedom:
        :param bool i_reference_length_flag:
        :return: None
        """
        return self.com_object.SetReferenceLengthFlag(i_degree_of_freedom, i_reference_length_flag)

    def __repr__(self):
        return f'SimConnectorBehavior(name="{ self.name }")'
