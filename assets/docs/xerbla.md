```fortran  
subroutine xerbla (  
srname,  
integer info  
)  
```  
  
XERBLA  is an error handler for the LAPACK routines.  
It is called by an LAPACK routine if an input parameter has an  
invalid value.  A message is printed and execution stops.  
  
Installers may consider modifying the STOP statement in order to  
call system-specific exception-handling facilities.  
  
## Parameters  
Srname : Character*(*) [in]  
> The name of the routine which called XERBLA.  
  
Info : Integer [in]  
> The position of the invalid parameter in the parameter list  
> of the calling routine.  
  
