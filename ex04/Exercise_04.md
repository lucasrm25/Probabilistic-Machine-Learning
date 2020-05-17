# Exercise 04

## Question 1

Consider the following model
$$ y = \phi_X^\top \w + \epsilon$$

with prior $p(\w) = \mathcal N(\w;\b\mu,\Sigma)$ and i.i.d noise $\epsilon=\mathcal N(0,\sigma^2)$.

The likelihood is then given by $p(\y|w,X) = \mathcal N(\y; \phi_X^\top \w,\Lambda)$, with $\Lambda=\sigma^2I $

#### (a) Marginal distribution (evidence)

The marginal distribution (or evidence) is given by:

$$ p(\y|X) = \int p(\y|\w) p(\w) d\w = \mathcal N(\y \,;\, \phi_X^\top \,\b\mu_\w \,,\, \phi_X^\top \,\Sigma_\w \, \phi_X + \Lambda) $$

#### (b) Posterior distribution

The posterior is then given by

$$ p(\w|\y,X) = \frac{p(\w) p(\y|\w,X)}{p(\y,X)} =  \frac{p(\w) p(\y|\w,X)}{\int p(\y|\w,X) p(\w) d\w} $$

which is Gaussian, since the likelihood and the prior are Gaussians. The posterior can therefore be evaluated by making use of Gaussian algebraic properties, such that Bayesian inference becomes linear algebra

$$ 
\boxed{
    p(\w|\y,X) = \mathcal N (
        \w
        \;;\;
        \b\mu+\Sigma \phi_X (\phi_X^\top \Sigma \phi_X+ \Lambda )^{-1} (\y-\phi_X^\top \b\mu ) 
        \;,\;
        \Sigma - \Sigma \, \phi_X (\phi_X^\top \Sigma \phi_X + \Lambda )^{-1} \phi_X^\top \, \Sigma)
    )
} 
$$

---

## Question 2

#### (a) Maximum Likelihood Estimation (ML)

Another way to find $\w$ is to use the **maximum likelihood estimation**. Note that we consider i.i.d. noise, such that the joint distribution $\y$ is independent when condtioned on $\w$, i.e. $\mathcal N(\y; \phi_X^\top \w,\Lambda) = \prod_i \, \mathcal N(y_i; \phi_{x_i}^\top \w, \sigma^2 )$

$$
\begin{align}
    \w_{ML} &= \min_w J(\w) \\
    &= \min_w - \log \; p(\y|\w,X) \\
    &= \min_w -\log \; \mathcal N(\y; \phi_X^\top \w,\Lambda) \\
    &= \min_w \left( \frac{n}{2}\log(2\pi)  + \frac{1}{2}\log |\Lambda| +  (\y - \phi_X^\top \w )^\top \, \Lambda^{-1} (\y - \phi_X^\top \w )  \right) \\
\end{align}
$$

According to the first order necessary optimality condition $\nabla_w J(\w) = 0 $ and remembering that $\Lambda$ is Hermitian we have

$$
\begin{align}
    \nabla_w J(\w) &= -\phi_X \Lambda^{-1} (\y - \phi_X^\top \w ) - \phi_X \Lambda^{-1\;T} (\y - \phi_X^\top \w )\\
    &= - 2 \; \phi_X \Lambda^{-1} (\y - \phi_X^\top \w ) \\
    &= 0
\end{align}
$$

$$
\begin{align}
    \Rightarrow \quad \phi_X \Lambda^{-1} \phi_X^\top \w = \phi_X \Lambda^{-1} \y \quad \\
    \boxed{
    \w = \left( \phi_X \Lambda^{-1} \phi_X^\top \right)^{-1} \phi_X \Lambda^{-1} \y }
\end{align}
$$

#### (b) Maximum a-posteriori Estimation (MAP)

By an analogous computation, we find $\w$ that maximizes the posterior distribution $p(\w|\y,X) = \mathcal N(\w; \b\mu',\Sigma')$, as defined in exercise 1b). We then get

$$
\begin{align}
    \w_{MAP} &= \min_w J(\w) \\
    &= \min_w - \log \; p(\w|\y,X) \\
    &= \min_w -\log \; \mathcal N(\w; \b\mu',\Sigma') \\
    &= \min_w \left( \frac{n}{2}\log(2\pi)  + \frac{1}{2}\log |\Sigma'| +  (\w - \b\mu')^\top \, \Sigma'^{-1} (\w - \b\mu' )  \right) \\
\end{align}
$$

which is clearly minimized when $\w = \mathbb E_{p(\w|\y)}[\w] = \b\mu'$. This implies that 

$$
\begin{align}
\boxed{
\w_{MAP}  = \mu + \Sigma \, \phi_X (\phi_X^\top \,\Sigma \, \phi_X + \Lambda )^{-1} (\y-\phi_X^\top \mu ) \\
\quad \quad \;\; = (\Sigma^{-1} + \phi_X \Lambda^{-1} \phi_X^\top )^{-1} (\phi_X \Lambda^{-1} \y + \Sigma^{-1} \b\mu )
}
\end{align}
$$

Please note that both formulas above are the same. They are just the Schur complement of oneanother.

For a particular choise $\b\mu=0$ we see that the MAP estimation is just a $\ell_2$-regularized least-square estimator

$$
\begin{align}
\w_{MAP} = (\Sigma^{-1} + \phi_X \Lambda^{-1} \phi_X^\top )^{-1} \phi_X \Lambda^{-1} \y 
\end{align}
$$

<br>

<br>

Please note that another way of seeing the same thing is to view the posterior as $p(\w|\y,X)\propto p(\y|\w,X)p(\w)$, which implies that


$$
\begin{align}
    \w_{MAP} &= \min_w J(\w) \\
    &= \min_w - \log \; p(\y|\w,X) \;\; p(\w) \\
    &= \min_w -\log \; \mathcal N(\y; \phi_X^\top \w,\Lambda) - \log \mathcal N(\w;\b\mu,\Sigma) \\
    &=  \min_w \;\; 
    \underbrace{ \|\y - \phi_X^\top \w \|^2_{\Lambda^{-1}} }_{least-square} +  
    \underbrace{ \|\w - \b\mu \|^2_{\Sigma^{-1}} }_{\ell_2-regularizer} \\
\end{align}
$$

---
$\newcommand{\b}{\boldsymbol}$
$\newcommand{\y}{\boldsymbol{y}}$
$\newcommand{\w}{\boldsymbol{w}}$
$\newcommand{\bphi}{\boldsymbol{\phi}}$