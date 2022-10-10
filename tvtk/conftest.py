# Make the tests report some useful information about the environment.


def pytest_report_header(config, start_path, startdir):
    from tvtk.pyface.api import DecoratedScene  # noqa
    from traits.etsconfig.api import ETSConfig
    infos = list()
    infos.append(f'ETSConfig.toolkit={repr(ETSConfig.toolkit)}')
    if ETSConfig.toolkit in ('qt4', 'qt'):
        import pyface
        from pyface.qt import api_name
        infos.append(f'api_name={repr(api_name)}')
    return ', '.join(infos)
