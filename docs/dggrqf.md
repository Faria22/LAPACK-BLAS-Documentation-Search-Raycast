# DGGRQF

## Function Signature

```fortran
DGGRQF(M, P, N, A, LDA, TAUA, B, LDB, TAUB, WORK,
*                          LWORK, INFO)
```

## Description


 DGGRQF computes a generalized RQ factorization of an M-by-N matrix A
 and a P-by-N matrix B:

             A = R*Q,        B = Z*T*Q,

 where Q is an N-by-N orthogonal matrix, Z is a P-by-P orthogonal
 matrix, and R and T assume one of the forms:

 if M <= N,  R = ( 0  R12 ) M,   or if M > N,  R = ( R11 ) M-N,
                  N-M  M                           ( R21 ) N
                                                      N

 where R12 or R21 is upper triangular, and

 if P >= N,  T = ( T11 ) N  ,   or if P < N,  T = ( T11  T12 ) P,
                 (  0  ) P-N                         P   N-P
                    N

 where T11 is upper triangular.

 In particular, if B is square and nonsingular, the GRQ factorization
 of A and B implicitly gives the RQ factorization of A*inv(B):

              A*inv(B) = (R*inv(T))*Z**T

 where inv(B) denotes the inverse of the matrix B, and Z**T denotes the
 transpose of the matrix Z.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### P (in)

P is INTEGER The number of rows of the matrix B. P >= 0.

### N (in)

N is INTEGER The number of columns of the matrices A and B. N >= 0.

### A (in,out)

A is DOUBLE PRECISION array, dimension (LDA,N) On entry, the M-by-N matrix A. On exit, if M <= N, the upper triangle of the subarray A(1:M,N-M+1:N) contains the M-by-M upper triangular matrix R; if M > N, the elements on and above the (M-N)-th subdiagonal contain the M-by-N upper trapezoidal matrix R; the remaining elements, with the array TAUA, represent the orthogonal matrix Q as a product of elementary reflectors (see Further Details).

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### TAUA (out)

TAUA is DOUBLE PRECISION array, dimension (min(M,N)) The scalar factors of the elementary reflectors which represent the orthogonal matrix Q (see Further Details).

### B (in,out)

B is DOUBLE PRECISION array, dimension (LDB,N) On entry, the P-by-N matrix B. On exit, the elements on and above the diagonal of the array contain the min(P,N)-by-N upper trapezoidal matrix T (T is upper triangular if P >= N); the elements below the diagonal, with the array TAUB, represent the orthogonal matrix Z as a product of elementary reflectors (see Further Details).

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,P).

### TAUB (out)

TAUB is DOUBLE PRECISION array, dimension (min(P,N)) The scalar factors of the elementary reflectors which represent the orthogonal matrix Z (see Further Details).

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= max(1,N,M,P). For optimum performance LWORK >= max(N,M,P)*max(NB1,NB2,NB3), where NB1 is the optimal blocksize for the RQ factorization of an M-by-N matrix, NB2 is the optimal blocksize for the QR factorization of a P-by-N matrix, and NB3 is the optimal blocksize for a call of DORMRQ. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INF0= -i, the i-th argument had an illegal value.

