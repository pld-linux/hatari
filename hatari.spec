Summary:	hatari - an Atari ST and STE emulator for Linux
Summary(pl.UTF-8):	hatari - emulator Atari ST i STE dla Linuksa
Name:		hatari
Version:	1.1.0
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/hatari/%{name}-%{version}.tar.bz2
# Source0-md5:	e782830f4d82dccb017159b302fd8b62
Patch0:		%{name}-useless_files.patch
URL:		http://hatari.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
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
%doc readme.txt doc/*.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/hatari.1*
%lang(fr) %{_mandir}/fr/man1/hatari.1*
