# Make the tests report some useful information about the environment.


def pytest_report_header(config, start_path, startdir):
    from tvtk.pyface.api import DecoratedScene  # noqa
    from traits.etsconfig.api import ETSConfig
    import pyface
    infos = list()
    infos.append(f'ETSConfig.toolkit={repr(ETSConfig.toolkit)}')
    infos.append(f'pyface={repr(pyface.__version__)}')
    if ETSConfig.toolkit in ('qt4', 'qt'):
        from pyface.qt import api_name
        infos.append(f'api_name={repr(api_name)}')
    return ', '.join(infos)
