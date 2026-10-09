# see Application.vba_type_name for usage.
type_name_function_name = 'type_name'
type_name_code = f'''
Public Function {type_name_function_name}(com_object)        
    tn = TypeName(com_object)
    type_name = tn        
End Function
'''

# todo: change this so that Application.system_service.evaluate doesn't need to
#  be invoked when used as in pycatia (see HybridShapeFactory.add_new_sphere
_vba_nothing = '''
Function N()        
    set N = Nothing        
End Function
'''


class VBANothing(str):

    def __init__(self, vba_code):
        self.vba_code = vba_code

    def __str__(self):
        return self.vba_code


vba_nothing = VBANothing(_vba_nothing)
