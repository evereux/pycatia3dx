"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.eng_connection.eng_connection import EngConnection
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class KinJoints(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     KinJoints
                | 
                | The collection of Joints.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def exclude(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Exclude(CATVariant iIndex)
                |     Dereferences a Joint using its index or its name from the Joint
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Joint to retrieve from the collection
                |             of Joint. As a numeric, this index is the rank of the Joint in the collection.
                |             The index of the first Joint in the collection is 1, and the index of the last
                |             Joint is Count. As a string, it is the name you assigned to the Joint using the
                |             AnyObject.Name property.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Exclude(i_index)

    def include(self, i_joint: EngConnection) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Include(EngConnection iJoint)
                |     References a Joint in the mechanism and adds it to the Joint collection.
                |     The Joint will have to exist in the assembly's collection.
                | 
                |     Parameters:
                | 
                |         iJoint
                |             The joint we want to refer.

        :param EngConnection i_joint:
        :return: None
        """
        return self.com_object.Include(i_joint.com_object)

    def item(self, i_index: CATVariant) -> EngConnection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func Item(CATVariant iIndex) As EngConnection
                |     Returns a Joint using its index or its name from the Joint
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Joint to retrieve from the collection
                |             of Joints. As a numeric, this index is the rank of the Joint in the collection.
                |             The index of the first Joint in the collection is 1, and the index of the last
                |             Joint is Count. As a string, it is the name you assigned to the Joint using the
                |             AnyObject.Name property. 
                | 
                |     Returns:
                |         The retrieved iJoint. 
                | 
                | 
                | Copyright © 1999-2024, Dassault Systèmes. All rights reserved.

        :param CATVariant i_index:
        :return: EngConnection
        """
        return EngConnection(self.com_object.Item(i_index))

    def __repr__(self):
        return f'KinJoints(name="{self.name}")'
