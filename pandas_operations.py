import pandas
d=pandas.read_csv("sind.csv")
print(d)
# print(d.shape) # shape method will show how many rows and columns
# print(d.head()) # head method will show first 5 rows data
# print(d.tail())  # tail method will print last 5 rows data
# print(d.head(1))
# print(d.tail(3))
# print(d[:]) # it will print all the rows in the table
# print(d[2:6])
# print(d[1:4])
# print(d.columns)
# print(d.Place)
# print(d[['Place','Name']])
# print(d)
# print(d['sal'].max())
# print(d['sal'].min())
# print(d.describe())
# print(d[d.sal>400])
# print(d['Place'][d.sal>400])
# print(d[d.sal<450])
# print(d[d.sal==d.sal.max()])
# print(d)
# print(d.loc[5])
# d1=d.set_index('ID')
# print(d1)

# print(dir(pandas))
# print(len(['BooleanDtype', 'Categorical', 'CategoricalDtype', 'CategoricalIndex', 'DataFrame',
# 'DateOffset', 'DatetimeIndex', 'DatetimeTZDtype', 'ExcelFile', 'ExcelWriter', 'Flags', 'Float32Dtype', 
# 'Float64Dtype', 'Float64Index', 'Grouper', 'HDFStore', 'Index', 'IndexSlice', 'Int16Dtype', 'Int32Dtype',
# 'Int64Dtype', 'Int64Index', 'Int8Dtype', 'Interval', 'IntervalDtype', 'IntervalIndex', 'MultiIndex',
# 'NA', 'NaT', 'NamedAgg', 'Period', 'PeriodDtype', 'PeriodIndex', 'RangeIndex', 'Series', 'SparseDtype',
# 'StringDtype', 'Timedelta', 'TimedeltaIndex', 'Timestamp', 'UInt16Dtype', 'UInt32Dtype', 'UInt64Dtype',
# 'UInt64Index', 'UInt8Dtype', '__builtins__', '__cached__', '__doc__', '__docformat__', '__file__',
# '__getattr__', '__git_version__', '__loader__', '__name__', '__package__', '__path__', '__spec__',
# '__version__', '_config', '_hashtable', '_is_numpy_dev', '_lib', '_libs', '_np_version_under1p18',
# '_testing', '_tslib', '_typing', '_version', 'api', 'array', 'arrays', 'bdate_range', 'compat',
# 'concat', 'core', 'crosstab', 'cut', 'date_range', 'describe_option', 'errors', 'eval', 'factorize',
# 'get_dummies', 'get_option', 'infer_freq', 'interval_range', 'io', 'isna', 'isnull','json_normalize', 
# 'lreshape', 'melt', 'merge', 'merge_asof', 'merge_ordered', 'notna', 'notnull','offsets', 'option_context',
# 'options', 'pandas', 'period_range', 'pivot', 'pivot_table', 'plotting', 'qcut', 'read_clipboard',
# 'read_csv', 'read_excel', 'read_feather', 'read_fwf', 'read_gbq', 'read_hdf', 'read_html', 'read_json',
# 'read_orc', 'read_parquet', 'read_pickle', 'read_sas', 'read_spss', 'read_sql','read_sql_query',
# 'read_sql_table', 'read_stata', 'read_table', 'read_xml', 'reset_option', 'set_eng_float_format', 
# 'set_option', 'show_versions', 'test', 'testing', 'timedelta_range', 'to_datetime', 'to_numeric', 
# 'to_pickle', 'to_timedelta', 'tseries', 'unique', 'util', 'value_counts','wide_to_long']))