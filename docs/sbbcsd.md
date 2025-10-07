# SBBCSD

## Function Signature

```fortran
SBBCSD(JOBU1, JOBU2, JOBV1T, JOBV2T, TRANS, M, P, Q,
*                          THETA, PHI, U1, LDU1, U2, LDU2, V1T, LDV1T,
*                          V2T, LDV2T, B11D, B11E, B12D, B12E, B21D, B21E,
*                          B22D, B22E, WORK, LWORK, INFO)
```

## Description


 SBBCSD computes the CS decomposition of an orthogonal matrix in
 bidiagonal-block form,


     [ B11 | B12 0  0 ]
     [  0  |  0 -I  0 ]
 X = [----------------]
     [ B21 | B22 0  0 ]
     [  0  |  0  0  I ]

                               [  C | -S  0  0 ]
                   [ U1 |    ] [  0 |  0 -I  0 ] [ V1 |    ]**T
                 = [---------] [---------------] [---------]   .
                   [    | U2 ] [  S |  C  0  0 ] [    | V2 ]
                               [  0 |  0  0  I ]

 X is M-by-M, its top-left block is P-by-Q, and Q must be no larger
 than P, M-P, or M-Q. (If Q is not the smallest index, then X must be
 transposed and/or permuted. This can be done in constant time using
 the TRANS and SIGNS options. See SORCSD for details.)

 The bidiagonal matrices B11, B12, B21, and B22 are represented
 implicitly by angles THETA(1:Q) and PHI(1:Q-1).

 The orthogonal matrices U1, U2, V1T, and V2T are input/output.
 The input matrices are pre- or post-multiplied by the appropriate
 singular vector matrices.

## Parameters

### JOBU1 (in)

JOBU1 is CHARACTER = 'Y': U1 is updated; otherwise: U1 is not updated.

### JOBU2 (in)

JOBU2 is CHARACTER = 'Y': U2 is updated; otherwise: U2 is not updated.

### JOBV1T (in)

JOBV1T is CHARACTER = 'Y': V1T is updated; otherwise: V1T is not updated.

### JOBV2T (in)

JOBV2T is CHARACTER = 'Y': V2T is updated; otherwise: V2T is not updated.

### TRANS (in)

TRANS is CHARACTER = 'T': X, U1, U2, V1T, and V2T are stored in row-major order; otherwise: X, U1, U2, V1T, and V2T are stored in column- major order.

### M (in)

M is INTEGER The number of rows and columns in X, the orthogonal matrix in bidiagonal-block form.

### P (in)

P is INTEGER The number of rows in the top-left block of X. 0 <= P <= M.

### Q (in)

Q is INTEGER The number of columns in the top-left block of X. 0 <= Q <= MIN(P,M-P,M-Q).

### THETA (in,out)

THETA is REAL array, dimension (Q) On entry, the angles THETA(1),...,THETA(Q) that, along with PHI(1), ...,PHI(Q-1), define the matrix in bidiagonal-block form. On exit, the angles whose cosines and sines define the diagonal blocks in the CS decomposition.

### PHI (in,out)

PHI is REAL array, dimension (Q-1) The angles PHI(1),...,PHI(Q-1) that, along with THETA(1),..., THETA(Q), define the matrix in bidiagonal-block form.

### U1 (in,out)

U1 is REAL array, dimension (LDU1,P) On entry, a P-by-P matrix. On exit, U1 is postmultiplied by the left singular vector matrix common to [ B11 ; 0 ] and [ B12 0 0 ; 0 -I 0 0 ].

### LDU1 (in)

LDU1 is INTEGER The leading dimension of the array U1, LDU1 >= MAX(1,P).

### U2 (in,out)

U2 is REAL array, dimension (LDU2,M-P) On entry, an (M-P)-by-(M-P) matrix. On exit, U2 is postmultiplied by the left singular vector matrix common to [ B21 ; 0 ] and [ B22 0 0 ; 0 0 I ].

### LDU2 (in)

LDU2 is INTEGER The leading dimension of the array U2, LDU2 >= MAX(1,M-P).

### V1T (in,out)

V1T is REAL array, dimension (LDV1T,Q) On entry, a Q-by-Q matrix. On exit, V1T is premultiplied by the transpose of the right singular vector matrix common to [ B11 ; 0 ] and [ B21 ; 0 ].

### LDV1T (in)

LDV1T is INTEGER The leading dimension of the array V1T, LDV1T >= MAX(1,Q).

### V2T (in,out)

V2T is REAL array, dimension (LDV2T,M-Q) On entry, an (M-Q)-by-(M-Q) matrix. On exit, V2T is premultiplied by the transpose of the right singular vector matrix common to [ B12 0 0 ; 0 -I 0 ] and [ B22 0 0 ; 0 0 I ].

### LDV2T (in)

LDV2T is INTEGER The leading dimension of the array V2T, LDV2T >= MAX(1,M-Q).

### B11D (out)

B11D is REAL array, dimension (Q) When SBBCSD converges, B11D contains the cosines of THETA(1), ..., THETA(Q). If SBBCSD fails to converge, then B11D contains the diagonal of the partially reduced top-left block.

### B11E (out)

B11E is REAL array, dimension (Q-1) When SBBCSD converges, B11E contains zeros. If SBBCSD fails to converge, then B11E contains the superdiagonal of the partially reduced top-left block.

### B12D (out)

B12D is REAL array, dimension (Q) When SBBCSD converges, B12D contains the negative sines of THETA(1), ..., THETA(Q). If SBBCSD fails to converge, then B12D contains the diagonal of the partially reduced top-right block.

### B12E (out)

B12E is REAL array, dimension (Q-1) When SBBCSD converges, B12E contains zeros. If SBBCSD fails to converge, then B12E contains the subdiagonal of the partially reduced top-right block.

### B21D (out)

B21D is REAL array, dimension (Q) When SBBCSD converges, B21D contains the negative sines of THETA(1), ..., THETA(Q). If SBBCSD fails to converge, then B21D contains the diagonal of the partially reduced bottom-left block.

### B21E (out)

B21E is REAL array, dimension (Q-1) When SBBCSD converges, B21E contains zeros. If SBBCSD fails to converge, then B21E contains the subdiagonal of the partially reduced bottom-left block.

### B22D (out)

B22D is REAL array, dimension (Q) When SBBCSD converges, B22D contains the negative sines of THETA(1), ..., THETA(Q). If SBBCSD fails to converge, then B22D contains the diagonal of the partially reduced bottom-right block.

### B22E (out)

B22E is REAL array, dimension (Q-1) When SBBCSD converges, B22E contains zeros. If SBBCSD fails to converge, then B22E contains the subdiagonal of the partially reduced bottom-right block.

### WORK (out)

WORK is REAL array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= MAX(1,8*Q). If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the work array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value. > 0: if SBBCSD did not converge, INFO specifies the number of nonzero entries in PHI, and B11D, B11E, etc., contain the partially reduced matrix.

