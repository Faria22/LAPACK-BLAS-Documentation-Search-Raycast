# SLAGTS

## Function Signature

```fortran
SLAGTS(JOB, N, A, B, C, D, IN, Y, TOL, INFO)
```

## Description


 SLAGTS may be used to solve one of the systems of equations

    (T - lambda*I)*x = y   or   (T - lambda*I)**T*x = y,

 where T is an n by n tridiagonal matrix, for x, following the
 factorization of (T - lambda*I) as

    (T - lambda*I) = P*L*U ,

 by routine SLAGTF. The choice of equation to be solved is
 controlled by the argument JOB, and in each case there is an option
 to perturb zero or very small diagonal elements of U, this option
 being intended for use in applications such as inverse iteration.

## Parameters

### JOB (in)

JOB is INTEGER Specifies the job to be performed by SLAGTS as follows: = 1: The equations (T - lambda*I)x = y are to be solved, but diagonal elements of U are not to be perturbed. = -1: The equations (T - lambda*I)x = y are to be solved and, if overflow would otherwise occur, the diagonal elements of U are to be perturbed. See argument TOL below. = 2: The equations (T - lambda*I)**Tx = y are to be solved, but diagonal elements of U are not to be perturbed. = -2: The equations (T - lambda*I)**Tx = y are to be solved and, if overflow would otherwise occur, the diagonal elements of U are to be perturbed. See argument TOL below.

### N (in)

N is INTEGER The order of the matrix T.

### A (in)

A is REAL array, dimension (N) On entry, A must contain the diagonal elements of U as returned from SLAGTF.

### B (in)

B is REAL array, dimension (N-1) On entry, B must contain the first super-diagonal elements of U as returned from SLAGTF.

### C (in)

C is REAL array, dimension (N-1) On entry, C must contain the sub-diagonal elements of L as returned from SLAGTF.

### D (in)

D is REAL array, dimension (N-2) On entry, D must contain the second super-diagonal elements of U as returned from SLAGTF.

### IN (in)

IN is INTEGER array, dimension (N) On entry, IN must contain details of the matrix P as returned from SLAGTF.

### Y (in,out)

Y is REAL array, dimension (N) On entry, the right hand side vector y. On exit, Y is overwritten by the solution vector x.

### TOL (in,out)

TOL is REAL On entry, with JOB < 0, TOL should be the minimum perturbation to be made to very small diagonal elements of U. TOL should normally be chosen as about eps*norm(U), where eps is the relative machine precision, but if TOL is supplied as non-positive, then it is reset to eps*max( abs( u(i,j) ) ). If JOB > 0 then TOL is not referenced. On exit, TOL is changed as described above, only if TOL is non-positive on entry. Otherwise TOL is unchanged.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: overflow would occur when computing the INFO(th) element of the solution vector x. This can only occur when JOB is supplied as positive and either means that a diagonal element of U is very small, or that the elements of the right-hand side vector y are very large.

