# _with_bonobo
# _with_gb
Summary:	The GNOME spreadsheet
Summary(pl):	Arkusz kalkulacyjny GNOME
Name:		gnumeric
Version:	0.70
Release:	2
Epoch:		1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Vendor:		Gnumeric List <gnumeric-list@gnome.org>
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnumeric/%{name}-%{version}.tar.gz
Patch0:		%{name}-miscfix.patch
Patch1:		%{name}-no_version.patch
Icon:		gnumeric.xpm
URL:		http://www.gnome.org/gnumeric/
BuildRequires:	ORBit-devel
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	automake
%{?_with_bonobo:BuildRequires:	bonobo-devel => 1.0.3}
BuildRequires:	gal-devel >= 0.11.2
%{?_with_gb:BuildRequires:	gb-devel >= 0.0.15}
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.0.56
BuildRequires:	gnome-print-devel => 0.25
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	guile-devel
BuildRequires:	libglade-devel >= 0.14
BuildRequires:	libxml-devel => 1.8.10
BuildRequires:	libole2-devel => 0.1.4
BuildRequires:	perl
BuildRequires:	python-devel >= 2.1
BuildRequires:	bison
BuildRequires:	flex
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
Bazuj±cy na GNOME arkusz kalkulacyjny. Je¶li znasz arkusz Excel to
jeste¶ gotów na u¿ywanie Gnumerica. Starali¶my siê sklonowaæ wszystkie
dobre cechy i byæ kompatybilnym z Excelem w sensie u¿yteczno¶ci.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
rm missing acinclude.m4
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
GNOME_LIBCONFIG_PATH=/usr/lib; export GNOME_LIBCONFIG_PATH 
%configure \
	--disable-static \
	--without-included-gettext \
	%{!?_with_bonobo:--without-bonobo} \
	%{!?_with_gb:--without-gb} \
	--with-guile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Office/Spreadsheets

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
# Two lines below are commented out only for 0.67.
# Please check with next version if they are back.
#%{_sysconfdir}/CORBA/servers/*
%attr(755,root,root) %{_bindir}/*
%attr(-,root,root) %{_libdir}/gnumeric
%attr(755,root,root) %{_libdir}/gnumericConf.sh
#%{_datadir}/gnome/ui/*

%{_applnkdir}/Office/Spreadsheets/*
%{_datadir}/gnumeric
%{_datadir}/mime-info/*
%{_pixmapsdir}/*
%{_datadir}/mc/*
%{_datadir}/oaf/*
