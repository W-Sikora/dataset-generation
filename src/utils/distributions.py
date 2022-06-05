import numpy.random as rnd

UNSUPPORTED_PROBABILITY_DISTRIBUTION = 'unsupported probability distribution was selected'


def generate(distribution_name: str, size: int, seed=None, **parameters):
    if seed is not None:
        rnd.default_rng(seed)

    if distribution_name == 'beta':
        a = parameters.get('a', )
        b = parameters.get('b', )
        return rnd.beta(a, b, size)

    elif distribution_name == 'binomial':
        n = parameters.get('n', )
        p = parameters.get('p', )
        return rnd.binomial(n, p, size)

    elif distribution_name == 'chisquare':
        df = parameters.get('df', )
        return rnd.chisquare('df', size)

    elif distribution_name == 'dirichlet':
        alpha = parameters.get('alpha', )
        return rnd.dirichlet(alpha, size)

    elif distribution_name == 'exponential':
        scale = parameters.get('scale', )
        return rnd.exponential()

    elif distribution_name == 'f':
        dfnum = parameters.get('dfnum', )
        dfden = parameters.get('dfden', )
        return rnd.f(dfnum, dfden, size)

    elif distribution_name == 'gamma':
        shape = parameters.get('shape', )
        scale = parameters.get('scale', 1.0)
        return rnd.gamma(shape, scale, size)

    elif distribution_name == 'geometric':
        p = parameters.get('p', )
        return rnd.geometric(p, size)

    elif distribution_name == 'gumbel':
        loc = parameters.get('loc', 0.00)
        scale = parameters.get('scale', 1.0)
        return rnd.gumbel(loc, scale, size)

    elif distribution_name == 'laplace':
        loc = parameters.get('loc', 0.00)
        scale = parameters.get('scale', 1.0)
        return rnd.laplace(loc, scale, size)

    elif distribution_name == 'logistic':
        loc = parameters.get('loc', 0.00)
        scale = parameters.get('scale', 1.0)
        return rnd.logistic(loc, scale, size)

    elif distribution_name == 'lognormal':
        mean = parameters.get('mean', 0.00)
        sigma = parameters.get('sigma', 1.0)
        return rnd.lognormal(mean, sigma, size)

    elif distribution_name == 'logseries':
        pass

    elif distribution_name == 'multinomial':
        rnd.multinomial()
        pass

    elif distribution_name == 'multivariate_normal':
        pass

    elif distribution_name == 'negative_binomial':
        pass

    elif distribution_name == 'noncentral_chisquare':
        pass

    elif distribution_name == 'noncentral_f':
        pass

    elif distribution_name == 'normal':
        pass

    elif distribution_name == 'pareto':
        pass

    elif distribution_name == 'poisson':
        pass

    elif distribution_name == 'power':
        pass

    elif distribution_name == 'rayleigh':
        pass

    elif distribution_name == 'standard_cauchy':
        pass

    elif distribution_name == 'standard_exponential':
        pass

    elif distribution_name == 'standard_gamma':
        pass

    elif distribution_name == 'standard_normal':
        pass

    elif distribution_name == 'standard_t':
        pass

    elif distribution_name == 'triangular':
        pass

    elif distribution_name == 'uniform':
        pass

    elif distribution_name == 'vonmises':
        pass

    elif distribution_name == 'wald':
        pass

    elif distribution_name == 'weibull':
        pass

    elif distribution_name == 'zipf':
        pass

    raise ValueError(UNSUPPORTED_PROBABILITY_DISTRIBUTION)




