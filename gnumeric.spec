Summary:	The GNOME spreadsheet
Name:		gnumeric
Version:	0.25
Release:	1
Copyright:	GPL
Group:		X11/Applications/Spreadsheets
Group(pl):	X11/Aplikacje/Arkusze kalkulacyjne
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/gnumeric/
BuildPrereq:	guile-devel
BuildPrereq:	gtk+-devel >= 1.2.0
BuildPrereq:	glib-devel >= 1.2.0
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildPrereq:	ORBit-devel
BuildPrereq:	gnome-libs-devel
Requires:	gtk+ >= 1.2.0
Requires:	glib >= 1.2.0
%requires_eq	guile
BuildRoot:	/tmp/%{name}-%{version}-root

%description
GNOME based spreadsheet.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr/X11R6 \
	--disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

strip --strip-debug $RPM_BUILD_ROOT/usr/X11R6/lib/gnumeric/plugins/lib*so.*.*

gzip -9fn AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz

%attr(755,root,root) /usr/X11R6/bin/*
%dir /usr/X11R6/lib/gnumeric
%dir /usr/X11R6/lib/gnumeric/plugins
%attr(755,root,root) /usr/X11R6/lib/gnumeric/plugins/lib*.so*
/usr/X11R6/lib/gnumeric/plugins/lib*.la
/usr/X11R6/share/gnome/apps/Applications/*
/usr/X11R6/share/gnome/help/gnumeric
/usr/X11R6/share/gnumeric
/usr/X11R6/share/mime-info/*
/usr/X11R6/share/pixmaps/*

%changelog
* Fri Apr 23 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.23-2]
- replacement in %files
- gzipped %%doc
- compiled on rpm 3

* Thu Apr  1 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.22-1]
- more locales (pl, ru).

* Tue Jan 05 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.6-1]
- more locales (cs, de, es_*, no*),
- updated %files for 0.6,
- added LDFLAGS="-s" to ./configure enviroment.

* Fri Oct  2 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.3-2]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added using $RPM_OPT_FLAGS during compile,
- removed COPYING from %doc,
- added stripping plugins and binaries,
- added %lang macros for /usr/X11R6/share/locale/*/LC_MESSAGES/gnumeric.mo
  files,
- added full %attr description in %files.

* Thu Sep 24 1998 Michael Fulbright <msf@redhat.com>
- Version 0.3

* Thu Sep 24 1998 Michael Fulbright <msf@redhat.com>
- Version 0.2
