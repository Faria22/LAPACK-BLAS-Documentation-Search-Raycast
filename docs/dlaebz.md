# DLAEBZ

## Function Signature

```fortran
DLAEBZ(IJOB, NITMAX, N, MMAX, MINP, NBMIN, ABSTOL,
*                          RELTOL, PIVMIN, D, E, E2, NVAL, AB, C, MOUT,
*                          NAB, WORK, IWORK, INFO)
```

## Description


 DLAEBZ contains the iteration loops which compute and use the
 function N(w), which is the count of eigenvalues of a symmetric
 tridiagonal matrix T less than or equal to its argument  w.  It
 performs a choice of two types of loops:

 IJOB=1, followed by
 IJOB=2: It takes as input a list of intervals and returns a list of
         sufficiently small intervals whose union contains the same
         eigenvalues as the union of the original intervals.
         The input intervals are (AB(j,1),AB(j,2)], j=1,...,MINP.
         The output interval (AB(j,1),AB(j,2)] will contain
         eigenvalues NAB(j,1)+1,...,NAB(j,2), where 1 <= j <= MOUT.

 IJOB=3: It performs a binary search in each input interval
         (AB(j,1),AB(j,2)] for a point  w(j)  such that
         N(w(j))=NVAL(j), and uses  C(j)  as the starting point of
         the search.  If such a w(j) is found, then on output
         AB(j,1)=AB(j,2)=w.  If no such w(j) is found, then on output
         (AB(j,1),AB(j,2)] will be a small interval containing the
         point where N(w) jumps through NVAL(j), unless that point
         lies outside the initial interval.

 Note that the intervals are in all cases half-open intervals,
 i.e., of the form  (a,b] , which includes  b  but not  a .

 To avoid underflow, the matrix should be scaled so that its largest
 element is no greater than  overflow**(1/2) * underflow**(1/4)
 in absolute value.  To assure the most accurate computation
 of small eigenvalues, the matrix should be scaled to be
 not much smaller than that, either.

 See W. Kahan "Accurate Eigenvalues of a Symmetric Tridiagonal
 Matrix", Report CS41, Computer Science Dept., Stanford
 University, July 21, 1966

 Note: the arguments are, in general, *not* checked for unreasonable
 values.

## Parameters

### IJOB (in)

IJOB is INTEGER Specifies what is to be done: = 1: Compute NAB for the initial intervals. = 2: Perform bisection iteration to find eigenvalues of T. = 3: Perform bisection iteration to invert N(w), i.e., to find a point which has a specified number of eigenvalues of T to its left. Other values will cause DLAEBZ to return with INFO=-1.

### NITMAX (in)

NITMAX is INTEGER The maximum number of "levels" of bisection to be performed, i.e., an interval of width W will not be made smaller than 2^(-NITMAX) * W. If not all intervals have converged after NITMAX iterations, then INFO is set to the number of non-converged intervals.

### N (in)

N is INTEGER The dimension n of the tridiagonal matrix T. It must be at least 1.

### MMAX (in)

MMAX is INTEGER The maximum number of intervals. If more than MMAX intervals are generated, then DLAEBZ will quit with INFO=MMAX+1.

### MINP (in)

MINP is INTEGER The initial number of intervals. It may not be greater than MMAX.

### NBMIN (in)

NBMIN is INTEGER The smallest number of intervals that should be processed using a vector loop. If zero, then only the scalar loop will be used.

### ABSTOL (in)

ABSTOL is DOUBLE PRECISION The minimum (absolute) width of an interval. When an interval is narrower than ABSTOL, or than RELTOL times the larger (in magnitude) endpoint, then it is considered to be sufficiently small, i.e., converged. This must be at least zero.

### RELTOL (in)

RELTOL is DOUBLE PRECISION The minimum relative width of an interval. When an interval is narrower than ABSTOL, or than RELTOL times the larger (in magnitude) endpoint, then it is considered to be sufficiently small, i.e., converged. Note: this should always be at least radix*machine epsilon.

### PIVMIN (in)

PIVMIN is DOUBLE PRECISION The minimum absolute value of a "pivot" in the Sturm sequence loop. This must be at least max |e(j)**2|*safe_min and at least safe_min, where safe_min is at least the smallest number that can divide one without overflow.

### D (in)

D is DOUBLE PRECISION array, dimension (N) The diagonal elements of the tridiagonal matrix T.

### E (in)

E is DOUBLE PRECISION array, dimension (N) The offdiagonal elements of the tridiagonal matrix T in positions 1 through N-1. E(N) is arbitrary.

### E2 (in)

E2 is DOUBLE PRECISION array, dimension (N) The squares of the offdiagonal elements of the tridiagonal matrix T. E2(N) is ignored.

### NVAL (in,out)

NVAL is INTEGER array, dimension (MINP) If IJOB=1 or 2, not referenced. If IJOB=3, the desired values of N(w). The elements of NVAL will be reordered to correspond with the intervals in AB. Thus, NVAL(j) on output will not, in general be the same as NVAL(j) on input, but it will correspond with the interval (AB(j,1),AB(j,2)] on output.

### AB (in,out)

AB is DOUBLE PRECISION array, dimension (MMAX,2) The endpoints of the intervals. AB(j,1) is a(j), the left endpoint of the j-th interval, and AB(j,2) is b(j), the right endpoint of the j-th interval. The input intervals will, in general, be modified, split, and reordered by the calculation.

### C (in,out)

C is DOUBLE PRECISION array, dimension (MMAX) If IJOB=1, ignored. If IJOB=2, workspace. If IJOB=3, then on input C(j) should be initialized to the first search point in the binary search.

### MOUT (out)

MOUT is INTEGER If IJOB=1, the number of eigenvalues in the intervals. If IJOB=2 or 3, the number of intervals output. If IJOB=3, MOUT will equal MINP.

### NAB (in,out)

NAB is INTEGER array, dimension (MMAX,2) If IJOB=1, then on output NAB(i,j) will be set to N(AB(i,j)). If IJOB=2, then on input, NAB(i,j) should be set. It must satisfy the condition: N(AB(i,1)) <= NAB(i,1) <= NAB(i,2) <= N(AB(i,2)), which means that in interval i only eigenvalues NAB(i,1)+1,...,NAB(i,2) will be considered. Usually, NAB(i,j)=N(AB(i,j)), from a previous call to DLAEBZ with IJOB=1. On output, NAB(i,j) will contain max(na(k),min(nb(k),N(AB(i,j)))), where k is the index of the input interval that the output interval (AB(j,1),AB(j,2)] came from, and na(k) and nb(k) are the the input values of NAB(k,1) and NAB(k,2). If IJOB=3, then on output, NAB(i,j) contains N(AB(i,j)), unless N(w) > NVAL(i) for all search points w , in which case NAB(i,1) will not be modified, i.e., the output value will be the same as the input value (modulo reorderings -- see NVAL and AB), or unless N(w) < NVAL(i) for all search points w , in which case NAB(i,2) will not be modified. Normally, NAB should be set to some distinctive value(s) before DLAEBZ is called.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (MMAX) Workspace.

### IWORK (out)

IWORK is INTEGER array, dimension (MMAX) Workspace.

### INFO (out)

INFO is INTEGER = 0: All intervals converged. = 1--MMAX: The last INFO intervals did not converge. = MMAX+1: More than MMAX intervals were generated.

