"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mmr_automation_interfaces.body import Body
from pycatia3dx.mmr_automation_interfaces.planar_face import PlanarFace
from pycatia3dx.mode.reference import Reference
from pycatia3dx.product_structure_client.vpm_occurrence import VPMOccurrence
from pycatia3dx.product_structure_client.vpm_rep_instance import VPMRepInstance
from pycatia3dx.system.any_object import AnyObject


class SelectedElement(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SelectedElement
                | 
                | Abstract object which allows manipulating an element selected during a
                | selection operation.
                | 
                | See also:
                |     Selection.SelectElement
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def leaf_product(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property LeafProduct() As AnyObject (Read Only)
                |     Returns the leaf product instance which aggregates this selected element in
                |     the specification tree.
                |     Role: The AnyObject returned is a VPMRepInstance , VPMInstance or
                |     VPMReference if a product appears in the specification tree, in the path
                |     corresponding to the current selection, or a fake AnyObject whose
                |     AnyObject.Name property is equal to "InvalidLeafProduct"
                |     otherwise.
                |     Used in combination with AnyObject.Parent property (which enables
                |     navigation in the object structure), the script can browse the path of the
                |     selected element.
                | 
                |     Example:
                | 
                |          This example supposes that a product structure similar to the
                |          following one be opened:
                |          
                | 
                |           +------------+ 
                |           !Product55228!                                                  <-
                |           VPMReference
                |           +------------+
                |               !
                |               +- Representation55228 (instance hidden)
                |               !
                |               +- Product55227 (Product55227.1)                            <-
                |               VPMReference (VPMInstance)
                |                     !
                |                     +- Product55226 (Product55226.1)                      <-
                |                     VPMReference (VPMInstance)
                |                           !
                |                           +- Representation55226 (instance hidden)        <-
                |                           Part/VPMRepReference
                |                           (VPMRepInstance)
                |                                     !
                |                                     +- PartBody
                |                                           !
                |                                           +- Pad.1                        <-
                |                                           Select the Pad
                |          
                | 
                |          
                | 
                |          The leaf product instance in this case is Representation55226.1
                |          (adheres to CATIAVPMRepInstance).
                | 
                |          
                | 
                |          The script asks the user to select a feature. It then browses the
                |          specification tree with a bottom-up approach starting from the selected
                |          element, and displays message boxes containing the names and types of the
                |          automation objects.
                |          When the bottom-up approach cannot continue, a top-down approach is
                |          started from the root product, to display the names, types, and abcissa of the
                |          encountered products.
                |          
                | 
                |          Option Explicit
                | 
                |          Sub CATMain()
                |          
                |            Dim Selection
                |            Set Selection = CATIA.ActiveEditor.Selection
                |          
                |            'We ask the user to select a feature
                |            Dim Status, InputObjectType(0)
                |            InputObjectType(0) = "AnyObject" 
                |            Status = Selection.SelectElement(InputObjectType, "Select a feature", False)
                |            If (Status = "Cancel") Then Exit Sub
                |          
                |            Dim Feature, LeafProduct
                |            Set Feature = Selection.Item(1).Value
                |            Set LeafProduct = Selection.Item(1).LeafProduct
                |            MsgBox "Selected feature name = " & Feature.Name & "; type = " & TypeName(Feature)
                |            MsgBox "Corresponding LeafProduct name = " & LeafProduct.Name & "; type = " & TypeName(LeafProduct)
                |          
                |            If (LeafProduct.Name="InvalidLeafProduct") Then Exit
                |            Sub
                |          
                |            Dim BottomUp, WholeTreeProcessed, Node, NextNode
                |            BottomUp = True
                |            WholeTreeProcessed = False
                |            Set Node = Feature
                |          
                |            MsgBox "**** Starting bottom-up browsing ****"
                |          
                |            Dim Position, AxisComponentsArray(11)
                |            
                |            On Error Resume Next
                |            Do While (Not WholeTreeProcessed)
                |              MsgBox "Current node name = " & Node.Name & "; type = " & TypeName(Node)
                |              
                |              'We determine the next automation tree Node or
                |              product
                |              If (BottomUp) Then
                |                Err.Clear
                |                Set NextNode = Node.Parent      'this method will fail for representations (no parent defined because of multirepresentation capability)
                |                If (Err.Number <> 0) Then
                |                  On Error GoTo 0              'deactivate error
                |                  handler
                | 
                |                  'Bottom-up browsing cannot go upper than the representation.
                |                  Then start a top-down approach starting from the root
                |                  product.
                |                  'VPM editor must be active for top-down
                |                  browsing
                |                  If TypeName(CATIA.ActiveEditor.ActiveObject) <> "VPMReference"
                |                  Then Exit Sub
                | 
                |                  Dim oContext
                |                  Set oContext = CATIA.ActiveEditor.GetService("PLMProductContext")
                |                  Set NextNode = oContext.RootOccurrence
                |                  BottomUp = False
                |                  MsgBox "**** Bottom-up browsing ended. Starting top-down
                |                  browsing. ****"
                |                End If
                |              Else
                |                If TypeName(Node) = "VPMOccurrence" Then
                |                  'Our current node is a VPMOccurrence. We display its abscissa
                |                  in the tree
                |                  Set Position = Node.Position
                |                  Call Position.GetComponents(AxisComponentsArray)    'Format:
                |                  (x0,x1,x2) (y3,y4,y5) (z6,z7,z8) (o9,o10,o11)
                |                  MsgBox "Position of the current VPMOccurrence = " & AxisComponentsArray(9)
                |                End If
                |                
                |                'Can we find our leaf product among the VPMRepInstances
                |                aggregated under the current VPMReference?
                |                'If so, break the loop
                |                Dim ReferenceNode
                |                If TypeName(Node) = "VPMRootOccurrence" Then
                |                  Set ReferenceNode = Node.ReferenceRootOccurrenceOf
                |                Else
                |                  Set ReferenceNode = Node.InstanceOccurrenceOf.ReferenceInstanceOf
                |                End If
                |                If (ReferenceNode.RepInstances.Count > 0) Then   
                |                
                |                  Dim oRepInstance
                |                  For Each oRepInstance In
                |                  ReferenceNode.RepInstances
                |                    If (oRepInstance.Name = LeafProduct.Name) Then
                |                      WholeTreeProcessed = True
                |                      MsgBox "**** Found the leaf product under " & Node.Name &
                |                      ". End of loop. ****"
                |                      Exit For
                |                    End If
                |                  Next
                |                End If
                |                
                |                'Otherwise, go down a VPMOccurrence level (in this example, we
                |                do not support multiple occurrences, but a recursive approach would make it
                |                easily)
                |                If (Not WholeTreeProcessed) Then
                |                  Set NextNode = Node.Occurrences.Item(1)
                |                End If
                |              End If
                |              
                |              Set Node = NextNode
                |            Loop
                |          
                |          End Sub
                |          
                | 
                | 
                |          The following message boxes should be displayed:
                |          
                | 
                |              Selected feature name = Pad.1; type = Pad
                |              Corresponding LeafProduct name = Representation55226.1; type = VPMRepInstance
                |              **** Starting bottom-up browsing ****
                |              Current node name = Pad.1; type = Pad
                |              Current node name = Shapes; type = Shapes
                |              Current node name = PartBody; type = Body
                |              Current node name = Bodies; type = Bodies
                |              Current node name = Representation55226 --- IN_WORK; type = Part
                |              Current node name = ---Representation55226; type = VPMRepReference
                |              **** Bottom-up browsing ended. Starting top-down browsing.
                |              ****
                |              Current node name = ---Product55228; type = VPMRootOccurrence
                |              Current node name = ---Product55227.2; type = VPMOccurrence
                |              Position of the current VPMOccurrence = 0
                |              Current node name = ---Product55226.1; type = VPMOccurrence
                |              Position of the current VPMOccurrence = 0
                |              **** Found the leaf product under Product55226.1. End of loop.
                |              ****

        :return: AnyObject
        """

        return AnyObject(self.com_object.LeafProduct)

    @property
    def reference(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Reference() As Reference (Read Only)
                |     Returns a Reference version of the Value property.
                |     Role: Returns a Reference version of Value .

        :return: Reference
        """

        return Reference(self.com_object.Reference)

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Type() As CATBSTR (Read Only)
                |     Returns the filter string that the selected element matched during the
                |     selection operation.
                |     Note: This property returns a string describing the first of the filters
                |     passed as the iFilterType parameter of interactive selection operations that
                |     the selected element fulfilled. This string constant may be an automation
                |     object name corresponding to the iFilterType parameter, or a CATSelectionFilter
                |     value name.
                | 
                |     Example:
                |
                |          Set Selection = CATIA.ActiveEditor.Selection
                |          ' We ask the user to select a Prism or a Hole
                |          ReDim InputObjectType(1)
                |          InputObjectType(0) = "Prism"
                |          InputObjectType(1) = "Hole"
                |          Status = Selection.SelectElement(InputObjectType, "Select a prism or a hole", True)
                |          If (Status = "Cancel") Then Exit Sub
                |          AutomationType = Selection.Item(1).Type
                | 
                | 
                |          If the user selects a Pad, the script AutomationType variable will
                |          contain "Prism"
                |          and not "Pad", as "Prism" was the first filter that the Pad matched
                |          (Pads' fathers are Prisms).
                |          
                | 
                |         Therefore, you may also want to use VB's native TypeName function
                |         instead of this property to get the actual type of the selected element: in
                |         this case, MsgBox TypeName(Selection.Item(1).Value) will display
                |         Pad.

        :return: str
        """

        return self.com_object.Type

    @property
    def value(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Value() As CATBaseDispatch (Read Only)
                |     Returns the actual selected automation object.

        :return: AnyObject
        """
        _object = AnyObject(self.com_object.Value)
        type_string = self.application.vba_type_name(_object)

        if type_string == "PlanarFace":
            return PlanarFace(self.com_object.Value)
        if type_string == "VPMRepInstance":
            return VPMRepInstance(self.com_object.Value)
        if type_string == "Body":
            return Body(self.com_object.Value)
        if type_string == "VPMOccurrence":
            return VPMOccurrence(self.com_object.Value)
        if type_string == "VPMRootOccurrence":
            return VPMOccurrence(self.com_object.Value)

        # todo: add more types. there's going to be a lot I suspect
        if type_string not in _object.__repr__():
            self.logger.warning(
                f'Please add type string "{type_string}" to checks so correct type is returned.'
            )

        return _object

    def get_coordinates(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub GetCoordinates(CATSafeArrayVariant ioPoint)
                |     Returns the coordinates of the pick point.
                | 
                |     Parameters:
                | 
                |         oPoint
                |             The coordinates of the pick point, i.e. the hit between the
                |             geometric object and the cursor.
                |             The length of this parameter can be 2 or 3.
                | 
                |     Example:
                | 
                |          This example retrieves the coordinates of the pick point in
                |          the
                |          array myArray:
                | 
                |          Dim oSelElem As SelectedElement
                |          Set oSelElem = CATIA.ActiveEditor.Selection.Item(1)
                |          ReDim myArray(2)
                |          oSelElem.GetCoordinates myArray

        :return: tuple
        """
        return self.com_object.GetCoordinates()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_coordinates'
        # vba_code = """
        # Public Function get_coordinates(selected_element)
        #     Dim ioPoint (2)
        #     selected_element.GetCoordinates ioPoint
        #     get_coordinates = ioPoint
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SelectedElement(name="{self.name}")'
