from PyQt5.QtCore import *
from conf import *
from conf import register_node, OP_NODE_OUTPUT
from node_base import *
from nodeeditor.utils import dumpException


class GateOutputContent(QDMNodeContentWidget):
    def initUI(self):
        self.lbl = QLabel("0", self)
        self.lbl.setAlignment(Qt.AlignHCenter)
        self.lbl.setContentsMargins(75,10,0,0)
        self.lbl.setFont(QFont("Arial", 15))
        self.lbl.setObjectName(self.node.content_label_objname)


@register_node(OP_NODE_OUTPUT)
class GateNode_Output(GateNode):
    op_code = OP_NODE_OUTPUT
    op_title = "Output"
    content_label_objname = "node_output"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[])

    def initInnerClasses(self):
        self.content = GateOutputContent(self)
        self.grNode = GateGraphicsNode(self)

    def evalImplementation(self):
        input_node = self.getInput(0)
        if not input_node:
            self.grNode.setToolTip("Input is not connected")
            self.markInvalid()
            return

        val = input_node.eval()

        if val is None:
            self.grNode.setToolTip("Input is NaN")
            self.markInvalid()
            return

        self.content.lbl.setText("%d" % val)
        self.markInvalid(False)
        self.markDirty(False)
        self.grNode.setToolTip("")

        return val
