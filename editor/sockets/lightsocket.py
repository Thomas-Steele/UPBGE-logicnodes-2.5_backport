from .socket import SOCKET_TYPE_OBJECT, NodeSocketLogic
from .socket import SOCKET_COLOR_OBJECT
from .socket import socket_type
from .socket import update_draw
from ..filter_types import filter_lights
from bpy.types import NodeSocket
#from bpy.types import Light ### Logic Nodes 2.8+ Implementation
from bpy.types import Lamp   ### Logic Nodes 2.79 Implementation
from bpy.props import PointerProperty
from bpy.props import BoolProperty
import bpy


### Logic Nodes 2.79 Implementation ; All names 'Lamp' are 'Light' in Logic Nodes 2.8+

@socket_type
class NodeSocketLogicLight(NodeSocket, NodeSocketLogic):
    bl_idname = "NLLightObjectSocket"
    bl_label = "Lamp"
    default_value: PointerProperty(
        name='Lamp',
        type=Lamp,
        poll=filter_lights
    )
    # XXX: Remove value property
    value: PointerProperty(
        name='Lamp',
        type=Lamp,
        poll=filter_lights
    )
    use_owner: BoolProperty(
        name='Use Owner',
        # update=update_tree_code,
        description='Use the owner of this tree'
    )

    nl_color = SOCKET_COLOR_OBJECT
    nl_type = SOCKET_TYPE_OBJECT

    def draw(self, context, layout, node, text):
        if self.is_output:
            layout.label(text=self.name)
        elif self.linked_valid:
            layout.label(text=self.name)
        else:
            if not self.use_owner:
                col = layout.column(align=False)
                row = col.row()
                if self.name:
                    row.label(text=self.name)
                row.prop(self, 'use_owner', icon='USER', text='')
                col.prop_search(
                    self,
                    'default_value',
                    bpy.context.scene,
                    'objects',
                    icon='NONE',
                    text=''
                )
            else:
                row = layout.row()
                row.label(text=self.name)
                row.prop(self, 'use_owner', icon='USER', text='')

    def get_unlinked_value(self):
        if self.use_owner:
            return 'game_object'
        if isinstance(self.default_value, Lamp):
            return f'scene.objects["{self.default_value.name}"]'
