# SORHR_COL

## Function Signature

```fortran
SORHR_COL(M, N, NB, A, LDA, T, LDT, D, INFO)
```

## Description


  SORHR_COL takes an M-by-N real matrix Q_in with orthonormal columns
  as input, stored in A, and performs Householder Reconstruction (HR),
  i.e. reconstructs Householder vectors V(i) implicitly representing
  another M-by-N matrix Q_out, with the property that Q_in = Q_out*S,
  where S is an N-by-N diagonal matrix with diagonal entries
  equal to +1 or -1. The Householder vectors (columns V(i) of V) are
  stored in A on output, and the diagonal entries of S are stored in D.
  Block reflectors are also returned in T
  (same output format as SGEQRT).

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. M >= N >= 0.

### NB (in)

NB is INTEGER The column block size to be used in the reconstruction of Householder column vector blocks in the array A and corresponding block reflectors in the array T. NB >= 1. (Note that if NB > N, then N is used instead of NB as the column block size.)

### A (in,out)

A is REAL array, dimension (LDA,N) On entry: The array A contains an M-by-N orthonormal matrix Q_in, i.e the columns of A are orthogonal unit vectors. On exit: The elements below the diagonal of A represent the unit lower-trapezoidal matrix V of Householder column vectors V(i). The unit diagonal entries of V are not stored (same format as the output below the diagonal in A from SGEQRT). The matrix T and the matrix V stored on output in A implicitly define Q_out. The elements above the diagonal contain the factor U of the "modified" LU-decomposition: Q_in - ( S ) = V * U ( 0 ) where 0 is a (M-N)-by-(M-N) zero matrix.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### T (out)

T is REAL array, dimension (LDT, N) Let NOCB = Number_of_output_col_blocks = CEIL(N/NB) On exit, T(1:NB, 1:N) contains NOCB upper-triangular block reflectors used to define Q_out stored in compact form as a sequence of upper-triangular NB-by-NB column blocks (same format as the output T in SGEQRT). The matrix T and the matrix V stored on output in A implicitly define Q_out. NOTE: The lower triangles below the upper-triangular blocks will be filled with zeros. See Further Details.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= max(1,min(NB,N)).

### D (out)

D is REAL array, dimension min(M,N). The elements can be only plus or minus one. D(i) is constructed as D(i) = -SIGN(Q_in_i(i,i)), where 1 <= i <= min(M,N), and Q_in_i is Q_in after performing i-1 steps of âmodifiedâ Gaussian elimination. See Further Details.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value

