# stdlib
import re

# 3rd party
from coincidence.regressions import AdvancedFileRegressionFixture
from domdf_folium_tools import set_branca_random_seed
from folium import Map

# this package
from folium_reset_control import ResetViewControl


def test_control(advanced_file_regression: AdvancedFileRegressionFixture):
	set_branca_random_seed("ZOOM")

	m = Map(location=(45.5236, -122.6750), zoom_start=7)
	ResetViewControl(centre=(45.5236, -122.6750), zoom=7).add_to(m)

	root = m.get_root()
	html = root.render()
	html = re.sub(
			"folium-reset-control@v.*/reset_control",
			"folium-reset-control@latest/reset_control",
			html,
			)
	advanced_file_regression.check(html, extension=".html")


def test_pos_only(advanced_file_regression: AdvancedFileRegressionFixture):
	set_branca_random_seed("ZOOM")

	m = Map(location=(45.5236, -122.6750), zoom_start=7)
	ResetViewControl(centre=(45.5236, -122.6750)).add_to(m)

	root = m.get_root()
	html = root.render()
	html = re.sub(
			"folium-reset-control@v.*/reset_control",
			"folium-reset-control@latest/reset_control",
			html,
			)
	advanced_file_regression.check(html, extension=".html")


def test_zoom_only(advanced_file_regression: AdvancedFileRegressionFixture):
	set_branca_random_seed("ZOOM")

	m = Map(location=(45.5236, -122.6750), zoom_start=7)
	ResetViewControl(zoom=7).add_to(m)

	root = m.get_root()
	html = root.render()
	html = re.sub(
			"folium-reset-control@v.*/reset_control",
			"folium-reset-control@latest/reset_control",
			html,
			)
	advanced_file_regression.check(html, extension=".html")


def test_bounds(advanced_file_regression: AdvancedFileRegressionFixture):
	set_branca_random_seed("ZOOM")

	m = Map(location=(45.5236, -122.6750), zoom_start=7)
	ResetViewControl(bounds=((49.5600, -6.7200), (56.0000, 1.9800))).add_to(m)

	root = m.get_root()
	html = root.render()
	html = re.sub(
			"folium-reset-control@v.*/reset_control",
			"folium-reset-control@latest/reset_control",
			html,
			)
	advanced_file_regression.check(html, extension=".html")


def test_from_map(advanced_file_regression: AdvancedFileRegressionFixture):
	set_branca_random_seed("ZOOM")

	m = Map(location=(45.5236, -122.6750), zoom_start=7)
	ResetViewControl.from_map(m).add_to(m)

	root = m.get_root()
	html = root.render()
	html = re.sub(
			"folium-reset-control@v.*/reset_control",
			"folium-reset-control@latest/reset_control",
			html,
			)
	advanced_file_regression.check(html, extension=".html")
