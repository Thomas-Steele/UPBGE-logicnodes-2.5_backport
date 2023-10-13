from .socket import NodeSocketLogic
from .socket import SOCKET_COLOR_INTEGER
from .socket import SOCKET_TYPE_INT
from .socket import socket_type
from .socket import update_draw
from ...utilities import key_event
from bpy.types import NodeSocket
from bpy.props import StringProperty



@socket_type
class NodeSocketLogicKeyboardKey(NodeSocket, NodeSocketLogic):
    bl_idname = "NLKeyboardKeySocket"
    bl_label = "Key"

    value: StringProperty(update=update_draw)
    color = SOCKET_COLOR_INTEGER

    nl_type = SOCKET_TYPE_INT
    valid_sockets = [SOCKET_TYPE_INT]

    def get_unlinked_value(self):
        return key_event(self.value)

    def draw(self, context, layout, node, text):
        if self.is_linked or self.is_output:
            layout.label(text=text)
        else:
            label = self.value
            if not label:
                label = "Press & Choose"
            layout.box().operator("logic_nodes.key_selector", text=label, emboss=False, icon='MOUSE_LMB')
