OK_FORMAT = True

test = {
  'name': 'q3',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          # Put all imports and seeds at the very top of the test case itself
          'code': r"""
          >>> import math
          >>> import random
          >>> random.seed(42)
          >>> result_1 = run_of_success(0.5, 10, 5, 10000)
          >>> math.isclose(result_1, 0.03, abs_tol=1e-2)
          True
          """,
          'hidden': False
        },
        {
          # You must re-import and re-seed in subsequent cases if they rely on it, 
          # as each case is evaluated independently.
          'code': r"""
          >>> import math
          >>> import random
          >>> random.seed(42)
          >>> result_2 = run_of_success(0.7, 10, 5, 10000)
          >>> math.isclose(result_2, 0.83, abs_tol=1e-2)
          True
          """,
          'hidden': True
        }
         {
          #testcase3
          'code': r"""
          >>> import math
          >>> import random
          >>> random.seed(42)
          >>> result_3 = run_of_success(0.7, 6, 1, 10000)
          >>> math.isclose(result_3, 0.11, abs_tol=1e-2)
          True
          """,
          'hidden': False
        },
      ],
      'scored': True,
      'type': 'doctest'
      # Notice: 'setup' and 'teardown' keys are completely deleted
    }
  ]
}
