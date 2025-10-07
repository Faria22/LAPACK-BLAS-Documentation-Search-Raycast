```fortran  
subroutine dlasv2 (  
double precision f,  
double precision g,  
double precision h,  
double precision ssmin,  
double precision ssmax,  
double precision snr,  
double precision csr,  
double precision snl,  
double precision csl  
)  
```  
  
DLASV2 computes the singular value decomposition of a 2-by-2  
triangular matrix  
[  F   G  ]  
[  0   H  ].  
On return, abs(SSMAX) is the larger singular value, abs(SSMIN) is the  
smaller singular value, and (CSL,SNL) and (CSR,SNR) are the left and  
right singular vectors for abs(SSMAX), giving the decomposition  
  
[ CSL  SNL ] [  F   G  ] [ CSR -SNR ]  =  [ SSMAX   0   ]  
[-SNL  CSL ] [  0   H  ] [ SNR  CSR ]     [  0    SSMIN ].  
  
## Parameters  
F : Double Precision [in]  
> The (1,1) element of the 2-by-2 matrix.  
  
G : Double Precision [in]  
> The (1,2) element of the 2-by-2 matrix.  
  
H : Double Precision [in]  
> The (2,2) element of the 2-by-2 matrix.  
  
Ssmin : Double Precision [out]  
> abs(SSMIN) is the smaller singular value.  
  
Ssmax : Double Precision [out]  
> abs(SSMAX) is the larger singular value.  
  
Snl : Double Precision [out]  
  
Csl : Double Precision [out]  
> The vector (CSL, SNL) is a unit left singular vector for the  
> singular value abs(SSMAX).  
  
Snr : Double Precision [out]  
  
Csr : Double Precision [out]  
> The vector (CSR, SNR) is a unit right singular vector for the  
> singular value abs(SSMAX).  
  
