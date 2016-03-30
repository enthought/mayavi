def has_attributes(dataset):
    """Returns `True` when the given TVTK `dataset` has any attribute
    arrays in point and cell data and `False` otherwise.
    """
    pd = dataset.point_data
    if pd is not None and pd.number_of_arrays > 0:
        return True
    cd = dataset.cell_data
    if cd is not None and cd.number_of_arrays > 0:
        return True
    return False
