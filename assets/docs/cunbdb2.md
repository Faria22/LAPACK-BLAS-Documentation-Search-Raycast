```fortran  
subroutine cunbdb2 (  
m,  
p,  
q,  
x11,  
ldx11,  
x21,  
ldx21,  
theta,  
phi,  
*                           taup1,  
taup2,  
tauq1,  
work,  
lwork,  
info  
)  
```  
  
CUNBDB2 simultaneously bidiagonalizes the blocks of a tall and skinny  
matrix X with orthonormal columns:  
  
[ B11 ]  
[ X11 ]   [ P1 |    ] [  0  ]  
[-----] = [---------] [-----] Q1**T .  
[ X21 ]   [    | P2 ] [ B21 ]  
[  0  ]  
  
X11 is P-by-Q, and X21 is (M-P)-by-Q. P must be no larger than M-P,  
Q, or M-Q. Routines CUNBDB1, CUNBDB3, and CUNBDB4 handle cases in  
which P is not the minimum dimension.  
  
The unitary matrices P1, P2, and Q1 are P-by-P, (M-P)-by-(M-P),  
and (M-Q)-by-(M-Q), respectively. They are represented implicitly by  
Householder vectors.  
  
B11 and B12 are P-by-P bidiagonal matrices represented implicitly by  
angles THETA, PHI.  
  
  
## Parameters  
M : Integer [in]  
> The number of rows X11 plus the number of rows in X21.  
  
P : Integer [in]  
> The number of rows in X11. 0 <= P <= min(M-P,Q,M-Q).  
  
Q : Integer [in]  
> The number of columns in X11 and X21. 0 <= Q <= M.  
  
X11 : Complex Array, Dimension (ldx11,q) [in,out]  
> On entry, the top block of the matrix X to be reduced. On  
> exit, the columns of tril(X11) specify reflectors for P1 and  
> the rows of triu(X11,1) specify reflectors for Q1.  
  
Ldx11 : Integer [in]  
> The leading dimension of X11. LDX11 >= P.  
  
X21 : Complex Array, Dimension (ldx21,q) [in,out]  
> On entry, the bottom block of the matrix X to be reduced. On  
> exit, the columns of tril(X21) specify reflectors for P2.  
  
Ldx21 : Integer [in]  
> The leading dimension of X21. LDX21 >= M-P.  
  
Theta : Real Array, Dimension (q) [out]  
> The entries of the bidiagonal blocks B11, B21 are defined by  
> THETA and PHI. See Further Details.  
  
Phi : Real Array, Dimension (q-1) [out]  
> The entries of the bidiagonal blocks B11, B21 are defined by  
> THETA and PHI. See Further Details.  
  
Taup1 : Complex Array, Dimension (p-1) [out]  
> The scalar factors of the elementary reflectors that define  
> P1.  
  
Taup2 : Complex Array, Dimension (q) [out]  
> The scalar factors of the elementary reflectors that define  
> P2.  
  
Tauq1 : Complex Array, Dimension (q) [out]  
> The scalar factors of the elementary reflectors that define  
> Q1.  
  
Work : Complex Array, Dimension (lwork) [out]  
  
Lwork : Integer [in]  
> The dimension of the array WORK. LWORK >= M-Q.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit.  
> < 0:  if INFO = -i, the i-th argument had an illegal value.  
  
