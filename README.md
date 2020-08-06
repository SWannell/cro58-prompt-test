# CRO58: COVID-19 prompt test

A copy of [CRO55](https://github.com/SWannell/cro55-prompt-test), but for email donors. See that repo's readme for test approach etc.

### How to check test progress

1. ✓ Get the LBL data from the web reporting database
2. ✓ _lbl_munge.py_: change path for the new LBL CSV if needed, run
3. ✘ Add new dates into [the less-sampled transaction ID sheet](https://docs.google.com/spreadsheets/d/10M-glXPJoNxjO2fNPybhvqE3AR0FUWh7u2Zsdp-hCtM/edit#gid=395427764). Download to RawData.
4. ✓ _FetchData.py_: run, with GA access token
5. * _lbl_ga_join.py_: change end date, run
6. ? _DoSeqAnalysis.py_ for the conversion % check
7. ? _seq_analysis_ttest.py_ for the average gift check

* Got a flag that 06498360025098340 was missing. Could be because it's a wholly numeric ID, so one system has removed the leading 0? It _is_ in the online Transaction Search report though. Hmm.

### Results

- _gift_distibution.py_: looking at the gift value distribution.
- _guardrail_checks.py_: looking at the guardrail metrics (Gift Aid, email opt-in).
- _income_projections.py_: projecting income out to a one-year estimate, as per the analysis plan.