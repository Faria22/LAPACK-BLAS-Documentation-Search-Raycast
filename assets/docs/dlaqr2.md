```fortran  
subroutine dlaqr2 (  
wantt,  
wantz,  
n,  
ktop,  
kbot,  
nw,  
h,  
ldh,  
iloz,  
*                          ihiz,  
z,  
ldz,  
ns,  
nd,  
sr,  
si,  
v,  
ldv,  
nh,  
t,  
*                          ldt,  
nv,  
wv,  
ldwv,  
work,  
lwork  
)  
```  
  
DLAQR2 is identical to DLAQR3 except that it avoids  
recursion by calling DLAHQR instead of DLAQR4.  
  
Aggressive early deflation:  
  
This subroutine accepts as input an upper Hessenberg matrix  
H and performs an orthogonal similarity transformation  
designed to detect and deflate fully converged eigenvalues from  
a trailing principal submatrix.  On output H has been over-  
written by a new Hessenberg matrix that is a perturbation of  
an orthogonal similarity transformation of H.  It is to be  
hoped that the final version of H has many zero subdiagonal  
entries.  
  
## Parameters  
Wantt : Logical [in]  
> If .TRUE., then the Hessenberg matrix H is fully updated  
> so that the quasi-triangular Schur factor may be  
> computed (in cooperation with the calling subroutine).  
> If .FALSE., then only enough of H is updated to preserve  
> the eigenvalues.  
  
Wantz : Logical [in]  
> If .TRUE., then the orthogonal matrix Z is updated so  
> so that the orthogonal Schur factor may be computed  
> (in cooperation with the calling subroutine).  
> If .FALSE., then Z is not referenced.  
  
N : Integer [in]  
> The order of the matrix H and (if WANTZ is .TRUE.) the  
> order of the orthogonal matrix Z.  
  
Ktop : Integer [in]  
> It is assumed that either KTOP = 1 or H(KTOP,KTOP-1)=0.  
> KBOT and KTOP together determine an isolated block  
> along the diagonal of the Hessenberg matrix.  
  
Kbot : Integer [in]  
> It is assumed without a check that either  
> KBOT = N or H(KBOT+1,KBOT)=0.  KBOT and KTOP together  
> determine an isolated block along the diagonal of the  
> Hessenberg matrix.  
  
Nw : Integer [in]  
> Deflation window size.  1 <= NW <= (KBOT-KTOP+1).  
  
H : Double Precision Array, Dimension (ldh,n) [in,out]  
> On input the initial N-by-N section of H stores the  
> Hessenberg matrix undergoing aggressive early deflation.  
> On output H has been transformed by an orthogonal  
> similarity transformation, perturbed, and the returned  
> to Hessenberg form that (it is to be hoped) has some  
> zero subdiagonal entries.  
  
Ldh : Integer [in]  
> Leading dimension of H just as declared in the calling  
> subroutine.  N <= LDH  
  
Iloz : Integer [in]  
  
Ihiz : Integer [in]  
> Specify the rows of Z to which transformations must be  
> applied if WANTZ is .TRUE.. 1 <= ILOZ <= IHIZ <= N.  
  
Z : Double Precision Array, Dimension (ldz,n) [in,out]  
> IF WANTZ is .TRUE., then on output, the orthogonal  
> similarity transformation mentioned above has been  
> accumulated into Z(ILOZ:IHIZ,ILOZ:IHIZ) from the right.  
> If WANTZ is .FALSE., then Z is unreferenced.  
  
Ldz : Integer [in]  
> The leading dimension of Z just as declared in the  
> calling subroutine.  1 <= LDZ.  
  
Ns : Integer [out]  
> The number of unconverged (ie approximate) eigenvalues  
> returned in SR and SI that may be used as shifts by the  
> calling subroutine.  
  
Nd : Integer [out]  
> The number of converged eigenvalues uncovered by this  
> subroutine.  
  
Sr : Double Precision Array, Dimension (kbot) [out]  
  
Si : Double Precision Array, Dimension (kbot) [out]  
> On output, the real and imaginary parts of approximate  
> eigenvalues that may be used for shifts are stored in  
> SR(KBOT-ND-NS+1) through SR(KBOT-ND) and  
> SI(KBOT-ND-NS+1) through SI(KBOT-ND), respectively.  
> The real and imaginary parts of converged eigenvalues  
> are stored in SR(KBOT-ND+1) through SR(KBOT) and  
> SI(KBOT-ND+1) through SI(KBOT), respectively.  
  
V : Double Precision Array, Dimension (ldv,nw) [out]  
> An NW-by-NW work array.  
  
Ldv : Integer [in]  
> The leading dimension of V just as declared in the  
> calling subroutine.  NW <= LDV  
  
Nh : Integer [in]  
> The number of columns of T.  NH >= NW.  
  
T : Double Precision Array, Dimension (ldt,nw) [out]  
  
Ldt : Integer [in]  
> The leading dimension of T just as declared in the  
> calling subroutine.  NW <= LDT  
  
Nv : Integer [in]  
> The number of rows of work array WV available for  
> workspace.  NV >= NW.  
  
Wv : Double Precision Array, Dimension (ldwv,nw) [out]  
  
Ldwv : Integer [in]  
> The leading dimension of W just as declared in the  
> calling subroutine.  NW <= LDV  
  
Work : Double Precision Array, Dimension (lwork) [out]  
> On exit, WORK(1) is set to an estimate of the optimal value  
> of LWORK for the given values of N, NW, KTOP and KBOT.  
  
Lwork : Integer [in]  
> suffices, but greater efficiency may result from larger  
> values of LWORK.  
> If LWORK = -1, then a workspace query is assumed; DLAQR2  
> only estimates the optimal workspace size for the given  
> values of N, NW, KTOP and KBOT.  The estimate is returned  
> in WORK(1).  No error message related to LWORK is issued  
> by XERBLA.  Neither H nor Z are accessed.  
  
