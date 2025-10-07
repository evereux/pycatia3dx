"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.int_param import IntParam
from pycatia3dx.system.any_object import AnyObject


class Repartition(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Repartition
                | 
                | Represents the repartition.
                | A repartition is a set of objects used by the pattern shapes. It is the base
                | object for linear and angular repartitions.
                | 
                | See also:
                |     LinearRepartition, AngularRepartition
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def instances_count(self) -> IntParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InstancesCount() As IntParam (Read Only)
                |     Returns the total number of copied shapes.
                | 
                |     Example:
                |         The following example returns in Nb the number of shapes of the
                |         repartition firstRepartition:
                | 
                |          Set Nb = firstRepartition.InstancesCount

        :return: IntParam
        """

        return IntParam(self.com_object.InstancesCount)

    def __repr__(self):
        return f'Repartition(name="{ self.name }")'
