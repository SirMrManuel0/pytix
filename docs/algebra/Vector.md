# Vector
***
The Vector-class inherits from the Matrix class. It is a simple n-dimensional vector.

La classe Vecteur hérite de la classe Matrice. Il s'agit d'un simple vecteur à n dimensions.

Examples:

```python
from pylix.algebra import Vector

v: Vector = Vector([1, 2, 3])

print(v + v)
print(v[0])
print(v[-1])
```

```title="output"
[2 4 6]
1
3
```

## cross
***
Computes the cross product of the vector with another 3D vector.

Calcule le produit vectoriel de 2 vecteurs.

(only for 3D vector)

Example:

```python
from pylix.algebra import Vector

v1: Vector = Vector([1, 0, 0])
v2: Vector = Vector([0, 1, 0])

print(v1.cross(v2))
```
```title="output"
[0 0 1]
```

## from_matrix
`classmethod`
***
Transforms a matrix into a vector.

Transforme une matrice en un vecteur.

(only if the matrix has row = 1)

Example:

```python
from pylix.algebra import Matrix, Vector

m: Matrix = Matrix([[1], [0], [0]])

print(Vector.from_matrix(m))
print(type(Vector.from_matrix(m)))
```
```title="output"
[1 0 0]
<class 'useful_utility.algebra.vector.Vector'>
```

## where
***
Creates a vector whose values are defined by the arg vector / list, which allows the values from self at a position.

Crée un vecteur dont les valeurs sont définies par l'arg Vecteur, qui autorise les valeurs de self à une position.

Example:

```python
from pylix.algebra import Vector

m: Vector = Vector([1, 2])
allowed: Vector = Vector([0, 1])

print(m.where(allowed))
```
```title="output"
[-1 2]
```

## rand_choice
***
Returns the index of a randomly chosen element of the list.

Renvoie l'indice d'un élément de la liste choisi au hasard.

- if heat = -1: Chooses nearly always the max
- if heat =  0: Uses the probability.
- if heat =  1: Randomises the choice even more.

Example:

```python
from pylix.algebra import Vector

m: Vector = Vector([.3, .4, .3])

print(m.rand_choice())
```
```title="output"
1
```

## sample
`classmethod`
***

Creates a vector of the size n with random data from the input vector.

Crée un vecteur de taille n avec des données aléatoires provenant du vecteur d'entrée.

```python
from pylix.algebra import Vector

m: Vector = Vector([1, 2, 3, 4])

print(Vector.sample(m, 3))
```
```title="output"
[4 3 1]
```

## randomise
***

Randomises the data of the vector n=1 amount of times.

Randomise les données du vecteur n=1 nombre de fois.

```python
from pylix.algebra import Vector

m: Vector = Vector([1, 2, 3, 4])
m.randomise()
print(m)
```
```title="output"
[4 2 3 1]
```
