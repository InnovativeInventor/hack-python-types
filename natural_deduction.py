from types import NotImplementedType
from typing import Callable, TypeVar, Tuple, Union
import types
from enum import Enum

P = TypeVar("P")
Q = TypeVar("Q")
R = TypeVar("R")
A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")
D = TypeVar("D")

"""
Hacking Python's Type System for (constructive) Propositional Proof Checking;
or, Constructive, Propositional Theorem Proving in Python's Type System with BHK

Some notes:
`raise` and `pass` are like "admit" or "assume" in a standard theorem prover
we cannot implement `NotImplementedType` without `raise` or `pass` (or stubs)
so we will treat the NotImplementedType as our bottom type. `Any` will be 
our top type.

Python's type system, by itself, produces a *very* weak logic. Several
statements are admitted as axioms 
"""

## Modus Ponens
def modus_ponens(a: A, f: Callable[[A], B]) -> B:
    """
    Given:
        - A
        - A -> B
    then:
        - B
    for any statements A, B, C.
    """
    return f(a)


# This is how we admit an inference rule without providing a corresponding implementation
# def contrapositive(
#     p_implies_q: Callable[[P], Q]
# ) -> Callable[[Callable[[Q], NotImplementedType]], Callable[[P], NotImplementedType]]:
#     ...

# Luckily, we have a proof for the contrapositive
def contrapositive(
    p_implies_q: Callable[[P], Q]
) -> Callable[[Callable[[Q], NotImplementedType]], Callable[[P], NotImplementedType]]:
    def transform_proof_of_not_q(
        not_q: Callable[[Q], NotImplementedType]
    ) -> Callable[[P], NotImplementedType]:
        def proof_not_p(P) -> NotImplementedType:
            return not_q(p_implies_q(P))

        return proof_not_p

    return transform_proof_of_not_q

def modus_tollens(
    p_implies_q: Callable[[P], Q], not_q: Callable[[Q], NotImplementedType]
) -> Callable[[P], NotImplementedType]:
    """
    Given:
        - P -> Q
        - not Q
    then:
        - not P
    for any statements P, Q.
    """
    return contrapositive(p_implies_q)(not_q)


# def modus_tollendo_ponens_1(p_or_q: Union[Tuple[P, None], Tuple[None, Q]], f: Callable[[P], NotImplementedType]) -> Q: ...
# def modus_tollendo_ponens_2(p_or_q: Union[Tuple[P, None], Tuple[None, Q]], f: Callable[[Q], NotImplementedType]) -> P: ...
def modus_tollendo_ponens_1(
    p_or_q: Union[P, Q], f: Callable[[P], NotImplementedType]
) -> Q:
    ...


def modus_tollendo_ponens_2(
    p_or_q: Union[P, Q], f: Callable[[Q], NotImplementedType]
) -> P:
    ...


## Proof of transitivity of logical implication
def transitive_implication(
    f: Callable[[A], B], g: Callable[[B], C]
) -> Callable[[A], C]:
    """
    Given:
        - A->B
        - B->C
    then:
        A->C
    for any statements A, B, C.
    """

    def a_implies_c(a: A) -> C:
        return g(f(a))

    return a_implies_c


def conjunction_elimination_1(p_and_q: Tuple[P, Q]) -> P:
    """
    Given:
        - P and Q
    then:
        - P
    for any statements P, Q.
    """
    return p_and_q[0]


def conjunction_elimination_2(p_and_q: Tuple[P, Q]) -> Q:
    """
    Given:
        - P and Q
    then:
        - Q
    for any statements P, Q.
    """
    return p_and_q[1]


def conjunction_introduction(p: P, q: Q) -> Tuple[P, Q]:
    """
    Given:
        - P
        - Q
    then:
        - P and Q
    for any statements P, Q.
    """
    return (p, q)


def disjunction_introduction(p: P) -> Union[P, Q]:
    return p

# Unfortunately, I have been unable to prove this in Python's type system thus far
def constructive_dilemma(
    p: Tuple[Callable[[A], B], Callable[[C], D]], a_or_c: Union[A, C]
) -> Union[B, D]:
    ...

## But hey, this proof fails (mypy will throw an error!)
# def invalid_transitivity_proof(f: Callable[[A], B], g: Callable[[B], C]) -> Callable[[A], D]:
#     """
#     Proof that if:
#         - A->B
#         - B->C
#     then:
#         A->D
#     for any statements A, B, C, D.
#     """
#     def a_implies_c(a: A) -> D:
#         return g(f(a))
#     return a_implies_c

# More proofs to come!
