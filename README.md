# Course on the Economics of Human Capital

> Although it is obvious that people acquire useful skills and knowledge, it is not obvious that these skills and
knowledge are a form of capital, that this capital is in substantial part a product of deliberate investment, that it has grown in Western societies at a much faster rate than conventional (nonhuman) capital, and that its growth may well be the most distinctive feature of the
economic system. It has been widely observed that increases in national output have been large compared with the increases of land, man-hours and physical reproducible capital. Investment in human capital is probably the major explanation for this difference. (Schultz, 1961)

Please use the table of content to navigate the rest of the material.

1. [Lectures](#lectures)
2. [Tutorials](#tutorials)
3. [Readings](#readings)
4. [References](#references)
5. [Iterations](#iterations)

For further questions, please do not hesitate to contact us:

[![project chat](https://img.shields.io/badge/zulip-join_chat-brightgreen.svg)](https://bonn-econ-teaching.zulipchat.com)

## Lectures <a name="lectures"></a>

We provide a brief description of the individual lectures and link the their slides. The material for our tutorial session is available [online](https://github.com/HumanCapitalAnalysis/labor-economics/blob/master/lectures/99-tutorial/slides.pdf) as well.

#### [Introduction](https://github.com/HumanCapitalAnalysis/labor-economics/blob/master/lectures/01-introduction/slides.pdf)

We outline the research program in the economics of human capital. We start by reviewing some facts about the distribution of human capital across and within countries and then study two seminal models emphasizing different mechanisms how education affects labor market outcomes. We present an overview on the National Longitudinal Survey of Youth 1979 with a focus on human capital information, the slides are available [here](https://github.com/OpenSourceEconomics/nlsy_dataset/blob/master/distribution/presentation.pdf). We also discuss the usefulness of mathematical modeling in economics, the slides are available [here](https://github.com/HumanCapitalAnalysis/talks/blob/master/research-skills/02-mathematical-modeling/slides.pdf)

#### [Returns to schooling](https://github.com/HumanCapitalAnalysis/labor-economics/blob/master/lectures/02-returns-schooling/slides.pdf)

We study several models of schooling decisions. We contrast their economic assumptions with a focus on the role of uncertainty and nonlinearities in the return to increasing schooling. In the process, we contrast alternative return concepts and investigate their empirical validity.

#### [Multidimensionality of skills](https://github.com/HumanCapitalAnalysis/labor-economics/blob/master/lectures/03-multidimensionality-skills/slides.pdf)

We sharpen our understanding of the multidimensionality of human capital. We review two papers that showcase the importance of cognitive as well as noncognitive skills for a variety of economic outcomes and objects of interest. But first of all, we start the lecture by briefly reviewing some best practices on how to read a research paper. The slides are available [here](https://github.com/HumanCapitalAnalysis/talks/blob/master/research-skills/01-reading-scientific-papers/slides.pdf).

#### [Static model of educational choice](https://github.com/HumanCapitalAnalysis/labor-economics/blob/master/lectures/04-static-model/slides.pdf)

We study the economics and econometrics of the generalized Roy model. We discuss alternative parameters of interest and clarify the policy questions they address. We also explore the capabilities of the [``grmpy`` package](http://grmpy.readthedocs.io). The manuscript [Issues in the Econometrics of Policy Evaluation](https://github.com/HumanCapitalAnalysis/econometrics/blob/master/distribution/Eisenhauer_2012.pdf) provides an additional introduction to the material discussed in the lecture. We discuss an application of the framework in [Estimating Marginal Returns to Education](https://github.com/HumanCapitalAnalysis/talks/blob/master/seminal-papers/01-Carneiro-al-2011/slides.pdf).

#### [Dynamic model of human capital accumulation](https://github.com/HumanCapitalAnalysis/labor-economics/blob/master/lectures/05-dynamic-model/slides.pdf)

We also study the seminal paper on the career decision of young men in [Keane & Wolpin (1997)](https://github.com/HumanCapitalAnalysis/talks/blob/master/seminal-papers/04-Keane-al-1997/slides.pdf). We explore the capabilities of the [``respy`` package](http://respy.readthedocs.io) to estimate the model presented there.

## Tutorials <a name="tutorials"></a>

We revisit the material of the course in tutorial. Please prepare for our review session using the questions posted [here](https://github.com/HumanCapitalAnalysis/labor-economics/blob/master/lectures/99-tutorial/slides.pdf)


## Readings <a name="readings"></a>

#### Introduction to the economics of human capital

* Becker, G. S. (1994). *Human capital: A theoretical and empirical analysis, with special reference to education* (3rd ed.). Chicago, IL: Chicago University Press.

* Ben-Porath, Y. (1967). [The production of human capital and the life cycle of earnings.](http://www.jstor.org/stable/pdf/1828596.pdf) *Journal of Political Economy, 75*(4, Part 1), 352–365.

* Lagakos, D., Moll, B., Porzio, T., Qian, N., & Schoellman, T. (2018). [Life cycle wage growth across countries.](https://www.journals.uchicago.edu/doi/abs/10.1086/696225?journalCode=jpe) *Journal of Political Economy, 126*(2), 797–849.

* Spence, M. (1973). [Job market signaling.](http://www.jstor.org/stable/1882010?seq=1#page_scan_tab_contents) *Quarterly Journal of Economics, 87*(3), 355–374.

* Weiss, Y. (1986). [The determination of life cycle earnings: A survey.](https://www.sciencedirect.com/science/article/pii/S1573446386010143) In O. Ashenfelter & R. Layard (Eds.), *Handbook of labor economics* (Vol. 1, pp. 603–640). Amsterdam, Netherlands: North-Holland Publishing Company.

#### Returns to schooling

* Heckman, J. J., Lochner, L. J., & Todd, P. E. (2006). [Earnings functions, rates of return and treatment effects: The Mincer equation and beyond.](https://www.sciencedirect.com/science/article/pii/S1574069206010075) In E. A. Hanushek & F. Welch (Eds.), *Handbook of the economics of education* (Vol. 1, pp. 307–458). Amsterdam, Netherlands: North-Holland Publishing Company.

#### Multidimensionality of skills

* Eisenhauer, P., Heckman, J. J., & Mosso, S. (2015). [Estimation of dynamic discrete choice models by maximum likelihood and the simulated method of moments.](https://onlinelibrary.wiley.com/doi/full/10.1111/iere.12107) *International Economic Review, 56*(2), 331–357.

* Heckman, J. J., Stixrud, J., & Urzua, S. (2006). [The effects of cognitive and noncognitive abilities on labor market outcomes and social behavior.](https://www.journals.uchicago.edu/doi/abs/10.1086/504455) *Journal of Labor Economics, 24*(3), 411–482.

#### Static model of educational choice

*  Heckman, J. J., & Vytlacil, E. J. (2007a). [Econometric evaluation of social programs, part
I: Causal effects, structural models and econometric policy evaluation.](https://www.sciencedirect.com/science/article/pii/S1573441207060709) In J. J. Heckman and E. E. Leamer (Eds.), *Handbook of econometrics* (Vol. 6B, pp. 4779–4874). Amsterdam, Netherlands: Elsevier Science.

* Heckman, J. J., & Vytlacil, E. J. (2007b). [Econometric evaluation of social programs, part
II: Using the marginal treatment effect to organize alternative economic estimators to evaluate social programs and to forecast their effects in new environments.](https://www.sciencedirect.com/science/article/pii/S1573441207060710) In J. J. Heckman and E. E. Leamer (Eds.), *Handbook of econometrics* (Vol. 6B, pp. 4779–4874). Amsterdam, Netherlands: Elsevier Science.

* Carneiro, P., Hansen K. T., & Heckman J. J. (2003). [2001 Lawrence R. Klein lecture: Estimating distributions of treatment effects with an application to the returns to schooling and measurement of the effects of uncertainty on college choice.](https://onlinelibrary.wiley.com/doi/10.1111/1468-2354.t01-1-00074) *International Economic Review, 44*(2), 361–422.

* Carneiro, P., Heckman, J. J., & Vytlacil, E. J. (2011). [Estimating marginal returns to education.](https://www.aeaweb.org/articles?id=10.1257/aer.101.6.2754) *American Economic Review, 101*(6), 2754–81.

#### Dynamic model of human capital accumulation

* Keane, M. P., & Wolpin, K. I. (1997). [The career decisions of young men.](https://www.journals.uchicago.edu/doi/abs/10.1086/262080) *Journal of Political Economy, 105*(3), 473–522.

* Keane, M. P., Todd, P. E., & Wolpin, K. I. (2011). [The structural estimation of behavioral models: Discrete choice dynamic programming methods and applications.](https://www.sciencedirect.com/science/article/pii/S0169721811004102) In O. Ashenfelter & D. Card (Eds.), *Handbook of labor economics* (Vol. 4a, pp. 331–461). Amsterdam, Netherlands: Elsevier Science.

## References <a name="references"></a>

* Cahuc, P., & Zylberberg, A. (2004). *Labor Economics.* Cambridge, MA: MIT Press.

* Schultz, T. (1961). [Investment in human capital.](https://www.ssc.wisc.edu/~walker/wp/wp-content/uploads/2012/04/schultz61.pdf) *American Economic Review, 51*(1), 1–17.

## Software packages

* grmpy (2018). *grmpy: A Python package for the simulation and estimation of the generalized Roy model.* Retrieved from http://doi.org/10.5281/zenodo.1162640

* respy (2018). *respy: A Python package for the simulation and estimation of a prototypical finite-horizon dynamic discrete choice model.* Retrieved from http://doi.org/10.5281/zenodo.1189209

## Iterations <a name="iterations"></a>

* **Summer Quarter 2020**, Graduate Program at the University of Bonn, please see [here](https://github.com/HumanCapitalAnalysis/labor-economics/tree/master/iterations/bonn-ss-2020) for details.

* **Summer Quarter 2019**, Graduate Program at the University of Bonn, please see [here](https://github.com/HumanCapitalAnalysis/labor-economics/tree/master/iterations/bonn-ss-2019) for details.

* **Summer Quarter 2018**, Graduate Program at the University of Bonn, please see [here](https://github.com/HumanCapitalAnalysis/labor-economics/tree/master/iterations/bonn-ss-2018) for details.


[![Build Status](https://travis-ci.org/HumanCapitalAnalysis/labor-economics.svg?branch=master)](https://travis-ci.org/HumanCapitalAnalysis/labor-economics)
