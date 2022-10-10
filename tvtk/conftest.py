import importlib


def pytest_report_header(config, start_path, startdir):
    """Make pytest report some useful information about the environment."""
    from traits.etsconfig.api import ETSConfig
    try:
        from tvtk.pyface.api import DecoratedScene  # noqa
    except ImportError:  # Cannot import any of ...
        pass
    infos = list()
    for module in ('pyface', 'traitsui', 'traits'):
        mod = importlib.import_module(module)
        infos.append(f'{module}-{mod.__version__}')
    infos.append(f'ETSConfig.toolkit={repr(ETSConfig.toolkit)}')
    if ETSConfig.toolkit in ('qt4', 'qt'):
        try:
            from pyface.qt import api_name
        except ImportError:
            infos.append('api_name=ImportError')
        else:
            infos.append(f'api_name={repr(api_name)}')
    return 'system:  ' + ', '.join(infos)
