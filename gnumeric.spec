Summary:	The GNOME spreadsheet
Summary(pl):	Arkusz kalkulacyjny GNOME
Name:		gnumeric
Version:	0.54
Release:	2
License:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Vendor:		Gnumeric List <gnumeric-list@gnome.org>
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnumeric/%{name}-%{version}.tar.gz
Patch0:		gnumeric-miscfix.patch
Icon:		gnumeric.xpm
URL:		http://www.gnome.org/gnumeric/
BuildRequires:	guile-devel
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	xpm-devel
BuildRequires:	ORBit-devel
BuildRequires:	gnome-libs-devel >= 1.0.56
BuildRequires:	libglade-devel >= 0.13
BuildRequires:	gnome-print-devel => 0.16
BuildRequires:	libxml-devel => 1.8.5
BuildRequires:	bonobo-devel => 0.2
BuildRequires:	gettext-devel
BuildRequires:	docbook-dsssl => 1.52
%requires_eq	guile
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
GNOME based spreadsheet. Gnumeric is a spreadsheet program for GNOME.
This program is intended to be a replacement for a commercial
spreadsheet, so quite a bit of work has gone into the program. If you
are familiar with Excel, you should be ready to use Gnumeric. We have
tried to clone all of the good features and stay as compatible as
possible with Excel in terms of usability.

%description -l pl
Bazuj�cy na GNOME arkusz kalkulacyjny. Je�li znasz arkusz Excel to
jeste� got�w na u�ywanie Gnumerica. Starali�my si� sklonowa� wszystkie
dobre cechy i by� kompatybilnym z Excelem w sensie u�yteczno�ci.

%prep
%setup  -q
%patch0 -p1

%build
LDFLAGS="-s"; export LDFLAGS
gettextize --copy --force
automake
autoconf
%configure \
	--disable-static \
	--without-included-gettext \
	--with-guile \
	--with-bonobo
#	--with-gb
make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Office/Spreadsheets \
	install

strip --strip-debug $RPM_BUILD_ROOT%{_libdir}/gnumeric/%{version}/plugins/gnum_*so*

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz

%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/gnumeric
%dir %{_libdir}/gnumeric/%{version}
%dir %{_libdir}/gnumeric/%{version}/plugins
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/gnum*.so*
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/gnum*.la

%{_sysconfdir}/CORBA/servers/*

%{_applnkdir}/Office/Spreadsheets/*
%{_datadir}/gnumeric
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*
%{_datadir}/mc/*
%{_datadir}/idl/*
