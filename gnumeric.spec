# _without_gb

%include	/usr/lib/rpm/macros.perl
Summary:	The GNOME spreadsheet
Summary(es):	La hoja de calculo del GNOME
Summary(pl):	Arkusz kalkulacyjny GNOME
Summary(pt_BR):	A planilha do GNOME
Summary(ru):	¸Ã≈À‘“œŒŒŸ≈ ‘¡¬Ã…√Ÿ ƒÃ— GNOME
Summary(uk):	ÂÃ≈À‘“œŒŒ¶ ‘¡¬Ã…√¶ ƒÃ— GNOME
Summary(zh_CN):	Linuxœ¬µƒExcel -- GNOMEµÁ◊”±Ì∏Ò 
Name:		gnumeric
Version:	1.0.9
Release:	6
Epoch:		1
License:	GPL
Group:		X11/Applications
Vendor:		Gnumeric List <gnumeric-list@gnome.org>
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnumeric/%{name}-%{version}.tar.bz2
# Source0-md5:	f424f16f8f4853482153299ce0a81849
Patch0:		%{name}-miscfix.patch
Patch1:		%{name}-no_version.patch
Patch2:		%{name}-gb.patch
Patch3:		%{name}-ac25x.patch
Patch4:		%{name}-am16.patch
Patch5:		%{name}-psicov_hack.patch
Patch6:		%{name}-omf.patch
Patch7:		%{name}-desktop.patch
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
BuildRequires:	gdk-pixbuf-gnome-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.0.56
BuildRequires:	gnome-print-devel >= 0.29
BuildRequires:	gtk+-devel >= 1.2.7
BuildRequires:	glib-devel >= 1.2.7
BuildRequires:	libglade-gnome-devel >= 0.16
BuildRequires:	libxml-devel >= 1.8.14
BuildRequires:	libole2-devel >= 0.2.4
#BuildRequires:	guile-devel >= 1.4
BuildRequires:	libgda-devel >= 0.2.93
#BuildRequires:	psiconv-devel
BuildRequires:	perl
BuildRequires:	python-devel >= 2.2
BuildRequires:	oaf-devel >= 0.6.2
#%requires_eq	guile
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

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
Bazuj±cy na GNOME arkusz kalkulacyjny. Je∂li znasz arkusz Excel to
jeste∂ gotÛw na uøywanie Gnumerica. Starali∂my siÍ sklonowaÊ wszystkie
dobre cechy i byÊ kompatybilnym z Excelem w sensie uøyteczno∂ci.

%description -l pt_BR
Este pacote instala a planilha do GNOME, que foi feita para substituir
qualquer planilha comercial, pois uma quantidade razo·vel de trabalho
foi (e est· sendo) colocada para torn·-la a melhor possÌvel.

%description -l ru
Gnumeric - ‹‘œ –“œ«“¡ÕÕ¡ ‹Ã≈À‘“œŒŒŸ» ‘¡¬Ã…√ ƒÃ— GNOME.

%description -l uk
Gnumeric - √≈ –“œ«“¡Õ¡ ≈Ã≈À‘“œŒŒ…» ‘¡¬Ã…√ÿ ƒÃ— GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
touch po/POTFILES
rm -f missing acinclude.m4
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I macros
autoheader
%{__autoconf}
%{__automake}
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
	Applicationsdir=%{_applnkdir}/Office/Spreadsheets \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/gnumeric
%dir %{_libdir}/gnumeric/plugins
%dir %{_libdir}/gnumeric/plugins/*
%{_libdir}/gnumeric/plugins/*/*.py
%{_libdir}/gnumeric/plugins/*/*.xml
%{_libdir}/gnumeric/plugins/*/*.la
%attr(755,root,root) %{_libdir}/gnumeric/plugins/*/*.so
%attr(755,root,root) %{_libdir}/gnumericConf.sh
%{_datadir}/gnumeric
%{_datadir}/mc/*
%{_datadir}/mime-info/*
%{_datadir}/oaf/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
%{_applnkdir}/Office/Spreadsheets/*
