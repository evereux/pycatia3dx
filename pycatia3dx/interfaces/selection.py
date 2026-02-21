"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx import CATMultiSelectionMode
from pycatia3dx.interfaces.editor import Editor
from pycatia3dx.interfaces.selected_element import SelectedElement
from pycatia3dx.interfaces.vis_property_set import VisPropertySet
from pycatia3dx.system.any_object import AnyObject


# noinspection GrazieInspection
class Selection(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Selection
                | 
                | Represents the selection.
                | The Selection allows to manipulate the objects selected by the end user,
                | usually with the mouse, and which are candidates for the next script
                | action.
                | 
                | A feature possesses parent objects in the specification tree (hierarchy). For
                | example, the Pad below possesses several parents:
                | 
                |   +------------+ 
                |   !Product55228!                                                  <-
                |   VPMReference
                |   +------------+
                |       !
                |       +- Representation55228 (instance hidden)
                |       !
                |       +- Product55227 (Product55227.1)                            <-
                |       VPMReference (VPMInstance)
                |             !
                |             +- Product55226 (Product55226.1)                      <-
                |             VPMReference (VPMInstance)
                |                   !
                |                   +- Representation55226 (instance hidden)        <-
                |                   Part/VPMRepReference (VPMRepInstance)
                |                             !
                |                             +- PartBody
                |                                   !
                |                                   +- Pad.1                        <- Selected
                |                                   feature
                |  
                | 
                | For a given selected feature, its parents which are exposed to Automation can
                | be accessed through recursive calls to the AnyObject.Parent property.
                | Automation exposition is an important thing to consider:
                | 
                |     If the feature is exposed to Automation (such as Pad ), it can be accessed
                |     by all Selection methods
                |     If the feature is not exposed to Automation, but at least one of its
                |     parents is exposed to Automation, several cases apply. For example, let's
                |     consider a DMU Navigator URL: the Hyperlink itself is not exposed to
                |     Automation, but the root Product, which contains the Hyperlink, is exposed to
                |     Automation. Then:
                |         no access is given to the feature through the Count and Item
                |         methods
                |         the first parent which is exposed to Automation (the root Product in
                |         our example) can be accessed through the Item and Count
                |         methods
                |         The Search, Delete, VisProperties, Copy, Cut, Paste and PasteSpecial
                |         methods take the feature into account.
                |         For example, if the user:
                |             Puts a DMU Navigator URL in the clipboard
                |             Runs a script calling the PasteSpecial method
                |         then, during the paste, the DMU Navigator URL will be pasted
                |         properly.
                |     If neither the feature nor any of its parents are exposed to Automation
                |     (such as a ResourcesList object of a .CATProcess), the following cases
                |     apply:
                |         no access is given to the feature through the Count and Item
                |         methods
                |         no access either is given to any parent object of the
                |         feature
                |         However, Search, Delete, VisProperties, Copy, Cut, Paste and
                |         PasteSpecial methods do take the feature into account.
                |         For example, if the user:
                |             Loads the "DPM - Process and Resource Definition"
                |             workshop
                |             Puts a ResourcesList object in the clipboard
                |             Runs a script calling the Selection.PasteSpecial
                |             method
                |         then, during the paste, the ResourcesList object will be pasted
                |         properly.
                | 
                | Note: The simplest way to access the Selection object is to call:
                | CATIA.ActiveEditor.Selection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Count() As long (Read Only)
                |     Returns the number of SelectedElement objects contained by the current
                |     selection.

        :return: int
        """

        return self.com_object.Count

    @property
    def count2(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Count2() As long (Read Only)
                | 
                |     Deprecated:
                |         R207 Count

        :return: int
        """

        return self.com_object.Count2

    @property
    def vis_properties(self) -> VisPropertySet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property VisProperties() As VisPropertySet (Read Only)
                |     Manages graphic properties on current selection.
                |     Role: Returns a VisPropertySet object so that graphic properties of the
                |     selected objects can be read or modified.
                |     Note: After the execution of the VisProperties methods which update graphic
                |     properties of the features, selected features which are not exposed to
                |     Automation will be updated. After the execution of the VisProperties methods
                |     which consult the selection to give the graphic properties, selected features
                |     which are not exposed to Automation will be consulted.
                | 
                |     Example:
                |         This example hides all elements of the current
                |         selection:
                | 
                |          Dim Selection, VisPropertySet
                |          Set Selection = CATIA.ActiveEditor.Selection
                |          Set VisPropertySet = Selection.VisProperties
                |          VisPropertySet.SetShow catVisPropertiesNoShowAttr

        :return: VisPropertySet
        """

        return VisPropertySet(self.com_object.VisProperties)

    def add(self, i_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Add(AnyObject iObject)
                |     Creates a SelectedElement object whose Value property is the given
                |     Automation object, and adds it to the selection.
                |     Role: Creates a SelectedElement object, whose Value property is the given
                |     Automation object, and whose LeafProduct property is the first (when scanning
                |     the specification tree) which contains the Automation object. The
                |     SelectedElement is added to the current selection.
                | 
                |     Example:
                |         This example creates a SelectedElement object, whose Value property is
                |         the ObjectToAdd Automation object, the SelectedElement being added to the
                |         current selection.
                | 
                |          CATIA.ActiveEditor.Selection.Add(ObjectToAdd)
                |          
                | 
                |     Note: If an element is passed to the selection in a context of
                |     multi-instances, the selected element could be in another instance than the
                |     initial one. To avoid retriving bad instances, you can keep a reference on the
                |     selected element :
                | 
                |     Example:
                |         This example retrieve the selection, and we save a reference of
                |         mysel.Item2(1).Value in sel1 and one reference of the selected object
                |         mysel.Item2(1) in sel1so Then some treatments are done on sel1. In order to
                |         retrieve the good element in the right instance, we then pass the sel1so to the
                |         selection.
                | 
                |          Set mysel = CATIA.ActiveEditor.Selection
                |          Set sel1 = mysel.Item2(1).Value
                |          Set sel1so = mysel.Item2(1) 'SelectedObject save to retrieve the good instance
                |          mysel.Clear
                |          'Perform intermediate task usig selection object sel1
                |          mysel.Add (sel1so)

        :param AnyObject i_object:
        :return: None
        """
        return self.com_object.Add(i_object.com_object)

    def clear(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Clear()
                |     Clears the selection.
                | 
                |     Example:
                |         This example clears the selection. The selection is then
                |         empty.
                | 
                |          CATIA.ActiveEditor.Selection.Clear

        :return: None
        """
        return self.com_object.Clear()

    def copy(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Copy()
                |     Copies, in a copy and paste operation.
                |     Role: Puts the contents of the selection in the clipboard, but leaves the
                |     selected elements in the Editor, and clears the selection. This is the
                |     programming equivalent of the Copy command from the Edit
                |     menu.
                |     Note: If a selected feature is not exposed to Automation, it will be copied
                |     into the clipboard anyway.
                | 
                |     Example:
                | 
                |          CATIA.ActiveEditor.Selection.Copy

        :return: None
        """
        return self.com_object.Copy()

    def cut(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Cut()
                |     Cuts, in a cut and paste operation.
                |     Role: Puts the contents of the selection in the clipboard, and removes the
                |     selected elements from the Editor, and clears the selection. This is the
                |     programming equivalent of the Cut command from the Edit
                |     menu.
                |     Note: If a selected feature is not exposed to Automation, it will be copied
                |     into the clipboard and removed from the Editor anyway.
                | 
                |     Example:
                | 
                |          CATIA.ActiveEditor.Selection.Cut

        :return: None
        """
        return self.com_object.Cut()

    def delete(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Delete()
                |     Deletes all selected objects.
                |     Role: For all SelectedElement objects contained by the selection, the
                |     SelectedElement.Value Automation object is deleted from the
                |     Editor.
                |     Note: If a selected feature is not exposed to Automation, it will be
                |     deleted anyway.
                | 
                |     Example:
                | 
                |          CATIA.ActiveEditor.Selection.Delete

        :return: None
        """
        return self.com_object.Delete()

    def filter_correspondence(self, i_filter_type: tuple) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Func FilterCorrespondence(CATSafeArrayVariant iFilterType) As
                | boolean
                |     Specifies if the Automation objects appearing as Value property of
                |     SelectedElement objects fit a given filter.
                |     Role: FilterCorrespondence filters the selection with respect to provided
                |     Automation types. The use of this method coupled with the use of SelectElement
                |     method offers a way to script multi-selection.
                |     It will enable, for example, to write a script reproducing the
                |     functionalities of the "Fillet" command of the "Part Design"
                |     workbench.
                |     This method, called before a loop of SelectElement calls, will enable to
                |     take into account all objects corresponding to the filter (which will be the
                |     same one as given to SelectElement). Otherwise, it will clear the
                |     selection.
                |     This scripted multi-selection allows to keep already selected elements
                |     while adding new ones into the selection.
                |
                |     Parameters:
                |
                |         iFilterType
                |             An array of string constants to be used as a filter for the current
                |             selection. Same as iFilterType parameter of the SelectElement method.
                |
                |         oAllFit
                |             All current selection objects fit the iFilterType filter, i.e.
                |             regarding each of the current selection objects, they all fit one of the
                |             iFilterType string constant.
                |
                |     Example:
                |
                |          The following example scripts an edge fillet creation command. It
                |          supposes that a part is currently edited,
                |          containing a Pad. It loops onto the following:
                |
                |
                |
                |
                |             it asks the end user to select an edge (see
                |             TriDimFeatEdge ). If the selected edge has not already been
                |             selected, the selected edge is added to the selection, otherwise it is removed
                |             from the selection
                |
                |
                |             it asks the end user if another edge has to be
                |             selected
                |
                |
                |
                |
                |          until the answer of the user to the preceding question is
                |          no.
                |
                |          Then, it creates an edge fillet (see
                |         ConstRadEdgeFillet ) taking into account all the selected edges as
                |         fillet specifications.
                |
                |
                |         Note: The edges which were selected before the script execution are
                |         taken into account. However,
                |          if, before the script execution, the selection contained an object
                |          which was not a
                |         TriDimFeatEdge element, the selection is cleared before the first
                |         selection proposal.
                |
                |         Note: During the selection of a given edge, the edges already selected
                |         remain highlighted.
                |
                |
                |
                |          Option Explicit
                |
                |          Sub CATMain()
                |
                |            If TypeName(CATIA.ActiveEditor.ActiveObject) <> "Part" Then Exit
                |            Sub
                |            Dim Part
                |            Set Part = CATIA.ActiveEditor.ActiveObject
                |
                |            CATIA.ScriptCommand = CatScriptCommandStart
                |            CATIA.HSOSynchronized = False
                |
                |            ReDim InputObjectType(0)
                |            InputObjectType(0)="TriDimFeatEdge"
                |            Dim EdgeSaveCount
                |            EdgeSaveCount = 0
                |
                |            'We determine if the selection contains an object which is not a
                |            TriDimFeatEdge element
                |            Dim Selection
                |            Set Selection = CATIA.ActiveEditor.Selection
                |            Dim AllFit
                |            AllFit = Selection.FilterCorrespondence(InputObjectType)
                |
                |            'If the selection contains an object which is not a TriDimFeatEdge
                |            element, we clear the selection
                |            If (Not AllFit) Then Selection.Clear
                |            Dim EdgeSaveAllocatedCount
                |            EdgeSaveAllocatedCount = Selection.Count + 10
                |            ReDim EdgeSave(EdgeSaveAllocatedCount - 1)
                |
                |            'We loop onto interactive selections
                |            Dim AllEdgesHaveBeenSelected
                |            AllEdgesHaveBeenSelected = False
                |            Do While (Not AllEdgesHaveBeenSelected)
                |              'We save the selection content in save variables.
                |              'This corresponds to the fact that:
                |              '  - we want that, during the following call to SelectElement, the
                |              TriDimFeatEdge elements previously selected
                |              '    remain highlighted
                |              '  - this is done using the False value for the
                |              iMaySkipInteractiveSelection
                |              '    parameter of the SelectElement method, the selection
                |              containing the TriDimFeatEdge elements. It requires
                |              that
                |              '    the selection content be saved
                |              If (EdgeSaveAllocatedCount < Selection.Count)
                |              Then
                |                  EdgeSaveAllocatedCount = EdgeSaveAllocatedCount + 10
                |                  ReDim EdgeSave(EdgeSaveAllocatedCount - 1)
                |              End If
                |              Dim EdgeIndex
                |              For EdgeIndex = 0 To Selection.Count - 1
                |                  Set EdgeSave(EdgeIndex) = Selection.Item(EdgeIndex + 1).Value
                |              Next
                |              EdgeSaveCount = Selection.Count
                |
                |              'We ask the user to select an edge
                |              Dim Status
                |              Status = Selection.SelectElement(InputObjectType, "Select an edge", False)
                |              If Status = "Cancel" Then
                |                  Selection.Clear
                |                  CATIA.HSOSynchronized = True
                |                  CATIA.ScriptCommand = CatScriptCommandStop
                |                  Exit Sub
                |              End If
                |
                |              'We save the selected edge in a dedicated
                |              variable
                |              Dim SelectedEdge
                |              Set SelectedEdge = Selection.Item(1).Value
                |
                |              'We merge the selected element with the save variables, and put
                |              the result in the selection.
                |              'At first, we determine If the selected edge already belongs to
                |              the EdgeSave array
                |              EdgeIndex = 0
                |              Dim SelectedElementBelongsToSaveVariables,
                |              AlreadySelectedEdgeIndex
                |              SelectedElementBelongsToSaveVariables = False
                |
                |              Do While ((EdgeIndex < EdgeSaveCount) And (Not
                |              SelectedElementBelongsToSaveVariables))
                |                  If EdgeSave(EdgeIndex).Name = SelectedEdge.Name Then
                |                      SelectedElementBelongsToSaveVariables = True
                |                      AlreadySelectedEdgeIndex = EdgeIndex
                |                  End If
                |                  EdgeIndex = EdgeIndex + 1
                |              Loop
                |
                |              'Effective merge
                |              If (Not SelectedElementBelongsToSaveVariables)
                |              Then
                |                'The selected element does not belong to the save variables. We
                |                add the save variables to the selection
                |                For EdgeIndex = 0 To EdgeSaveCount - 1
                |                  Selection.Add EdgeSave(EdgeIndex)
                |                Next
                |              Else
                |                'We remove the selected element from the save
                |                variables
                |                For EdgeIndex = AlreadySelectedEdgeIndex To EdgeSaveCount - 2
                |                  Set EdgeSave(EdgeIndex) = EdgeSave(EdgeIndex + 1)
                |                Next
                |                EdgeSaveCount = EdgeSaveCount - 1
                |                Selection.Clear
                |                'We add the save variables to the selection
                |                For EdgeIndex = 0 To EdgeSaveCount - 1
                |                  Selection.Add EdgeSave(EdgeIndex)
                |                Next
                |              End If
                |              'We ask the end user if another edge has to be
                |              selected
                |              CATIA.HSOSynchronized = True
                |              Dim OtherEdgeAnswer
                |              OtherEdgeAnswer = MsgBox ("Do you want to select another edge?", 3, "Edge Fillet Definition")
                |              CATIA.HSOSynchronized = False
                |              If (OtherEdgeAnswer = 2) Then
                |                CATIA.HSOSynchronized = True
                |                CATIA.ScriptCommand = CatScriptCommandStop
                |                Exit Sub
                |              End If
                |              If (OtherEdgeAnswer = 7) Then AllEdgesHaveBeenSelected = True
                |            Loop
                |
                |            'We create an edge fillet taking into account all the selected edges
                |            as fillet specifications
                |            If (Selection.Count > 0) Then
                |              Dim Fillet
                |              Set Fillet = Part.ShapeFactory.AddNewEdgeFilletWithConstantRadius(Selection.Item(1).Value, 1, 5.0)
                |              Fillet.EdgePropagation = 1
                |              For EdgeIndex = 2 To Selection.Count
                |                Fillet.AddObjectToFillet
                |                Selection.Item(EdgeIndex).Value
                |              Next
                |              Part.Update
                |              Selection.Clear
                |              Selection.Add Fillet
                |            End If
                |
                |            CATIA.HSOSynchronized = True
                |            CATIA.ScriptCommand = CatScriptCommandStop
                |
                |          End Sub

        :param tuple i_filter_type:
        :return: bool
        """
        return self.com_object.FilterCorrespondence(i_filter_type)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'filter_correspondence'
        # vba_code = """
        # Public Function filter_correspondence(selection)
        #     Dim iFilterType (2)
        #     selection.FilterCorrespondence iFilterType
        #     filter_correspondence = iFilterType
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def find_object(self, i_object_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func FindObject(CATBSTR iObjectType) As AnyObject
                |     Finds an object in the current selection and deletes it from the
                |     selection.
                |     Role: Determines the first object or parent of object whose type is equal
                |     to the specified input type. It returns directly the object and deletes the
                |     corresponding SelectedElement object from the current
                |     selection.
                |     Note: If the string specified in input is "CATIAProduct", the possible
                |     object specified in SelectedElement.LeafProduct is also looked
                |     for.
                | 
                |     Example:
                |         This example searches a Pad object in the current selection and puts it
                |         into FoundObject.
                | 
                |          Dim FoundObject As AnyObject
                |          Set FoundObject = CATIA.ActiveEditor.Selection.FindObject("CATIAPad")

        :param str i_object_type:
        :return: AnyObject
        """
        return AnyObject(self.com_object.FindObject(i_object_type))

    def indicate_or_select_element_2d(
            self,
            i_message: str,
            i_filter_type: tuple,
            i_may_skip_interactive_selection: bool,
            i_tooltip: bool,
            i_triggering_on_mouse_move: bool,
            o_object_selected: bool,
            o_window_location: tuple
    ) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func IndicateOrSelectElement2D(CATBSTR iMessage,CATSafeArrayVariant
                | iFilterType,boolean iMaySkipInteractiveSelection,boolean iTooltip,boolean
                | iTriggeringOnMouseMove,boolean oObjectSelected,CATSafeArrayVariant
                | oWindowLocation) As CATBSTR
                |     Runs an interactive command enabling both indication and selection, 2D
                |     version.
                |     Role: IndicateOrSelectElement2D asks the end user to select either a
                |     location into the window, or a feature (in the geometry or in the specification
                |     tree).
                |     During execution, when entering this method, the active editor must be in
                |     2D.
                |     Note: The method (and script execution) fails if one of the following error
                |     occurs:
                | 
                |         CATIA.ScriptCommand is equal to CatScriptCommandDefault.
                |         Selection.IndicateOrSelectElement2D cannot be called.
                |         CATIA.ScriptCommand is equal to CatScriptCommandStop.
                |         Selection.IndicateOrSelectElement2D cannot be called.
                | 
                | 
                |     Parameters:
                | 
                |         iMessage
                |             A string displayed in the status bar which tells the user what
                |             he/she should select (location, object...). 
                |         iFilterType
                |             An array of string constants defining the Automation object types
                |             with which the selection will be filtered.
                |             Note: If iFilterType contains only an empty string, the interactive
                |             command will only enable indication. 
                |         iMaySkipInteractiveSelection
                |             If true and if the user has selected something before running the
                |             script, the interactive step of this method will be skipped. See SelectElement
                |             . 
                |         iTooltip
                |             Displays a tooltip as soon as an object is located under the mouse
                |             without being selected. 
                |         iTriggeringOnMouseMove
                |             Triggers as soon as a mouse move event is detected. This option
                |             beeing set, oOutputState may be valued to "MouseMove".
                |             
                |         oObjectSelected
                |             Flag precising if the user choosed selection or indication.
                |             
                |         oWindowLocation
                |             An array made of 2 doubles: X, Y - coordinates array of the
                |             location that the user specified in the window. This parameter is valuated only
                |             if oObjectSelected equals to False. 
                |         oOutputState
                |             The state of the interactive command once IndicateOrSelectElement2D
                |             returns. The possible values are the same than the values described regarding
                |             the oOutputState parameter of the SelectElement method, except that "MouseMove"
                |             value can also be returned. 
                | 
                |     Example:
                | 
                |          The following example supposes that a drawing is currently edited. It
                |          creates a point (see 
                |         Point2D ), and asks the end user to click to define the circle
                |         center.
                | 
                |          When it is done, as the mouse moves without clicking the left button,
                |          the script determines the location into
                |          the drawing window, and creates a temporary circle as
                |          feedback.
                | 
                |          A click into the window or the selection of a point definitively
                |          creates the circle 
                |          (see 
                |         Circle2D ) located at the specified location (whether the location is
                |         into the drawing window or whether it is the existing point
                |         location).
                | 
                |          
                | 
                |          Option Explicit
                |          
                |          Sub CATMain()
                |            
                |            If TypeName(CATIA.ActiveEditor.ActiveObject) <> "DrawingRoot" Then
                |            Exit Sub
                |            Dim DrawingSheets
                |            Set DrawingSheets  = CATIA.ActiveEditor.ActiveObject.Sheets
                |            
                |            Dim Selection
                |            Set Selection = CATIA.ActiveEditor.Selection
                |           
                |            CATIA.ScriptCommand = CatScriptCommandStart
                |            CATIA.HSOSynchronized = False
                |           
                |            Dim DrawingSheet, DrawingViews, DrawingView,
                |            Factory2D
                |            Set DrawingSheet = DrawingSheets.ActiveSheet
                |            Set DrawingViews = DrawingSheet.Views
                |            Set DrawingView = DrawingViews.ActiveView
                |            Set Factory2D = DrawingView.Factory2D
                |          
                |            'We create a point
                |            Dim HardCodedPoint 
                |            Set HardCodedPoint = Factory2D.CreatePoint(700.,400.)
                |            HardCodedPoint.ReportName = 1
                |            HardCodedPoint.Construction = False
                |          
                |            'We ask the user to define the circle center
                |            Dim InputObjectType(0), Status, WindowLocation(1),
                |            ObjectSelected
                |            InputObjectType(0) = ""
                |            Status = Selection.IndicateOrSelectElement2D("click to define the circle center", InputObjectType, False, False, False, ObjectSelected, WindowLocation)
                |            If Status = "Cancel" Or Status = "Undo" Or Status = "Redo" Then
                |              CATIA.HSOSynchronized = True
                |              CATIA.ScriptCommand = CatScriptCommandStop
                |              Exit Sub
                |            End If
                |            
                |            Dim XCenter, YCenter, TempCircleHasBeenCreatedAtLeastOnce, Radius,
                |            Circle2D
                |            XCenter = WindowLocation(0)
                |            YCenter = WindowLocation(1)
                |          
                |            'We ask the user to specify a location into the drawing window or a
                |            point
                |            InputObjectType(0) = "Point2D"
                |            Status = "MouseMove"
                |            TempCircleHasBeenCreatedAtLeastOnce = 0
                |            Status = Selection.IndicateOrSelectElement2D("Select a point or click to locate the circle radius point", InputObjectType, False, False, True, ObjectSelected, WindowLocation)
                |          
                |            'We loop onto mouse moves without click
                |            Do While Status = "MouseMove"
                |              If TempCircleHasBeenCreatedAtLeastOnce Then 
                |                Selection.Add Circle2D
                |                Selection.Delete
                |              End If
                |               
                |              Radius = Sqr( ( (WindowLocation(0) - XCenter) * (WindowLocation(0) - XCenter) )+ _ 
                |                            ( (WindowLocation(1) - YCenter) * (WindowLocation(1)
                |                            - YCenter) ) )
                |                             
                |              Set Circle2D = Factory2D.CreateClosedCircle(XCenter, YCenter, Radius)
                |              TempCircleHasBeenCreatedAtLeastOnce = 1
                |          
                |              Status = Selection.IndicateOrSelectElement2D("Select a point or click to locate the circle radius point", InputObjectType, False, False, True, ObjectSelected, WindowLocation)
                |            Loop
                |            
                |            'We go out if necessary
                |            If Status = "Cancel" Or Status = "Undo" Or Status = "Redo" Then 
                |               If TempCircleHasBeenCreatedAtLeastOnce Then 
                |                Selection.Add Circle2D
                |                Selection.Add HardCodedPoint
                |                Selection.Delete
                |               End if
                |               CATIA.HSOSynchronized = True
                |               CATIA.ScriptCommand = CatScriptCommandStop
                |               Exit Sub
                |            End If
                |            
                |            'We determine the possible selected point
                |            coordinates
                |            Dim ExistingPoint
                |            If ObjectSelected Then
                |              Set ExistingPoint = Selection.Item(1).Value
                |              ExistingPoint.GetCoordinates WindowLocation
                |              Selection.Clear
                |            End If
                |          
                |            'We clean up the temporary circle
                |            If TempCircleHasBeenCreatedAtLeastOnce Then 
                |              Selection.Add Circle2D
                |              Selection.Delete
                |            End If
                |            
                |            'We create the definitive circle
                |            Radius = Sqr( ( (WindowLocation(0) - XCenter) * (WindowLocation(0) - XCenter) )+ _ 
                |                          ( (WindowLocation(1) - YCenter) * (WindowLocation(1) -
                |                          YCenter) ) )
                |                           
                |            Set Circle2D = Factory2D.CreateClosedCircle(XCenter, YCenter, Radius)
                |            Selection.Add Circle2D
                |            
                |            CATIA.HSOSynchronized=True
                |              
                |          End Sub

        :param str i_message:
        :param tuple i_filter_type:
        :param bool i_may_skip_interactive_selection:
        :param bool i_tooltip:
        :param bool i_triggering_on_mouse_move:
        :param bool o_object_selected:
        :param tuple o_window_location:
        :return: str
        """
        return self.com_object.IndicateOrSelectElement2D(
            i_message,
            i_filter_type,
            i_may_skip_interactive_selection,
            i_tooltip,
            i_triggering_on_mouse_move,
            o_object_selected,
            o_window_location
        )

    def indicate_or_select_element_3d(
            self,
            i_planar_geometric_object: AnyObject,
            i_message: str,
            i_filter_type: tuple,
            i_may_skip_interactive_selection: bool,
            i_tooltip: bool,
            i_triggering_on_mouse_move: bool,
            o_object_selected: bool,
            o_window_location_2d: tuple,
            o_window_location_3d: tuple
    ) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func IndicateOrSelectElement3D(AnyObject iPlanarGeometricObject,CATBSTR
                | iMessage,CATSafeArrayVariant iFilterType,boolean
                | iMaySkipInteractiveSelection,boolean iTooltip,boolean
                | iTriggeringOnMouseMove,boolean oObjectSelected,CATSafeArrayVariant
                | oWindowLocation2D,CATSafeArrayVariant oWindowLocation3D) As
                | CATBSTR
                |     Runs an interactive command enabling both indication and selection, 3D
                |     version.
                |     Role: IndicateOrSelectElement3D asks the end user to select either a
                |     location into the window, or a feature (in the geometry or in the specification
                |     tree).
                |     During execution, when entering this method, the active editor must be in
                |     3D.
                |     Note: The method (and script execution) fails if one of the following error
                |     occurs:
                | 
                |         CATIA.ScriptCommand is equal to CatScriptCommandDefault.
                |         Selection.IndicateOrSelectElement3D cannot be called.
                |         CATIA.ScriptCommand is equal to CatScriptCommandStop.
                |         Selection.IndicateOrSelectElement3D cannot be called.
                | 
                | 
                |     Parameters:
                | 
                |         iPlanarGeometricObject
                |             A planar geometric object. 
                |         iMessage
                |             A string displayed in the status bar which tells the user what
                |             he/she should select (location, object...). 
                |         iFilterType
                |             An array of string constants defining the Automation object types
                |             with which the selection will be filtered.
                |             Note: If iFilterType contains only an empty string, the interactive
                |             command will only enable indication. 
                |         iMaySkipInteractiveSelection
                |             If true and if the user has selected something before running the
                |             script, the interactive step of this method will be skipped. See SelectElement
                |             . 
                |         iTooltip
                |             Displays a tooltip as soon as an object is located under the mouse
                |             without being selected. 
                |         iTriggeringOnMouseMove
                |             Triggers as soon as a mouse move event is detected. This option
                |             beeing set, oOutputState may be valued to "MouseMove".
                |             
                |         oObjectSelected
                |             Flag precising if the user choosed selection or indication.
                |             
                |         oWindowLocation2D
                |             X, Y - coordinates array of the location that the user specified
                |             into the window. This parameter is valuated only if oObjectSelected equals to
                |             False. 
                |         oWindowLocation3D
                |             X, Y, Z - coordinates array of the location that the user specified
                |             in the window. This parameter is valuated only if oObjectSelected equals to
                |             False. 
                |         oOutputState
                |             The state of the interactive command once IndicateOrSelectElement3D
                |             returns. The possible values are the same than the values described regarding
                |             the oOutputState parameter of the SelectElement method, except that "MouseMove"
                |             value can also be returned. 
                | 
                |     Example:
                | 
                |          The following example supposes that a part is currently edited,
                |          containing a plane. It creates a point 
                |          (see 
                |         HybridShapePointOnPlane ), asks the end user to select a location into
                |         the part window, onto the Plane.1 plane, or to select a
                |         point.
                | 
                |          As the mouse moves without clicking the left button, the location into
                |          the drawing window is determined, and the
                |          script creates a temporary point as feedback.
                | 
                |          A click into the window or the selection of a point definitively
                |          creates the point
                |          (see 
                |         HybridShapePointOnPlane ) located at the specified location (whether
                |         the location is a location into the part window or whether it is the existing
                |         point location).
                | 
                |          
                | 
                |          Option Explicit
                |          
                |          Sub CATMain()
                |            
                |            If TypeName(CATIA.ActiveEditor.ActiveObject) <> "Part" Then Exit
                |            Sub
                |            Dim Part
                |            Set Part = CATIA.ActiveEditor.ActiveObject
                |            
                |            Dim Selection
                |            Set Selection = CATIA.ActiveEditor.Selection
                |            
                |            CATIA.ScriptCommand = CatScriptCommandStart
                |            CATIA.HSOSynchronized = False
                |           
                |            Dim HybridShapeFactory, Body, HybridShapePlane,
                |            PlaneReference
                |            Set HybridShapeFactory = Part.HybridShapeFactory
                |            Set Body = Part.Bodies.Item("PartBody")
                |            Set HybridShapePlane = Body.HybridShapes.Item("Plane.1")
                |            Set PlaneReference = Part.CreateReferenceFromObject(HybridShapePlane)
                |          
                |            'We create a point
                |            Dim HardCodedPoint
                |            Set HardCodedPoint = HybridShapeFactory.AddNewPointOnPlane(PlaneReference,30.,30.)
                |            Body.InsertHybridShape HardCodedPoint
                |            Part.InWorkObject = HardCodedPoint
                |            Part.Update 
                |          
                |            'We ask the user to specify a location into the part window or a
                |            point
                |            Dim InputObjectType(0), Status, WindowLocation2D(1),
                |            WindowLocation3D(2), TempPointHasBeenCreatedAtLeastOnce,
                |            ObjectSelected
                |            InputObjectType(0) = "HybridShapePointOnPlane"
                |            Status = "MouseMove"
                |            TempPointHasBeenCreatedAtLeastOnce = 0
                |            Selection.Clear
                |            Status = Selection.IndicateOrSelectElement3D(HybridShapePlane, "Select a point or click to locate the point", InputObjectType, False, False, True, ObjectSelected, WindowLocation2D, WindowLocation3D)
                |          
                |            'We loop onto mouse moves without click
                |            Dim Point
                |            Do While Status = "MouseMove"
                |              If TempPointHasBeenCreatedAtLeastOnce Then 
                |                Selection.Add Point
                |                Selection.Delete
                |              End If
                |              Set Point = HybridShapeFactory.AddNewPointOnPlane(PlaneReference, WindowLocation2D(0), WindowLocation2D(1))
                |              Body.InsertHybridShape Point
                |              Part.InWorkObject = Point
                |              Part.Update 
                |              TempPointHasBeenCreatedAtLeastOnce = 1
                |              
                |              Status = Selection.IndicateOrSelectElement3D(HybridShapePlane, "Select a point or click to locate the point", InputObjectType, False, False, True, ObjectSelected, WindowLocation2D, WindowLocation3D)
                |            Loop
                |           
                |            'We go out if necessary
                |            If Status = "Cancel" Or Status = "Undo" Or Status = "Redo" Then 
                |              If TempPointHasBeenCreatedAtLeastOnce Then 
                |                Selection.Add Point
                |                Selection.Add HardCodedPoint
                |                Selection.Delete
                |                Part.Update
                |              End If
                |              CATIA.HSOSynchronized = True
                |              CATIA.ScriptCommand = CatScriptCommandStop
                |              Exit Sub
                |            End If
                |            
                |            'We determine the possible selected point
                |            coordinates
                |            If ObjectSelected Then
                |              Dim ExistingPoint
                |              Set ExistingPoint = Selection.Item(1).Value
                |              WindowLocation2D(0) = ExistingPoint.XOffset.Value
                |              WindowLocation2D(1) = ExistingPoint.YOffset.Value
                |              Selection.Clear
                |            End If
                |          
                |            'We cleanup the temporary point
                |            If TempPointHasBeenCreatedAtLeastOnce Then 
                |              Selection.Add Point
                |              Selection.Delete
                |            End If
                |            
                |            'We create the definitive point
                |            Set Point = HybridShapeFactory.AddNewPointOnPlane(PlaneReference, WindowLocation2D(0), WindowLocation2D(1))
                |            Body.InsertHybridShape Point 
                |            Part.InWorkObject = Point 
                |            Part.Update
                |            
                |            CATIA.HSOSynchronized = True
                |            CATIA.ScriptCommand = CatScriptCommandStop
                |           
                |          End Sub

        :param AnyObject i_planar_geometric_object:
        :param str i_message:
        :param tuple i_filter_type:
        :param bool i_may_skip_interactive_selection:
        :param bool i_tooltip:
        :param bool i_triggering_on_mouse_move:
        :param bool o_object_selected:
        :param tuple o_window_location_2d:
        :param tuple o_window_location_3d:
        :return: str
        """
        return self.com_object.IndicateOrSelectElement3D(
            i_planar_geometric_object.com_object,
            i_message,
            i_filter_type,
            i_may_skip_interactive_selection,
            i_tooltip,
            i_triggering_on_mouse_move,
            o_object_selected,
            o_window_location_2d,
            o_window_location_3d
        )

    def item(self, i_index: int) -> SelectedElement:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func Item(long iIndex) As SelectedElement
                |     Returns the iIndex-th SelectedElement object contained by the current
                |     selection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the SelectedElement object to return,
                |             1≤iIndex≤Selection.Count . 
                |         oSelectedElement
                |             The SelectedElement object 
                | 
                |     Example:
                | 
                |          See the 
                |         SelectMultipleElements method first example.

        :param int i_index:
        :return: SelectedElement
        """
        return SelectedElement(self.com_object.Item(i_index))

    def item2(self, i_index: int) -> SelectedElement:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func Item2(long iIndex) As SelectedElement
                | 
                |     Deprecated:
                |         R207 Item

        :param int i_index:
        :return: SelectedElement
        """
        return SelectedElement(self.com_object.Item2(i_index))

    def paste(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Paste()
                |     Puts the contents of the clipboard in the Editor at the indicated
                |     location.
                |     Role: After the execution of the Paste method, there may be, among the
                |     pasted features, some which are not exposed to Automation. If so, the Paste
                |     operation will be performed anyway.
                | 
                |     Example:
                | 
                |          CATIA.ActiveEditor.Selection.Paste

        :return: None
        """
        return self.com_object.Paste()

    def paste_from(self, i_objects: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub PasteFrom(CATSafeArrayVariant iObjects)
                |     Pastes an array of elements in the Editor at the indicated
                |     location.
                |     Role: After the execution of the Paste method, there may be, among the
                |     pasted features, some which are not exposed to Automation. If so, the Paste
                |     operation will be performed anyway.
                |
                |     Example:
                |
                |          ReDim Object(0)
                |          Object(0)=WhateverObject
                |          CATIA.ActiveEditor.Selection.PasteFrom(Object)

        :param tuple i_objects:
        :return: None
        """
        return self.com_object.PasteFrom(i_objects)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'paste_from'
        # vba_code = """
        # Public Function paste_from(selection)
        #     Dim iObjects (2)
        #     selection.PasteFrom iObjects
        #     paste_from = iObjects
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def paste_special(self, i_format: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub PasteSpecial(CATBSTR iFormat)
                |     Puts the contents of the clipboard in the Editor at the indicated location,
                |     according to the specified format.
                |     Role: After the execution of the PasteSpecial method, there may be, among
                |     the pasted features, some which are not exposed to Automation. If so, the
                |     PasteSpecial operation will be performed anyway.
                | 
                |     Formats are:
                | 
                |         In all containers
                |         "CATIA_LINK_FORMAT" to paste "Catia Link Source",
                |         "OLE_LINK_FORMAT" to paste "Ole Link Source",
                |         "OLE_EMBED_FORMAT" to paste "Ole Embed Source".
                | 
                | 
                |         In a Part container
                |         "CATPrtCont" to paste "As Specified In Part
                |         representation",
                |         "CATPrtResultWithOutLink" to paste "AsResult",
                |         "CATPrtResult" to paste "AsResultWithLink",
                |         "CATMaterialCont" to paste "As material",
                |         "AsMaterialLink" to paste "As material link",
                |         "CATMechProdCont" to paste "As specified in Assembly",
                |         "CATProdCont" to paste "As specified in Product
                |         Structure",
                |         "CATIA_SPEC" to paste "CATIA_SPEC",
                |         "CATIA_RESULT" to paste "CATIA_RESULT".
                | 
                |         Warning:
                | 
                |              Using PasteSpecial with CATPrtResult will not copy links between
                |              several Part containers. This API does not support
                |              it.
                |              It will copy links only for copy paste operations inside the same
                |              Part Container.
                |              This is a different behavior from the interactive
                |              one.
                |              To perform copy paste operation as result with link between
                |              several Part Containers, it must be done
                |              interactively.
                |              
                |              
                | 
                | 
                |         In a Product container
                |         "CATProdCont" to paste "As specified in Product
                |         Structure",
                | 
                | 
                |         In a Process container
                |         "SPPProcessCont" to paste "Simple paste",
                |         "SPP_I" to paste "Paste with Items",
                |         "SPP_R" to paste "Paste with Resources",
                |         "SPP_IR" to paste "Paste with Items and Resources",
                |         "SPPI_I" to paste "Paste with Items and entire
                |         hierarchy",
                |         "SPPI_R" to paste "Paste with Resources and entire
                |         hierarchy",
                |         "SPPI_IR" to paste "Paste with Items and Resources and entire
                |         hierarchy".
                | 
                | 
                |         In a Material container
                |         "CATMaterialCont" to paste "As material",
                |         "AsMaterialLink" to paste "As material link".
                | 
                | 
                |         In a Rendering Scene container
                |         "CATRscLightContainer" to paste "As light",
                |         "CATRscEnvironmentContainer" to paste "As
                |         environment",
                |         "CATRscShootingContainer" to paste "As shooting",
                |         "CATRscTurntableContainer" to paste "As turntable".
                | 
                | 
                |         In a Deneb Resource Program container
                |         "DNBProgCont" to paste "Resource Program".
                | 
                | 
                |         In a Behavior container
                |         "Behaviors" to paste "Behaviors".
                | 
                | 
                |         In a CATCamera container
                |         "CATCameraContainer" to paste "Camera".
                | 
                | 
                |     To learn more about these formats, refer to the equivalent interactive
                |     command.
                | 
                |     Example:
                | 
                |          CATIA.ActiveEditor.Selection.PasteSpecial
                |          "CATPrtResultWithOutLink"

        :param str i_format:
        :return: None
        """
        return self.com_object.PasteSpecial(i_format)

    def remove(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Remove(long iIndex)
                |     Removes the iIndex-th SelectedElement object contained by the current
                |     selection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the SelectedElement object to remove,
                |             1≤iIndex≤Selection.Count .
                | 
                |             Example:
                |                 This example removes the second SelectedElement object
                |                 contained by the current selection.
                | 
                |                  CATIA.ActiveEditor.Selection.Remove(2)

        :param int i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def remove2(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Remove2(long iIndex)
                | 
                |     Deprecated:
                |         R207 Remove

        :param int i_index:
        :return: None
        """
        return self.com_object.Remove2(i_index)

    def search(self, i_string_bstr: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Search(CATBSTR iStringBSTR)
                |     Finds an object in the Editor using the Edit/Search grammar, and fills the
                |     selection with the results.
                |     A criterium is created, based on the Search grammar, which also defines the
                |     investigation field depth.
                |     Note: After the execution of the Search method, there may be, among the
                |     selected features, some which are not exposed to
                |     Automation.
                | 
                |     Example:
                |         The following example searches the objects matching the following
                |         criterium in the whole CATIAEditor: Part.Sketcher.Color='White'
                |         .
                | 
                |         CATIA.ActiveEditor.Selection.Search("Part.Sketcher.Color='White',all")

        :param str i_string_bstr:
        :return: None
        """
        return self.com_object.Search(i_string_bstr)

    def select_element(self, i_filter_type: tuple, i_message: str, i_may_skip_interactive_selection: bool) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Func SelectElement(CATSafeArrayVariant iFilterType,CATBSTR iMessage,boolean
                | iMaySkipInteractiveSelection) As CATBSTR
                |     Runs an interactive selection command.
                |     Role: SelectElement asks the end user to select a feature (in the geometry
                |     or in the specification tree). During the selection, when the end user moves
                |     the mouse above a feature which fits in the given filter, the mouse pointer
                |     turns into the "hand" cursor; otherwise into the "no entry"
                |     cursor.
                |
                |         If iMaySkipInteractiveSelection is equal to False:
                |         The end user is asked to interactively select an appropriate element.
                |         When this is done, the Selection object is cleared, and filled with the
                |         selected element.
                |
                |         If iMaySkipInteractiveSelection is equal to True:
                |         SelectElement determines whether the already selected objects (
                |         SelectedElement.Value ) are appropriate:
                |             If it is the case, the interaction step is skipped, the Selection
                |             object is cleared, and filled with the appropriate
                |             element.
                |             Otherwise, the Selection object is cleared, and the end user is
                |             asked to interactively select an appropriate
                |             element.
                |         Note: During the selection scan to find an Automation object, a
                |         "Product" string constant specified in iFilterType will imply that
                |         SelectElement will also look for the possible Automation object specified in
                |         SelectedElement.LeafProduct .
                |
                |     Note: The method (and script execution) fails if one of the following error
                |     occurs:
                |
                |         CATIA.ScriptCommand is equal to CatScriptCommandDefault.
                |         Selection.SelectElement cannot be called.
                |         CATIA.ScriptCommand is equal to CatScriptCommandStop.
                |         Selection.SelectElement cannot be called.
                |
                |     Note: After a call to SelectElement, if the return value is "Normal", a
                |     call to the Count method will return one, and a call to Item(1) will return the
                |     selected element.
                |
                |     Note: If the scripting language is VBA or VSTA, the use of an interactive
                |     selection method (such as this one) from within a user form is
                |     unadvised.
                |     Indeed, interactive selection methods are blocking commands inside CATIA,
                |     but non-blocking inside VBA/VSTA user forms. This means that the end user can
                |     continue interacting with the user form, and potentially execute additional
                |     CATIA Automation methods. This could lead to unpredictable
                |     results.
                |     The code should be written in the following way:
                |
                |       - macro module main variables:
                |         Dim AFormMethodIsBeingExecuted As Boolean
                |
                |       - form method calling SelectElement:
                |         Private Sub
                |         FormPossessingOneMethodCallingSelectElement_Click()
                |             Dim InputObjectType(0), Status
                |             AFormMethodIsBeingExecuted = True
                |             InputObjectType(0) = "TriDimFeatEdge"
                |             Status = Selection.SelectElement(InputObjectType, "Select an edge", False)
                |             AFormMethodIsBeingExecuted = False
                |         End Sub
                |
                |       - sample form method:
                |         Private Sub SampleForm_Click()
                |             If (AFormMethodIsBeingExecuted) Then
                |               'we go out of the method
                |               CATIA.HSOSynchronized = True
                |               Exit Sub
                |             End If
                |             . . .
                |             'content of the form method itself
                |             . . .
                |         End Sub
                |
                |     Parameters:
                |
                |         iFilterType
                |             An array of string constants defining the Automation object types
                |             with which the selection will be filtered. The resulting filter is a logical OR
                |             of the supplied string constants. For instance, if the array contains two
                |             elements "Point" and "Line", moving the mouse over a feature of
                |             HybridShapePointCoord type will show a "hand" cursor. Contrarily, if the
                |             feature under the mouse is neither a Point nor a Line, the cursor will be a "no
                |             entry" cursor.
                |
                |             Beside the regular Automation object names, CATSelectionFilter
                |             value names are also supported.
                |         iMessage
                |             A string displayed in the status bar which tells the user what
                |             he/she should select (location, object...).
                |         iMaySkipInteractiveSelection
                |             If true and if the user has selected something before running the
                |             script, the interactive step of this method will be skipped. Note: If any of
                |             the previously selected elements is not part of the input filter, SelectElement
                |             will be interactive. Also note that iMaySkipInteractiveSelection can be False
                |             even if the selection is not empty before entering the method. This keeps the
                |             previously selected elements highlighted during the selection, but also
                |             requires the user to re-select them if he/she wants so. Otherwise, when
                |             SelectElement ends, they will not be selected anymore.
                |
                |         oOutputState
                |             The state of the selection command after SelectElement returns. It
                |             can either be "Normal", "Cancel", "Undo" or
                |             "Redo".
                |             Note: "Cancel" value is returned if any of the following cases
                |             occured:
                |
                |                 the user started another command
                |                 ESCAPE key was pressed
                |                 another window was selected
                |
                |             Caution: The script should exit properly (after the necessary
                |             clean-up) when "Cancel" value is returned.
                |             If not, an error message may be displayed when running the
                |             following selection methods.
                |
                |     Example:
                |
                |          The following example asks the end user to select a sketch (see
                |
                |         Sketch ) in the current  window, and creates a Pad (see
                |
                |         ShapeFactory.AddNewPad ). If, before the script execution, a sketch was
                |         already selected, it will be taken into account.
                |
                |          Then, it asks the end user to select an edge of the pad, and creates
                |          an edge fillet. The end user
                |          is asked to select a 1-D entity whose geometry is rectilinear (see
                |
                |         CATSelectionFilter ), such as an edge of the Pad.
                |          Next, the end user should select a pad face which is perpendicular to
                |          the 1-D entity previously selected. Finally, it
                |          creates a hole at the face selected point, the hole direction being
                |          the direction of the 1-D selected entity.
                |
                |          During the face selection, the 1-D entity previously selected is
                |          highlighted.
                |
                |          Option Explicit
                |
                |          Sub CATMain()
                |
                |            If TypeName(CATIA.ActiveEditor.ActiveObject) <> "Part"
                |            Then
                |              CATIA.SystemService.Print "Not in Part context"
                |              Exit Sub
                |            End If
                |            Dim Part
                |            Set Part = CATIA.ActiveEditor.ActiveObject
                |
                |            Dim Selection
                |            Set Selection = CATIA.ActiveEditor.Selection
                |
                |            Dim ShapeFactory, SketchHasBeenAcquiredAtLeastOnce,
                |            EdgeHasBeenAcquiredAtLeastOnce,
                |            FaceHasBeenAcquiredAtLeastOnce,MonoDimEntityHasBeenAcquiredAtLeastOnce,
                |            FirstExtrudeNotFinished
                |            Set ShapeFactory = Part.ShapeFactory
                |            SketchHasBeenAcquiredAtLeastOnce = False
                |            EdgeHasBeenAcquiredAtLeastOnce = False
                |            FaceHasBeenAcquiredAtLeastOnce = False
                |            MonoDimEntityHasBeenAcquiredAtLeastOnce = False
                |            FirstExtrudeNotFinished = True
                |
                |            CATIA.ScriptCommand = CatScriptCommandStart
                |            CATIA.HSOSynchronized = False
                |
                |            'We save the current selection content
                |            ReDim SelectionAtBeginning(1)
                |            ReDim SelectionAtBeginning(Selection.Count)
                |            Dim SelectionObjectIndex
                |            For SelectionObjectIndex = 0 To Selection.Count - 1
                |              Set SelectionAtBeginning(SelectionObjectIndex) = Selection.Item(1).Value
                |            Next
                |            Dim SelectionAtBeginningLength
                |            SelectionAtBeginningLength = Selection.Count
                |
                |            'Feature creation
                |            Dim PadNotFinished, Status, SketchForPadPartBody, SelectedElement,
                |            MonoDimEntity
                |            PadNotFinished = True
                |
                |            Do While PadNotFinished
                |              'We ask the user to select a sketch
                |              Dim InputObjectType(0)
                |              InputObjectType(0) = "Sketch"
                |              Status = Selection.SelectElement(InputObjectType, "Select a sketch", True)
                |
                |              If Status = "Cancel" Or Status = "Undo" Then
                |                'We restore the selection to its initial
                |                content
                |                Selection.Clear
                |                For SelectionObjectIndex = 0 To SelectionAtBeginningLength - 1
                |                       Selection.Add SelectionAtBeginning(SelectionObjectIndex)                |                Next
                |                CATIA.HSOSynchronized = True
                |                CATIA.ScriptCommand = CatScriptCommandStop
                |                Exit Sub
                |
                |              ElseIf Status = "Redo" And Not SketchHasBeenAcquiredAtLeastOnce then
                |                'We do nothing: Redo has no meaning in this
                |                context
                |
                |              Else
                |                Dim SketchForPad
                |                If Status <> "Redo" Then Set SketchForPad = Selection.Item(1).Value
                |                SketchHasBeenAcquiredAtLeastOnce = True
                |
                |                'We determine the PartBody corresponding to the
                |                Sketch
                |                Set SketchForPadPartBody = SketchForPad.Parent.Parent
                |
                |                'We create the Pad
                |                Dim Pad
                |                Set Pad = ShapeFactory.AddNewPad(SketchForPad, 20.0)
                |                Pad.SecondLimit.Dimension.Value = 0.0
                |                Part.Update
                |                PadNotFinished = False
                |                Selection.Clear
                |
                |                'We create the fillet and the hole
                |                Dim FilletNotFinished
                |                FilletNotFinished = True
                |
                |                Do While (FilletNotFinished And Not
                |                PadNotFinished)
                |                  'We ask the user to select an edge
                |                  InputObjectType(0) = "TriDimFeatEdge"
                |                  Status = Selection.SelectElement(InputObjectType, "Select an edge of the Pad", False)
                |
                |                  If Status = "Cancel" Then
                |                    'We remove the pad, restore the selection to its initial
                |                    content and go out
                |                    Selection.Clear
                |                    Selection.Add(Pad)
                |                    Selection.Delete
                |                    Part.Update
                |                    Selection.Clear
                |                    For SelectionObjectIndex = 0 To SelectionAtBeginningLength - 1
                |                      Selection.Add SelectionAtBeginning(SelectionObjectIndex)                |                    Next
                |                    CATIA.HSOSynchronized = True
                |                    CATIA.ScriptCommand = CatScriptCommandStop
                |                    Exit Sub
                |
                |                  ElseIf Status = "Redo" And Not EdgeHasBeenAcquiredAtLeastOnce Then
                |                    'We do nothing: Redo has no meaning in this
                |                    context
                |
                |                  ElseIf Status = "Undo" then
                |                    'We copy the sketch to the clipboard
                |                    Selection.Clear
                |                    Selection.Add(SketchForPad)
                |
                |                    'We remove the pad
                |                    Selection.Clear
                |                    Selection.Add(Pad)
                |                    Selection.Delete
                |                    Part.Update
                |
                |                    'We re-create the sketch
                |                    Selection.Clear
                |                    Selection.Add(SketchForPadPartBody)
                |                    Selection.Paste
                |
                |                    PadNotFinished = True
                |
                |                  Else
                |                    Dim FilletEdge
                |                    If Status <> "Redo" then Set FilletEdge = Selection.Item(1).Value
                |                    EdgeHasBeenAcquiredAtLeastOnce = True
                |
                |                    'Create the Fillet
                |                    Dim Fillet
                |                    Set Fillet = ShapeFactory.AddNewSolidEdgeFilletWithConstantRadius(FilletEdge, catTangencyFilletEdgePropagation, 5.0)
                |                    Part.Update
                |                    FilletNotFinished = False
                |                    Selection.Clear
                |
                |                    'Determine the 1-D entity
                |                    Dim MonoDimEntityDeterminationNotFinished
                |                    MonoDimEntityDeterminationNotFinished = True
                |
                |                    Do While MonoDimEntityDeterminationNotFinished And Not
                |                    FilletNotFinished
                |                      'We ask the user to select a 1-D entity whose geometry is
                |                      rectilinear
                |                      InputObjectType(0) = "RectilinearMonoDim"
                |                      Status=Selection.SelectElement(InputObjectType, "Select a
                |                      1-D entity whose geometry is rectilinear", False)
                |
                |
                |                      If Status = "Cancel" Then
                |                        'We remove the fillet, the pad, restore the selection to
                |                        its initial content and go out
                |                        Selection.Clear
                |                        Selection.Add(Fillet)
                |                        Selection.Delete
                |                        Selection.Clear
                |                        Selection.Add(Pad)
                |                        Selection.Delete
                |                        Part.Update
                |                        Selection.Clear
                |                        For SelectionObjectIndex = 0 To SelectionAtBeginningLength - 1
                |                          Selection.Add SelectionAtBeginning(SelectionObjectIndex)                |                        Next
                |                        CATIA.HSOSynchronized = True
                |                        CATIA.ScriptCommand = CatScriptCommandStop
                |                        Exit Sub
                |
                |                      ElseIf Status = "Redo" And Not MonoDimEntityHasBeenAcquiredAtLeastOnce Then
                |                        'We do nothing: Redo has no meaning in this
                |                        context
                |
                |                      ElseIf Status = "Undo" then
                |                        'We remove the fillet
                |                        Selection.Clear
                |                        Selection.Add(Fillet)
                |                        Selection.Delete
                |                        Part.Update
                |                        FilletNotFinished = True
                |
                |                      Else
                |                        If Status = "Redo" Then
                |                          Selection.Clear
                |                          Selection.Add(MonoDimEntity)
                |                        Else
                |                          Set SelectedElement = Selection.Item(1)
                |                          Set MonoDimEntity = SelectedElement.Value
                |                        End If
                |
                |                        MonoDimEntityHasBeenAcquiredAtLeastOnce = True
                |                        MonoDimEntityDeterminationNotFinished = False
                |
                |                        'Create the Hole
                |                        Dim HoleNotFinished, MonoDimEntitySave
                |                        HoleNotFinished = True
                |
                |                        Do While HoleNotFinished And Not
                |                        MonoDimEntityDeterminationNotFinished
                |                          'We save the selection content in save
                |                          variables.
                |                          'This corresponds to the fact that:
                |                          '  - we want that, during the following call to
                |                          SelectElement, the 1-D entity
                |                          previously
                |                          '    selected remains highlighted
                |                          '  - this is done using the False value of the
                |                          iMaySkipInteractiveSelection
                |                          '    parameter, the selection containing the 1-D
                |                          entity. It requires that the
                |                          selection
                |                          '    content be saved
                |                          Set MonoDimEntitySave = Selection.Item(1).Value
                |
                |                          'We ask the user to select a face
                |                          InputObjectType(0) = "Face"
                |                          Status = Selection.SelectElement(InputObjectType, "Select a face perpendicular to the 1-D entity", False)
                |
                |                          If Status = "Cancel" Then
                |                            'We remove the fillet, the pad, restore the
                |                            selection of the editor which was active before the selection to its initial
                |                            content and go out
                |                            Selection.Clear
                |                            Selection.Add(Fillet)
                |                            Selection.Delete
                |                            Selection.Clear
                |                            Selection.Add(Pad)
                |                            Selection.Delete
                |                            Selection.Clear
                |                            For SelectionObjectIndex = 0 to SelectionAtBeginningLength - 1
                |                                 Selection.Add SelectionAtBeginning(SelectionObjectIndex)                |                            Next
                |                            Part.Update
                |                            CATIA.HSOSynchronized = True
                |                            CATIA.ScriptCommand = CatScriptCommandStop
                |                            Exit Sub
                |
                |                          ElseIf Status = "Redo" And Not FaceHasBeenAcquiredAtLeastOnce Then
                |                            'We do nothing: Redo has no meaning in this
                |                            context
                |
                |                          ElseIf Status = "Undo" Then
                |                            Selection.Clear
                |                            'The 1-D entity must be re-selected
                |                            MonoDimEntityDeterminationNotFinished = True
                |
                |                          Else
                |                            Dim PadFace, HoleLocation(2)
                |
                |                            If Status <> "Redo" Then
                |                              Set SelectedElement = Selection.Item(1)
                |                              Set PadFace = SelectedElement.Value
                |                              SelectedElement.GetCoordinates
                |                              HoleLocation
                |
                |                              'We merge the selected element with the save
                |                              variables, and put the result in the
                |                              selection
                |                              Selection.Add MonoDimEntitySave
                |                            End If
                |
                |                            FaceHasBeenAcquiredAtLeastOnce = True
                |
                |                            'We create the Hole
                |                            Dim Hole
                |                            Set Hole = Part.ShapeFactory.AddNewHoleFromPoint(HoleLocation(0), HoleLocation(1), HoleLocation(2), PadFace, 10.0)
                |                            Hole.ThreadingMode = 1
                |                            Hole.ThreadSide = 0
                |                            Hole.Diameter.Value = 5.0
                |                            Hole.SetDirection FilletEdge
                |                            Part.Update
                |                            HoleNotFinished = False
                |
                |                            'We clear the selection
                |                            Selection.Clear
                |                          End If  'Face selected
                |                        Loop    'Hole created
                |                      End If  'Monodim entity selected
                |                    Loop    'Monodim entity determined
                |                  End If  'Edge selected
                |                Loop    'Fillet created
                |              End If  'Sketch selected
                |            Loop    'Pad creation
                |
                |            CATIA.HSOSynchronized = True
                |            CATIA.ScriptCommand = CatScriptCommandStop
                |
                |          End Sub

        :param tuple i_filter_type:
        :param str i_message:
        :param bool i_may_skip_interactive_selection:
        :return: str
        """
        return self.com_object.SelectElement(i_filter_type, i_message, i_may_skip_interactive_selection)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'select_element'
        # vba_code = """
        # Public Function select_element(selection)
        #     Dim iFilterType (2)
        #     selection.SelectElement iFilterType
        #     select_element = iFilterType
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def select_element2(
            self,
            i_filter_type: tuple,
            i_message: str,
            i_object_selection_before_command_use_possibility: bool
    ) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Func SelectElement2(CATSafeArrayVariant iFilterType,CATBSTR iMessage,boolean
                | iObjectSelectionBeforeCommandUsePossibility) As CATBSTR
                |
                |     Deprecated:
                |         R207 SelectElement

        :param tuple i_filter_type:
        :param str i_message:
        :param bool i_object_selection_before_command_use_possibility:
        :return: str
        """
        return self.com_object.SelectElement2(
            i_filter_type,
            i_message,
            i_object_selection_before_command_use_possibility
        )
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'select_element2'
        # vba_code = """
        # Public Function select_element2(selection)
        #     Dim iFilterType (2)
        #     selection.SelectElement2 iFilterType
        #     select_element2 = iFilterType
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def select_element3(
            self,
            i_filter_type: tuple,
            i_message: str,
            i_object_selection_before_command_use_possibility: bool,
            i_multi_selection_mode: CATMultiSelectionMode,
            i_tooltip: bool
    ) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Func SelectElement3(CATSafeArrayVariant iFilterType,CATBSTR iMessage,boolean
                | iObjectSelectionBeforeCommandUsePossibility,CATMultiSelectionMode
                | iMultiSelectionMode,boolean iTooltip) As CATBSTR
                |
                |     Deprecated:
                |         R207 SelectMultipleElements

        :param tuple i_filter_type:
        :param str i_message:
        :param bool i_object_selection_before_command_use_possibility:
        :param CATMultiSelectionMode i_multi_selection_mode:
        :param bool i_tooltip:
        :return: str
        """
        return self.com_object.SelectElement3(
            i_filter_type,
            i_message,
            i_object_selection_before_command_use_possibility,
            i_multi_selection_mode.com_object,
            i_tooltip
        )
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'select_element3'
        # vba_code = """
        # Public Function select_element3(selection)
        #     Dim iFilterType (2)
        #     selection.SelectElement3 iFilterType
        #     select_element3 = iFilterType
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def select_element_other_editor(
            self,
            i_filter_type: tuple,
            i_active_editor_message: str,
            i_non_active_editor_message: str,
            i_tooltip: bool,
            o_editor: Editor
    ) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Func SelectElementOtherEditor(CATSafeArrayVariant iFilterType,CATBSTR
                | iActiveEditorMessage,CATBSTR iNonActiveEditorMessage,boolean iTooltip,Editor
                | oEditor) As CATBSTR
                |     Runs an interactive selection command, enabling the selection in a
                |     non-active editor.
                |     Role: SelectElementOtherEditor asks the end user to select a feature (in
                |     the geometry or in the specification tree) of a non-active editor. During the
                |     selection, when the end user moves the mouse above a feature (in a non-active
                |     editor) which fits in the given filter, the mouse pointer turns into the "hand"
                |     cursor. Otherwise, into the "no entry" cursor.
                |     This method may be used, for example, to write a script which does the
                |     following:
                |
                |         a drawing is currently edited
                |         the user is asked to select a reference plane in the 3D geometry (a
                |         part)
                |         a front view is created in the drawing, projecting the 3D geometry onto
                |         the selected reference plane
                |
                |
                |     Compared to the SelectElement , the result of the selection will not be
                |     accessed through the Count and Item methods of the current selection object,
                |     but through the Count and Item methods of the Selection object aggregated by
                |     the Editor object returned through the oEditor parameter.
                |     Note: the Selection object aggregated by the Editor object returned through
                |     the oEditor parameter is emptied by before the effective interactive
                |     selection.
                |
                |     Parameters:
                |
                |         iFilterType
                |             An array of string constants defining the Automation object types
                |             with which the selection will be filtered.
                |         iActiveEditorMessage
                |             A string displayed in the status bar when the current editor is
                |             active, and which tells the user what he/she should select (location,
                |             object...).
                |         iNonActiveEditorMessage
                |             A string displayed in the status bar when another editor is active,
                |             and which tells the user what he/she should select (location, object...).
                |
                |         iTooltip
                |             Displays a tooltip as soon as an object is located under the mouse
                |             without being selected.
                |         oOutputState
                |             The state of the selection command after SelectElementOtherEditor
                |             returns. It can either be "Normal", "Cancel", "Undo" or "Redo".
                |
                |
                |     Example:
                |
                |          The following example supposes that a part, containing a pad, and
                |          drawing are currently edited, the drawing
                |          window being the current window. It asks the end user to select a 2-D
                |          topological entity, such as a
                |
                |         Plane , in a part. Then it creates a front view in the drawing,
                |         projecting the 3D geometry onto the selected 2-D topological
                |         entity.
                |
                |
                |          Option Explicit
                |
                |          Sub CATMain()
                |
                |            If TypeName(CATIA.ActiveEditor.ActiveObject) <> "DrawingRoot"
                |            Then
                |              CATIA.SystemService.Print "Not in Drawing
                |              context"
                |              Exit Sub
                |            End If
                |
                |            Dim DrawingSheets
                |            Set DrawingSheets  = CATIA.ActiveEditor.ActiveObject.Sheets
                |
                |            Dim DrawingSelection
                |            Set DrawingSelection = CATIA.ActiveEditor.Selection
                |
                |            CATIA.ScriptCommand = CatScriptCommandStart
                |            CATIA.HSOSynchronized = False
                |
                |            Dim DrawingSheet
                |            Set DrawingSheet = DrawingSheets.ActiveSheet
                |
                |            'We save the current selection content
                |            ReDim
                |            DrawingSelectionAtBeginning(DrawingSelection.Count)
                |            Dim SelectionObjectIndex
                |            For SelectionObjectIndex = 0 To DrawingSelection.Count - 1
                |               Set DrawingSelectionAtBeginning(SelectionObjectIndex) = DrawingSelection.Item(1).Value
                |            Next
                |            Dim SelectionAtBeginningLength
                |            SelectionAtBeginningLength = DrawingSelection.Count
                |
                |            'Feature creation
                |            Dim Status, InputObjectType(0), oOtherEditor
                |            InputObjectType(0) = "BiDimInfinite"
                |
                |            Status = DrawingSelection.SelectElementOtherEditor( InputObjectType, "Select a 2-D topological entity in a 3-D geometry", "Select a 2-D topological entity", False, oOtherEditor)
                |            If Status = "Cancel" Or Status = "Undo" Or Status = "Redo" Then
                |              'We restore the selection to its initial content
                |              oOtherEditor.Selection.Clear
                |              For SelectionObjectIndex = 0 to SelectionAtBeginningLength - 1
                |                DrawingSelection.Add DrawingSelectionAtBeginning(SelectionObjectIndex)                |              Next
                |              Exit Sub
                |
                |            Else
                |              Dim BiDimFeature, V1(2), V2(2)
                |              Set BiDimFeature = oOtherEditor.Selection.Item(1).Value
                |              If TypeName(BiDimFeature) = "Plane" Or TypeName(BiDimFeature) = "PlanarFace" Then
                |                BiDimFeature.GetFirstAxis V1
                |                BiDimFeature.GetSecondAxis V2
                |              Else
                |                Exit Sub
                |              End If
                |
                |              'We create a view called "Front View" in the current sheet, using
                |              the Plane as projection plane, and whose origin coordinates are
                |              (300,150)
                |              Dim DrawingFrontView
                |              Set DrawingFrontView = DrawingSheet.Views.AddFrontView(300., 150., "Front View", V1(0), V1(1), V1(2), V2(0), V2(1), V2(2))
                |
                |              oOtherEditor.Selection.Clear
                |            End If
                |
                |            CATIA.HSOSynchronized = True
                |            CATIA.ScriptCommand = CatScriptCommandStop
                |
                |          End Sub

        :param tuple i_filter_type:
        :param str i_active_editor_message:
        :param str i_non_active_editor_message:
        :param bool i_tooltip:
        :param Editor o_editor:
        :return: str
        """
        return self.com_object.SelectElementOtherEditor(
            i_filter_type,
            i_active_editor_message,
            i_non_active_editor_message,
            i_tooltip,
            o_editor.com_object
        )
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'select_element_other_editor'
        # vba_code = """
        # Public Function select_element_other_editor(selection)
        #     Dim iFilterType (2)
        #     selection.SelectElementOtherEditor iFilterType
        #     select_element_other_editor = iFilterType
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def select_multiple_elements(
            self,
            i_filter_type: tuple,
            i_message: str,
            i_may_skip_interactive_selection: bool,
            i_multi_selection_mode: CATMultiSelectionMode,
            i_tooltip: bool
    ) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Func SelectMultipleElements(CATSafeArrayVariant iFilterType,CATBSTR
                | iMessage,boolean iMaySkipInteractiveSelection,CATMultiSelectionMode
                | iMultiSelectionMode,boolean iTooltip) As CATBSTR
                |     Runs an interactive multiselection command.
                |     Role: SelectMultipleElements asks the end user to select a feature (in the
                |     geometry or in the specification tree). It is identical to the SelectElement
                |     method except that it manages complex uses through the specification of two
                |     additional parameters.
                |     Note: The method (and script execution) fails if one of the following error
                |     occurs:
                |
                |         CATIA.ScriptCommand is equal to CatScriptCommandDefault.
                |         Selection.SelectMultipleElements cannot be called.
                |         CATIA.ScriptCommand is equal to CatScriptCommandStop.
                |         Selection.SelectMultipleElements cannot be called.
                |
                |     Parameters:
                |
                |         iFilterType
                |             An array of string constants defining the Automation object types
                |             with which the selection will be filtered.
                |         iMessage
                |             A string displayed in the status bar which tells the user what
                |             he/she should select (location, object...).
                |         iMaySkipInteractiveSelection
                |             If true and if the user has selected something before running the
                |             script, the interactive step of this method will be skipped. See SelectElement
                |             .
                |         iMultiSelectionMode
                |             The type of multi-selection which will be offered to the user.
                |
                |         iTooltip
                |             Displays a tooltip as soon as an object is located under the mouse
                |             without being selected.
                |         oOutputState
                |             The state of the selection command after SelectMultipleElements
                |             returns. It can either be "Normal", "Cancel", "Undo" or "Redo". See
                |             SelectElement .
                |
                |     Example:
                |
                |          This first example asks the end user to select several points (see
                |
                |         Point ) into the current Part window, drawing a trap, and performs a
                |         symmetry with respect to the XZ plane on the selected points
                |
                |          (see
                |         HybridShapeSymmetry ). The points can be selected before running the
                |         script.
                |
                |
                |          Option Explicit
                |
                |          Sub CATMain()
                |
                |            If TypeName(CATIA.ActiveEditor.ActiveObject) <> "Part" Then Exit
                |            Sub
                |            Dim Part
                |            Set Part = CATIA.ActiveEditor.ActiveObject
                |
                |            Dim Selection
                |            Set Selection = CATIA.ActiveEditor.Selection
                |
                |            CATIA.ScriptCommand = CatScriptCommandStart
                |            CATIA.HSOSynchronized = False
                |
                |            Dim HybridShapeFactory, Bodies, Body, OriginElements, Plane,
                |            PlaneReference
                |            Set HybridShapeFactory = Part.HybridShapeFactory
                |            Set Bodies = Part.Bodies
                |            Set Body = Bodies.Item("PartBody")
                |            Set OriginElements = Part.OriginElements
                |            Set Plane = OriginElements.PlaneZX
                |            Set PlaneReference = Part.CreateReferenceFromObject(Plane)
                |
                |            'We ask the user to select several points, drawing a
                |            trap
                |            Dim InputObjectType(0), Status
                |            InputObjectType(0) = "Point"
                |            Status = Selection.SelectMultipleElements(InputObjectType, "Select points", True, CATMultiSelTriggWhenSelPerf, False)
                |
                |            If Status = "Cancel" Then
                |              CATIA.HSOSynchronized = True
                |              CATIA.ScriptCommand = CatScriptCommandStop
                |              Exit Sub
                |            End If
                |
                |            Dim PointIndex, PointReference, HybridShapeSymmetry
                |            For PointIndex = 1 To Selection.Count
                |               Set PointReference = Part.CreateReferenceFromObject(Selection.Item(PointIndex).Value)
                |               Set HybridShapeSymmetry = HybridShapeFactory.AddNewSymmetry(PointReference, PlaneReference)
                |               HybridShapeSymmetry.VolumeResult = False
                |               Body.InsertHybridShape HybridShapeSymmetry
                |               Part.InWorkObject = HybridShapeSymmetry
                |               Part.Update
                |            Next
                |
                |            Selection.Clear
                |            CATIA.HSOSynchronized = True
                |
                |          End Sub
                |
                |     Example:
                |
                |          This second example illustrates the use of the
                |          CATMultiSelTriggWhenUserValidatesSelection value for the
                |
                |          iMultiSelectionMode parameter.
                |
                |          It creates a drawing containing a line and three points, and guides
                |          the user through:
                |
                |             the selection of points
                |             the selection of the symmetry axis
                |
                |          the selected points being moved by symmetry according to the selected
                |          axis. This example will not work for the origin or other specific
                |          points.
                |
                |          Option Explicit
                |
                |          Sub CATMain()
                |
                |            'We create a drawing
                |            Dim oNewService, newEditor
                |            Set oNewService = CATIA.GetSessionService("PLMNewService")
                |            oNewService.PLMCreate("Drawing"), newEditor
                |
                |            'Get the drawing root from the Editor
                |            Dim myDrwRoot
                |            Set myDrwRoot = newEditor.ActiveObject
                |
                |            'Set the drawing standard
                |            myDrwRoot.Standard = catISO
                |
                |            Dim DrawingSheets, DrawingSheet
                |            Set DrawingSheets = myDrwRoot.Sheets
                |            Set DrawingSheet = DrawingSheets.Item("Sheet.1")
                |
                |            DrawingSheet.PaperSize = catPaperA0
                |            DrawingSheet.Scale = 1.000000
                |            DrawingSheet.Orientation = catPaperLandscape
                |
                |            CATIA.ScriptCommand = CatScriptCommandStart
                |            CATIA.HSOSynchronized = False
                |
                |            Dim DrawingViews, DrawingView
                |            Set DrawingViews = DrawingSheet.Views
                |            Set DrawingView = DrawingViews.ActiveView
                |
                |            Dim Factory2D
                |            Set Factory2D = DrawingView.Factory2D
                |
                |            'We create a horizontal line with a zero ordinate
                |            Dim LineLeftExtremity, LineRightExtremity, Line2D
                |            Set LineLeftExtremity = Factory2D.CreatePoint(-100.0, 0.0)
                |            LineLeftExtremity.ReportName = 3
                |            Set LineRightExtremity = Factory2D.CreatePoint(100.0, 0.0)
                |            LineRightExtremity.ReportName = 4
                |            Set Line2D = Factory2D.CreateLine(-100.0, 0.0, 100.0, 0.0)
                |            Line2D.ReportName = 5
                |            Line2D.StartPoint = LineLeftExtremity
                |            Line2D.EndPoint = LineRightExtremity
                |
                |            'We create three points
                |            Dim Point2D1, Point2D2, Point2D3
                |            Set Point2D1 = Factory2D.CreatePoint(-50.0, 50.0)
                |            Point2D1.ReportName = 6
                |            Point2D1.Construction = False
                |            Set Point2D2 = Factory2D.CreatePoint(0.0, 70.0)
                |            Point2D2.ReportName = 7
                |            Point2D1.Construction = False
                |            Set Point2D3 = Factory2D.CreatePoint(50.0, 50.0)
                |            Point2D3.ReportName = 8
                |            Point2D3.Construction = False
                |
                |            CATIA.HSOSynchronized = True
                |            MsgBox "First select several points to be
                |            symmetrized."
                |            CATIA.HSOSynchronized = False
                |
                |            'We ask the user to select several points
                |            Dim Selection
                |            Set Selection = CATIA.ActiveEditor.Selection
                |            Dim InputObjectType(0), Status
                |            InputObjectType(0) = "Point2D"
                |            Status = Selection.SelectMultipleElements(InputObjectType, "Select the set of elements to be symmetrized", True, CATMultiSelTriggWhenUserValidatesSelection, False)
                |
                |            If Status = "Cancel" Then
                |              CATIA.HSOSynchronized = True
                |              CATIA.ScriptCommand = CatScriptCommandStop
                |              Exit Sub
                |            End If
                |
                |            'We add the selected points to SelectedPoint
                |            Dim SelectedPoint(10), SelectedPointCount,
                |            PointIndex
                |            SelectedPointCount = 0
                |            For PointIndex = 0 To Selection.Count - 1
                |              Set SelectedPoint(PointIndex) = Selection.Item(PointIndex + 1).Value
                |              SelectedPointCount = SelectedPointCount + 1
                |            Next
                |
                |            CATIA.HSOSynchronized = True
                |            MsgBox "Then select the line from which the elements will remain
                |            equidistant"
                |            CATIA.HSOSynchronized = False
                |
                |            'We ask the user to select the line
                |            InputObjectType(0) = "Line2D"
                |            Status = Selection.SelectElement(InputObjectType, "Select the line or axis from which the elements will remain equidistant", False)
                |
                |            If Status = "Cancel" Then
                |              CATIA.HSOSynchronized = True
                |              CATIA.ScriptCommand = CatScriptCommandStop
                |              Exit Sub
                |            End If
                |
                |            'We move the selected points by symmetry according to the selected
                |            line
                |            Dim Coordinates(2), CurrentPoint2D
                |            For PointIndex = 0 To SelectedPointCount - 1
                |              Set CurrentPoint2D = SelectedPoint(PointIndex)
                |              CurrentPoint2D.GetCoordinates Coordinates
                |              CurrentPoint2D.SetData Coordinates(0),
                |              -Coordinates(1)
                |            Next
                |
                |            Selection.Clear
                |            CATIA.HSOSynchronized = True
                |            CATIA.ScriptCommand = CatScriptCommandStop
                |            MsgBox "The points have successfully been moved."
                |
                |          End Sub

        :param tuple i_filter_type:
        :param str i_message:
        :param bool i_may_skip_interactive_selection:
        :param CATMultiSelectionMode i_multi_selection_mode:
        :param bool i_tooltip:
        :return: str
        """
        return self.com_object.SelectMultipleElements(
            i_filter_type,
            i_message,
            i_may_skip_interactive_selection,
            i_multi_selection_mode.com_object,
            i_tooltip
        )

        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'select_multiple_elements'
        # vba_code = """
        # Public Function select_multiple_elements(selection)
        #     Dim iFilterType (2)
        #     selection.SelectMultipleElements iFilterType
        #     select_multiple_elements = iFilterType
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Selection(name="{self.name}")'
