{ 'array':

array([('Foo', 12.5, 85.4),
       ('Bar', 14.1, 87.6),
       ('Baz', 14.3, 89.0)],
      dtype=[('Sample Name', 'S3'), ('Radius', float), ('Speed', float)]),

  'kwds': { 'comments': '%',
            'delimiter': ':',
            'dtype': { 'formats': ('S3', float, float),
                       'names': ('Sample Name', 'Radius', 'Speed')},
            'skiprows': 3
            }
  }
