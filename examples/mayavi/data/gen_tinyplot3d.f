c gen_tinyplot3d - generate little Plot3D files
c
c
c Copyright (c) 2006 Francesco Poli <frx@firenze.linux.it>
c 
c Permission is hereby granted, free of charge, to any person obtaining
c a copy of this software and associated documentation files (the
c "Software"), to deal in the Software without restriction, including
c without limitation the rights to use, copy, modify, merge, publish,
c distribute, sublicense, and/or sell copies of the Software, and to
c permit persons to whom the Software is furnished to do so, subject to
c the following conditions:
c 
c The above copyright notice and this permission notice shall be
c included in all copies or substantial portions of the Software.
c 
c THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
c EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
c MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
c IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
c CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
c TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
c SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


      program main


c     constant definitions:

      integer imm,jmm,kmm,ngrid
      parameter (imm=2,jmm=2,kmm=2,ngrid=5)


c     variable declarations:

      character*32 filenm
      integer i,j,k,nx,igrid
      real x(imm,jmm,kmm),y(imm,jmm,kmm),z(imm,jmm,kmm)
      real ga,rgas,ro,wx,wy,wz,p,q(5)
      real fsmach,alpha,re,time


c     generate mesh and solution:

      do 10 k = 1, kmm
      do 10 j = 1, jmm
      do 10 i = 1, imm
        x(i,j,k) = real(i)
        y(i,j,k) = real(j)
        z(i,j,k) = real(k)
 10   continue

      ga   = 1.4
      rgas = 1.0

      ro = 0.9
      wx = 1.3
      wy = 1.2
      wz = 1.1
      p  = 2.3
      q(1) = ro
      q(2) = ro*wx
      q(3) = ro*wy
      q(4) = ro*wz
      q(5) = p/(ga - 1.0) + 0.5*ro*(wx**2 + wy**2 + wz**2)
      

c     write out 3D mesh Plot3D file:

      filenm = 'tiny.xyz'
      open (unit=1,file=filenm,form='unformatted')
      rewind 1
      write(1) ngrid
      write(1) (imm,jmm,kmm, igrid=1,ngrid)
      do 80 igrid = 1, ngrid
        write(1)
     $  (((x(i,j,k) + (igrid - 1.0),
     $     i=1,imm), j=1,jmm), k=1,kmm),
     $  (((y(i,j,k),
     $     i=1,imm), j=1,jmm), k=1,kmm),
     $  (((z(i,j,k),
     $     i=1,imm), j=1,jmm), k=1,kmm)
 80   continue
      close(unit=1)


c     write out 3D solution Plot3D file:

      filenm = 'tiny.q'
      fsmach = 0.5
      alpha  = 0.0
      re     = 1.0e5
      time   = 0.0
      open (unit=1,file=filenm,form='unformatted')
      rewind 1
      write(1) ngrid
      write(1) (imm,jmm,kmm, igrid=1,ngrid)
      do 90 igrid = 1, ngrid
        write(1) fsmach,alpha,re,time
        write(1)
     $  ((((q(nx),
     $      i=1,imm), j=1,jmm), k=1,kmm), nx=1,5)
 90   continue
      close(unit=1)


      stop
      end
