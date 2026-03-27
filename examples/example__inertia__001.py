"""
    Example - Inertia - 001

    Catia must be running with a Part open that contains a solid object within
    the MainBody (PartBody).

    This example will only measure the inertia for the MainBody.

    Additional PartBodies will be ignored.
"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia3dx'))
##########################################################

from pycatia3dx import catia3dx
from pycatia3dx.mmr_automation_interfaces.part import Part
from pycatia3dx.inertia.inertia import Inertia
from pycatia3dx.types.service import InertiaService

__author__ = '[ptm] by plm-forum.ru | ported to pycatia3dx by HdCadUser'

# com3dx=False is required if com3dx.py cannot be found in your system.
application = catia3dx(com3dx=False)
# if the active document is a CATPart this will return a PartDocument

part = Part(application.active_editor.active_object.com_object)
part.update()

# get the Bodies() collection
bodies = part.bodies

body = part.main_body

# or get the body by name
# body_by_name = bodies.get_item_by_name('AnotherPartBody')

# initialise the inertia service
inertia_service: InertiaService = InertiaService(
    application.active_editor.get_service("InertiaService").com_object
)

# create a reference to measure.
reference = part.create_reference_from_object(part)
inertia: Inertia = inertia_service.get_inertia_element(reference)

print(f'Density={part.density}\n\n')
# Density setter has been removed from 3DX; Only getter is available

print(f'Mass={inertia.get_mass()}\n\n')

inertia_matrix = inertia.get_inertia_matrix()
print('--------------\n'
      'Interia Matrix\n'
      '--------------\n'
      f'Ixx={inertia_matrix[0]}\n'
      f'Ixy={inertia_matrix[1]}\n'
      f'Ixz={inertia_matrix[2]}\n'
      f'Iyx={inertia_matrix[3]}\n'
      f'Iyy={inertia_matrix[4]}\n'
      f'Iyz={inertia_matrix[5]}\n'
      f'Izx={inertia_matrix[6]}\n'
      f'Izy={inertia_matrix[7]}\n'
      f'Izz={inertia_matrix[8]}\n')

principal_axis = inertia.get_principal_axes()
print('--------------\n'
      'Principal Axis\n'
      '--------------\n'
      f'A1x={principal_axis[0]}\n'
      f'A2x={principal_axis[1]}\n'
      f'A3x={principal_axis[2]}\n'
      f'A1y={principal_axis[3]}\n'
      f'A2y={principal_axis[4]}\n'
      f'A3y={principal_axis[5]}\n'
      f'A1z={principal_axis[6]}\n'
      f'A2z={principal_axis[7]}\n'
      f'A3z={principal_axis[8]}\n')

principal_moments = inertia.get_principal_moments()
print('-----------------\n'
      'Principal Moments\n'
      '-----------------\n'
      f'M1={principal_moments[0]}\n'
      f'M2={principal_moments[1]}\n'
      f'M3={principal_moments[2]}\n')

cog = inertia.get_cog_position()
print('-----------------\n'
      'Center Of Gravity\n'
      '-----------------\n'
      f'X={cog[0]}\n'
      f'Y={cog[1]}\n'
      f'Z={cog[2]}')
