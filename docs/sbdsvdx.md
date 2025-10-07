# SBDSVDX

## Function Signature

```fortran
SBDSVDX(UPLO, JOBZ, RANGE, N, D, E, VL, VU, IL, IU,
*    $                    NS, S, Z, LDZ, WORK, IWORK, INFO)
```

## Description


  SBDSVDX computes the singular value decomposition (SVD) of a real
  N-by-N (upper or lower) bidiagonal matrix B, B = U * S * VT,
  where S is a diagonal matrix with non-negative diagonal elements
  (the singular values of B), and U and VT are orthogonal matrices
  of left and right singular vectors, respectively.

  Given an upper bidiagonal B with diagonal D = [ d_1 d_2 ... d_N ]
  and superdiagonal E = [ e_1 e_2 ... e_N-1 ], SBDSVDX computes the
  singular value decomposition of B through the eigenvalues and
  eigenvectors of the N*2-by-N*2 tridiagonal matrix

        |  0  d_1                |
        | d_1  0  e_1            |
  TGK = |     e_1  0  d_2        |
        |         d_2  .   .     |
        |              .   .   . |

  If (s,u,v) is a singular triplet of B with ||u|| = ||v|| = 1, then
  (+/-s,q), ||q|| = 1, are eigenpairs of TGK, with q = P * ( u' +/-v' ) /
  sqrt(2) = ( v_1 u_1 v_2 u_2 ... v_n u_n ) / sqrt(2), and
  P = [ e_{n+1} e_{1} e_{n+2} e_{2} ... ].

  Given a TGK matrix, one can either a) compute -s,-v and change signs
  so that the singular values (and corresponding vectors) are already in
  descending order (as in SGESVD/SGESDD) or b) compute s,v and reorder
  the values (and corresponding vectors). SBDSVDX implements a) by
  calling SSTEVX (bisection plus inverse iteration, to be replaced
  with a version of the Multiple Relative Robust Representation
  algorithm. (See P. Willems and B. Lang, A framework for the MR^3
  algorithm: theory and implementation, SIAM J. Sci. Comput.,
  35:740-766, 2013.)

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': B is upper bidiagonal; = 'L': B is lower bidiagonal.

### JOBZ (in)

JOBZ is CHARACTER*1 = 'N': Compute singular values only; = 'V': Compute singular values and singular vectors.

### RANGE (in)

RANGE is CHARACTER*1 = 'A': all singular values will be found. = 'V': all singular values in the half-open interval [VL,VU) will be found. = 'I': the IL-th through IU-th singular values will be found.

### N (in)

N is INTEGER The order of the bidiagonal matrix. N >= 0.

### D (in)

D is REAL array, dimension (N) The n diagonal elements of the bidiagonal matrix B.

### E (in)

E is REAL array, dimension (max(1,N-1)) The (n-1) superdiagonal elements of the bidiagonal matrix B in elements 1 to N-1.

### VL (in)

VL is REAL If RANGE='V', the lower bound of the interval to be searched for singular values. VU > VL. Not referenced if RANGE = 'A' or 'I'.

### VU (in)

VU is REAL If RANGE='V', the upper bound of the interval to be searched for singular values. VU > VL. Not referenced if RANGE = 'A' or 'I'.

### IL (in)

IL is INTEGER If RANGE='I', the index of the smallest singular value to be returned. 1 <= IL <= IU <= min(M,N), if min(M,N) > 0. Not referenced if RANGE = 'A' or 'V'.

### IU (in)

IU is INTEGER If RANGE='I', the index of the largest singular value to be returned. 1 <= IL <= IU <= min(M,N), if min(M,N) > 0. Not referenced if RANGE = 'A' or 'V'.

### NS (out)

NS is INTEGER The total number of singular values found. 0 <= NS <= N. If RANGE = 'A', NS = N, and if RANGE = 'I', NS = IU-IL+1.

### S (out)

S is REAL array, dimension (N) The first NS elements contain the selected singular values in ascending order.

### Z (out)

Z is REAL array, dimension (2*N,K) If JOBZ = 'V', then if INFO = 0 the first NS columns of Z contain the singular vectors of the matrix B corresponding to the selected singular values, with U in rows 1 to N and V in rows N+1 to N*2, i.e. Z = [ U ] [ V ] If JOBZ = 'N', then Z is not referenced. Note: The user must ensure that at least K = NS+1 columns are supplied in the array Z; if RANGE = 'V', the exact value of NS is not known in advance and an upper bound must be used.

### LDZ (in)

LDZ is INTEGER The leading dimension of the array Z. LDZ >= 1, and if JOBZ = 'V', LDZ >= max(2,N*2).

### WORK (out)

WORK is REAL array, dimension (14*N)

### IWORK (out)

IWORK is INTEGER array, dimension (12*N) If JOBZ = 'V', then if INFO = 0, the first NS elements of IWORK are zero. If INFO > 0, then IWORK contains the indices of the eigenvectors that failed to converge in DSTEVX.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, then i eigenvectors failed to converge in SSTEVX. The indices of the eigenvectors (as returned by SSTEVX) are stored in the array IWORK. if INFO = N*2 + 1, an internal error occurred.

