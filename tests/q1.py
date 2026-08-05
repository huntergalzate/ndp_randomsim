OK_FORMAT = True

test = {
  'name': 'q1',
  'points': 2,
  'suites': [
    {
      # Import both required libraries and set the seed before testing
      'setup': r"""
      >>> import random
      >>> import math
      >>> random.seed(42)
      """,
      'cases': [
        {
          'code': r"""
          >>> result_1 = sim_diff_integers(5,4,10000)
          >>> # Checks if result_1 is within 0.01 of 1.82
          >>> math.isclose(result_1, 0.23, abs_tol=1e-2)
          True
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> result_2 = sim_diff_integers(20,4,10000)
          >>> # Checks if the next random generation is within 0.01 of 0.98
          >>> math.isclose(result_2, 0.98, abs_tol=1e-2)
          True
          """,
          'hidden': True
        }
      ],
      'scored': True,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
