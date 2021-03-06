

import numpy as np
import pytest
import mock

import unittest   # The test framework'
from unittest.mock import MagicMock

###################################
from evaluator import Evaluator
from tests.test_common import create_data, create_simple_individual, create_simple_population
###################################

 
@pytest.fixture(name="eval_handler")
def evaluator_fixture(mocker):
    #  Bring up
    X,X_test, y ,y_test, column_names = create_data()
    yield Evaluator(X=X,X_test=X_test, y=y,y_test = y_test, column_names=column_names)
    #  Tear Down


@pytest.mark.parametrize('input_num', [-1, 0, 1, 10])
def test_get_string_data_column(input_num, eval_handler):
    output = eval_handler.get_string_data_column(input_num)
    assert(output == 'X[:,{}]'.format(input_num))


@pytest.mark.parametrize('input_str', ['(_1_+_3_*_5_**(_2_-(_4_)/_6_))'])
def test_build_math_evaluation(input_str, eval_handler):
    output = eval_handler.build_math_evaluation(input_str)
    assert(output == '(X[:,1]+X[:,3]*X[:,5]**(X[:,2]-(X[:,4])/X[:,6]))')


def test_evaluate_individual(eval_handler):
    individual = create_simple_individual()
    output_train_mse, output_test_mse, output_train_r2, output_test_r2 = eval_handler.evaluate_individual(individual)
    assert(round(output_train_mse) == 0)
    assert(round(output_test_mse) == 0)
    assert(output_train_r2 == 1)
    assert(output_test_r2 == 1)




def test_evaluate_population(eval_handler):
    population = create_simple_population()
    output_train_mse, output_test_mse, output_train_r2, output_test_r2 = eval_handler.evaluate_population(population)

    assert(np.all(output_train_mse < np.array([0.001, 0.001, 0.001])))
    assert(np.all(output_test_mse < np.array([0.001, 0.001, 0.001])))
    assert(np.all(output_train_r2 == np.array([1,1,1])))
    assert(np.all(output_test_r2 == np.array([1,1,1])))

def test_evaluate_population_paralal(eval_handler):
    population = create_simple_population()
    output_train_mse, output_test_mse, output_train_r2, output_test_r2 = eval_handler.evaluate_population_paralal(population)
    print(output_train_mse)
    print(output_test_mse)
    print(output_train_r2)
    print(output_test_r2)

    assert(np.all(output_train_mse < np.array([0.001,0.001,0.001])))
    assert(np.all(output_test_mse < np.array([0.001,0.001,0.001])))
    assert(np.all(output_train_r2 == np.array([1,1,1])))
    assert(np.all(output_test_r2 == np.array([1,1,1])))