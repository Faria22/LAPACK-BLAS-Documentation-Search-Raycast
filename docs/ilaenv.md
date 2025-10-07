# ILAENV

## Function Signature

```fortran
ILAENV(ISPEC, NAME, OPTS, N1, N2, N3, N4)
```

## Description


 ILAENV is called from the LAPACK routines to choose problem-dependent
 parameters for the local environment.  See ISPEC for a description of
 the parameters.

 ILAENV returns an INTEGER
 if ILAENV >= 0: ILAENV returns the value of the parameter specified by ISPEC
 if ILAENV < 0:  if ILAENV = -k, the k-th argument had an illegal value.

 This version provides a set of parameters which should give good,
 but not optimal, performance on many of the currently available
 computers.  Users are encouraged to modify this subroutine to set
 the tuning parameters for their particular machine using the option
 and problem size information in the arguments.

 This routine will not function correctly if it is converted to all
 lower case.  Converting it to all upper case is allowed.

## Parameters

### ISPEC (in)

ISPEC is INTEGER Specifies the parameter to be returned as the value of ILAENV. = 1: the optimal blocksize; if this value is 1, an unblocked algorithm will give the best performance. = 2: the minimum block size for which the block routine should be used; if the usable block size is less than this value, an unblocked routine should be used. = 3: the crossover point (in a block routine, for N less than this value, an unblocked routine should be used) = 4: the number of shifts, used in the nonsymmetric eigenvalue routines (DEPRECATED) = 5: the minimum column dimension for blocking to be used; rectangular blocks must have dimension at least k by m, where k is given by ILAENV(2,...) and m by ILAENV(5,...) = 6: the crossover point for the SVD (when reducing an m by n matrix to bidiagonal form, if max(m,n)/min(m,n) exceeds this value, a QR factorization is used first to reduce the matrix to a triangular form.) = 7: the number of processors = 8: the crossover point for the multishift QR method for nonsymmetric eigenvalue problems (DEPRECATED) = 9: maximum size of the subproblems at the bottom of the computation tree in the divide-and-conquer algorithm (used by xGELSD and xGESDD) =10: ieee infinity and NaN arithmetic can be trusted not to trap =11: infinity arithmetic can be trusted not to trap 12 <= ISPEC <= 17: xHSEQR or related subroutines, see IPARMQ for detailed explanation

### NAME (in)

NAME is CHARACTER*(*) The name of the calling subroutine, in either upper case or lower case.

### OPTS (in)

OPTS is CHARACTER*(*) The character options to the subroutine NAME, concatenated into a single character string. For example, UPLO = 'U', TRANS = 'T', and DIAG = 'N' for a triangular routine would be specified as OPTS = 'UTN'.

### N1 (in)

N1 is INTEGER

### N2 (in)

N2 is INTEGER

### N3 (in)

N3 is INTEGER

### N4 (in)

N4 is INTEGER Problem dimensions for the subroutine NAME; these may not all be required.

