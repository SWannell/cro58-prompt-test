# CRO58: COVID-19 prompt test

A copy of [CRO55](https://github.com/SWannell/cro55-prompt-test), but for email donors. See that repo's readme for test approach etc.

### How to check test progress

1. ✓ Get the LBL data from the web reporting database
2. ✓ _lbl_munge.py_: change path for the new LBL CSV if needed, run
3. ✓ _FetchData.py_: run, with GA access token
4. * _lbl_ga_join.py_: change end date, run

* Got a flag that 06498360025098340 was missing. Could be because it's a wholly numeric ID, so one system has removed the leading 0? It _is_ in the online Transaction Search report though. Hmm.

=> ran just on [the GA data](https://docs.google.com/spreadsheets/d/1oWN1gwe0B5TUNKBAbZfrUyhcPAdjjdj2FErfz8HsGNs/edit#gid=1226024178).

0. Get the chi sq results from [GA > Behaviour > Experiments](https://analytics.google.com/analytics/web/#/siteopt-experiment/siteopt-detail/a203531w84011461p149197394/_r.drilldown=analytics.gwoExperimentId:p1QJ_NkPQ9upbkKUn--OhQ&createExperimentWizard.experimentId=p1QJ_NkPQ9upbkKUn--OhQ)
1. ✓ Get the gift value data from GA
2. ✓ _munge_ga.py_ to reformat GA extract

### Results

- _ttest.py_ to get the average gift results
- _income_projections.py_: projecting income out to a one-year estimate, as per the analysis plan.
- _gift_distibution.py_: looking at the gift value distribution.