# _without_gb

%include	/usr/lib/rpm/macros.perl
Summary:	The GNOME spreadsheet
Summary(es):	La hoja de calculo del GNOME
Summary(pl):	Arkusz kalkulacyjny GNOME
Summary(pt_BR):	A planilha do GNOME
Name:		gnumeric
Version:	1.0.4
Release:	2
Epoch:		1
License:	GPL
Group:		X11/Applications
Vendor:		Gnumeric List <gnumeric-list@gnome.org>
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnumeric/%{name}-%{version}.tar.bz2
Patch0:		%{name}-miscfix.patch
Patch1:		%{name}-no_version.patch
Patch2:		%{name}-am15.patch
Patch3:		%{name}-gb.patch
Icon:		gnumeric.xpm
URL:		http://www.gnome.org/gnumeric/
Requires:	gnome-print >= 0.34-3
Conflicts:	Guppi < 0.40.3
BuildRequires:	ORBit-devel
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	bonobo-devel >= 1.0.9
BuildRequires:	docbook-utils
BuildRequires:	flex
BuildRequires:	gal-devel >= 0.19
%{?_with_gb:BuildRequires:	gb-devel >= 0.0.19}
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.0.56
BuildRequires:	gnome-print-devel >= 0.29
BuildRequires:	gtk+-devel >= 1.2.7
BuildRequires:	glib-devel >= 1.2.7
BuildRequires:	intltool
BuildRequires:	libglade-devel >= 0.16
BuildRequires:	libxml-devel >= 1.8.14
BuildRequires:	libole2-devel >= 0.2.4
#BuildRequires:	guile-devel >= 1.4
BuildRequires:	libgda-devel >= 0.2.93
#BuildRequires:	psiconv-devel
BuildRequires:	perl
BuildRequires:	python-devel >= 2.2
BuildRequires:	oaf-devel >= 0.6.2
#%requires_eq	guile
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

%description -l es
La hoja de calculo del GNOME.

%description -l pl
Bazuj±cy na GNOME arkusz kalkulacyjny. Je¶li znasz arkusz Excel to
jeste¶ gotów na u¿ywanie Gnumerica. Starali¶my siê sklonowaæ wszystkie
dobre cechy i byæ kompatybilnym z Excelem w sensie u¿yteczno¶ci.

%description -l pt_BR
Este pacote instala a planilha do GNOME, que foi feita para substituir
qualquer planilha comercial, pois uma quantidade razoável de trabalho
foi (e está sendo) colocada para torná-la a melhor possível.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing acinclude.m4
libtoolize --copy --force
gettextize --copy --force
intltoolize --copy --force
aclocal -I macros
autoconf
automake -a -c
GNOME_LIBCONFIG_PATH=/usr/lib; export GNOME_LIBCONFIG_PATH 
%configure \
	--disable-gtk-doc \
	--disable-static \
	--without-included-gettext \
	--with-bonobo \
%{?_with_gb:--with-gb} \
%{!?_with_gb:--without-gb} \
	--with-python \
	--without-evolution \
	--without-guile \
	--with-gda

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
%attr(755,root,root) %{_bindir}/*
%attr(-,root,root) %{_libdir}/gnumeric
%attr(755,root,root) %{_libdir}/gnumericConf.sh
%{_datadir}/gnumeric
%{_datadir}/mc/*
%{_datadir}/mime-info/*
%{_datadir}/oaf/*
%{_pixmapsdir}/*
%{_applnkdir}/Office/Spreadsheets/*
