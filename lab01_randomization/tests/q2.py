OK_FORMAT = True

test = {
  'name': 'q2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          # Put all imports and seeds at the very top of the test case itself
          'code': r"""
          >>> import math
          >>> import random
          >>> random.seed(42)
          >>> result_1 = gamblers_expected_time(10,100,0.5,10000)
          >>> math.isclose(result_1, 919.53, abs_tol=1e-2)
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
          >>> result_2 = gamblers_expected_time(20,150,0.5,10000)
          >>> math.isclose(result_2, 2703.72, abs_tol=1e-2)
          True
          """,
          'hidden': True
        }
      ],
      'scored': True,
      'type': 'doctest'
      # Notice: 'setup' and 'teardown' keys are completely deleted
    }
  ]
}
