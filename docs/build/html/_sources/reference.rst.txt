Reference
=========

.. _excel_utilities.getExcelSheet:

.. py:function:: excel_utilities.getExcelSheet(inputfile)
    
    Retrieves data from an excel file

    :param inputfile: The excel file you want to retriece data from.
    :return: sheet
    :rtype: <class 'openpyxl.worksheet.worksheet.Worksheet'>

.. note::

    The getExcelSheet function is used to retrieve data form an excel file. In order to do so, the 
    `openpyxl library <https://openpyxl.readthedocs.io>`_ is used!


.. _excel_utilities.getSheetNames:

excel_utilities.getSheetNames
-----------------------------

To retrieve a tuple containting the column names (default, use b_rows=True to retrieve the row names instead) 
of the specified excel spreadsheet you can use the excel_utilities.getSheetNames function:

.. py:function::  excel_utilities.getSheetNames(sheet, b_rows=False)

    Return a tuple of column names as strings

    :param sheet: Required excel spreadsheet.
    :type sheet: <class 'openpyxl.worksheet.worksheet.Worksheet'>
    :raise excel_utilities.InvalidSheetError: If the sheet argument is an invalid type.
    :param b_rows: Optional, set to True in order to return row names instead.
    :type b_rows: Boolean
    :return: The column names tuple.
    :rtype: tuple(str)

| The sheet parameter should be retrieved using the :ref:`excel_utilities.getExcelSheet <excel_utilities.getExcelSheet>`.
| Otherwise, :py:func:`excel_utilities.getSheetNames` will raise an exception.

.. py:exception:: excel_utilities.InvalidSheetError
    
    Raised if the sheet argument is an invalid type. 
    *openpyxl does not support  file format, please check you can open it with Excel first.
    Supported formats are: .xlsx,.xlsm,.xltx,.xltm*


.. _excel_utilities.getDataList:

excel_utilities.getDataList
---------------------------

To etrieve a list of lists. Each sublist containts the values, provided by the specified excel spreadsheet, 
of each column (default, use b_rows=True to retrieve values of rows instead). 

.. note:: 

    The first value of each column is scipped due to being the column name. You can 
    retrieve column names using the :ref:`excel_utilities.getSheetNames <excel_utilities.getSheetNames>` function. 

.. py:function:: excel_utilities.getDataList(sheet, b_rows=False)

    Return a list of columns

    :param sheet: Required excel spreadsheet.
    :type sheet: <class 'openpyxl.worksheet.worksheet.Worksheet'>
    :raise excel_utilities.InvalidSheetError: If the sheet argument is an invalid type.
    :param b_rows: Optional, set to True in order to retrieve lists of rows instead of columns.
    :type b_rows: Boolean
    :return: A list of lists
    :rtype: list()

| The sheet parameter should be retrieved using the :ref:`excel_utilities.getExcelSheet <excel_utilities.getExcelSheet>`.
| Otherwise, :py:func:`excel_utilities.getDataList <excel_utilities.getDataList>` will raise an exception.

.. _excel_utilities.getDataDict:

excel_utilities.getDataDict
---------------------------

To retrieve a dictionary, where keys are the names of each column and the values are the values of that column.

.. py:function:: getDataDict(sheet, col_names, data_list_row)

    Return the values of the specified excel spreadsheet as a dictionary.

    :param sheet: Required excel spreadsheet.
    :type sheet: <class 'openpyxl.worksheet.worksheet.Worksheet'>
    :raise excel_utilities.InvalidSheetError: If the sheet argument is an invalid type.
    :param col_names: The name of each column that will be set as keys in the dictionary. Can be retrived using the :py:func:`excel_utilities.getSheetNames` function.
    :type col_names: tuple(str)
    :param data_list_row: The values of the columns, besides the first row which contains the column names. Can be retrieved using the :py:func:`excel_utilities.getDataList` function.
    :type data_list_row: list()
    :return: A dictionary
    :rtype: dict

stats_proc.arithMean_col
------------------------

.. _stats_proc.arithMean_col:

.. py:function:: stats_proc.arithMean_col(columnName, col_names, data_list_columns)

    Return the arithmetic of a list.

    :param columnName: The name of the column of which the function computes the arithmetic mean.
    :type columnName: str
    :param col_names: The name of each column. Can be retrived using the :py:func:`excel_utilities.getSheetNames` function.
    :type col_names: tuple(str)
    :param data_list_columns: The values of the columns, besides the first row which contains the column names. Can be retrieved using the :py:func:`excel_utilities.getDataList` function.
    :type data_list_columns: list()
    :return: The value of the arithmetic mean of a column.
    :rtype: float

stats_proc.median
-----------------

.. _stats_proc.median:

.. py:function:: stats_proc.median(columnName, col_names, data_list_columns)

    Return the median of a list

    :param columnName: The name of the column of which the function computes the median.
    :type columnName: str
    :param col_names: The name of each column. Can be retrived using the :ref:`excel_utilities.getSheetNames <excel_utilities.getSheetNames>` function.
    :type col_names: tuple(str)
    :param data_list_columns: The values of the columns, besides the first row which contains the column names. Can be retrieved using the :ref:`excel_utilities.getDataList <excel_utilities.getDataList>` function.
    :type data_list_columns: list()
    :return: The value of the median of a column.
    :rtype: float

stats_proc.stat_mode
--------------------

.. _stats_proc.stat_mode:

.. py:function:: stats_proc.stat_mode(columnName, col_names, data_list_columns)

    Return the statistical mode of a list

    :param columnName: The name of the column of which the function computes the mode.
    :type columnName: str
    :param col_names: The name of each column. Can be retrived using the :ref:`excel_utilities.getSheetNames <excel_utilities.getSheetNames>` function.
    :type col_names: tuple(str)
    :param data_list_columns: The values of the columns, besides the first row which contains the column names. Can be retrieved using the :ref:`excel_utilities.getDataList <excel_utilities.getDataList>` function.
    :type data_list_columns: list()
    :return: The value of the mode of a column.
    :rtype: float


graph_creator_func
------------------

.. _graph_creator_func:

.. py:function:: graph_creator_func(inputfile)

    Returns a number of histograms, one for each value retrieved by the :ref:`excel_utilities.getSheetNames <excel_utilities.getSheetNames>` function. 
    The Y-axis is the range of the values accordingly.