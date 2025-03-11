
# Matrix

A class representing a mathematical matrix with various operations like addition, subtraction, multiplication, and more. The matrix can be created from a 2D list of numbers or initialized as a zero matrix. It supports operations with other matrices and scalar values, and provides methods for accessing and modifying matrix components. This matrix is iterable.

Une classe qui représente une matrice mathématique. Elle a différentes méthodes comme l'addition, la soustraction, multiplication et plus encore. La matrice peut être créée à partir d'une liste de nombres en 2D ou initialisée en tant que matrice zéro. Elle prend en charge les opérations avec d'autres matrices et valeurs scalaires, et fournit des méthodes pour accéder aux composants de la matrice et les modifier. Cette matrice est itérable.

Examples:


Equal:
```python
from useful_utility.algebra import Matrix

m: Matrix = Matrix([[1, 2], [3, 4]])
n: Matrix = Matrix([[1, 2], [3, 4]])

print(n == m)
```
```title="output"
True
```


Addition:

```python
from useful_utility.algebra import Matrix

m: Matrix = Matrix([[1, 2], [3, 4]])

print(m + m)
```
```title="output"
[
    [2, 4],
    [6, 8]
]
```



## create_identity_matrix(n=2)`
`classmethod`

Creates an identity matrix of size n x n.

Crée une matrice unité.

default n = 2

Example:
```python
from useful_utility.algebra import Matrix

print(Matrix.create_identity_matrix(2))
```
```title="output"
[
    [1, 0],
    [0, 1]
]
```

## rotation matrix 2D
`classmethod`

Creates a rotation matrix (counterclockwise) for a 2D vector.

Crée une matrice de rotation (anti-horaire) pour un 2D vecteur.

Example:
```python
from useful_utility.algebra import Matrix

print(Matrix.create_rotation_matrix_2D(90))
```
```title="output"
[
    [0, -1],
    [1, 0]
]
```

## rotation matrix 3D
`classmethod`

Creates a rotation matrix (counterclockwise) for a 3D vector.

Crée une matrice de rotation (anti-horaire) pour un 3D vecteur.

An Axis needs to be given:
```python
from useful_utility.algebra import Axis

Axis.X
Axis.Y
Axis.Z
```

Example:
```python
from useful_utility.algebra import Matrix, Axis

print(Matrix.create_rotation_matrix_3D(90, Axis.X))
```
```title="output"
[
    [1, 0, 0],
    [0, 0, -1],
    [0, 1, 0]
]
```


## invers
`classmethod`

Creates the inverse matrix for the matrix.

Crée une matrice inverse pour la matrice.

(only for quadratic matrices)

Example:
```python
from useful_utility.algebra import Matrix

m: Matrix = Matrix([[0, 1], [1, 0]])

print(m.get_invers())
```
```title="output"
[
    [0, 1],
    [1, 0]
]
```