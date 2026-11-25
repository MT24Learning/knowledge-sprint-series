"""Text of the Phase 9 images, for the website's sprint and phase pages.

Transcribed line by line from the published images (phases/phase-09-classical-machine-learning/).
Card texts, notes, check lines, the summary's tiles and boxes and the source lines are word for word;
the figure panels are read in words from their labels (fig.panels), with the printed captions in
italics. The code of each Try It box is not repeated here: the pages show the sprint's file from
code/, which ends with the printed output. tools/website.py turns this file into the pages.

Marks inside texts: **bold**, *italic*. Thousands are written with a space, as on the images
(1 131); the pages keep each group together with a no-break space.

Regions: where each part sits on the image, in pixels of the 2160 × 2700 PNG (x0, y0, x1, y1),
measured on the images. The page lights the part of the image whose text is being read.
"""

PHASE = dict(
    n=9,
    accents={26: "#6a4796", 27: "#6a4796", 28: "#6a4796", 29: "#6a4796", 30: "#6a4796"},
    # The summary prints each sprint in its own colour (figure labels, tiles).
    summary_accents={26: "#4d7a43", 27: "#9a7414", 28: "#a9522b", 29: "#6a4796", 30: "#3f6491"},
    regions={
        "head": (56, 320, 2104, 580), "fig": (56, 592, 2104, 992),
        "01": (56, 1008, 692, 1416), "02": (708, 1008, 1344, 1416),
        "03": (56, 1432, 692, 1840), "04": (708, 1432, 1344, 1840),
        "06": (56, 1856, 692, 2264), "07": (708, 1856, 1344, 2264),
    },
    summary_regions={
        "head": (60, 60, 1300, 720), "figure": (1390, 270, 2090, 710),
        "tile-0": (80, 796, 552, 1252), "tile-1": (590, 796, 1062, 1252), "tile-2": (1100, 796, 1572, 1252),
        "tile-3": (1610, 796, 2082, 1252), "tile-4": (80, 1284, 552, 1740),
        "block-0": (590, 1284, 1062, 1740), "block-1": (1100, 1284, 1572, 1740), "block-2": (80, 1772, 552, 2216),
        "references": (1610, 1284, 2082, 1740), "next": (590, 1772, 2082, 2216),
    },
)

SPRINTS = {
    26: dict(
        regions={"05": (1360, 1008, 2104, 1832), "R": (1360, 1848, 2104, 2264)},
        em="Rule",
        names="Fisher · Vapnik · Mitchell · Wolpert",
        fig=dict(
            title="100 iris flowers · 70 learned, 30 held out · same data as code 05",
            panels=[
                ("Petal length · petal width", [
                    "petal length (cm), 3 to 7 · petal width (cm), 1.0 to 2.5",
                    "filled dots: learned from · 70 · hollow dots: held out · 30",
                    "green: versicolor · purple: virginica",
                    "red ring: missed by the cut",
                    "dashed line: width > 1.6 → virginica · below it: otherwise → versicolor",
                    "① a dashed circle round a green and a purple dot at the same spot · ② the dashed line of the cut",
                ]),
                ("30 new: right · wrong · no answer", [
                    "Memorise · lookup table · learn 1 / 70 · 1 wrong ③ · a row of mostly empty squares: no answer",
                    "*answers only flowers it has already seen*",
                    "Nearest neighbour · learn 1 / 70 · 3 wrong",
                    "*assumes close flowers share a species*",
                    "One cut · chosen by ERM · learn 3 / 70 · 3 wrong ④",
                    "*assumes one measurement and one threshold*",
                ]),
            ],
            notes_title="Determination notes",
            notes=[
                ("Clash", "Two flowers at 4.8 × 1.8 cm: one versicolor, one virginica. A rule on petals alone must miss one."),
                ("ERM", "Of 42 candidate cuts, width > 1.6 makes the fewest training errors: 3 of 70 (tied with > 1.7)."),
                ("Silent", "The lookup answers only flowers it saw: 24 of 30 get nothing. Its one wrong answer is the clash."),
                ("Tie", "Neighbour and cut both miss 3 of 30. Training errors had ranked them 1 against 3."),
            ],
        ),
        cards=[
            dict(no="01", title="Pairs In, Rule Out", tag="Setup", items=[
                "Training data: pairs of measurements *x* and right answers *y*",
                "The learner returns a rule *h* for a new *x*",
                "Predict a class: classification. Predict a number: regression",
            ], note="Fisher (1936) analysed iris data collected by Anderson (1935): 50 flowers per species, four measurements in cm."),
            dict(no="02", title="Fewest Mistakes Wins", tag="ERM", items=[
                "Loss: 0 if the answer is right, 1 if wrong",
                "Empirical risk: mean loss on my examples; true risk: on new cases (Vapnik 1991)",
                "ERM keeps the rule in my class with the lowest empirical risk",
            ], note="The true risk is never observed. Flowers held out before learning estimate it."),
            dict(no="03", title="Seen vs. Unseen", tag="Overfit", items=[
                "The lookup misses 1 training flower yet answers only 6 of 30 new ones",
                "A memoriser can err 0 on its examples and 1/2 on new ones (Shalev-Shwartz & Ben-David)",
                "Test error, not training error, grades learning",
            ], note="Fewer training errors did not buy fewer test errors: 1 and 3 in training, 3 and 3 on test."),
            dict(no="04", title="No Free Lunch", tag="Induction", items=[
                "Each rule in Fig. 1 carries an assumption",
                "With no assumption a learner can only memorise (Mitchell 1997, ch. 2)",
                "Over all targets, any two learners win equally often off the training set (Wolpert 1996)",
            ], note="Choosing the class of rules is the assumption. I write it down (Sprint 11)."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Hold out the test flowers first (Sprint 20)",
                "Report training and test errors as counts",
                "UCI's iris copy has two wrong rows (Bezdek et al. 1999); scikit-learn's follows Fisher's paper",
            ], note="This random split left 10 versicolor and 20 virginica in the test set. Sprint 27 starts there."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Rerun with seeds 1 to 5; log all three scores",
                "Split by species: 35 + 35, then 15 + 15",
                "Add both sepal measurements: how many new flowers can the lookup still answer?",
                "Write each rule's assumption beside its score",
            ], note="With all four measurements and seed 26, the lookup answers 0 of 30."),
        ],
        tryit=dict(versions="PYTHON 3.13.15",
                   check="Check: 30 − 24 = 6 answered · 1/70 = 1.4% · 3/70 = 4.3% · 3/30 = 10% · numpy 2.5.3 · scikit-learn 1.9.1"),
        sources=[
            ("Fisher (1936). *The Use of Multiple Measurements in Taxonomic Problems.* Ann. Eugen. 7(2), 179–188",
             "https://doi.org/10.1111/j.1469-1809.1936.tb02137.x"),
            ("Anderson (1935). *The Irises of the Gaspé Peninsula.* Bull. Am. Iris Soc. 59, 2–5",
             "https://archive.org/details/bulletinofameric5559unse"),
            ("Bezdek et al. (1999). *Will the Real Iris Data Please Stand Up?* IEEE Trans. Fuzzy Syst. 7(3), 368–369",
             "https://doi.org/10.1109/91.771092"),
            ("Vapnik (1991). *Principles of Risk Minimization for Learning Theory.* NIPS 4, 831–838",
             "https://proceedings.neurips.cc/paper/1991/hash/ff4d5fbbafdf976cfdc032e3bde78de5-Abstract.html"),
            ("Shalev-Shwartz & Ben-David (2014). *Understanding Machine Learning: From Theory to Algorithms*, ch. 2. CUP",
             "https://doi.org/10.1017/CBO9781107298019"),
            ("Mitchell (1997). *Machine Learning*, ch. 2. McGraw-Hill", "https://www.cs.cmu.edu/~tom/mlbook.html"),
            ("Wolpert (1996). *The Lack of A Priori Distinctions Between Learning Algorithms.* Neural Comput. 8(7), 1341–1390",
             "https://doi.org/10.1162/neco.1996.8.7.1341"),
            ("scikit-learn docs: *load_iris* · *An introduction to machine learning with scikit-learn*",
             "https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html"),
        ],
    ),

    27: dict(
        regions={"05": (1360, 1008, 2104, 1872), "R": (1360, 1888, 2104, 2264)},
        em="First",
        names="Holte · Brodersen · Ferrari Dacrema · Hyndman",
        fig=dict(
            title="Two floors · iris from Sprint 26 · handwritten digits · same data as code 05",
            panels=[
                ("Iris · Sprint 26 split", [
                    "learn: versicolor 40 · virginica 30",
                    "test: versicolor 10 · virginica 20",
                    "green: versicolor · purple: virginica · *flowers*",
                    "test accuracy · 30 flowers, on a scale from 0 to 1:",
                    "① 0.333 · *always versicolor*",
                    "0.5 · *a coin, expected*",
                    "0.900 · *the cut, Sprint 26*",
                ]),
                ("Digits · is it a 9? · 540 test images, 54 nines", [
                    "Always “no” · *the majority*: accuracy 0.900 · balanced accuracy 0.500",
                    "Pixel 38 > 12 · *picked by accuracy*: 0.894 · 0.505 ③",
                    "Pixel 29 > 11 · *picked by balanced*: 0.759 · 0.809 ④",
                    "Logistic · *all 64 pixels*: 0.983 · 0.941",
                    "a small grid beside each pixel rule marks its pixel in red",
                    "dotted line at 0.5: chance · balanced · dashed line at 0.900: always “no” ②",
                    "grey bars: accuracy · purple bars: balanced accuracy · scale 0 to 1",
                ]),
            ],
            notes_title="Determination notes",
            notes=[
                ("Floor", "Learn set: 40 versicolor, 30 virginica. Test set: 10 and 20. “Always versicolor” scores 0.333."),
                ("Rare", "“No” to all 540 digits scores 0.900 and finds no 9. Balanced accuracy: 0.500."),
                ("Trap", "Picked by accuracy, pixel 38 beat “no” by one learn image (1 132 vs 1 131), then lost on test."),
                ("Fix", "Picked by balanced accuracy, pixel 29 finds 47 of 54 nines. Accuracy drops, balanced rises."),
            ],
        ),
        cards=[
            dict(no="01", title="What a Floor Is", tag="Setup", items=[
                "A baseline answers without reading the input: majority class, mean, last value",
                "DummyClassifier “makes predictions that ignore the input features” (scikit-learn)",
                "A model's claim is its gap above that floor",
            ], note="Holte (1993): on most datasets studied, the best one-attribute rule was as accurate as most learners."),
            dict(no="02", title="Accuracy Lies", tag="Imbalance", items=[
                "54 of 540 test digits are 9s: “always no” scores 0.900",
                "Balanced accuracy averages the recall of each class: “always no” gets 0.500 (Brodersen et al. 2010)",
            ], note="Recall is the share of a class the rule finds: 0 of 54 nines here. I read all four counts."),
            dict(no="03", title="The Score Steers", tag="Loss", items=[
                "By accuracy: pixel 38 says “yes” 5 times and finds 1 nine",
                "By balanced accuracy: pixel 29 finds 47 of 54 and flags 123 others",
                "So the score decides what ERM learns",
            ], note="Logistic regression on all 64 pixels: 0.983 and 0.941. It clears both floors."),
            dict(no="04", title="Weak Baselines", tag="Evidence", items=[
                "Of 18 neural recommenders, 7 could be reproduced with reasonable effort; 6 of those were often beaten "
                "by simple heuristics (Ferrari Dacrema et al. 2019)",
                "A method is only as new as the strongest baseline it beat",
            ], note="So I tune the baseline as hard as the model."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Fit the baseline on the learn set only",
                "Stratify the split to keep the class shares",
                "Numbers: R² measures against the mean. Forecasts: MASE divides by the naive forecast's error "
                "(Hyndman & Koehler 2006)",
            ], note="In Sprint 26's split the learn-set majority was the test-set minority."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Rerun with random_state 1 to 5",
                "Ask “is it a 1?”, then “is it an 8?”",
                "Stratify the iris split; recompute the floor",
                "Diabetes data: DummyRegressor vs LinearRegression, scored by R²",
            ], note="With random_state 27, the learn-set mean scores R² = −0.016 on test; linear regression 0.451."),
        ],
        tryit=dict(versions="PYTHON 3.13.15",
                   check="Check: 486/540 = 0.900 · (482+1)/540 = 0.894 · (47/54 + 363/486)/2 = 0.809 · 10/30 = 0.333. "
                         "scikit-learn 1.9.1"),
        sources=[
            ("Holte (1993). *Very Simple Classification Rules Perform Well on Most Commonly Used Datasets.* "
             "Mach. Learn. 11(1), 63–90", "https://doi.org/10.1023/A:1022631118932"),
            ("Brodersen, Ong, Stephan & Buhmann (2010). *The Balanced Accuracy and Its Posterior Distribution.* "
             "ICPR, 3121–3124", "https://doi.org/10.1109/ICPR.2010.764"),
            ("Ferrari Dacrema, Cremonesi & Jannach (2019). *Are We Really Making Much Progress? A Worrying Analysis of "
             "Recent Neural Recommendation Approaches.* RecSys", "https://doi.org/10.1145/3298689.3347058"),
            ("Hyndman & Koehler (2006). *Another Look at Measures of Forecast Accuracy.* Int. J. Forecast. 22(4), 679–688",
             "https://doi.org/10.1016/j.ijforecast.2006.03.001"),
            ("Alpaydin & Kaynak (1998). *Optical Recognition of Handwritten Digits.* UCI ML Repository",
             "https://doi.org/10.24432/C50P49"),
            ("scikit-learn docs: *DummyClassifier* · *balanced_accuracy_score* · *r2_score*",
             "https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html"),
        ],
    ),

    28: dict(
        regions={"05": (1360, 1008, 2104, 1848), "R": (1360, 1864, 2104, 2264)},
        em="Neighbours",
        names="Cox · Breiman · Fix & Hodges · Cover & Hart",
        fig=dict(
            title="178 Italian wines · two measurements · four maps · same data as code 05",
            panels=[
                ("Linear · z-scores · 0.926", [
                    "*proline* (500 to 1 500) against *flavanoids* (1 to 5), the same axes in all four maps",
                    "dots: cultivar 1 (green) · cultivar 2 (gold) · cultivar 3 (purple) · red ring: missed",
                    "① three regions parted by straight lines",
                ]),
                ("Tree · depth 3 · 0.907", [
                    "② box-shaped regions",
                    "dashed line: proline ≤ 755?",
                ]),
                ("5-NN · z-scores · 0.944", [
                    "③ regions that follow the shape of the clouds",
                ]),
                ("5-NN · raw units · 0.704", [
                    "④ thin horizontal bands of all three colours",
                    "red rings on many wines at the left and in the bands",
                ]),
            ],
            notes_title="Determination notes",
            notes=[
                ("Lines", "Logistic regression splits the plane with straight lines: 50 of 54 test wines right."),
                ("Boxes", "The tree asks “proline ≤ 755?” first, then about flavanoids. Its regions are boxes: 49 of 54."),
                ("Local", "Five nearest neighbours on z-scores follow the clouds' shape: 51 of 54."),
                ("Units", "In raw units proline (278 to 1 680) drowns flavanoids (0.34 to 5.08). Bands appear: 38 of 54."),
            ],
        ),
        cards=[
            dict(no="01", title="Linear: Weigh, Add", tag="Linear", items=[
                "Logistic regression sums weighted measurements and turns the sum into a probability (Cox 1958)",
                "Its boundaries are straight lines, or flat planes in more dimensions",
            ], note="Assumption: the classes part along straight lines. Here it held: 0.926 on two columns, 1.000 on all 13."),
            dict(no="02", title="Tree: Ask, Split", tag="Tree", items=[
                "One yes/no question per node, until a leaf names the class (Breiman et al. 1984)",
                "Regions are boxes; scaling the columns left its score unchanged",
                "Small changes in data can grow a different tree (scikit-learn)",
            ], note="Depth 3 here: 0.907 on two columns, 0.870 on all 13."),
            dict(no="03", title="Neighbours: Vote", tag="k-NN", items=[
                "5-NN labels a wine by the vote of its 5 closest learn wines (Fix & Hodges 1951)",
                "With unlimited data, 1-NN errs at most twice as often as the best possible rule (Cover & Hart 1967)",
            ], note="Assumption: close in measurement means close in class. “Close” needs a common scale."),
            dict(no="04", title="Scale First", tag="Units", items=[
                "Raw units: 5-NN scores 0.704 on two columns, 0.741 on 13",
                "z-scores fitted on the learn set: 0.944 and 1.000",
                "The tree does not move: 0.870 either way",
            ], note="Scaling sits inside the pipeline, so test wines never shape it (Sprint 20)."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Pick a learner for its assumption, then test it",
                "One wine in 54 moves accuracy by 0.019: a gap of one or two wines is noise",
                "Read the data's provenance, not only its rows",
            ], note="scikit-learn's wine notes repeat the iris file's creator, donor and date. UCI credits Aeberhard and Forina."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Rerun with random_state 1 to 5",
                "Try k = 1, 15 and 51 on the two columns",
                "Let the tree grow to full depth",
                "Print each tree's first question",
            ], note="Seeds 1 to 5 opened with colour intensity three times, proline once, alcohol once."),
        ],
        tryit=dict(versions="PYTHON 3.13.15",
                   check="Check: 50/54 = 0.926 · 49/54 = 0.907 · 51/54 = 0.944 · 38/54 = 0.704 · 47/54 = 0.870 · "
                         "1/54 = 0.019. scikit-learn 1.9.1"),
        sources=[
            ("Cox (1958). *The Regression Analysis of Binary Sequences.* J. R. Stat. Soc. B 20(2), 215–242",
             "https://doi.org/10.1111/j.2517-6161.1958.tb00292.x"),
            ("Breiman, Friedman, Olshen & Stone (1984). *Classification and Regression Trees.* Wadsworth",
             "https://doi.org/10.1201/9781315139470"),
            ("Fix & Hodges (1951). *Discriminatory Analysis. Nonparametric Discrimination: Consistency Properties.* "
             "USAF School of Aviation Medicine, Report 4",
             "https://apps.dtic.mil/sti/pdfs/ADA800276.pdf"),
            ("Cover & Hart (1967). *Nearest Neighbor Pattern Classification.* IEEE Trans. Inf. Theory 13(1), 21–27",
             "https://doi.org/10.1109/TIT.1967.1053964"),
            ("Aeberhard & Forina (1992). *Wine.* UCI ML Repository", "https://doi.org/10.24432/C5PC7J"),
            ("scikit-learn docs: *Decision Trees* · *Importance of Feature Scaling* · *load_wine*",
             "https://scikit-learn.org/stable/modules/tree.html"),
        ],
    ),

    29: dict(
        regions={"05": (1360, 1008, 2104, 1874), "R": (1360, 1890, 2104, 2264)},
        em="Cross-Validation",
        names="Hoerl & Kennard · Tibshirani · Stone · Hastie",
        fig=dict(
            title="442 diabetes patients · 15 penalties · 5 folds each · same data as code 05",
            panels=[
                ("5 folds · 309 learn patients", [
                    "run 1 to run 5: each run scores one fold and fits on the other four",
                    "fit on 4 folds · score 1 fold",
                    "① test 133 sealed",
                    "*CV error = mean of the 5 fold scores, standard error = their sd ÷ √5*",
                ]),
                ("Ridge on 65 terms · error (MSE) by penalty `α`", [
                    "train (fold mean) · CV ± 1 SE, error 2 000 to 5 000",
                    "*too free: it memorises* · ② CV 4 027 at α 0.001 · train 2 037",
                    "③ α 31.6 · 3 047",
                    "④ best + 1 SE = 3 250",
                    "CV 5 214 at α 10 000",
                    "*too tight: it cannot bend*",
                    "*penalty α (log scale) → more penalty, simpler model*: 0.001 to 10 000",
                ]),
            ],
            notes_title="Determination notes",
            notes=[
                ("Folds", "Each learn patient is scored once, by a model fitted on the other 4 folds. The 133 test patients wait."),
                ("Free", "α = 0.001: training error 2 037, CV error 4 027. The 65 terms memorise."),
                ("Best", "CV error bottoms out at α = 31.6: 3 047 ± 203."),
                ("1-SE", "α = 100 is the most penalised model under 3 250. Sealed test: 3 717 against 3 760."),
            ],
        ),
        cards=[
            dict(no="01", title="Price the Weights", tag="Penalty", items=[
                "Ridge adds α × (sum of squared weights) to the squared error (Hoerl & Kennard 1970)",
                "Lasso prices absolute weights and “tends to produce some coefficients that are exactly 0” (Tibshirani 1996)",
            ], note="α = 0 is plain least squares. The penalty treats all columns alike, so I scale first (Sprint 28)."),
            dict(no="02", title="Too Free, Too Tight", tag="Fit", items=[
                "α = 0.001: training error 2 037, CV error 4 027",
                "α = 10 000: both above 5 000; the model can barely bend",
                "Between them, CV error bottoms out at α = 31.6",
            ], note="Too loose chases noise, too tight misses signal: the bias–variance trade-off (Hastie et al. 2009, ch. 7)."),
            dict(no="03", title="K Folds", tag="Cross-val", items=[
                "Cut the learn set into 5 folds: fit on 4, score the 5th, rotate",
                "Every learn patient is scored once, by a model that never saw it",
                "Stone (1974) formalised choosing and assessing predictions this way",
            ], note="The 133 test patients never enter the folds (Sprint 20)."),
            dict(no="04", title="One Standard Error", tag="1-SE", items=[
                "The best CV error is an estimate too: 3 047 ± 203",
                "The 1-SE rule takes the most penalised model within one standard error of the best (Hastie et al. 2009, §7.10)",
            ], note="Here α = 100, CV 3 062. On the sealed test set: 3 717 against 3 760."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "Build terms and scale inside the pipeline, so each fold fits its own",
                "Report the CV mean with its standard error",
                "A CV score used to pick α flatters the model it picked (Cawley & Talbot 2010)",
            ], note="scikit-learn's diabetes columns come centred and scaled on all 442 patients, test rows included."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Swap Ridge for Lasso; count the zero weights",
                "Use 10 folds, then 5 shuffled repeats",
                "Fit the plain 10 columns: does CV prefer them?",
                "Plot train and CV error against α",
            ], note="Lasso at α = 3: CV 2 907, with 16 of 65 weights non-zero. The plain 10 columns: CV 3 040."),
        ],
        tryit=dict(versions="PYTHON 3.13.15",
                   check="Check: 4 027 − 2 037 = 1 990 gap at α = 0.001 · 3 047 + 203 = 3 250 ≥ 3 062 · "
                         "10^{k/2}, k = −6 … 8: 15 penalties. scikit-learn 1.9.1"),
        sources=[
            ("Hoerl & Kennard (1970). *Ridge Regression: Biased Estimation for Nonorthogonal Problems.* "
             "Technometrics 12(1), 55–67", "https://doi.org/10.1080/00401706.1970.10488634"),
            ("Tibshirani (1996). *Regression Shrinkage and Selection via the Lasso.* J. R. Stat. Soc. B 58(1), 267–288",
             "https://doi.org/10.1111/j.2517-6161.1996.tb02080.x"),
            ("Stone (1974). *Cross-Validatory Choice and Assessment of Statistical Predictions.* "
             "J. R. Stat. Soc. B 36(2), 111–147", "https://doi.org/10.1111/j.2517-6161.1974.tb00994.x"),
            ("Hastie, Tibshirani & Friedman (2009). *The Elements of Statistical Learning*, 2nd ed., ch. 7. Springer",
             "https://doi.org/10.1007/978-0-387-84858-7"),
            ("Cawley & Talbot (2010). *On Over-fitting in Model Selection and Subsequent Selection Bias in Performance "
             "Evaluation.* JMLR 11, 2079–2107", "https://jmlr.org/papers/v11/cawley10a.html"),
            ("Efron, Hastie, Johnstone & Tibshirani (2004). *Least Angle Regression.* Ann. Stat. 32(2), 407–499",
             "https://doi.org/10.1214/009053604000000067"),
        ],
    ),

    30: dict(
        regions={"05": (1360, 1008, 2104, 1880), "R": (1360, 1896, 2104, 2264)},
        em="Generalises",
        names="Hoeffding · Vapnik · Chervonenkis · Valiant",
        fig=dict(
            title="Why a training score can be trusted, and when it cannot · same data as code 05",
            panels=[
                ("The price of choosing · 70 examples · 95% confidence", [
                    "bound ε = √(ln(2|H|/δ) / 2n) · median gap, best of |H| noise rules",
                    "*training-to-true gap*, 0.0 to 0.4, against *number of rules tried, |H| (log scale)*, 1 to 1 000 000",
                    "bound: 0.162 for 1 rule · 142 cuts: 0.248 · ② · bound 0.354 at 1 000 000",
                    "① noise gap 0.286",
                ]),
                ("Sprint 26 · width > 1.6", [
                    "error rate, 0.0 to 0.3: 0.043 *train* · 0.100 *test* ④ · 0.291 *bound* ③",
                    "*true error ≤ 0.291 at 95%, if the flowers are independent draws*",
                    "**ε = 0.05 needs 1 729 flowers**",
                ]),
            ],
            notes_title="Determination notes",
            notes=[
                ("Noise", "The best of a million coin-flip rules typically errs on just 15 of 70 random labels: 78.6% “right”."),
                ("Price", "The bound grows like √ln|H|: 0.162 for one rule, 0.354 for a million."),
                ("Cut", "142 cuts fixed in advance; ERM keeps width > 1.6 at 0.043. So true error ≤ 0.043 + 0.248 = 0.291."),
                ("Test", "The 30 held-out flowers gave 0.100: inside the bound, which is loose."),
            ],
        ),
        cards=[
            dict(no="01", title="One Fixed Rule", tag="Hoeffding", items=[
                "For one rule fixed in advance, training error misses true error by ε or more with chance ≤ 2e⁻²ⁿᵋ² "
                "(Hoeffding 1963)",
                "More data shrinks ε like 1/√n",
            ], note="The rule must be fixed before the data arrive. ERM chooses after seeing them, so one rule is not the whole story."),
            dict(no="02", title="The Price of Choice", tag="Union", items=[
                "ERM picks among |H| rules, so all of them must stay close at once",
                "Then ε = √(ln(2|H|/δ) / 2n) (Shalev-Shwartz & Ben-David, Cor. 4.6)",
                "A million rules cost 2.2× the ε of one",
            ], note="Each rule I try is one more chance to fit noise."),
            dict(no="03", title="Infinite Classes", tag="VC · PAC", items=[
                "VC dimension counts how many points a class can label in every way (Vapnik & Chervonenkis 1971)",
                "PAC: probably (1 − δ) approximately (ε) correct (Valiant 1984)",
            ], note="“x > c means yes” has VC dimension 1: it cannot say yes to a low point and no to a higher one."),
            dict(no="04", title="The Open Puzzle", tag="Frontier", items=[
                "Large networks fit random labels perfectly, yet generalise on real ones (Zhang et al. 2017)",
                "Past the point of fitting every example, test error can fall again: “double descent” (Belkin et al. 2019)",
            ], note="The bounds stay true; for such models they are loose. This theory is still being written."),
            dict(no="06", title="General Notes", tag="Practice", items=[
                "A guarantee holds only under its assumptions: independent draws, one distribution",
                "Count every rule tried, the discarded ones too",
                "A loose bound still ranks choices: fewer rules, more data",
            ], note="Sprint 26 drew its 42 cuts from the training values. A grid fixed in advance keeps the count honest."),
            dict(no="07", title="Mini Project", tag="Hands-on", items=[
                "Simulate 70 random labels and 1 000 random rules",
                "Plot ε against n for |H| = 142",
                "Find the n that gives ε = 0.02",
                "Shatter 3 points with lines; try 4",
            ], note="ε = 0.02 needs 10 806 flowers. Lines can shatter 3 points in the plane, never 4."),
        ],
        tryit=dict(versions="PYTHON 3.13.15",
                   check="Check: 0.500 − 0.214 = 0.286 · 0.354 ÷ 0.162 = 2.18 · ln(2·142/0.05) ÷ (2 · 0.05²) = 1 728.9 → 1 729. "
                         "scipy 1.18.1 · scikit-learn 1.9.1"),
        sources=[
            ("Hoeffding (1963). *Probability Inequalities for Sums of Bounded Random Variables.* JASA 58(301), 13–30",
             "https://doi.org/10.1080/01621459.1963.10500830"),
            ("Vapnik & Chervonenkis (1971). *On the Uniform Convergence of Relative Frequencies of Events to Their "
             "Probabilities.* Theory Probab. Appl. 16(2), 264–280", "https://doi.org/10.1137/1116025"),
            ("Valiant (1984). *A Theory of the Learnable.* Commun. ACM 27(11), 1134–1142", "https://doi.org/10.1145/1968.1972"),
            ("Shalev-Shwartz & Ben-David (2014). *Understanding Machine Learning: From Theory to Algorithms*, ch. 4–6. CUP",
             "https://doi.org/10.1017/CBO9781107298019"),
            ("Zhang, Bengio, Hardt, Recht & Vinyals (2017). *Understanding Deep Learning Requires Rethinking "
             "Generalization.* ICLR", "https://arxiv.org/abs/1611.03530"),
            ("Belkin, Hsu, Ma & Mandal (2019). *Reconciling Modern Machine-Learning Practice and the Classical "
             "Bias–Variance Trade-Off.* PNAS 116(32), 15849–15854", "https://doi.org/10.1073/pnas.1903070116"),
        ],
    ),
}

SUMMARY = dict(
    style="catalog",
    kicker="Phase 9 · Summary · Sprints 26–30 of 90",
    em="Classical",
    dek="Floors, learners, a penalty and a bound: five sprints on rules that hold on new data, every number rerun in code.",
    badges=["5 sprints, 5 code runs", "Verified sources", "One phase project"],
    figure=dict(label="Figure", lines=[
        "A dark code window with two small plots",
        "purple dots above and green dots below a dashed line · width > 1.6",
        "a U-shaped error curve with its lowest point ringed, above a rising lighter curve · CV error by α",
        "five tags beside it: Rule · Floor · Learners · Penalty · Bound",
    ]),
    tiles=[
        dict(sprint=26, title="Learning a Rule", tag="Sprint 26",
             text="Memory answered 6 of 30 new flowers; one cut on petal width got 27."),
        dict(sprint=27, title="Baselines First", tag="Sprint 27",
             text="“Always no” scores 0.900 on rare 9s. Balanced accuracy says 0.500."),
        dict(sprint=28, title="Three Learners", tag="Sprint 28",
             text="Line, box, neighbourhood. Unscaled, 5-NN fell from 0.944 to 0.704."),
        dict(sprint=29, title="Penalty & Folds", tag="Sprint 29",
             text="Ridge on 65 terms: CV error 4 027 → 3 047. The 1-SE rule picks α = 100."),
        dict(sprint=30, title="Why It Generalises", tag="Sprint 30",
             text="Best of a million noise rules: 78.6% “right”. Bound on its gap: 0.354."),
    ],
    blocks=[
        dict(title="Now I Can", tag="Outcome", colour="#9186b2",
             text="Set a floor, choose a learner by its assumption, tune α by CV, bound the gap."),
        dict(title="Mistakes Avoided", tag="Lessons", colour="#cc7279",
             text="Accuracy on rare classes, unscaled k-NN, a CV score reused as a grade."),
        dict(title="Phase Project", colour="#758fb0",
             text="One dataset end to end: a floor, three learners, α tuned by 5-fold CV, and a bound for the rule kept."),
    ],
    references_title="Trusted Sources",
    references=[
        ("Vapnik 1991", "https://proceedings.neurips.cc/paper/1991/hash/ff4d5fbbafdf976cfdc032e3bde78de5-Abstract.html"),
        ("Holte 1993", "https://doi.org/10.1023/A:1022631118932"),
        ("Cover & Hart 1967", "https://doi.org/10.1109/TIT.1967.1053964"),
        ("Tibshirani 1996", "https://doi.org/10.1111/j.2517-6161.1996.tb02080.x"),
        ("Hoeffding 1963", "https://doi.org/10.1080/01621459.1963.10500830"),
    ],
    next_issue=("Next · Phase 10", "Neural Networks", "From rules to networks."),
)
