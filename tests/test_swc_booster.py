import pytest
from swc_booster import compile_with_swc_booster, CompilationResult

def test_compile_with_swc_booster_success(tmp_path):
    input_file = tmp_path / 'input.txt'
    output_file = tmp_path / 'output.txt'
    with open(input_file, 'w') as f:
        f.write('Hello World!')
    result = compile_with_swc_booster(str(input_file), str(output_file))
    assert result.success
    assert result.time_taken > 0
    with open(output_file, 'r') as f:
        assert f.read() == 'Hello World!'

def test_compile_with_swc_booster_failure(tmp_path):
    input_file = tmp_path / 'input.txt'
    output_file = tmp_path / 'output.txt'
    with open(input_file, 'w') as f:
        f.write('Hello World!')
    # Simulate failure by passing invalid output file
    result = compile_with_swc_booster(str(input_file), '/invalid/output.txt')
    assert not result.success
    assert result.time_taken == 0

def test_compile_with_swc_booster_invalid_input(tmp_path):
    input_file = tmp_path / 'input.txt'
    output_file = tmp_path / 'output.txt'
    # Simulate invalid input file
    result = compile_with_swc_booster('/invalid/input.txt', str(output_file))
    assert not result.success
    assert result.time_taken == 0
