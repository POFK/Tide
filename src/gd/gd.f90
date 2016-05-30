program gd
implicit none

integer(4),parameter::L=1024
character(5),parameter::z_string='1.000'
!character(100)::inden='../'//z_string//'denfss1.25_c0.5.bin'
!character(100)::outden='../'//z_string//'denfss1.25gd_c0.5.bin'
character(100)::inerf='iderf.txt'

integer(4),parameter::L1d=L*L*L
real(4),allocatable::den(:,:,:)
real(4),allocatable::den1d(:)
integer(4),allocatable::gid(:)

integer(4),parameter::nline=10551
real(8)::iderf(2,nline)

logical(4)::debug=.false.
integer(4)::i,j,k

character(100)::inden
character(100)::outden
call getarg(1,inden)
call getarg(2,outden)
write(*,*) inden
write(*,*) outden



call memo(1)
call readinerf
call readdata
call packit
call sortgrid
call transform
call unpackit
call writedata
call memo(0)

contains

subroutine memo(command)
implicit none
integer(4)::command
if (command.eq.1) then
  write(*,*) 'memo for den:',float(L)**3*(4)/1024.**3,'G'
  allocate(den(L,L,L))
  write(*,*) 'memo for den1d:',float(L)**3*(4)/1024.**3,'G'
  allocate(den1d(L1d))
  write(*,*) 'memo for gid:',float(L)**3*(4)/1024.**3,'G'
  allocate(gid(L1d))
elseif (command.eq.0) then
  deallocate(den)
  deallocate(den1d)
  deallocate(gid)
endif
endsubroutine memo

subroutine readinerf
implicit none
write(*,*) 'opening:',trim(inerf)
open(31,file=inerf,status='old',form='formatted')
do i=1,nline
  read(31,'(2e24.15)') iderf(1:2,i)
enddo
close(31)
write(*,*) 'iderf obtained'
endsubroutine readinerf

subroutine readdata
implicit none
character(1)::s_string
character(100)::filename
filename=trim(inden)
write(*,*) 'reading:',trim(filename)
open(31,file=filename,status='old',form='binary')
read(31) den
close(31)
write(*,*) 'mean:',real(sum(real(den,8))/float(L)**3,4)
write(*,*) 'sigma:',real(sqrt(sum(real(den**2,8))/float(L)**3),4)
write(*,*) 'max:',maxval(den)
write(*,*) 'min:',minval(den)
endsubroutine readdata

subroutine packit
implicit none
integer(4)::id
write(*,*) 'converting to 1d...'
do k=1,L
  do j=1,L
    do i=1,L
      id=(k-1)*L*L+(j-1)*L+i
      den1d(id)=den(i,j,k)
    enddo
  enddo
enddo
write(*,*) 'conversion finished'
endsubroutine packit

subroutine unpackit
implicit none
integer(4)::id
write(*,*) 'converting to 3d...'
do id=1,L1d
  i=mod(id-1,L)+1
  j=mod((id-i),L*L)/L+1
  k=(id-(j-1)*L-i)/L/L+1
  den(i,j,k)=den1d(id)
enddo
write(*,*) 'conversion finished'
endsubroutine unpackit

subroutine sortgrid
implicit none
do i=1,L1d
  gid(i)=i
enddo
write(*,*) 'sorting...'
call sort2_real_int(L1d,den1d,gid)
write(*,*) 'sorted'
endsubroutine sortgrid

subroutine transform
implicit none
real(8)::cdf,y,x1,x2,y1,y2,slope,b
integer(4)::i1,i2,mid
do i=1,L1d
  cdf=(real(i,8)-0.5d0)/real(L1d,8)*2.d0-1.d0
  if (cdf.lt.iderf(1,1)) then
    k=0
    y=iderf(2,1)
  elseif (cdf.gt.iderf(1,nline)) then
    k=nline+1
    y=iderf(2,nline)
  else
    i1=1
    i2=nline
    do while(i2-i1.gt.1)
      mid=(i1+i2)/2
      if (cdf.gt.iderf(1,mid)) then
        i1=mid
      else
        i2=mid
      endif
    enddo
    x1=iderf(1,i1)
    x2=iderf(1,i2)
    y1=iderf(2,i1)
    y2=iderf(2,i2)
    y=y1+(y2-y1)*(cdf-x1)/(x2-x1)
  endif  
  if (debug) write(*,'(i8,e24.15,i8,e24.15,i10)') i,cdf,k,y,gid(i)
  den1d(gid(i))=real(y,4)
enddo
endsubroutine transform

subroutine writedata
implicit none
character(100)::filename
write(*,*) 'mean:',real(sum(real(den,8))/float(L)**3,4)
write(*,*) 'sigma:',real(sqrt(sum(real(den**2,8))/float(L)**3),4)
write(*,*) 'max:',maxval(den)
write(*,*) 'min:',minval(den)
filename=trim(outden)
write(*,*) 'writing:',trim(filename)
open(31,file=filename,status='replace',form='binary')
write(31) den
close(31)
endsubroutine writedata


endprogram gd

include 'recipes08.f90'
