# decorator
***

## TODO
***
This decorator gives a warning if a not fully implemented function is called, but still executes it.

Ce Décorateur avertit, si une fonction qui n'a pas encore été implémentée en entier est demandée, mais elle
    s'exécute quand même.

Example:
```python
from pylix.errors import TODO

@TODO
def not_done():
    print("I am doing something.")

not_done()
```
```title="output"
<stdin>:7: UserWarning: not_done - TODO: implementation pending.
  not_done()
I am doing something.
```

with custom message:
```python
from pylix.errors import TODO

@TODO("Needs to be refactored.")
def not_done():
    print("I am doing something.")

not_done()
```
```title="output"
<stdin>:7: UserWarning: not_done - TODO: Needs to be refactored.
  not_done()
I am doing something.
```
