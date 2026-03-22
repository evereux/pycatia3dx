"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.eng_connection.eng_connection import EngConnection
from pycatia3dx.kin_mechanism.kin_command import KinCommand
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class KinCommands(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     KinCommands
                | 
                | The collection of mechanism commands.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=KinCommand)
        self.com_object = com_object

    def add(self, i_joint: EngConnection, i_type: int) -> KinCommand:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(EngConnection iJoint,CATKinMechanismCommandType iType) As
                | KinCommand
                |     Creates a new mechanism command and adds it to the command collection. The
                |     command will be created with an input joint and type.
                | 
                |     Parameters:
                | 
                |         iJoint
                |             The joint of mechanism command. 
                |         iType
                |             The type of mechanism command. 
                | 
                |     Returns:
                |         The created command

        :param EngConnection i_joint:
        :param int i_type:
        :return: KinCommand
        """
        return KinCommand(self.com_object.Add(i_joint.com_object, i_type))

    def item(self, i_index: CATVariant) -> KinCommand:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As KinCommand
                |     Returns a command using its index or its name from the command
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the command to retrieve from the
                |             collection of commands. As a numeric, this index is the rank of the command in
                |             the collection. The index of the first command in the collection is 1, and the
                |             index of the last command is Count. As a string, it is the name you assigned to
                |             the command using the AnyObject.Name property. 
                | 
                |     Returns:
                |         The retrieved command.

        :param CATVariant i_index:
        :return: KinCommand
        """
        return KinCommand(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a command using its index or its name from the command
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the command to retrieve from the
                |             collection of command. As a numeric, this index is the rank of the command in
                |             the collection. The index of the first command in the collection is 1, and the
                |             index of the last command is Count. As a string, it is the name you assigned to
                |             the command using the AnyObject.Name property.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'KinCommands(name="{self.name}")'
