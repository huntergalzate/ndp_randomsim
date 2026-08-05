OK_FORMAT = True

test = {
  'name': 'q1',
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
          >>> result_1 = sim_diff_integers(5,4,10000)
          >>> math.isclose(result_1, 0.23, abs_tol=1e-2)
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
          >>> # advance the generator if needed, or test a different condition
          >>> result_2 = sim_diff_integers(20,4,10000)
          >>> math.isclose(result_2, 0.98, abs_tol=1e-2)
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
