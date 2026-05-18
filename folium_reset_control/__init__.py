#!/usr/bin/env python3
#
#  __init__.py
"""
Folium plugin that adds a control for resetting the map view.
"""
#
#  Copyright © 2026 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# 3rd party
import folium.elements
from folium.template import Template
from folium.utilities import remove_empty

__all__ = ["ResetViewControl"]

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2026 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "0.1.0b2"
__email__: str = "dominic@davis-foster.co.uk"


class ResetViewControl(folium.elements.JSCSSMixin, folium.elements.MacroElement):
	r"""
	Control for swapping between maps.

	:param centre: Latitude and longiture of the map centre to reset to.
	:param zoom: Zoom level to reset to.
	:param icon: The control's icon.
	:param bounds: The bounding box (top left and bottom right corners) to display. Overrides centre and zoom options.
	:param \*\*kwargs: Additional options for the javascript ``ResetViewControl`` class.
	"""

	def __init__(
			self,
			centre: tuple[float, float] | None = None,
			zoom: int | None = None,
			icon: str = "fa-solid fa-arrow-rotate-left",
			bounds: tuple[tuple[float, float], tuple[float, float]] | None = None,
			**kwargs,
			):
		super().__init__()
		self._name = "ResetViewControl"
		self.options = remove_empty(centre=centre, zoom=zoom, icon=icon, bounds=bounds, **kwargs)

	default_js = [
			(
					"reset_control_js",
					f"https://cdn.jsdelivr.net/gh/domdfcoding/folium-reset-control@v{__version__}/folium_reset_control/reset_control.min.js",
					),
			]

	default_css = [
			(
					"fontawesome_css",
					"https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.7.2/css/all.min.css",
					),
			(
					"reset_control_css",
					f"https://cdn.jsdelivr.net/gh/domdfcoding/folium-reset-control@v{__version__}/folium_reset_control/reset_control.min.css",
					),
			]

	_template = Template(
			"""
			{% macro header(this, kwargs) %}
				<style>
					.leaflet-control-reset-view {
						a {
							font-size: 1.4em;
							.leaflet-reset-view-icon {
								color: black;
							}
						}
					}
				</style>
			{% endmacro %}

			{% macro script(this, kwargs) %}
				var {{this.get_name()}} = new ResetViewControl(
					{{this.options | tojson}}
				).addTo({{ this._parent.get_name() }});
			{% endmacro %}
			""",
			)
