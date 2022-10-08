from pytest import fixture
from pytest_pyodide import run_in_pyodide,spawn_web_server
import bob
from pathlib import Path

@fixture
def get_wheel_url():
    with spawn_web_server(Path(__file__).parent / "dist") as server:
        server_hostname, server_port, _ = server
        base_url = f"http://{server_hostname}:{server_port}/"
        url = "no_wheel_found_in_dist"
        for wheel in (Path(__file__).parent / "dist") .glob("*.whl"):
          url=base_url+wheel.name
          break
        yield url



def test_0(selenium_standalone,get_wheel_url):
  selenium=selenium_standalone
  selenium.run_js(f"await pyodide.loadPackage('{get_wheel_url}')")
  selenium.run(f"""
    import bob
    assert(bob.ret_0()==0)
    """)

def test_1(selenium_standalone,get_wheel_url):
  selenium=selenium_standalone
  selenium.run_js(f"await pyodide.loadPackage('{get_wheel_url}')")
  r=selenium.run(f"""
    import bob
    bob.ret_1()
    """)
  assert(r==1)
