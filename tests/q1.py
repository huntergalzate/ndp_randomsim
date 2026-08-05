OK_FORMAT = True

test = {
  'name': 'q1',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> square(5)
          25
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> square(2.5)
          6.25
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> square(-4)
          16
          """,
          'hidden': True
        },
        {
          'code': r"""
          >>> square(0)
          0
          """,
          'hidden': True
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
