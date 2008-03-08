#
# Conditional build:
%bcond_without	gda	# build without gda
%bcond_without	gnome	# build without gnome
%bcond_without	python	# build without python support
%bcond_with	mono	# build without mono scripting engine
#
%ifnarch %{ix86} %{x8664} alpha arm hppa ppc s390 sparc sparcv9 sparc64
%undefine	with_mono
%endif
%include	/usr/lib/rpm/macros.perl
Summary:	The GNOME spreadsheet
Summary(es.UTF-8):	La hoja de cálculo del GNOME
Summary(pl.UTF-8):	Arkusz kalkulacyjny GNOME
Summary(pt_BR.UTF-8):	A planilha do GNOME
Summary(ru.UTF-8):	Электронные таблицы для GNOME
Summary(uk.UTF-8):	Електронні таблиці для GNOME
Summary(zh_CN.UTF-8):	Linux下的Excel -- GNOME电子表格
Name:		gnumeric
Version:	1.8.2
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Vendor:		Gnumeric List <gnumeric-list@gnome.org>
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnumeric/1.8/%{name}-%{version}.tar.bz2
# Source0-md5:	f60edc6ca42daa2fb3717f3c90fa8a6e
#Patch0:		%{name}-help-path.patch
#Patch1:		%{name}-gda12.patch
URL:		http://www.gnome.org/gnumeric/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	ORBit2-devel >= 1:2.14.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	docbook-utils
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.1
BuildRequires:	intltool >= 0.35
BuildRequires:	libart_lgpl-devel >= 2.3.12
%if %{with gnome}
BuildRequires:	libbonoboui-devel >= 2.14.0
BuildRequires:	libgoffice-devel >= 0.6.0
BuildRequires:	libgsf-gnome-devel >= 1.14.6
%endif
%if %{with gda}
BuildRequires:	libgda3-devel >= 3.1.1
BuildRequires:	libgnomedb3-devel >= 3.1.1
%endif
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeprint-devel >= 2.12.0
BuildRequires:	libgnomeprintui-devel >= 2.12.1
%{?with_gnome:BuildRequires:	libgnomeui-devel >= 2.15.90}
BuildRequires:	libgsf-devel >= 1.14.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
# disabled by default - still experimental
%{?with_mono:BuildRequires:	mono-devel >= 1.0.0}
BuildRequires:	pango-devel >= 1:1.13.4
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	psiconv-devel >= 0.9.3
BuildRequires:	pxlib-devel
%if %{with python}
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-pygtk-devel >= 2:2.9.3
%endif
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2 >= 2.14.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires:	libspreadsheet = %{epoch}:%{version}-%{release}
%{?with_gnome:Requires:	libgnomeui >= 2.15.1}
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME based spreadsheet. Gnumeric is a spreadsheet program for GNOME.
This program is intended to be a replacement for a commercial
spreadsheet, so quite a bit of work has gone into the program. If you
are familiar with Excel, you should be ready to use Gnumeric. We have
tried to clone all of the good features and stay as compatible as
possible with Excel in terms of usability.

%description -l es.UTF-8
Gnumeric es un programa de hoja de cálculo para GNOME. Este programa
procura ser reemplazar los programas comerciales, así que ha gozado
bastante esfuerzo. Si conoce Excel, debería estar preparado para usar
Gnumeric. Intentamos clonar todas las buenas cualidades y seguir lo
más compatible que fuera posible, en cuanto a la usabilidad.

%description -l pl.UTF-8
Bazujący na GNOME arkusz kalkulacyjny. Jeśli znasz arkusz Excel to
jesteś gotów na używanie Gnumerica. Staraliśmy się sklonować wszystkie
dobre cechy i być kompatybilnym z Excelem w sensie użyteczności.

%description -l pt_BR.UTF-8
Este pacote instala a planilha do GNOME, que foi feita para substituir
qualquer planilha comercial, pois uma quantidade razoável de trabalho
foi (e está sendo) colocada para torná-la a melhor possível.

%description -l ru.UTF-8
Gnumeric - это программа электронных таблиц для GNOME.

%description -l uk.UTF-8
Gnumeric - це програма електронних таблиць для GNOME.

%package -n libspreadsheet
Summary:	libspreadsheet library
Summary(pl.UTF-8):	Biblioteka libspreadsheet
Group:		Libraries
%{?with_gnome:Requires:	libgoffice >= 0.5.0}

%description -n libspreadsheet
libspreadsheet library.

%description -n libspreadsheet -l pl.UTF-8
Biblioteka libspreadsheet.

%package -n libspreadsheet-devel
Summary:	Header files for libspreadsheet library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libspreadsheet
Group:		Development/Libraries
Requires:	libspreadsheet = %{epoch}:%{version}-%{release}

%description -n libspreadsheet-devel
This is the package containing the header files for libspreadsheet library.

%description -n libspreadsheet-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libspreadsheet.

# plugins - import/export
# applix
%package plugin-applix
Summary:	Applix plugin
Summary(pl.UTF-8):	Wtyczka Applix
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-applix
Imports Applix 4.[234] spreadsheets.

%description plugin-applix -l pl.UTF-8
Importuje arkusze Applix w wersjach 4.[234].

# data interchange format (DIF) 
%package plugin-dif
Summary:	Data Interchange Format plugin
Summary(pl.UTF-8):	Wtyczka Data Interchange Format
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-dif
Reads and writes information stored in the Data Interchange Format
(*.dif).

%description plugin-dif -l pl.UTF-8
Odczytuje i zapisuje informacje w uniwersalnym formacie wymiany
danych (*.dif).

# ms excel
%package plugin-excel
Summary:	MS Excel (tm) plugin
Summary(pl.UTF-8):	Wtyczka MS Excel (tm)
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-excel
Imports/exports MS Excel (tm) files.

%description plugin-excel -l pl.UTF-8
Importuje/eksporuje pliki MS Excel (tm).

# html
%package plugin-html
Summary:	HTML plugin
Summary(pl.UTF-8):	Wtyczka HTML
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-html
Imports/exports of HTML, TeX, DVI and roff formats.

%description plugin-html -l pl.UTF-8
Importuje/eksportuje formaty HTML, TeX, DVI i roff.

# lotus 123
%package plugin-lotus123
Summary:	Lotus 123 plugin
Summary(pl.UTF-8):	Wtyczka Lotus 123
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-lotus123
Imports Lotus 123 files.

%description plugin-lotus123 -l pl.UTF-8
Importuje pliki Lotusa 123.

# gnu oleo
%package plugin-gnuoleo
Summary:	GNU Oleo plugin
Summary(pl.UTF-8):	Wtyczka GNU Oleo
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-gnuoleo
Imports GNU Oleo documents.

%description plugin-gnuoleo -l pl.UTF-8
Importuje dokumenty GNU Oleo.

# openoffice
%package plugin-openoffice
Summary:	OpenOffice.org plugin
Summary(pl.UTF-8):	Wtyczka OpenOffice.org
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-openoffice
Imports/exports OpenOffice.org/StarOffice spreadsheets.

%description plugin-openoffice -l pl.UTF-8
Importuje/eksportuje arkusze OpenOffice.org/StarOffice.

# paradox
%package plugin-paradox
Summary:	Paradox plugin
Summary(pl.UTF-8):	Wtyczka Paradox
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-paradox
Imports Paradox files.

%description plugin-paradox -l pl.UTF-8
Importuje pliki w formacie Paradoxa.

# plan perfect
%package plugin-planperfect
Summary:	Plan Perfect plugin
Summary(pl.UTF-8):	Wtyczka Plan Perfect
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-planperfect
Imports Plan Perfect formatted documents.

%description plugin-planperfect -l pl.UTF-8
Importuje dokumenty w formacie Plan Perfect.

# psiconv
%package plugin-psiconv
Summary:	Psiconv plugin
Summary(pl.UTF-8):	Wtyczka Psiconv
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-psiconv
Imports Psion 5 series Sheet files.

%description plugin-psiconv -l pl.UTF-8
Importuje pliki arkuszy Psion serii 5.

# qpro
%package plugin-qpro
Summary:	Quattro Pro(tm) plugin
Summary(pl.UTF-8):	Wtyczka Quattro Pro(tm)
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-qpro
Imports Quattro Pro (tm) files.

%description plugin-qpro -l pl.UTF-8
Importuje pliki Quattro Pro (tm).

# sc/xspread
%package plugin-sc
Summary:	SC/XSpread plugin
Summary(pl.UTF-8):	Wtyczka SC/XSpread
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sc
Imports SC/XSpread files.

%description plugin-sc -l pl.UTF-8
Importuje pliki SC/XSpread.

# sylk
%package plugin-sylk
Summary:	MultiPlan (SYLK) plugin
Summary(pl.UTF-8):	Wtyczka MultiPlan (SYLK)
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sylk
Imports MultiPlan (SYLK) files.

%description plugin-sylk -l pl.UTF-8
Importuje pliki MultiPlan (SYLK).

# xbase
%package plugin-xbase
Summary:	XBase plugin
Summary(pl.UTF-8):	Wtyczka Xbase
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-xbase
Imports Xbase files.

%description plugin-xbase -l pl.UTF-8
Importuje pliki XBase.

# other plugins
# gda
%package plugin-gdaif
Summary:	Database plugin
Summary(pl.UTF-8):	Wtyczka baz danych
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-gdaif
Database functions for retrieval of data from a database.

%description plugin-gdaif -l pl.UTF-8
Funkcje bazodanowe, pozwalające na pobieranie danych z baz danych.

# gnome db
%package plugin-gnomedb
Summary:	GNOME DB plugin
Summary(pl.UTF-8):	Wtyczka GNOME DB
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gnumeric-plugin-gdaif

%description plugin-gnomedb
Gnumeric frontend for libgnomedb.

%description plugin-gnomedb -l pl.UTF-8
Nakładka Gnumerica na libgnomedb.

# samples
%package plugin-sample
Summary:	Sample plugins
Summary(pl.UTF-8):	Przykładowe wtyczki
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sample
Sample database and UI plugins.

%description plugin-sample -l pl.UTF-8
Przykładowe wtyczki bazy danych oraz interfejsu użytkownika.

# perl/python stuff
# perl-func/perl loader
%package plugin-perl
Summary:	Perl plugin
Summary(pl.UTF-8):	Wtyczk Perla
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-perl
Sample Perl plugin providing some (useless) functions.

%description plugin-perl -l pl.UTF-8
Przykładowa wtyczka Perla dostarczająca różnych (bezużytecznych)
funkcji.

# perl-func/perl loader
%package plugin-python
Summary:	Python plugin
Summary(pl.UTF-8):	Wtyczk Pythona
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-modules
Requires:	python-pygtk-gtk

%description plugin-python
Sample Python plugin providing some (useless) functions.

%description plugin-python -l pl.UTF-8
Przykładowa wtyczka Pythona, dostarczająca różnych (bezużytecznych)
funkcji.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1 - obsoleted

%build
%{__gnome_doc_common}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--disable-schemas-install \
	--with-psiconv \
	--with%{!?with_gnome:out}-gnome \
	--with%{!?with_python:out}-python \
	--with%{!?with_gda:out}-gda \
	--with%{!?with_mono:out}-mono \
	--without-gb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=/usr/share/gnome/help/gnumeric/C \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_libdir}/gnumeric/%{version}/plugins/*/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%if %{with gnome}
%gconf_schema_install gnumeric-dialogs.schemas
%gconf_schema_install gnumeric-general.schemas
%gconf_schema_install gnumeric-plugins.schemas
%update_desktop_database_post
%endif
%scrollkeeper_update_post

%if %{with gnome}
%preun
%gconf_schema_uninstall gnumeric-dialogs.schemas
%gconf_schema_uninstall gnumeric-general.schemas
%gconf_schema_uninstall gnumeric-plugins.schemas
%endif

%postun
%scrollkeeper_update_postun
%if %{with gnome}
%update_desktop_database_postun
%endif

%post	-n libspreadsheet -p /sbin/ldconfig
%postun	-n libspreadsheet -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README

%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/gnumeric
%dir %{_libdir}/gnumeric/%{version}
%dir %{_libdir}/gnumeric/%{version}/plugins
%dir %{_libdir}/gnumeric/%{version}/plugins/derivatives
%dir %{_libdir}/gnumeric/%{version}/plugins/fn-*
%dir %{_libdir}/gnumeric/%{version}/plugins/mps
%dir %{_libdir}/gnumeric/%{version}/plugins/numtheory

%if %{with gnome}
%{_datadir}/gnumeric/%{version}/idl
%{_sysconfdir}/gconf/schemas/gnumeric-dialogs.schemas
%{_sysconfdir}/gconf/schemas/gnumeric-general.schemas
%{_sysconfdir}/gconf/schemas/gnumeric-plugins.schemas

%dir %{_libdir}/gnumeric/%{version}/plugins/corba
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/corba/*.so
%{_libdir}/gnumeric/%{version}/plugins/corba/*.xml
%endif

%{_libdir}/gnumeric/%{version}/plugins/derivatives/*.xml
%{_libdir}/gnumeric/%{version}/plugins/fn-*/*.xml
%{_libdir}/gnumeric/%{version}/plugins/mps/*.xml
%{_libdir}/gnumeric/%{version}/plugins/numtheory/*.xml
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/derivatives/*.so
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/fn-*/*.so
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/mps/*.so
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/numtheory/*.so

%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_omf_dest_dir}/%{name}

%dir %{_datadir}/gnumeric
%dir %{_datadir}/gnumeric/%{version}*
%{_datadir}/gnumeric/%{version}/*.xml
%{_datadir}/gnumeric/%{version}/autoformat-templates
%{_datadir}/gnumeric/%{version}/glade
%{_datadir}/gnumeric/%{version}/templates

%{_mandir}/man1/gnumeric.1*
%{_mandir}/man1/ssconvert.1*
%{_mandir}/man1/ssindex.1*

%files -n libspreadsheet
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so

%files -n libspreadsheet-devel
%defattr(644,root,root,755)
%{_includedir}/libspreadsheet-1.8
%{_pkgconfigdir}/*.pc

# applix
%files plugin-applix
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/applix
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/applix/*.so
%{_libdir}/gnumeric/%{version}/plugins/applix/*.xml

# data interchange format (DIF) 
%files plugin-dif
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/dif
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/dif/*.so
%{_libdir}/gnumeric/%{version}/plugins/dif/*.xml

# ms excel
%files plugin-excel
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/excel
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/excel/*.so
%{_libdir}/gnumeric/%{version}/plugins/excel/*.xml

# html
%files plugin-html
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/html
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/html/*.so
%{_libdir}/gnumeric/%{version}/plugins/html/*.xml

# lotus 123
%files plugin-lotus123
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/lotus
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/lotus/*.so
%{_libdir}/gnumeric/%{version}/plugins/lotus/*.xml

# gnu oleo
%files plugin-gnuoleo
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/oleo
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/oleo/*.so
%{_libdir}/gnumeric/%{version}/plugins/oleo/*.xml

# openoffice
%files plugin-openoffice
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/openoffice
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/openoffice/*.so
%{_libdir}/gnumeric/%{version}/plugins/openoffice/*.xml

# paradox
%files plugin-paradox
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/paradox
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/paradox/*.so
%{_libdir}/gnumeric/%{version}/plugins/paradox/*.xml

# plan perfect
%files plugin-planperfect
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/plan_perfect
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/plan_perfect/*.so
%{_libdir}/gnumeric/%{version}/plugins/plan_perfect/*.xml

# psiconv
%files plugin-psiconv
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/psiconv
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/psiconv/*.so
%{_libdir}/gnumeric/%{version}/plugins/psiconv/*.xml

# qpro
%files plugin-qpro
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/qpro
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/qpro/*.so
%{_libdir}/gnumeric/%{version}/plugins/qpro/*.xml

# sc/xspread
%files plugin-sc
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/sc
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/sc/*.so
%{_libdir}/gnumeric/%{version}/plugins/sc/*.xml

# sylk
%files plugin-sylk
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/sylk
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/sylk/*.so
%{_libdir}/gnumeric/%{version}/plugins/sylk/*.xml

# xbase
%files plugin-xbase
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/xbase
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/xbase/*.so
%{_libdir}/gnumeric/%{version}/plugins/xbase/*.xml

%if %{with gda}
# gda
%files plugin-gdaif
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/gdaif
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/gdaif/*.so
%{_libdir}/gnumeric/%{version}/plugins/gdaif/*.xml

# gnome db
%files plugin-gnomedb
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/gnome-db
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/gnome-db/*.so
%{_libdir}/gnumeric/%{version}/plugins/gnome-db/*.xml
%endif

# samples
%files plugin-sample
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/sample_datasource
%dir %{_libdir}/gnumeric/%{version}/plugins/uihello
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/sample_datasource/*.so
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/uihello/*.so
%{_libdir}/gnumeric/%{version}/plugins/sample_datasource/*.xml
%{_libdir}/gnumeric/%{version}/plugins/uihello/*.xml

# perl-func/perl loader
%files plugin-perl
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/perl-*
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/perl-*/*.so
%{_libdir}/gnumeric/%{version}/plugins/perl-*/*.pl
%{_libdir}/gnumeric/%{version}/plugins/perl-*/*.xml

# python-func/perl loader
%if %{with python}
%files plugin-python
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/gnome-glossary
%dir %{_libdir}/gnumeric/%{version}/plugins/py*
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/py*/*.so
%{_libdir}/gnumeric/%{version}/plugins/py*/*.py
%{_libdir}/gnumeric/%{version}/plugins/py*/*.xml
%{_libdir}/gnumeric/%{version}/plugins/gnome-glossary/glossary-po-header
%{_libdir}/gnumeric/%{version}/plugins/gnome-glossary/*.py
%{_libdir}/gnumeric/%{version}/plugins/gnome-glossary/*.xml
%endif
