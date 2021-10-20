# Using TeX math

You can use TeX math! One option is to use it in-line, via single \$, like here where we show the term $f(x) = \frac{L}{1 + e^{-k(x-x_0)}}$ for the logistic function as part of the text. An here it is as a \$\$-block:

```latex
$$
f(x) = \frac{L}{1 + e^{-k(x-x_0)}}
$$

```

___Result___:

$$
f(x) = \frac{L}{1 + e^{-k(x-x_0)}}
$$

You can also number formulars by putting parenthesis with a `(label)` behind the closing \$\$:

```latex
$$
f(x) = \frac{1}{1 + e^{-x}} = \frac{e^x}{e^x + 1} = \frac12 + \frac12 \tanh\left(\frac{x}{2}\right)
$$(eq:stdlog)

```

___Result___:

$$
f(x) = \frac{1}{1 + e^{-x}} = \frac{e^x}{e^x + 1} = \frac12 + \frac12 \tanh\left(\frac{x}{2}\right)
$$(eq:stdlog)

However, referencing formulars is a feature yet to be implemented. 

And, of course, it is possible to use any kind of TeX math constructs like `array` or `align`

```latex
$$
\begin{align}
\tanh(x) & = \frac{e^x - e^{-x}}{e^x + e^{-x}} = \frac{e^x \cdot \left(1 - e^{-2x}\right)}{e^x \cdot \left(1 + e^{-2x}\right)} \\
         &= f(2x) - \frac{e^{-2x}}{1 + e^{-2x}} = f(2x) - \frac{e^{-2x} + 1 - 1}{1 + e^{-2x}} = 2f(2x) - 1.
\end{align}
$$

```

___Result___:

$$
\begin{align}
\tanh(x) & = \frac{e^x - e^{-x}}{e^x + e^{-x}} = \frac{e^x \cdot \left(1 - e^{-2x}\right)}{e^x \cdot \left(1 + e^{-2x}\right)} \\
         &= f(2x) - \frac{e^{-2x}}{1 + e^{-2x}} = f(2x) - \frac{e^{-2x} + 1 - 1}{1 + e^{-2x}} = 2f(2x) - 1.
\end{align}
$$