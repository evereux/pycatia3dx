"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.plm_document.plm_document import PLMDocument
from pycatia3dx.system.any_object import AnyObject


class SimKeywordEdit(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimKeywordEdit
                | 
                | Represents the Keyword Edit object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimKeywordEdit as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyKeywordEdit As SimKeywordEdit
                |      Set MyKeywordEdit = MyFeatures.Add("SimKeywordEdit")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimKeywordEdit named
                |     "Keyword Edit.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyKeywordEdit As SimKeywordEdit
                |      Set MyKeywordEdit = MyFeatures.Item("Keyword Edit.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimKeywordEdit as
                |     following:
                | 
                |      ...
                |      myKeywordEdit = myFeatures.Add("SimKeywordEdit")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimKeywordEdit
                |     named "Keyword Edit.1" as following:
                | 
                |      ...
                |      myKeywordEdit = myFeatures.Item("Keyword Edit.1")
                |      
                | 
                | See also:
                |     SimFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def activated(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Activated() As boolean
                |     Returns or sets the activation status.

        :return: bool
        """

        return self.com_object.Activated

    @activated.setter
    def activated(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Activated = value

    @property
    def keyword_edit_document(self) -> PLMDocument:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property KeywordEditDocument() As PLMDocument
                |     Returns or sets the PLM document associated with the keyword edit.

        :return: PLMDocument
        """

        return PLMDocument(self.com_object.KeywordEditDocument)

    @keyword_edit_document.setter
    def keyword_edit_document(self, value: PLMDocument):
        """
        :param PLMDocument value:
        """

        self.com_object.KeywordEditDocument = value

    @property
    def spec_tree_category(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecTreeCategory() As CATBSTR (Read Only)
                |     Returns a string representing the specification tree category of the
                |     feature. 

        :return: str
        """

        return self.com_object.SpecTreeCategory

    def __repr__(self):
        return f'SimKeywordEdit(name="{ self.name }")'
