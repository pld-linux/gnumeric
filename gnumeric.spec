#
# Conditional build:
# _without_bonobo
# _without_python
# _without_gda
#
%include	/usr/lib/rpm/macros.perl
Summary:	The GNOME spreadsheet
Summary(es):	La hoja de calculo del GNOME
Summary(pl):	Arkusz kalkulacyjny GNOME
Summary(pt_BR):	A planilha do GNOME
Summary(ru):	¸Ã≈À‘“œŒŒŸ≈ ‘¡¬Ã…√Ÿ ƒÃ— GNOME
Summary(uk):	ÂÃ≈À‘“œŒŒ¶ ‘¡¬Ã…√¶ ƒÃ— GNOME
Summary(zh_CN):	Linuxœ¬µƒExcel -- GNOMEµÁ◊”±Ì∏Ò
Name:		gnumeric
Version:	1.1.18
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Vendor:		Gnumeric List <gnumeric-list@gnome.org>
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/gnumeric/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	b847d5ad0c932e3afdb48842efba508b
URL:		http://www.gnome.org/gnumeric/
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	docbook-utils
BuildRequires:	flex
BuildRequires:	gal-devel >= 1.99.6
BuildRequires:	gettext-devel
BuildRequires:	perl
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libgnome-devel >= 2.2.0
BuildRequires:	libgnomeprint-devel >= 2.2.0
BuildRequires:	libgnomeprintui-devel >= 2.2.0
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libgsf-devel >= 1.8.1
BuildRequires:	libxml2-devel >= 2.4.12
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomecanvas-devel >= 2.2.0
BuildRequires:	libart_lgpl-devel >= 2.3.12
%if %{!?_without_python:1}0
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-pygtk-devel >= 1.99.16
%endif
%if %{!?_without_bonobo:1}0
BuildRequires:	libbonobo-devel >= 2.0.0
BuildRequires:	libbonoboui-devel >= 2.0.0
BuildRequires:	libgsf-gnome-devel >= 1.8.2
%endif
%if %{!?_without_gda:1}0
BuildRequires:	libgda-devel
%endif
%if %{!?_without_python:1}0
Requires:	python-modules
%endif
Requires(post):	GConf2
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%build
export LC_ALL=C
#rm -f missing acinclude.m4
#%%{__libtoolize}
#%%{__gettextize}
#%%{__aclocal}
#%%{__autoheader}
#%%{__autoconf}
#%%{__automake}
#GNOME_LIBCONFIG_PATH=/usr/lib; export GNOME_LIBCONFIG_PATH
%configure \
	--disable-static \
	--without-included-gettext \
	--with%{?_without_bonobo:out}-bonobo \
	--with%{?!_with_gb:out}-gb \
	--with%{?_without_python:out}-python \
	--without-evolution \
	--without-guile \
	--with%{?_without_gda:out}-gda

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

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

%if %{?!_without_bonobo:1}0
%attr(755,root,root) %{_libdir}/gnumeric-component
%{_libdir}/bonobo/servers/*
%endif
%dir %{_libdir}/gnumeric
%dir %{_libdir}/gnumeric/%{version}*
%dir %{_libdir}/gnumeric/%{version}*/plugins
%dir %{_libdir}/gnumeric/%{version}*/plugins/*
%attr(755,root,root) %{_libdir}/gnumeric/%{version}*/plugins/*/*.so
%{_libdir}/gnumeric/%{version}*/plugins/*/*.glade
%{_libdir}/gnumeric/%{version}*/plugins/*/*.xml
%{_libdir}/gnumeric/%{version}*/plugins/*/*.la
%{_libdir}/gnumeric/%{version}*/plugins/*/*.py
%{_libdir}/gnumeric/%{version}*/plugins/gnome-glossary/glossary-po-header

%{_desktopdir}/*.desktop
%{_datadir}/mime-info/*
%{_pixmapsdir}/*.???
%{_pixmapsdir}/gnumeric
%{_omf_dest_dir}/%{name}

%dir %{_datadir}/gnumeric
%dir %{_datadir}/gnumeric/%{version}*
%{_datadir}/gnumeric/%{version}*/glade
%{_datadir}/gnumeric/%{version}*/gnome-2.0
%{_datadir}/gnumeric/%{version}*/idl
%{_datadir}/gnumeric/%{version}*/autoformat-templates
%{_datadir}/gnumeric/%{version}*/templates
%dir %{_datadir}/gnumeric/%{version}*/gnome
%dir %{_datadir}/gnumeric/%{version}*/gnome/help
