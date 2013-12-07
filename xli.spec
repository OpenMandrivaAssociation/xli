%define fver	2006-11-10
%define	url	http://pantransit.reptiles.org/prog/

Summary:	X11 Image Loading Utility
Name:		xli
Version:	20061110
Release:	16
URL:		%{url}
Source0:	%{url}/%{name}/%{name}-%{fver}.tar.gz
Patch1:		xli-1.17.0-mdkpath.patch
Patch2:		xli-1.17.0-compile-fixes.patch
License:	MIT
Group:		Graphics
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	gccmakedep
BuildRequires:	imake
BuildRequires:	jpeg-devel
BuildRequires:	png-devel
BuildRequires:	rman
Provides:	xloadimage
Obsoletes:	xloadimage

%description
This utility will view several types of images under X11, or load
images onto the X11 root window.  Can view the following image types
under X11: 

FBM Image, Sun Rasterfile, CMU WM Raster, Portable Bit Map (PBM, PGM,
PPM), Faces Project, GIF Image, JFIF style jpeg Image, Utah RLE Image,
Windows, OS/2 RLE Image, Photograph on CD Image, X Window Dump, Targa 
Image, McIDAS areafile, G3 FAX Image, PC Paintbrush Image, GEM Bit Image,
MacPaint Image, X Pixmap (.xpm), XBitmap

%prep
%setup -q -n %{name}-%{fver}
%patch1 -p1
%patch2 -p1

%build
xmkmf -a
%make CFLAGS="%{optflags}" EXTRA_LDOPTIONS="%{ldflags}"
for i in xli xlito; do cp -f $i.man $i.1; done
cp -f xliguide.man xliguide.5

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/X11/app-defaults/
make install SYSPATHFILE=%{buildroot}%{_sysconfdir}/X11/app-defaults/Xli BINDIR=%{buildroot}%{_bindir}

for i in *.1;do install -m644 $i -D %{buildroot}%{_mandir}/man1/$i;done
install -m644 xliguide.5 -D %{buildroot}%{_mandir}/man5/xliguide.5

ln -sf xli %{buildroot}%{_bindir}/xsetbg
ln -sf xli %{buildroot}%{_bindir}/xview 
ln -sf xli %{buildroot}%{_bindir}/xloadimage

# quick fix for doc permissions
chmod 644 README*
 
%clean  

%files
%doc chkgamma.jpg README* ABOUTGAMMA
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/X11/app-defaults/*
%{_mandir}/*/*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 20061110-8mdv2011.0
+ Revision: 671333
- mass rebuild

* Thu Dec 23 2010 Funda Wang <fwang@mandriva.org> 20061110-7mdv2011.0
+ Revision: 623957
- build with our own flags

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 20061110-6mdv2011.0
+ Revision: 608218
- rebuild

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 20061110-5mdv2010.1
+ Revision: 488816
- rebuilt against libjpeg v8

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 20061110-4mdv2010.0
+ Revision: 416668
- rebuilt against libjpeg v7

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 20061110-3mdv2009.1
+ Revision: 366701
- rediff png patch

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 20061110-2mdv2009.0
+ Revision: 226051
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 20061110-1mdv2008.1
+ Revision: 130253
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 20061110-1mdv2008.0
+ Revision: 76537
- rebuild for 2008
- don't package the license, not needed
- drop patches 3 and 4 (superseded upstream)
- new release 2006-11-10
- Import xli



* Sun Jun 25 2006 Dick Gevers <dvgevers@xs4all.nl> 1.17.0-11
- /usr/X11R6 deprecated since xorg 7.0
- adjusted Imake Makefile for xorg 7 paths
- worked around bug #22937 at build time

* Sat Jun 17 2006 Stefan van der Eijk <stefan@eijk.nu> 1.17.0-10
- %%mkrel
- BuildRequires

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.17.0-9mdk
- Rebuild

* Sat Dec 25 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.17.0-8mdk
- fix buildrequires
- cosmetics

* Thu Jul 24 2003 G�tz Waschk <waschk@linux-mandrake.com> 1.17.0-7mdk
- rediff patch3

* Mon Jul 14 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.17.0-6mdk
- fix gcc-3.3 build (P4)

* Mon Mar 24 2003 Florin <florin@mandrakesoft.com> 1.17.0-5mdk
- added missing link to xloadimage (thx to Wesley J. Landaker)
- use License and Url

* Tue Oct 16 2001 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.17.0-4mdk
- rebuilt with libpng3

* Tue Aug 28 2001 Vincent Danen <vdanen@mandrakesoft.com> 1.17.0-3mdk
- patch to fix buffer overflow

* Thu Jul 12 2001 Stefan van der Eijk <stefan@eijk.nu> 1.17.0-2mdk
- BuildRequires:	libjpeg-devel
- Removed BuildRequires:	zlib-devel

* Mon Feb  5 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.17.0-1mdk
- Get compile with last glibc.
- 1.17.0.

* Thu Aug 31 2000 Florin Grad <florin@mandrakesoft.com> 1.16-7mdk
- removed the png from the description according to the README file

* Wed Aug 30 2000 Florin Grad <florin@mandrakesoft.com> 1.16-6mdk- removed the png from the description according to the README file
- fixed the strange permissions of the source files

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.16-5mdk
- automatically added BuildRequires

* Fri Apr  7 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.16-4mdk
- Add Obsoletes: Provides: xloadimage.

* Mon Mar 20 2000 Camille Begnis <camille@mandrakesoft.com> 1.16-3mdk
- Fixed group
- fixed bad symlinks

* Sat Mar 18 2000 Camille Begnis <camille@mandrakesoft.com> 1.16-2mdk
- let spec-helper do its job
                    
* Sat Feb  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.16-1mdk
- Apply debian patchs.
- First packaging.
