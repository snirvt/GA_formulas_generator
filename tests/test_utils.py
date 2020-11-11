import numpy as np
import pytest
import mock
import utils


@pytest.mark.parametrize("test_input, expected", [(0, 1),(1,0)])
def test_swap_binary_value(test_input, expected):
    result = utils.swap_binary_value(test_input)
    assert(result == expected)


@pytest.mark.parametrize("test_input, expected", [(np.array([1,2,3,4,5]), np.array([-1.414213562373095,-0.7071067811865475,0.,0.7071067811865475,1.414213562373095]))])
def test_scale(test_input, expected):
    result = utils.scale(test_input)
    assert(np.all(result == expected))


@pytest.mark.parametrize("test_input, expected", [(0, '+'),(1,'-'),(2,'*'),(3,'/'),(4,'^')])
def test_get_action(test_input, expected):
    result = utils.get_action(test_input)
    assert(result == expected)


@pytest.mark.parametrize("test_input, expected", [(0, ''),(1,'exp'),(2,'cos'),(3,'sin'),(4,'absln')])
def test_get_activation(test_input, expected):
    result = utils.get_activation(test_input)
    assert(result == expected)


