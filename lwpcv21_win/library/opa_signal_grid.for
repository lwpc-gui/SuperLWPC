      SUBROUTINE OPA_SIGNAL_GRID
     &          (lu_lwf,lu_grd,print_grd,
     &           prgm_id,prfl_id,
     &           area_id,xlat1,xlon1,xlat2,xlon2,
     &           freq,power,ralt,stndev,
     &           mxpath,nrpath,bearing,rhomax,rxlat,rxlon,
     &           mxprm,nrprm,param,
     &           mxpts,nrpts,dst_lwf,amp_lwf,phs_lwf,
     &           amp_rho,sig_rho,
     &           nrcmp,mxlat,nrlat,mxlon,nrlon,
     &           xclt,cxclt,sxclt,xlng,amp_grd,sig_grd,
     &           data_format)

c***********************************************************************

c Reads file generated by mode summing program from LU_LWF.  It is
c assummed that this file contains signal vs. distance along several
c paths. Writes the signal data in a grid of longitude vs. latitude
c to logical unit LU_GRD.

c***********************************************************************

c     lu_lwf        logical unit number for  input data
c     lu_grd        logical unit number for output data
c     print_grd     integer flag to print summary information
 
c     prgm_id       program id for labeling output file
c     prfl_id       ionospheric profile identification
 
c     area_id       op area identification; 8 characters
c     xlat1         lower bound of the op area; degrees N
c     xlon1         right bound of the op area; degrees W
c     xlat2         upper bound of the op area; degrees N
c     xlon2         left  bound of the op area; degrees W
 
c     freq          frequency; kHz
c     power         power; kW
c     ralt          receiver altitude; km
c     stndev        standard deviation of the signal for day, night,
c                   dawn, dusk; dB
 
c     mxpath
c     nrpath
c     bearing
c     rhomax
c     rxlat
c     rxlon
 
c     mxprm         maximum number of parameters
c     nrprm                 number of parameters
c     param                           parameters
 
c     mxpts
c     nrpts
c     dst_lwf
c     amp_lwf
c     phs_lwf
 
c     amp_rho
c     sig_rho
 
c     nrcmp         number of field components
c     mxlat         dimension of the grid arrays in latitude
c     nrlat         output number of points in latitude
c     mxlon         dimension of the grid arrays in longitude
c     nrlon         output number of points in longitude
 
c     xclt
c     cxclt
c     sxclt
c     xlng
 
c     amp_grd
c     sig_grd
 
c     data_format   [s] 'b' if data is in binary format
c                       'a' if data is in ASCII format

c***********************************************************************

c  Change history:

c     29 Jan 94     Added ASCII/BINARY option.

c     06 Apr 94     Changed output to be dB; output the standard
c                   deviation as dB instead of weighting it by the
c                   signal amplitude.

c*******************!***************************************************

      character*(*) data_format
      character*  8 archive,prgm_id
      character* 20 xmtr_id,path_id,area_id
      character* 40 prfl_id
      character* 80 case_id
      character*120 file_id(3)
      logical       begin_file
      integer       print_grd,
     &              ibeta(721)
      real          param(mxprm),
     &              oplat1,oplon1,oplat2,oplon2,
     &              bearing(mxpath),rhomax(mxpath),
     &              rxlat(mxpath),rxlon(mxpath),
     &              dst_lwf(mxpts),amp_lwf(mxpts,3),phs_lwf(mxpts,3),
     &              amp_rho(mxpts,2,mxpath),sig_rho(mxpts,2,mxpath),
     &              beta(721),
     &              xclt(mxlat),cxclt(mxlat),sxclt(mxlat),xlng(mxlon),
     &              amp_grd(mxlon,mxlat,2),ampl(2),
     &              sig_grd(mxlon,mxlat,2),sigm(2),
     &              stndev(4)

      data          dtr/0.01745329252/


      nlwf=0
      nrlwf=1
      do while (nlwf .lt. nrlwf)
         nlwf=nlwf+1
         call OPA_READ_LWF
     &       (lu_lwf,file_id,
     &        case_id,prfl_id,
     &        xmtr_id,freq,tlat,tlon,
     &        power,ralt,stndev,
     &        path_id,oplat1,oplon1,oplat2,oplon2,
     &        mxpath,nrpath,bearing,rhomax,rxlat,rxlon,
     &        mxprm,nrprm,param,
     &        mxpts,nrpts,dst_lwf,amp_lwf,phs_lwf,
     &        nrcmp,nrlwf,nlwf,
     &        amp_rho,sig_rho)

c        Map the transmitter data onto the grid
         tclt=(90.-tlat)*dtr
         ctclt=COS(tclt)
         stclt=SIN(tclt)
         tlng=tlon*dtr

         nbeta=nrpath
         do nb=1,nbeta
            ibeta(nb)=nb
            beta(nb)=bearing(nb)*dtr
         end do

         if (nbeta .gt. 1)
c           Arrange betas in increasing order
     &      call SORTR (beta,nbeta,ibeta,nbeta,1,nbeta)
 
c        Store signal amplitude and standard deviation as dB
         nout=0
         do l=1,nrlat
            rclt=xclt(l)
            crclt=cxclt(l)
            srclt=sxclt(l)
            do k=1,nrlon
               rlng=xlng(k)
               call OPA_INTERPOLATE
     &             (tlng,tclt,ctclt,stclt,
     &              rlng,rclt,crclt,srclt,
     &              mxpath,nrpath,beta,ibeta,
     &              mxpts,nrpts,nrcmp,dst_lwf,
     &              amp_rho,sig_rho,
     &              ampl,sigm,nout)

c              Store signal amplitude
               amp_grd(k,l,1)=ampl(1)
               if (nrcmp .gt. 1) amp_grd(k,l,2)=ampl(2)

c              Store standard deviation of signal
               sig_grd(k,l,1)=sigm(1)
               if (nrcmp .gt. 1) sig_grd(k,l,2)=sigm(2)
            end do
         end do

         if (nlwf .eq. 1) then ! first time; write header

            archive='***'

c           Define the unique file identification
            call SET_FILE_ID (lu_grd,prgm_id,file_id(3))

            call WRITE_HDR
     &          (lu_grd,print_grd,
     &           archive,file_id,prgm_id,
     &           case_id,prfl_id,
     &           xmtr_id,freq,tlat,tlon,
     &           path_id,oplat1,oplon1,oplat2,oplon2,
     &           mxpath,nrpath,bearing,rhomax,rxlat,rxlon,
     &           begin_file,
     &           data_format)
         end if

c        Save this data
         do ncmp=1,nrcmp
            call WRITE_GRD
     &          (lu_grd,print_grd,
     &           mxprm,nrprm,param,nrcmp,nrlwf,
     &           area_id,xlat1,xlon1,xlat2,xlon2,
     &           mxlat,nrlat,mxlon,nrlon,
     &           amp_grd(1,1,ncmp),sig_grd(1,1,ncmp),
     &           begin_file,
     &           data_format)
         end do
      end do

      RETURN
      END      ! OPA_SIGNAL_GRID
