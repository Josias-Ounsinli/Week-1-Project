from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
import clean_transform as transf

def engagement_scores(df, clust):
    clusters = transf.aggregate(df, 'cluster', ['sessions frequency', 'Dur. (ms)', 'Total DL (Bytes)', 'Total UL (Bytes)'], ['mean', 'mean', 'mean', 'mean'])
    clust_less = clusters.loc[clusters['cluster'] == clust].drop(['cluster'], axis=1)

    data_point = df[['sessions frequency', 'Dur. (ms)', 'Total DL (Bytes)', 'Total UL (Bytes)']]

    df['eng_scores'] = euclidean_distances(data_point, clust_less)

    return df


def experience_scores(df, clust):
    clusters = transf.aggregate(df, 'cluster', ['Avg RTT DL (ms)', 'Avg RTT UL (ms)', 'Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)'], ['mean', 'mean', 'mean', 'mean'])
    clust_less = clusters.loc[clusters['cluster'] == clust].drop(['cluster'], axis=1)

    data_point = df[['Avg RTT DL (ms)', 'Avg RTT UL (ms)', 'Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)']]

    df['exp_scores'] = euclidean_distances(data_point, clust_less)

    return df


