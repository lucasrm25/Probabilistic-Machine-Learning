# Exercise 04

## Question 1

Consider the following model
$$ y = \phi_X^T \w + \epsilon$$

with prior $p(\w) = \mathcal N(\w;\b\mu_w,\Sigma_w)$ and i.i.d noise $\epsilon=\mathcal N(0,\sigma^2)$.

The likelihood is then given by $p(\y|w,X) = \mathcal N(\y; \phi_X^T \w,\Lambda)$, with $\Lambda=\sigma^2I $

### (a)

The marginal distribution (or evidence) is given by:

$$ p(\y|X) = \int p(\y|\w) p(\w) d\w = \mathcal N(\y \,;\, \phi_X^T \,\b\mu_\w \,,\, \phi_X^T \,\Sigma_\w \, \phi_X + \Lambda) $$

### (b)

The posterior is then given by

$$ p(\w|\y,X) = \frac{p(\w) p(\y|\w,X)}{p(\y,X)} =  \frac{p(\w) p(\y|\w,X)}{\int p(\y|\w,X) p(\w) d\w} $$

which is Gaussian, since the likelihood and the prior are Gaussians. The posterior can therefore be evaluated by making use of Gaussian algebraic properties, such that Bayesian inference becomes linear algebra

$$ 
\boxed{
    p(\w|\y,X) = \mathcal N (
        \w
        \;;\;
        \mu+\Sigma \phi_X (\phi_X^T \Sigma \phi_X+ \Lambda )^{-1} (y-\phi_X^T \mu ) 
        \;,\;
        \Sigma-\Sigma \phi_X (\phi_X^T \Sigma \phi_X + \Lambda )^{-1} \phi_{\chi}^T \Sigma)
    )
} 
$$

---

## Question 2

### (a)

Another way to find $\w$ is to use the maximum likelihood estimation. Note that we consider i.i.d. noise, such that the joint distribution $\y$ is independent when condtioned on $\w$, i.e. $\mathcal N(\y; \phi_X^T \w,\Lambda) = \prod_i \, \mathcal N(y_i; \phi_{x_i}^T \w, \sigma^2 )$

<!-- $$
\begin{align}
    \w_{ML} &= \min_w J(\w) \\
    &= \min_w - \log \; p(\y|\w,X) \\
    &= \min_w -\log \; \mathcal N(\y; \phi_X^T \w,\Lambda) \\
    &= \min_w -\log \prod_i \, \mathcal N(y_i; \phi_{x_i}^T \w, \sigma^2 ) \\
    &= \min_w - \sum_i \left( -  \frac{1}{2}\log(2\pi)  - \log \sigma -  \frac{1}{\sigma^2} \| y_i - \phi_{x_i}^T \w \|^2  \right) \\
    &= \min_w \sum_i \left( \frac{1}{2}\log(2\pi)  + \log \sigma +  \frac{1}{\sigma^2} \| y_i - \phi_{x_i}^T \w \|^2  \right)
\end{align}
$$ -->

$$
\begin{align}
    \w_{ML} &= \min_w J(\w) \\
    &= \min_w - \log \; p(\y|\w,X) \\
    &= \min_w -\log \; \mathcal N(\y; \phi_X^T \w,\Lambda) \\
    &= \min_w \left( \frac{n}{2}\log(2\pi)  + \frac{1}{2}\log |\Sigma| +  (\y - \phi_X^T \w )^T \, \Sigma^{-1} (\y - \phi_X^T \w )  \right) \\
\end{align}
$$

According to the first order necessary optimality condition $\nabla_w J(\w) = 0 $ and remembering that $\Sigma$ is Hermitian we have

$$
\begin{align}
    \nabla_w J(\w) &= -\phi_X \Sigma^{-1} (\y - \phi_X^T \w ) - \phi_X \Sigma^{-1\;T} (\y - \phi_X^T \w )\\
    &= - 2 \; \phi_X \Sigma^{-1} (\y - \phi_X^T \w ) \\
    &= 0
\end{align}
$$

$$
\begin{align}
    \Rightarrow \quad \phi_X \Sigma^{-1} \phi_X^T \w = \phi_X \Sigma^{-1} \y \\
    \boxed{
    \w = \left( \phi_X \Sigma^{-1} \phi_X^T \right)^{-1} \phi_X \Sigma^{-1} \y }
\end{align}
$$

### (b)



---
$\newcommand{\b}{\boldsymbol}$
$\newcommand{\y}{\boldsymbol{y}}$
$\newcommand{\w}{\boldsymbol{w}}$
$\newcommand{\bphi}{\boldsymbol{\phi}}$