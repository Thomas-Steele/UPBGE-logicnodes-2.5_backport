from .socket import SOCKET_TYPE_NODETREE, NodeSocketLogic
from .socket import SOCKET_COLOR_GENERIC
from .socket import socket_type
from .socket import update_draw
from ..filter_types import filter_logic_trees
from bpy.types import NodeTree
from bpy.types import NodeSocket
from bpy.props import PointerProperty
import bpy


@socket_type
class NodeSocketLogicTree(NodeSocket, NodeSocketLogic):
    bl_idname = "NLSocketLogicTree"
    bl_label = "Logic Tree"
    value: PointerProperty(
        name='Logic Tree',
        type=NodeTree,
        description=(
            'Select a Logic Tree'
        ),
        poll=filter_logic_trees
        # update=update_tree_code
    )

    color = SOCKET_COLOR_GENERIC
    nl_type = SOCKET_TYPE_NODETREE

    def draw(self, context, layout, node, text):
        icon = 'OUTLINER'
        if self.is_linked or self.is_output:
            layout.label(text=text)
        else:
            col = layout.column(align=False)
            if text and self.is_linked:
                col.label(text=text)
            col.prop_search(
                self,
                "value",
                bpy.data,
                'node_groups',
                icon=icon,
                text=''
            )

    def get_unlinked_value(self):
        if isinstance(self.value, NodeTree):
            return '"{}"'.format(self.value.name)
