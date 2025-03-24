# Vector
***
The Vector-class inherits from the Matrix class. It is a simple n-dimensional vector.

La classe Vecteur hérite de la classe Matrice. Il s'agit d'un simple vecteur à n dimensions.

Examples:
```python
from useful_utility.algebra import Vector

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
from useful_utility.algebra import Vector

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
from useful_utility.algebra import Matrix, Vector

m: Matrix = Matrix([[1], [0], [0]])

print(Vector.from_matrix(m))
print(type(Vector.from_matrix(m)))
```
```title="output"
[1 0 0]
<class 'useful_utility.algebra.vector.Vector'>
```
