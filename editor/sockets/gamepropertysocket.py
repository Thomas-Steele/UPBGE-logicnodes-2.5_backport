from .socket import SOCKET_TYPE_STRING, NodeSocketLogic
from .objectsocket import NodeSocketLogicObject
from .socket import SOCKET_COLOR_STRING
from .socket import socket_type
from .socket import update_draw
from ...utilities import LOGIC_NODE_IDENTIFIER
from ...utilities import make_valid_name
from bpy.types import NodeSocket
from bpy.types import Object
from bpy.props import StringProperty
from bpy.props import BoolProperty
from bpy.props import IntProperty
import bpy


@socket_type
class NodeSocketLogicGameProperty(NodeSocket, NodeSocketLogic):
    bl_idname = "NLGamePropertySocket"
    bl_label = "Property"

    value: StringProperty(
        update=update_draw
    )
    ref_index: IntProperty(default=0)
    use_custom: BoolProperty(
        name='Free Edit'
    )

    color = SOCKET_COLOR_STRING
    nl_type = SOCKET_TYPE_STRING

    def draw(self, context, layout, node, text):
        mode = getattr(self.node, 'mode', '0')
        if self.is_output:
            layout.label(text=self.name)
        elif self.is_linked:
            layout.label(text=self.name)
        else:
            col = layout.column(align=False)
            tree = getattr(context.space_data, 'edit_tree', None)
            if not tree:
                return
            data_block = None
            data_block_socket = self.node.inputs[self.ref_index]
            if not getattr(data_block_socket, 'use_owner', False):
                data_block = data_block_socket.value
            elif isinstance(data_block_socket, NodeSocketLogicObject):
                prop_name = f'{LOGIC_NODE_IDENTIFIER}{make_valid_name(tree.name)}'
                for obj in bpy.data.objects:
                    if prop_name in obj.game.properties:
                        data_block = obj
                        break
            if self.name:
                row = col.row()
                row.label(text=self.name)
                if not data_block_socket.is_linked and data_block and not mode:
                    row.prop(self, 'use_custom', text='', icon='GREASEPENCIL')
            if data_block or data_block_socket.is_linked:
                if not data_block_socket.is_linked and not self.use_custom and mode == '0':

                    if isinstance(data_block, Object):
                        data_block = data_block.game
                    col.prop_search(
                        self,
                        'value',
                        data_block,
                        'properties',
                        icon='NONE',
                        text=''
                    )
                else:
                    col.prop(self, 'value', text='')
            else:
                col.prop(self, 'value', text='')

    def get_unlinked_value(self):
        return '"{}"'.format(self.value)