"""
Copyright 2016 Deepgram

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from . import Optimizer

################################################################################
class Adam(Optimizer):
	""" Adam optimizer
	"""

	############################################################################
	def __init__(self, learning_rate=None, *args, **kwargs):
		""" Create a new Adam optimizer.

			# Arguments

			learning_rate: float. The learning rate to use.
		"""
		super().__init__(*args, **kwargs)

		self.learning_rate = learning_rate or 0.001

	############################################################################
	def get_optimizer(self, backend):
		""" Returns a backend-specific instantiation of the optimizer.
		"""
		if backend.get_name() == 'keras':
			import keras.optimizers as O		# pylint: disable=import-error
			return O.Adam(lr=self.learning_rate)
		else:
			raise ValueError('Unsupported backend "{}" for optimizer "{}"'
				.format(backend.get_name(), self.get_name()))

#### EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF
