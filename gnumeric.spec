#
# Conditional build:
%bcond_without	gda	# GDA support
%bcond_with	gnomedb	# GNOMEDB support
%bcond_without	python	# Python support
%bcond_with	guile	# Guile support [disabled upstream as experimental]
%bcond_with	mono	# mono scripting engine [disabled upstream as experimental]
%bcond_with	psiconv		# psiconv / psion support
#
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ia64 mips ppc ppc64 s390x sparc sparcv9 sparc64
%undefine	with_mono
%endif
Summary:	The GNOME spreadsheet
Summary(es.UTF-8):	La hoja de cálculo del GNOME
Summary(pl.UTF-8):	Arkusz kalkulacyjny GNOME
Summary(pt_BR.UTF-8):	A planilha do GNOME
Summary(ru.UTF-8):	Электронные таблицы для GNOME
Summary(uk.UTF-8):	Електронні таблиці для GNOME
Summary(zh_CN.UTF-8):	Linux下的Excel -- GNOME电子表格
Name:		gnumeric
Version:	1.12.48
Release:	4
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnumeric/1.12/%{name}-%{version}.tar.xz
# Source0-md5:	6141a2ff1790484933aafec2d0dce129
Patch0:		%{name}-gnomedb.patch
URL:		http://www.gnumeric.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gcc >= 5:3.2
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gobject-introspection-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.8.7
%{?with_guile:BuildRequires:	guile-devel >= 1.5}
BuildRequires:	intltool >= 0.35
BuildRequires:	itstool
BuildRequires:	libgoffice-devel >= 0.10.48
%if %{with gda}
BuildRequires:	libgda5-devel >= 5.0.0
BuildRequires:	libgda5-ui-devel >= 5.0.0
%endif
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgsf-devel >= 1.14.33
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 1:2.6.26
# disabled by default - still experimental
%{?with_mono:BuildRequires:	mono-devel >= 1.0.0}
BuildRequires:	pango-devel >= 1:1.24.0
BuildRequires:	perl-base
BuildRequires:	perl-devel
BuildRequires:	pkgconfig >= 1:0.18
BuildRequires:	popt-devel
%{?with_psiconv:BuildRequires:	psiconv-devel >= 0.9.3}
BuildRequires:	pxlib-devel >= 0.4.0
BuildRequires:	rpm-perlprov
%if %{with python}
BuildRequires:	python3-devel >= 1:2.7
BuildRequires:	python3-pygobject3-devel >= 3.0.0
%endif
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	yelp-tools
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires:	libspreadsheet = %{epoch}:%{version}-%{release}
%if %{without gda}
Obsoletes:	gnumeric-plugin-gdaif
%endif
%if %{without gnomedb}
Obsoletes:	gnumeric-plugin-gnomedb
%endif
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
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.8.7
Requires:	libgoffice >= 0.10.48
Requires:	libgsf >= 1.14.33
Requires:	libxml2 >= 1:2.6.26

%description -n libspreadsheet
libspreadsheet library.

%description -n libspreadsheet -l pl.UTF-8
Biblioteka libspreadsheet.

%package -n libspreadsheet-devel
Summary:	Header files for libspreadsheet library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libspreadsheet
Group:		Development/Libraries
Requires:	libspreadsheet = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= 1:2.40.0
Requires:	gtk+3-devel >= 3.8.7
Requires:	libgoffice-devel >= 0.10.48
Requires:	libgsf-devel >= 1.14.33
Requires:	libxml2-devel >= 1:2.6.26

%description -n libspreadsheet-devel
This is the package containing the header files for libspreadsheet
library.

%description -n libspreadsheet-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libspreadsheet.

# plugins - import/export
# applix
%package plugin-applix
Summary:	Applix plugin
Summary(pl.UTF-8):	Wtyczka Applix
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-applix
Imports Applix 4.[234] spreadsheets.

%description plugin-applix -l pl.UTF-8
Importuje arkusze Applix w wersjach 4.[234].

# data interchange format (DIF)
%package plugin-dif
Summary:	Data Interchange Format plugin
Summary(pl.UTF-8):	Wtyczka Data Interchange Format
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-dif
Reads and writes information stored in the Data Interchange Format
(*.dif).

%description plugin-dif -l pl.UTF-8
Odczytuje i zapisuje informacje w uniwersalnym formacie wymiany danych
(*.dif).

# ms excel
%package plugin-excel
Summary:	MS Excel (tm) plugin
Summary(pl.UTF-8):	Wtyczka MS Excel (tm)
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libspreadsheet = %{epoch}:%{version}-%{release}

%description plugin-excel
Imports/exports MS Excel (tm) files.

%description plugin-excel -l pl.UTF-8
Importuje/eksporuje pliki MS Excel (tm).

# glpk
%package plugin-glpk
Summary:	GLPK plugin
Summary(pl.UTF-8):	Wtyczka GLPK
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-glpk
Imports/exports GLPK files.

%description plugin-glpk -l pl.UTF-8
Importuje/eksporuje pliki GLPK.

# html
%package plugin-html
Summary:	HTML plugin
Summary(pl.UTF-8):	Wtyczka HTML
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-html
Imports/exports of HTML, TeX, DVI and roff formats.

%description plugin-html -l pl.UTF-8
Importuje/eksportuje formaty HTML, TeX, DVI i roff.

# lotus 123
%package plugin-lotus123
Summary:	Lotus 123 plugin
Summary(pl.UTF-8):	Wtyczka Lotus 123
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-lotus123
Imports Lotus 123 files.

%description plugin-lotus123 -l pl.UTF-8
Importuje pliki Lotusa 123.

# lpsolve
%package plugin-lpsolve
Summary:	lpsolve plugin
Summary(pl.UTF-8):	Wtyczka lpsolve
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-lpsolve
Imports lpsolve files.

%description plugin-lpsolve -l pl.UTF-8
Importuje pliki lpsolve.

# nlsolve
%package plugin-nlsolve
Summary:	nlsolve plugin
Summary(pl.UTF-8):	Wtyczka nlsolve
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-nlsolve
Imports nlsolve files.

%description plugin-nlsolve -l pl.UTF-8
Importuje pliki nlsolve.

# gnu oleo
%package plugin-gnuoleo
Summary:	GNU Oleo plugin
Summary(pl.UTF-8):	Wtyczka GNU Oleo
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-gnuoleo
Imports GNU Oleo documents.

%description plugin-gnuoleo -l pl.UTF-8
Importuje dokumenty GNU Oleo.

# openoffice
%package plugin-openoffice
Summary:	OpenOffice.org plugin
Summary(pl.UTF-8):	Wtyczka OpenOffice.org
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-openoffice
Imports/exports OpenOffice.org/StarOffice spreadsheets.

%description plugin-openoffice -l pl.UTF-8
Importuje/eksportuje arkusze OpenOffice.org/StarOffice.

# paradox
%package plugin-paradox
Summary:	Paradox plugin
Summary(pl.UTF-8):	Wtyczka Paradox
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-paradox
Imports Paradox files.

%description plugin-paradox -l pl.UTF-8
Importuje pliki w formacie Paradoxa.

# plan perfect
%package plugin-planperfect
Summary:	Plan Perfect plugin
Summary(pl.UTF-8):	Wtyczka Plan Perfect
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-planperfect
Imports Plan Perfect formatted documents.

%description plugin-planperfect -l pl.UTF-8
Importuje dokumenty w formacie Plan Perfect.

# psiconv
%package plugin-psiconv
Summary:	Psiconv plugin
Summary(pl.UTF-8):	Wtyczka Psiconv
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-psiconv
Imports Psion 5 series Sheet files.

%description plugin-psiconv -l pl.UTF-8
Importuje pliki arkuszy Psion serii 5.

# qpro
%package plugin-qpro
Summary:	Quattro Pro(tm) plugin
Summary(pl.UTF-8):	Wtyczka Quattro Pro(tm)
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-qpro
Imports Quattro Pro (tm) files.

%description plugin-qpro -l pl.UTF-8
Importuje pliki Quattro Pro (tm).

# sc/xspread
%package plugin-sc
Summary:	SC/XSpread plugin
Summary(pl.UTF-8):	Wtyczka SC/XSpread
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sc
Imports SC/XSpread files.

%description plugin-sc -l pl.UTF-8
Importuje pliki SC/XSpread.

# sylk
%package plugin-sylk
Summary:	MultiPlan (SYLK) plugin
Summary(pl.UTF-8):	Wtyczka MultiPlan (SYLK)
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sylk
Imports MultiPlan (SYLK) files.

%description plugin-sylk -l pl.UTF-8
Importuje pliki MultiPlan (SYLK).

# xbase
%package plugin-xbase
Summary:	XBase plugin
Summary(pl.UTF-8):	Wtyczka Xbase
Group:		X11/Applications
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
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-gdaif
Database functions for retrieval of data from a database.

%description plugin-gdaif -l pl.UTF-8
Funkcje bazodanowe, pozwalające na pobieranie danych z baz danych.

# gnome db
%package plugin-gnomedb
Summary:	GNOME DB plugin
Summary(pl.UTF-8):	Wtyczka GNOME DB
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gnumeric-plugin-gdaif
Requires:	/usr/bin/gnome-database-properties-4.0

%description plugin-gnomedb
Gnumeric frontend for GNOME DB configuration tool.

%description plugin-gnomedb -l pl.UTF-8
Interfejs Gnumerica do narzędzia konfiguracyjnego GNOME DB.

# samples
%package plugin-sample
Summary:	Sample plugins
Summary(pl.UTF-8):	Przykładowe wtyczki
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sample
Sample database and UI plugins.

%description plugin-sample -l pl.UTF-8
Przykładowe wtyczki bazy danych oraz interfejsu użytkownika.

# perl/python stuff
# perl-func/perl loader
%package plugin-perl
Summary:	Perl plugin
Summary(pl.UTF-8):	Wtyczka Perla
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-perl
Sample Perl plugin providing some (useless) functions.

%description plugin-perl -l pl.UTF-8
Przykładowa wtyczka Perla dostarczająca różnych (bezużytecznych)
funkcji.

# python-func/python loader
%package plugin-python
Summary:	Python plugin
Summary(pl.UTF-8):	Wtyczka Pythona
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-modules

%description plugin-python
Sample Python plugin providing some (useless) functions.

%description plugin-python -l pl.UTF-8
Przykładowa wtyczka Pythona, dostarczająca różnych (bezużytecznych)
funkcji.

# gnumeric support for goffice
%package plugin-goffice
Summary:	Gnumeric plugin for goffice
Summary(pl.UTF-8):	Wtyczka dla goffice
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libgoffice >= 0.10.48
Requires:	libgsf >= 1.14.33
Requires:	libspreadsheet = %{epoch}:%{version}-%{release}

%description plugin-goffice
Gnumeric plugin for goffice.

%description plugin-goffice -l pl.UTF-8
Wtyczka dla goffice.

%prep
%setup -q
# actually libgnomedb is not required to build gnomedb plugin
# ... but it expects gnome-database-properties-4.0 tool, which no longer exists
#patch0 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON=%{__python3} \
	--disable-silent-rules \
	--with-gda%{!?with_gda:=no} \
	%{?with_guile:--with-guile} \
	%{?with_mono:--with-mono} \
	%{?with_psiconv:--with-psiconv} \
	--with-python%{!?with_python:=no}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libspreadsheet.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnumeric/%{version}/plugins/*/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/goffice/*/plugins/gnumeric/*.la

# "gnumeric-%{version}" and "gnumeric-%{version}-functions" po domains
# "gnumeric" help domain
%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_desktop_database_post

%postun
%glib_compile_schemas
%update_desktop_database_postun

%post	-n libspreadsheet -p /sbin/ldconfig
%postun	-n libspreadsheet -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README

%attr(755,root,root) %{_bindir}/gnumeric
%attr(755,root,root) %{_bindir}/gnumeric-%{version}
%attr(755,root,root) %{_bindir}/ssconvert
%attr(755,root,root) %{_bindir}/ssdiff
%attr(755,root,root) %{_bindir}/ssgrep
%attr(755,root,root) %{_bindir}/ssindex

%dir %{_libdir}/gnumeric
%dir %{_libdir}/gnumeric/%{version}
%dir %{_libdir}/gnumeric/%{version}/plugins
%dir %{_libdir}/gnumeric/%{version}/plugins/fn-*
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/fn-*/*.so
%{_libdir}/gnumeric/%{version}/plugins/fn-*/plugin.xml
%dir %{_libdir}/gnumeric/%{version}/plugins/mps
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/mps/mps.so
%{_libdir}/gnumeric/%{version}/plugins/mps/plugin.xml

%{_datadir}/appdata/gnumeric.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnumeric.dialogs.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnumeric.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnumeric.plugin.gschema.xml

%{_desktopdir}/gnumeric.desktop
%{_pixmapsdir}/gnumeric
%{_pixmapsdir}/gnome-application-vnd.lotus-1-2-3.png
%{_pixmapsdir}/gnome-application-x-applix-spreadsheet.png
%{_pixmapsdir}/gnome-application-x-generic-spreadsheet.png
%{_pixmapsdir}/gnome-application-x-gnumeric.png
%{_pixmapsdir}/gnome-application-x-xls.png
%{_pixmapsdir}/win32-gnumeric.ico
%{_iconsdir}/hicolor/*x*/apps/gnumeric.png

%dir %{_datadir}/gnumeric
%dir %{_datadir}/gnumeric/%{version}
%{_datadir}/gnumeric/%{version}/Gnumeric-embed.xml
%{_datadir}/gnumeric/%{version}/autoformat-templates
%{_datadir}/gnumeric/%{version}/templates

%{_mandir}/man1/gnumeric.1*
%{_mandir}/man1/ssconvert.1*
%{_mandir}/man1/ssdiff.1*
%{_mandir}/man1/ssgrep.1*
%{_mandir}/man1/ssindex.1*

%files -n libspreadsheet
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspreadsheet-%{version}.so

%files -n libspreadsheet-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspreadsheet.so
%{_includedir}/libspreadsheet-1.12
%{_pkgconfigdir}/libspreadsheet-1.12.pc

# applix
%files plugin-applix
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/applix
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/applix/applix.so
%{_libdir}/gnumeric/%{version}/plugins/applix/plugin.xml

# data interchange format (DIF)
%files plugin-dif
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/dif
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/dif/dif.so
%{_libdir}/gnumeric/%{version}/plugins/dif/plugin.xml

# ms excel
%files plugin-excel
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/excel
# R: zlib
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/excel/excel.so
%{_libdir}/gnumeric/%{version}/plugins/excel/plugin.xml
%dir %{_libdir}/gnumeric/%{version}/plugins/excelplugins
# R: libspreadsheet libgoffice
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/excelplugins/plugin.so
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/excelplugins/xlcall32.so
%{_libdir}/gnumeric/%{version}/plugins/excelplugins/plugin.xml

%if %{with gda}
# gda
%files plugin-gdaif
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/gdaif
# R: libgda5 libgda5-ui
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/gdaif/gdaif.so
%{_libdir}/gnumeric/%{version}/plugins/gdaif/plugin.xml
%{_libdir}/gnumeric/%{version}/plugins/gdaif/ui.xml
%endif

%if %{with gnomedb}
# gnome db
%files plugin-gnomedb
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/gnome-db
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/gnome-db/gnomedb.so
%{_libdir}/gnumeric/%{version}/plugins/gnome-db/plugin.xml
%endif

# glpk
%files plugin-glpk
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/glpk
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/glpk/glpk.so
%{_libdir}/gnumeric/%{version}/plugins/glpk/plugin.xml

# html
%files plugin-html
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/html
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/html/html.so
%{_libdir}/gnumeric/%{version}/plugins/html/plugin.xml

# lotus 123
%files plugin-lotus123
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/lotus
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/lotus/lotus.so
%{_libdir}/gnumeric/%{version}/plugins/lotus/plugin.xml

# lpsolve
%files plugin-lpsolve
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/lpsolve
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/lpsolve/lpsolve.so
%{_libdir}/gnumeric/%{version}/plugins/lpsolve/plugin.xml

# nlsolve
%files plugin-nlsolve
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/nlsolve
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/nlsolve/nlsolve.so
%{_libdir}/gnumeric/%{version}/plugins/nlsolve/plugin.xml

# gnu oleo
%files plugin-gnuoleo
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/oleo
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/oleo/oleo.so
%{_libdir}/gnumeric/%{version}/plugins/oleo/plugin.xml

# openoffice
%files plugin-openoffice
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/openoffice
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/openoffice/openoffice.so
%{_libdir}/gnumeric/%{version}/plugins/openoffice/plugin.xml

# paradox
%files plugin-paradox
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/paradox
# R: pxlib
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/paradox/paradox.so
%{_libdir}/gnumeric/%{version}/plugins/paradox/plugin.xml

# plan perfect
%files plugin-planperfect
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/plan_perfect
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/plan_perfect/plan_perfect.so
%{_libdir}/gnumeric/%{version}/plugins/plan_perfect/plugin.xml

# psiconv
%if %{with psiconv}
%files plugin-psiconv
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/psiconv
# R: psiconv
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/psiconv/psiconv.so
%{_libdir}/gnumeric/%{version}/plugins/psiconv/plugin.xml
%endif

# qpro
%files plugin-qpro
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/qpro
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/qpro/qpro.so
%{_libdir}/gnumeric/%{version}/plugins/qpro/plugin.xml

# sc/xspread
%files plugin-sc
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/sc
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/sc/sc.so
%{_libdir}/gnumeric/%{version}/plugins/sc/plugin.xml

# sylk
%files plugin-sylk
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/sylk
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/sylk/sylk.so
%{_libdir}/gnumeric/%{version}/plugins/sylk/plugin.xml

# xbase
%files plugin-xbase
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/xbase
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/xbase/xbase.so
%{_libdir}/gnumeric/%{version}/plugins/xbase/plugin.xml

# samples
%files plugin-sample
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/sample_datasource
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/sample_datasource/sample_datasource.so
%{_libdir}/gnumeric/%{version}/plugins/sample_datasource/plugin.xml
%dir %{_libdir}/gnumeric/%{version}/plugins/uihello
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/uihello/plugin.so
%{_libdir}/gnumeric/%{version}/plugins/uihello/hello.xml
%{_libdir}/gnumeric/%{version}/plugins/uihello/plugin.xml

# perl-func/perl loader
%files plugin-perl
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/perl-func
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/perl-func/perl_func.pl
%{_libdir}/gnumeric/%{version}/plugins/perl-func/plugin.xml
%dir %{_libdir}/gnumeric/%{version}/plugins/perl-loader
# R: perl-libs
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/perl-loader/perl_loader.so
%{_libdir}/gnumeric/%{version}/plugins/perl-loader/plugin.xml

# python-func/python loader
%if %{with python}
%files plugin-python
%defattr(644,root,root,755)
%dir %{_libdir}/gnumeric/%{version}/plugins/gnome-glossary
%{_libdir}/gnumeric/%{version}/plugins/gnome-glossary/glossary-po-header
%{_libdir}/gnumeric/%{version}/plugins/gnome-glossary/gnome_glossary.py
%{_libdir}/gnumeric/%{version}/plugins/gnome-glossary/plugin.xml
%dir %{_libdir}/gnumeric/%{version}/plugins/py-func
%{_libdir}/gnumeric/%{version}/plugins/py-func/py_func.py
%{_libdir}/gnumeric/%{version}/plugins/py-func/plugin.xml
%dir %{_libdir}/gnumeric/%{version}/plugins/python-loader
# R: python-libs
%attr(755,root,root) %{_libdir}/gnumeric/%{version}/plugins/python-loader/python_loader.so
%{_libdir}/gnumeric/%{version}/plugins/python-loader/plugin.xml
%{_libdir}/gnumeric/%{version}/plugins/python-loader/ui-console-menu.xml
%endif

%files plugin-goffice
%defattr(644,root,root,755)
%dir %{_libdir}/goffice/0.10/plugins/gnumeric
%attr(755,root,root) %{_libdir}/goffice/0.10/plugins/gnumeric/gnumeric.so
%{_libdir}/goffice/0.10/plugins/gnumeric/plugin.xml
