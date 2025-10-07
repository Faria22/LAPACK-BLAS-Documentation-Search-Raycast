```fortran
subroutine slabad (
		real small,
		real large
)
```

 SLABAD is a no-op and kept for compatibility reasons. It used
 to correct the overflow/underflow behavior of machines that
 are not IEEE-754 compliant.

## Parameters
Small : Real [in,out]
> On entry, the underflow threshold as computed by SLAMCH.
> On exit, the unchanged value SMALL.

Large : Real [in,out]
> On entry, the overflow threshold as computed by SLAMCH.
> On exit, the unchanged value LARGE.

