import functools
import dask
import dask.dataframe as dd
import pandas as pd

pdf = pd.DataFrame({
    'x': range(0, 100),
    'y': range(0, 100),
    'z': range(0, 100)
})

ddf = dd.from_pandas(pdf, npartitions=8)

print('Number of partitions', ddf.npartitions)


def compute_stats(row):
    return {
        'sum': row['x'] + row['y'] + row['z'],
        'min': min(row),
        'max': max(row)
    }


def accum_stats(stats_accum, stats):
    return {
        'sum': stats_accum['sum'] + stats['sum'],
        'min': min(stats_accum['min'], stats['min']),
        'max': max(stats_accum['max'], stats['max'])
    }


def compute_stats_partition(pdf):
    pds = pdf.apply(compute_stats, axis=1)
    return functools.reduce(accum_stats, pds)


def merge_stats_series(pds):
    return functools.reduce(accum_stats, pds)


res = ddf.reduction(
    compute_stats_partition,
    merge_stats_series,
    meta={
        'sum': 'int64',
        'min': 'int64',
        'max': 'int64'
    })

# singleton dataframe to list of delayed objects
# where each row is a delayed object
# and in this case we just want the first one
delayed_dict = res.to_delayed()[0]

delayed_dict.visualize('graph.svg')