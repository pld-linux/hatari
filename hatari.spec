Summary:	hatari - an Atari ST and STE emulator for Linux
Summary(pl.UTF-8):	hatari - emulator Atari ST i STE dla Linuksa
Name:		hatari
Version:	1.4.0
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
Source0:	http://download.berlios.de/hatari/%{name}-%{version}.tar.bz2
# Source0-md5:	2f30e5c9e146ee92e3f2f5ae1cef3673
Patch0:		%{name}-useless_files.patch
Patch1:		%{name}-python_init.patch
Patch2:		%{name}-desktop.patch
URL:		http://hatari.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	cmake >= 2.6
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.577
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Requires:	python >= 1:2.4
Requires:	python-pygtk-gtk >= 2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hatari is an Atari ST and STE emulator for Linux and other systems
that are supported by the SDL library. Hatari supports the emulation
of most of the ST and STE hardware.

%description -l pl.UTF-8
Hatari jest emulatorem Atari ST i STE dla Linuksa i innych systemów
obsługiwanych przez bibliotekę SDL. Hatari emuluje większość sprzętu
Atari ST i STE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
install -d build
cd build
%cmake .. \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DCMAKE_C_FLAGS_RELEASE="-DNDEBUG"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_mandir}/{,fr}/man1}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/fr/hatari.1	$RPM_BUILD_ROOT%{_mandir}/fr/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt doc/*.txt python-ui/{README,TODO}
%attr(755,root,root) %{_bindir}/atari-hd-image.sh
%attr(755,root,root) %{_bindir}/hatari
%attr(755,root,root) %{_bindir}/hatari-console.py
%attr(755,root,root) %{_bindir}/hatariui
%attr(755,root,root) %{_bindir}/hmsa
%attr(755,root,root) %{_bindir}/zip2st.sh
%{_datadir}/%{name}
%{_mandir}/man1/hatariui.1*
%lang(fr) %{_mandir}/fr/man1/hatari.1*
%{_desktopdir}/hatariui.desktop
%{_iconsdir}/hicolor/32x32/apps/hatari-icon.png
