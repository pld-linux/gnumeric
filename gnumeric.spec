# _with_bonobo
# _without_gb
%include	/usr/lib/rpm/macros.perl
Summary:	The GNOME spreadsheet
Summary(pl):	Arkusz kalkulacyjny GNOME
Name:		gnumeric
Version:	0.72
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Vendor:		Gnumeric List <gnumeric-list@gnome.org>
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnumeric/%{name}-%{version}.tar.bz2
Patch0:		%{name}-miscfix.patch
Patch1:		%{name}-no_version.patch
Patch2:		%{name}-am15.patch
Patch3:		%{name}-xml-i18n.patch
Patch4:		%{name}-bonobo.patch
Icon:		gnumeric.xpm
URL:		http://www.gnome.org/gnumeric/
BuildRequires:	ORBit-devel
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_without_bonobo:BuildRequires:	bonobo-devel >= 1.0.9}
BuildRequires:	gal-devel >= 0.14
%{!?_with_gb:BuildRequires:	gb-devel >= 0.0.15}
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.0.56
BuildRequires:	gnome-print-devel >= 0.29
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	libglade-devel >= 0.16
BuildRequires:	libxml-devel >= 1.8.14
BuildRequires:	libole2-devel >= 0.2.3
#BuildRequires:	guile-devel >= 1.5
#BuildRequires:	libgda-devel >= 0.2.11
#BuildRequires:	psiconv-devel
BuildRequires:	perl
BuildRequires:	python-devel >= 2.1
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	xml-i18n-tools >= 0.9-3
#%#requires_eq	guile
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
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f missing acinclude.m4
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
GNOME_LIBCONFIG_PATH=/usr/lib; export GNOME_LIBCONFIG_PATH 
%configure \
	--disable-static \
	--without-included-gettext \
	--with%{?_without_bonobo:out}-bonobo \
	--with%{!?_with_gb:out}-gb \
	--with-bonobo \
	--with-guile \
	--with-python
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
