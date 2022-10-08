from pytest_pyodide import run_in_pyodide

@run_in_pyodide
def test_1():
  import bob
  assert(bob.ret_1()==1)

@run_in_pyodide
def test_0():
  import bob
  assert(bob.ret_0()==0)
