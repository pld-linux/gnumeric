Summary:	The GNOME spreadsheet
Name:		gnumeric
Version:	0.38
Release:	1
Copyright:	GPL
Group:		X11/Applications/Spreadsheets
Group(pl):	X11/Aplikacje/Arkusze kalkulacyjne
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/gnumeric/%{name}-%{version}.tar.gz
Patch0:		gnumeric-applnkdir.patch
Patch1:		gnumeric-miscfix.patch
Patch2:		gnumeric-DESTDIR.patch
Patch3:		gnumeric-bonobo_fix.patch
Icon:		gnumeric.xpm
URL:		http://www.gnome.org/gnumeric/
BuildRequires:	guile-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRequires:	ORBit-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libglade-devel >= 0.2
BuildRequires:	gnome-print-devel => 0.8
BuildRequires:	libxml-devel => 1.7.1
BuildRequires:	bonobo-devel => 0.2
BuildRequires:	gettext-devel
%requires_eq	guile
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_applnkdir	%{_datadir}/applnk

%description
GNOME based spreadsheet. Gnumeric is a spreadsheet program for GNOME. This
program is intended to be a replacement for a commercial spreadsheet, so
quite a bit of work has gone into the program.

If you are familiar with Excel, you should be ready to use Gnumeric. We
have tried to clone all of the good features and stay as compatible as
possible with Excel in terms of usability.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
LDFLAGS="-s"; export LDFLAGS
gettextize --copy --force
automake
autoconf
%configure \
	--disable-static \
	--with-bonobo
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_bindir}/gnumeric-bonobo \
	$RPM_BUILD_ROOT%{_bindir}/gnumeric

strip --strip-debug $RPM_BUILD_ROOT%{_libdir}/gnumeric/plugins/lib*so.*.*

gzip -9fn AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz

%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/gnumeric
%dir %{_libdir}/gnumeric/plugins
%attr(755,root,root) %{_libdir}/gnumeric/plugins/lib*.so*
%attr(755,root,root) %{_libdir}/gnumeric/plugins/lib*.la

%{_sysconfdir}/CORBA/servers/*

%{_applnkdir}/Applications/*
%{_datadir}/gnome/help/gnumeric
%{_datadir}/gnumeric
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*
