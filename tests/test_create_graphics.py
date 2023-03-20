#pylint: disable=unused-variable
'''
Tests for create_graphics driver
'''
from pygraf.BR_test_func import br_func     # test to import module in pygraf directory
from pygraf.create_graphics import *        # offending import statement


# test to determine if tests working properly
def test_tester():
    br_str = br_func()
    assert br_str == "You called the tester"



# def test_parse_args():
#     '''
#     Test function for command line args.
#     '''
#     cla = ["skewts", "-d", ".../data", "-f", "0", "-o", ".../output", "-s", "2021052315", "--file_tmpl", "hrrr.t00z.wrfnatf00.grib2", "--sites", "../static/conus_raobs.txt", "--max_plev 100"]
#     test_args = parse_args(cla)
#     print(test_args)
#     assert 5 == 5