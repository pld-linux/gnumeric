
%bcond_without gnome	# build without gnome
%bcond_without python	# build without python support
%bcond_without gda	# build without gda

%include	/usr/lib/rpm/macros.perl
Summary:	The GNOME spreadsheet
Summary(es):	La hoja de c·lculo del GNOME
Summary(pl):	Arkusz kalkulacyjny GNOME
Summary(pt_BR):	A planilha do GNOME
Summary(ru):	¸Ã≈À‘“œŒŒŸ≈ ‘¡¬Ã…√Ÿ ƒÃ— GNOME
Summary(uk):	ÂÃ≈À‘“œŒŒ¶ ‘¡¬Ã…√¶ ƒÃ— GNOME
Summary(zh_CN):	Linuxœ¬µƒExcel -- GNOMEµÁ◊”±Ì∏Ò
Name:		gnumeric
Version:	1.3.2
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Vendor:		Gnumeric List <gnumeric-list@gnome.org>
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.3/%{name}-%{version}.tar.bz2
# Source0-md5:	14c7e3cf3f3eda61f1d029f6f473d678
#Patch0:		%{name}-compile_fix.patch
URL:		http://www.gnome.org/gnumeric/
BuildRequires:	GConf2-devel
BuildRequires:	ORBit2-devel >= 2.4.2
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	docbook-utils
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.4.4
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	intltool >= 0.28
BuildRequires:	libart_lgpl-devel >= 2.3.12
%if %{with gnome}
BuildRequires:	libbonobo-devel >= 2.6.0
BuildRequires:	libbonoboui-devel >= 2.6.0
BuildRequires:	libgsf-gnome-devel >= 1.10.0
%endif
%if %{with gda}
BuildRequires:	libgda-devel >= 1.0.1
BuildRequires:	libgnomedb-devel >= 1.0.1
%endif
BuildRequires:	libglade2-devel >= 1:2.4.0
%{?with_gnome:BuildRequires:	libgnome-devel >= 2.6.0}
BuildRequires:	libgnomecanvas-devel >= 2.6.0
BuildRequires:	libgnomeprint-devel >= 2.6.0
BuildRequires:	libgnomeprintui-devel >= 2.6.0
%{?with_gnome:BuildRequires:	libgnomeui-devel >= 2.6.0}
BuildRequires:	libgsf-devel >= 1.10.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.12
BuildRequires:	perl-base
%if %{with python}
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-pygtk-devel >= 2.0.0
%endif
Requires(post):	GConf2
Requires(post):	scrollkeeper
%if %{with python}
Requires:	python-modules
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME based spreadsheet. Gnumeric is a spreadsheet program for GNOME.
This program is intended to be a replacement for a commercial
spreadsheet, so quite a bit of work has gone into the program. If you
are familiar with Excel, you should be ready to use Gnumeric. We have
tried to clone all of the good features and stay as compatible as
possible with Excel in terms of usability.

%description -l es
Gnumeric es un programa de hoja de c·lculo para GNOME. Este programa
procura ser reemplazar los programas comerciales, asÌ que ha gozado
bastante esfuerzo. Si conoce Excel, deberÌa estar preparado para usar
Gnumeric. Intentamos clonar todas las buenas cualidades y seguir lo
m·s compatible que fuera posible, en cuanto a la usabilidad.

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
#%patch0 -p1

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--disable-schemas-install \
	--with%{?!with_gnome:out}-gnome \
	--with%{?!with_python:out}-python \
	--with%{?!with_gda:out}-gda \
	--without-guile \
	--without-gb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_sysconfdir}/gconf/schemas/*

%attr(755,root,root) %{_bindir}/*

%{_libdir}/bonobo/servers/*
%dir %{_libdir}/gnumeric
%dir %{_libdir}/gnumeric/%{version}*
%dir %{_libdir}/gnumeric/%{version}*/plugins
%dir %{_libdir}/gnumeric/%{version}*/plugins/*
%attr(755,root,root) %{_libdir}/gnumeric/%{version}*/plugins/*/*.so
%{_libdir}/gnumeric/%{version}*/plugins/*/*.glade
%{_libdir}/gnumeric/%{version}*/plugins/*/*.xml
%{_libdir}/gnumeric/%{version}*/plugins/*/*.la
%if %{with python}
%{_libdir}/gnumeric/%{version}*/plugins/*/*.py
%{_libdir}/gnumeric/%{version}*/plugins/gnome-glossary/glossary-po-header
%endif

%{_desktopdir}/*.desktop
%{_datadir}/mime-info/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/%{name}

%dir %{_datadir}/gnumeric
%dir %{_datadir}/gnumeric/%{version}*
%{_datadir}/gnumeric/%{version}*/*.xml
%{_datadir}/gnumeric/%{version}*/autoformat-templates
%{_datadir}/gnumeric/%{version}*/idl
%{_datadir}/gnumeric/%{version}*/glade
%{_datadir}/gnumeric/%{version}*/templates

#%{_mandir}/man1/*
