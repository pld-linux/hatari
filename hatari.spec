Summary:	hatari - an Atari ST and STE emulator for Linux
Summary(pl.UTF-8):	hatari - emulator Atari ST i STE dla Linuksa
Name:		hatari
Version:	1.3.0
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
Source0:	http://download.berlios.de/hatari/%{name}-%{version}.tar.bz2
# Source0-md5:	1440230be3dd38098f4e0ef36b0a90df
Patch0:		%{name}-useless_files.patch
Patch1:		%{name}-destdir.patch
Patch2:		%{name}-python_init.patch
Patch3:		%{name}-desktop.patch
URL:		http://hatari.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
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
obsługiwanych przez bibliotekę SDL. Hatari emuluje większość
sprzętu Atari ST i STE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%{__sed} -i 's#path=$(DATAPATH)#path=%{_datadir}/hatari/hatariui#' python-ui/Makefile

%build
%{__aclocal}
%{__autoconf}
%configure \
	--datadir=%{_datadir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_mandir}/{,fr}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/hatari.1	$RPM_BUILD_ROOT%{_mandir}/man1/hatari.1
install doc/fr/hatari.1	$RPM_BUILD_ROOT%{_mandir}/fr/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt doc/*.txt python-ui/{Changelog,README,TODO}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/hatari.1*
%lang(fr) %{_mandir}/fr/man1/hatari.1*
%{_desktopdir}/hatariui.desktop
%{_iconsdir}/hicolor/32x32/apps/hatari-icon.png
