import numpy
from matplotlib import pyplot

class Gaussian1d(object):

    def __init__(self, mu=0.0, sigma=1.0):
        self.mu = float(mu)
        self.sigma = float(sigma)

    def __call__(self, x):
        """Evaluate the function at 'x' (may be a numpy.ndarray or a scalar)."""
        return numpy.exp(-0.5*((x - self.mu)/self.sigma)**2) / (self.sigma*numpy.sqrt(2*numpy.pi))

    def __mul__(self, alpha):
        """Multiply this function by a constant (returns a Mixture1d)."""
        return Mixture1d(func=self, norm=alpha)

    def __rmul__(self, alpha):
        """Multiply this function by a constant (returns a Mixture1d)."""
        return self.__mul__(alpha)

    def __add__(self, other):
        """Add this function to another function (returns a Mixture1d)."""
        # Let Mixture1d handle adding functions
        return Mixture1d(func=self) + other

    def __radd__(self, other):
        """Add this function to another function (returns a Mixture1d)."""
        return self.__add__(other)

    def convolve(self, other):
        """Return another function that is the convolution of this function with another.

        'other' must be a Gaussian1d or Mixture1d instance.
        """
        if isinstance(other, Gaussian1d):
            return Gaussian1d(mu=(self.mu + other.mu), sigma=numpy.sqrt(self.sigma**2 + other.sigma**2))
        else:
            # Let Mixture1d handling convolving with other Mixture1d instances
            return other.convolve(self)


class Mixture1d(object):

    def __init__(self, components=(), func=None, norm=1.0):
        self.components = list(components)
        if func is not None:
            self.components.append((func, norm))

    def copy(self):
        return Mixture1d(components=list(self.components))

    def __mul__(self, alpha):
        """Multiply this function by a constant (returns a Mixture1d)."""
        m = Mixture1d()
        for func, norm in self.components:
            m.components.append(func, alpha*norm)
        return m

    def __rmul__(self, alpha):
        """Multiply this function by a constant (returns a Mixture1d)."""
        return self.__mul__(alpha)

    def __add__(self, other):
        """Add this function to another function (returns a Mixture1d)."""
        if not isinstance(other, Mixture1d):
            other = Mixture1d(func=other)
        m = self.copy()
        for func, norm in other.components:
            m.components.append((func, norm))
        return m

    def __radd__(self, other):
        """Add this function to another function (returns a Mixture1d)."""
        return self.__add__(other)

    def __call__(self, x):
        """Evaluate the function at 'x' (may be a numpy.ndarray or a scalar)."""
        # Handle the first one specially, because we can't += to nothing,
        # and we don't know if x is a single number or an array of numbers
        func, norm = self.components[0]
        result = norm*func(x)
        for func, norm in self.components[1:]:
            result += norm*func(x)
        return result

    def convolve(self, other):
        """Return another function that is the convolution of this function with another.

        'other' must be a Gaussian1d or Mixture1d instance.
        """
        m = Mixture1d()
        if isinstance(other, Gaussian1d):
            for func, norm in self.components:
                m.components.append((func.convolve(other), norm))
        else:
            for func1, norm1 in self.components:
                for func2, norm2 in other.components:
                    m.components.append((func1.convolve(func2), norm1*norm2))
        return m


def plot1d():
    x = numpy.linspace(-30, 30.0, 1000)
    G = Gaussian1d(mu=-15, sigma=2) + 1.5*Gaussian1d(mu=-5, sigma=5) + 2.0*Gaussian1d(mu=10, sigma=3)
    pyplot.rcParams['figure.figsize'] = 16, 8
    ax1 = pyplot.subplot(3,1,1)
    ax2 = pyplot.subplot(3,1,2)
    ax3 = pyplot.subplot(3,1,3)
    ax1.plot(x, G(x), 'k')
    for s in range(1, 8, 2):
        T = Gaussian1d(mu=0, sigma=s)
        I = T.convolve(G)
        ax2.plot(x, T(x), label='sigma={}'.format(s))
        ax3.plot(x, I(x))
    ax1.set_yticks([])
    ax1.set_ylabel("G(x)")
    ax2.set_yticks([])
    ax2.set_ylabel("T(x)")
    ax3.set_yticks([])
    ax3.set_ylabel("(T*G)(x)")
    pyplot.show()
