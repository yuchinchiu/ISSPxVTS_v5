    knitr::opts_chunk$set(fig.width=6, fig.height=4, fig.path='figure/', echo = FALSE, warning = FALSE, message = FALSE)

#### First, Set up the environment and load the data: gpData.csv

This file came from python scripts - cleaning and preprocessing

#### Set up some formating for the plots

Set up some good format, here I am using apatheme with white background,
with black axis lines, no grids.

#### First summarize individual subject's data

#### Then, calculate the group mean and within-subject SEM using "getWSSE" (a function I wrote)

    ## [1] "Group means:"

    ## [1] "cued: swCost:75% = 56.70 ms"

    ## [1] "cued: swCost:25% = 86.03 ms"

### RESULTS:

#### Figure 1: cued trials: ISSP(phase x swProb x trialtype\_sw) effect in **RT** (correct trials)

![](figure/Figure1-1.png)

#### 3-way ANOVA: cued trials: RT ~ 2 phase x 2 swProb x 2 trialType\_sw

    ## $ANOVA
    ##                      Effect DFn DFd          SSn        SSd            F
    ## 1               (Intercept)   1  39 2.097253e+08 3330911.88 2455.5703984
    ## 2                     phase   1  39 3.629620e+04  195846.80    7.2278526
    ## 3                    swProb   1  39 2.764147e+02   41323.71    0.2608714
    ## 4              trialType_sw   1  39 3.404905e+05  178730.01   74.2971532
    ## 5              phase:swProb   1  39 1.051895e+02   30283.17    0.1354678
    ## 6        phase:trialType_sw   1  39 3.000149e+03   52269.81    2.2384965
    ## 7       swProb:trialType_sw   1  39 7.686732e+03   26375.68   11.3658688
    ## 8 phase:swProb:trialType_sw   1  39 1.892957e+03   25606.23    2.8830994
    ##              p p<.05          ges
    ## 1 7.784311e-37     * 9.818295e-01
    ## 2 1.050282e-02     * 9.264804e-03
    ## 3 6.124014e-01       7.121110e-05
    ## 4 1.439912e-10     * 8.064984e-02
    ## 5 7.148191e-01       2.710056e-05
    ## 6 1.426612e-01       7.723687e-04
    ## 7 1.698310e-03     * 1.976514e-03
    ## 8 9.748026e-02       4.874684e-04

#### 2-way ANOVA: cued trials(training): RT ~ 2 swProb x 2 trialType

    ## $ANOVA
    ##                Effect DFn DFd          SSn        SSd            F
    ## 1         (Intercept)   1  39 1.076399e+08 1978476.78 2121.8111846
    ## 2              swProb   1  39 3.613188e+02   44248.65    0.3184602
    ## 3        trialType_sw   1  39 2.037066e+05  131887.08   60.2375714
    ## 4 swProb:trialType_sw   1  39 8.604376e+03   36635.88    9.1596174
    ##              p p<.05          ges
    ## 1 1.282675e-35     * 0.9800489258
    ## 2 5.757659e-01       0.0001648646
    ## 3 1.976902e-09     * 0.0850565469
    ## 4 4.367183e-03     * 0.0039113417

#### 2-way ANOVA: cued trials(hybrid): RT ~ 2 swProb x 2 trialType

    ## $ANOVA
    ##                Effect DFn DFd          SSn        SSd            F
    ## 1         (Intercept)   1  39 1.021218e+08 1548281.90 2.572367e+03
    ## 2              swProb   1  39 2.028545e+01   27358.23 2.891753e-02
    ## 3        trialType_sw   1  39 1.397841e+05   99112.74 5.500382e+01
    ## 4 swProb:trialType_sw   1  39 9.753127e+02   15346.03 2.478634e+00
    ##              p p<.05          ges
    ## 1 3.188344e-37     * 9.837196e-01
    ## 2 8.658487e-01       1.200238e-05
    ## 3 5.783594e-09     * 7.638963e-02
    ## 4 1.234809e-01       5.767415e-04

#### Figure 2: ISSP(swProb x trialtype\_sw) effect in **accuracy** by phase

![](figure/Figure2-1.png)

#### 3-way ANOVA: cued trials: ACCURACY ~ 2 phase x 2 swProb x 2 trialType\_sw

    ## $ANOVA
    ##                      Effect DFn DFd          SSn        SSd            F
    ## 1               (Intercept)   1  39 2.530437e+02 2.57037816 3.839398e+03
    ## 2                     phase   1  39 1.067381e-01 0.69236680 6.012399e+00
    ## 3                    swProb   1  39 5.154705e-05 0.08240331 2.439629e-02
    ## 4              trialType_sw   1  39 6.206628e-02 0.10382073 2.331504e+01
    ## 5              phase:swProb   1  39 1.405381e-04 0.05086014 1.077659e-01
    ## 6        phase:trialType_sw   1  39 2.315099e-03 0.04607624 1.959553e+00
    ## 7       swProb:trialType_sw   1  39 4.824377e-04 0.03208948 5.863313e-01
    ## 8 phase:swProb:trialType_sw   1  39 9.399691e-04 0.04614250 7.944692e-01
    ##              p p<.05          ges
    ## 1 1.421511e-40     * 9.858800e-01
    ## 2 1.878618e-02     * 2.860940e-02
    ## 3 8.766865e-01       1.422306e-05
    ## 4 2.148023e-05     * 1.683745e-02
    ## 5 7.444582e-01       3.877686e-05
    ## 6 1.694659e-01       6.383921e-04
    ## 7 4.484509e-01       1.331002e-04
    ## 8 3.782184e-01       2.592963e-04

#### Figure 3: Voluntary task-switching rate (VSR) ~ 2 swProb (25%, 75%)

    ## [1] "VSR_25% swProb = 34.31 %"

    ## [1] "VSR_75% swProb = 35.38 %"

    ## 
    ##  Welch Two Sample t-test
    ## 
    ## data:  meanVSR by swProb
    ## t = -0.68882, df = 76.935, p-value = 0.493
    ## alternative hypothesis: true difference in means is not equal to 0
    ## 95 percent confidence interval:
    ##  -0.04186157  0.02034377
    ## sample estimates:
    ## mean in group sw25% mean in group sw75% 
    ##           0.3430741           0.3538330

![](figure/Figure3-1.png)

#### Figure 4: Voluntary task-switching rate (VSR) ~ 2 runHalf x 2 swProb (25%, 75%)

![](figure/Figure4-1.png)

#### ANOVA: switch rate ~ 2 run x 2 swProb

    ## $ANOVA
    ##              Effect DFn DFd          SSn       SSd            F
    ## 1       (Intercept)   1  39 19.489664685 0.6408901 1186.0019350
    ## 2        runId_half   1  39  0.006884349 0.2243151    1.1969307
    ## 3            swProb   1  39  0.004616441 0.1164709    1.5458045
    ## 4 runId_half:swProb   1  39  0.003637526 0.2801326    0.5064157
    ##              p p<.05         ges
    ## 1 8.267894e-31     * 0.939194263
    ## 2 2.806473e-01       0.005426331
    ## 3 2.211783e-01       0.003645254
    ## 4 4.809299e-01       0.002874501

    ## # A tibble: 1 x 1
    ##   pval_ttest
    ##        <dbl>
    ## 1     0.1711
