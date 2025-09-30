"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingUserRepresentation(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingUserRepresentation
                | 
                | Interface dedicated to manage user representation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_representation(self, i_cutting_type: str, i_name_representation: str, i_tool_represention: AnyObject, i_state: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddRepresentation(CATBSTR iCuttingType,CATBSTR
                | iNameRepresentation,AnyObject iToolRepresention,CATBSTR
                | iState)
                |     Adds a User Representation to the Object following some
                |     criteria.
                | 
                |     Parameters:
                | 
                |         iCuttingType
                |             Define the type of cutting element (Cut,NoCut,Cleaner)
                |             
                |         iNameRepresentation
                |             Define the name of representation (Static,Rotary,Worn ...)
                |             
                |         iToolRepresention
                |             The representation to add. 
                |         iState
                |             Define the state of representation (Normal,Worn)

        :param str i_cutting_type:
        :param str i_name_representation:
        :param AnyObject i_tool_represention:
        :param str i_state:
        :return: None
        """
        return self.com_object.AddRepresentation(i_cutting_type, i_name_representation, i_tool_represention.com_object, i_state)

    def add_representation_step(self, i_step_file_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddRepresentationStep(CATBSTR iStepFilePath)
                |     Adds a User Representation to the Object following some
                |     criteria.
                | 
                |     Parameters:
                | 
                |         strStepFilePath
                |             The file path of step file

        :param str i_step_file_path:
        :return: None
        """
        return self.com_object.AddRepresentationStep(i_step_file_path)

    def compute_standard_representation(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ComputeStandardRepresentation()
                |     Compute the standard representation

        :return: None
        """
        return self.com_object.ComputeStandardRepresentation()

    def compute_worn_representation(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ComputeWornRepresentation()
                |     Compute the Worn representation

        :return: None
        """
        return self.com_object.ComputeWornRepresentation()

    def get_representation(self, i_cutting_type: str, i_state: str, i_name_representation: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRepresentation(CATBSTR iCuttingType,CATBSTR iState,CATBSTR
                | iNameRepresentation) As CATSafeArrayVariant
                |     Returns a list of User Representation Associated to the Object following
                |     some criteria.
                | 
                |     Parameters:
                | 
                |         iCuttingType
                |             Define the type of cutting element (Cut,NoCut,Cleaner)
                |             
                |         iState
                |             Define the state of representation (Normal,Worn) 
                |         iNameRepresentation
                |             Define the name of representation (Static,Rotary,Worn ...)
                |             
                |         oListofToolRepresentation
                |             List of Tool Representation.

        :param str i_cutting_type:
        :param str i_state:
        :param str i_name_representation:
        :return: tuple
        """
        return self.com_object.GetRepresentation(i_cutting_type, i_state, i_name_representation)

    def hide(self, i_name_representation: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Hide(CATBSTR iNameRepresentation)
                |     Hide Representation

        :param str i_name_representation:
        :return: None
        """
        return self.com_object.Hide(i_name_representation)

    def is_existing_one_representation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsExistingOneRepresentation() As boolean
                |     Checking if at least one representation is assotiated.

        :return: bool
        """
        return self.com_object.IsExistingOneRepresentation()

    def is_existing_representation(self, i_cutting_type: str, i_name_representation: str, i_state: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsExistingRepresentation(CATBSTR iCuttingType,CATBSTR
                | iNameRepresentation,CATBSTR iState) As boolean
                |     Checking if an Representation is assotiated to selected
                |     criteria.
                | 
                |     Parameters:
                | 
                |         iCuttingType
                |             Define the type of cutting element (Cut,NoCut,Cleaner)
                |             
                |         iNameRepresentation
                |             Define the name of representation (Static,Rotary,Worn ...)
                |             
                |         iState
                |             Define the state of representation (Normal,Worn)

        :param str i_cutting_type:
        :param str i_name_representation:
        :param str i_state:
        :return: bool
        """
        return self.com_object.IsExistingRepresentation(i_cutting_type, i_name_representation, i_state)

    def remove_all_representation(self, i_cutting_type: str, i_name_representation: str, i_state: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveAllRepresentation(CATBSTR iCuttingType,CATBSTR
                | iNameRepresentation,CATBSTR iState)
                |     Removes All User Representation from the Object following some
                |     criteria.
                | 
                |     Parameters:
                | 
                |         iCuttingType
                |             Define the type of cutting element (Cut,NoCut,Cleaner)
                |             
                |         iNameRepresentation
                |             Define the name of representation (Static,Rotary...)
                |             
                |         iState
                |             Define the state of representation (Normal,Worn)

        :param str i_cutting_type:
        :param str i_name_representation:
        :param str i_state:
        :return: None
        """
        return self.com_object.RemoveAllRepresentation(i_cutting_type, i_name_representation, i_state)

    def remove_representation(self, i_cutting_type: str, i_name_representation: str, i_tool_representation: AnyObject, i_state: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveRepresentation(CATBSTR iCuttingType,CATBSTR
                | iNameRepresentation,AnyObject iToolRepresentation,CATBSTR
                | iState)
                |     Removes a User Representation from the Object following some
                |     criteria.
                | 
                |     Parameters:
                | 
                |         iCuttingType
                |             Define the type of cutting element (Cut,NoCut,Cleaner)
                |             
                |         iNameRepresentation
                |             Define the name of representation (Static,Rotary ...)
                |             
                |         iToolRepresention
                |             The representation to remove. 
                |         iState
                |             Define the state of representation (Normal,Worn)

        :param str i_cutting_type:
        :param str i_name_representation:
        :param AnyObject i_tool_representation:
        :param str i_state:
        :return: None
        """
        return self.com_object.RemoveRepresentation(i_cutting_type, i_name_representation, i_tool_representation.com_object, i_state)

    def show(self, i_name_representation: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Show(CATBSTR iNameRepresentation)
                |     Show Representation

        :param str i_name_representation:
        :return: None
        """
        return self.com_object.Show(i_name_representation)

    def update_position(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub UpdatePosition()
                |     Update Position of user representation After modification of user
                |     representation or modification of base or mount point, Call this method to
                |     update position of user representation

        :return: None
        """
        return self.com_object.UpdatePosition()

    def __repr__(self):
        return f'ManufacturingUserRepresentation(name="{ self.name }")'
