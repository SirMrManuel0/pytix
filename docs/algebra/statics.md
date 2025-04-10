# statics
***


## rnd
***
Returns the rounded value.

Renvoie la valeur arrondie.

It takes one positional argument, which is the decimal count.

Example:
```python
from pylix.algebra import rnd

number = 5.200_021_895_1
rounded = rnd(5.200_021_895_1)
print(rounded)
```

```title="output"
5.200_021_895
```

with positional argument

```python
from pylix.algebra import rnd

number = 5.200_021_895_1
rounded = rnd(5.200_021_895_1, 6)
print(rounded)
```

```title="output"
5.200_022
```

## average
***
This function calculates the average value of an iterable.

Ca fonction calcule l'intersection d'iterable.

Example:
```python
from pylix.algebra import average

list_ = [-5, 4, 5, 6, 15]
average_ = average(list_)
print(average_)
```

```title="output"
5
```

## variance
***
This function calculates the variance of an iterable.

Ca fonction calcule la variance d'iterable.

Example:
```python
from pylix.algebra import variance

list_ = [-5, 4, 5, 6, 15]
variance_ = variance(list_)
print(variance_)
```

```title="output"
40.4
```

## std
***
This function calculates the standard deviation of an iterable.

Ca fonction calcule l'écart-type d'iterable.

Example:
```python
from pylix.algebra import std

list_ = [-5, 4, 5, 6, 15]
std_ = std(list_)
print(std_)
```

```title="output"
6.356_099_433
```
