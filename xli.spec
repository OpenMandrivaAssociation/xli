# sometime i hope to remove the xv shareware and replace it by this
# one.
%define	name	xli
%define	version	1.17.0
%define	release	%mkrel 11
%define	url	http://pantransit.reptiles.org/prog/

Summary:	XLI - X11 Image Loading Utility
Name:		%{name}
Version:	%{version}
Release:	%{release}
Url:		%{url}
# I was need to redo the tarball.
Source0:	%{url}/%{name}-%{version}.tar.bz2
Patch1:		xli-1.17.0-mdkpath.patch.bz2
Patch2:		xli-1.17.0-compile-fixes.patch.bz2
Patch3:		xli-1.16-faces.patch.bz2
Patch4:		xli-1.17.0-gcc-3.3.patch.bz2
License:	MIT
Group:		Graphics
BuildRequires:	XFree86-devel
BuildRequires:	gccmakedep
BuildRequires:	imake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	rman
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p0 -b .faces
%patch4 -p0 -b .gcc3.3

%build
xmkmf -a
%make CFLAGS="%optflags"
for i in xli xlito; do cp -f $i.man $i.1; done
cp -f xliguide.man xliguide.5
cp mit.cpyrght COPYRIGHT

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/app-defaults/
make install SYSPATHFILE=$RPM_BUILD_ROOT%{_sysconfdir}/X11/app-defaults/Xli BINDIR=$RPM_BUILD_ROOT%{_bindir}

for i in *.1;do install -m644 $i -D $RPM_BUILD_ROOT%{_mandir}/man1/$i;done
install -m644 xliguide.5 -D $RPM_BUILD_ROOT%{_mandir}/man5/xliguide.5

ln -sf xli $RPM_BUILD_ROOT%{_bindir}/xsetbg
ln -sf xli $RPM_BUILD_ROOT%{_bindir}/xview 
ln -sf xli $RPM_BUILD_ROOT%{_bindir}/xloadimage

# quick fix for doc permissions
chmod 644 README*
 
%clean  
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc chkgamma.jpg README* ABOUTGAMMA COPYRIGHT 
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/X11/app-defaults/*
%{_mandir}/*/*
