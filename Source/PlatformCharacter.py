###############################################################################
#               Platformer Game | Template v 1.0 | UPBGE 0.2.4+               #
###############################################################################
#                      Created by: Guilherme Teres Nunes                      #
#                       Access: youtube.com/UnidayStudio                      #
#                               github.com/UnidayStudio                       #
###############################################################################
import bge
import mathutils
from collections import OrderedDict

class PlatformCharacter(bge.types.KX_PythonComponent):

	args = OrderedDict([
		("Walk speed", 0.1),
	])

	def start(self, args):
		self.character = bge.constraints.getCharacter(self.object)

		self.walkSpeed = args["Walk speed"]

	def update(self):
		keyboard = bge.logic.keyboard.inputs
		keyTAP = bge.logic.KX_INPUT_JUST_ACTIVATED

		movement = 0
		if keyboard[bge.events.DKEY].active:
			movement = 1
		elif keyboard[bge.events.AKEY].active:
			movement = -1

		movement *= self.walkSpeed

		movVec = mathutils.Vector([0, movement, 0])

		self.character.walkDirection = self.object.worldOrientation * movVec

		if keyTAP in keyboard[bge.events.SPACEKEY].queue:
			self.character.jump()

