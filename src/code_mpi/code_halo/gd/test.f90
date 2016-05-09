program gd
implicit none

integer(4),parameter::L=1024
character(5),parameter::z_string='1.000'
!character(100)::inden='../'//z_string//'denfss1.25_c0.5.bin'
!character(100)::outden='../'//z_string//'denfss1.25gd_c0.5.bin'
character(100)::inden
character(100)::outden
call getarg(1,inden)
call getarg(2,outden)
write(*,*) inden
write(*,*) outden
end
