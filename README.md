## hack-python-types
This repo contains the code and fully type-checkable proofs for various natural deduction inference rules in Python's type system.
It is intended to accompany [my blog post on the hacking Python's type system](https://max.fan/posts/hacking-python-types/).

You can see the corresponding proofs at [`/natural_deduction.py`](/natural_deduction.py).

To type-check the proofs yourself, run:
```
mypy .
```

See [https://max.fan/posts/hacking-python-types/](https://max.fan/posts/hacking-python-types/) for more.

## Contents
This repo proves the following natural deduction rules in Python's type system:
- modus ponens
- contrapositive
- modus tollens
- transitive implication (if A implies B and B implies C, then A implies C)
- conjunction introduction
- conjunction elimination
- disjunction introduction

Additionally, type definitions/stubs are given for:
- modus tollendo ponens (admitted as axiom -- not proven yet)
- constructive dilemma (admitted as axiom -- not proven yet)

Feedback is welcome.
