import utool as ut


def benchmark_knn():
    r"""
    CommandLine:
        python ~/code/ibeis/ibeis/algo/hots/tests/bench.py benchmark_knn --profile

    Example:
        >>> # DISABLE_DOCTEST
        >>> from bench import *  # NOQA
        >>> result = benchmark_knn()
        >>> print(result)
    """
    from ibeis.algo.hots import _pipeline_helpers as plh
    from ibeis.algo.hots.pipeline import nearest_neighbors
    import ibeis
    verbose = True
    qreq_ = ibeis.testdata_qreq_(
        defaultdb='PZ_PB_RF_TRAIN',
        t='default:K=3,requery=True,can_match_samename=False',
        a='default:qsize=100', verbose=1
    )
    locals_ = plh.testrun_pipeline_upto(qreq_, 'nearest_neighbors')
    Kpad_list, impossible_daids_list = ut.dict_take(
       locals_, ['Kpad_list', 'impossible_daids_list'])
    nns_list1 = nearest_neighbors(qreq_, Kpad_list, impossible_daids_list,
                                  verbose=verbose)


if __name__ == '__main__':
    r"""
    CommandLine:
        export PYTHONPATH=$PYTHONPATH:/home/joncrall/code/ibeis/ibeis/algo/hots/tests
        python ~/code/ibeis/ibeis/algo/hots/tests/bench.py
        python ~/code/ibeis/ibeis/algo/hots/tests/bench.py --allexamples
    """
    import multiprocessing
    multiprocessing.freeze_support()  # for win32
    import utool as ut  # NOQA
    ut.doctest_funcs()
