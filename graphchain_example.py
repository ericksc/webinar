import dask
import graphchain
import pandas as pd

def create_dataframe(num_rows, num_cols):
    print('Creating DataFrame...')
    return pd.DataFrame(data=[range(num_cols)]*num_rows)

def complicated_computation(df, num_quantiles):
    print('Running complicated computation on DataFrame...')
    return df.quantile(q=[i / num_quantiles for i in range(num_quantiles)])

def summarise_dataframes(*dfs):
    print('Summing DataFrames...')
    return sum(df.sum().sum() for df in dfs)

dsk = {
    'df_a': (create_dataframe, 11_000, 1000),
    'df_b': (create_dataframe, 10_000, 1000),
    'df_c': (complicated_computation, 'df_a', 2048),
    'df_d': (complicated_computation, 'df_b', 2048),
    'result': (summarise_dataframes, 'df_c', 'df_d')
}

# %time dask.get(dsk, 'result')

# %time graphchain.get(dsk, 'result')

# %time graphchain.get(dsk, 'result')