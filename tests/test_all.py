import pytest
from app import dash_app
import sys
sys.path.insert(0, '/home/jacob/python_dash/quantium-start-repo/src')

def test_001_header(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#heading", timeout=10)
    assert dash_duo.find_element("#heading").text == "Pin Morsel Sales 2018 - 2022"

def test_002_visualisation(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element('#graph', timeout=10)

def test_003_radio(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element('#region-radio', timeout=10)

    