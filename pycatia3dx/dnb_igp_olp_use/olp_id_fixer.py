"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class OLPIdFixer(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpIDFixer
                | 
                | Represents an interface that handles fixing object names to conform to the
                | robot language requirements.
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | This interface provides methods to set the requirements for the name, as well
                | as to generate a correct name and returning the corrected
                | name.
                | 
                | Example:
                | 
                |      This example code shows how to create and use the ID
                |      Fixer.
                | 
                |      The examples here are written in Visual Studio Tools for Applications
                |      (VSTA) VB.NET
                |      
                | 
                |      ' Create the Translator Helper and ID Fixer.
                |      Dim helper As OlpTranslatorHelper = CATIA.Application.GetSessionService("OlpTranslatorHelper")
                |      Dim idFixer As DELOlp.OlpIDFixer = helper.CreateIDFixer
                | 
                |      'Set the properties
                |      idFixer.ReplaceWhiteSpace = 0
                |      idFixer.Unique = 0
                |      idFixer.ReplaceWithChars = "aaa"
                |      idFixer.CharactersToRemove = "abc"
                |      idFixer.InvalidStartingChars = "R"
                |      idFixer.MaxLength = 20
                | 
                |      ' Loop through the tasks, correcting each name
                |      Dim tasks As Object() = helper.Tasks
                |         For Each task As OlpRobotTask In tasks
                |            Dim newName As String = idFixer.FixID(task)
                |            MsgBox(" Correcting task named: " & task.Name & " Corrected name is:
                |            " & newName)
                |        Next
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def characters_to_remove(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CharactersToRemove() As CATBSTR
                |     Gets/sets the characters to remove from the ID.
                |     The default is none. If this property is set, every character in the
                |     CharactersToRemove string will be removed from the ID. If the ID becomes empty
                |     because all the characters have been removed, an error is thrown. If there are
                |     any numbers in the characters to remove string, an error is thrown.

        :return: str
        """

        return self.com_object.CharactersToRemove

    @characters_to_remove.setter
    def characters_to_remove(self, value: str):
        """
        :param str value:
        """

        self.com_object.CharactersToRemove = value

    @property
    def invalid_names(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InvalidNames() As CATSafeArrayVariant
                |     Gets/sets the list of invalid names.
                |     For example, this could be a list of keywords.

        :return: tuple
        """

        return self.com_object.InvalidNames

    @invalid_names.setter
    def invalid_names(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.InvalidNames = value

    @property
    def invalid_prefix(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InvalidPrefix() As CATBSTR
                |     Gets/sets the prefix to use when an invalid name is found.

        :return: str
        """

        return self.com_object.InvalidPrefix

    @invalid_prefix.setter
    def invalid_prefix(self, value: str):
        """
        :param str value:
        """

        self.com_object.InvalidPrefix = value

    @property
    def invalid_starting_chars(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InvalidStartingChars() As CATBSTR
                |     Gets/sets the characters to remove from the first character of the
                |     ID.
                |     The default is none. (No beginning characters will be removed.) If set and
                |     the first character of the ID is any one of the characters in the
                |     InvalidStartingChars string, the first character is replace with
                |     ReplaceWithChars. If this property is set, so must the ReplaceWithChars
                |     property.

        :return: str
        """

        return self.com_object.InvalidStartingChars

    @invalid_starting_chars.setter
    def invalid_starting_chars(self, value: str):
        """
        :param str value:
        """

        self.com_object.InvalidStartingChars = value

    @property
    def max_length(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaxLength() As long
                |     Gets/sets the maximum character length for an ID.
                |     The default value is 0, meaning no character limit for the ID. The value
                |     must be greater than 0. If set, the corrected ID can be no longer than the
                |     specified length. Characters are removed from the end of the ID.

        :return: int
        """

        return self.com_object.MaxLength

    @max_length.setter
    def max_length(self, value: int):
        """
        :param int value:
        """

        self.com_object.MaxLength = value

    @property
    def replace_white_space(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReplaceWhiteSpace() As boolean
                |     Gets/sets the flag to replace white space in the ID with an
                |     underscore.
                |     The default is TRUE, replace all white space with an underscore. Otherwise,
                |     nothing is done to the ID.

        :return: bool
        """

        return self.com_object.ReplaceWhiteSpace

    @replace_white_space.setter
    def replace_white_space(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ReplaceWhiteSpace = value

    @property
    def replace_with_chars(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReplaceWithChars() As CATBSTR
                |     Gets/sets the characters to remove from the ID.
                |     This must be used in conjuction with InvalidStartingChars, otherwise it is
                |     ignored. The default value is "x", and cannot be set to empty. Used to set the
                |     first character of an ID, if InvalidStartingChars is set.

        :return: str
        """

        return self.com_object.ReplaceWithChars

    @replace_with_chars.setter
    def replace_with_chars(self, value: str):
        """
        :param str value:
        """

        self.com_object.ReplaceWithChars = value

    @property
    def unique(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Unique() As boolean
                |     Gets/sets whether the ID should be unique.
                |     The default value is TRUE, the name should be unique and no two objects
                |     will have the same ID. Numbers will be appended to the end of the ID until a
                |     unique ID is found. If a unique name can't be found, a warning will be posted
                |     indicating this. If the value is FALSE, no test for uniqueness will be done.

        :return: bool
        """

        return self.com_object.Unique

    @unique.setter
    def unique(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Unique = value

    def fix_id(self, i_object: AnyObject) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FixID(AnyObject iObject) As CATBSTR
                |     Fixes the ID of the input object.
                |     The input object's name will be fetched and used as the starting point for
                |     generating a name. The name will be generated based on the properties
                |     specified. Once a name has been generated, none of the properties can be
                |     changed.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object whose name will be fixed. 
                | 
                |     Returns:
                |         The fixed name for the object.

        :param AnyObject i_object:
        :return: str
        """
        return self.com_object.FixID(i_object.com_object)

    def fix_id_with_name(self, i_object: AnyObject, i_starting_name: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FixIDWithName(AnyObject iObject,CATBSTR iStartingName) As
                | CATBSTR
                |     Fixes the ID of the input object with a specified starting
                |     name.
                |     The starting point for generating a name will be iStartingName, not the
                |     name of the object. The name will be generated based on the properties
                |     specified. Once a name nas been generated, none of the properties can be
                |     changed.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object whose name will be fixed. 
                |         iStartingName
                |             The name to be used to fix. (Instead of the name of iObject.)
                |             
                | 
                |     Returns:
                |         The fixed name for the object. 

        :param AnyObject i_object:
        :param str i_starting_name:
        :return: str
        """
        return self.com_object.FixIDWithName(i_object.com_object, i_starting_name)

    def __repr__(self):
        return f'OLPIdFixer(name="{ self.name }")'
