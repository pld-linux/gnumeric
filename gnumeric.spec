Summary:     The GNOME spreadsheet
Name:        gnumeric
Version:     0.3
Release:     2
Copyright:   GPL
Group:       Applications/Spreadsheets
Source:      ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
URL:         http://www.gnome.org/gnumeric
Requires:    gnome-libs >= 0.30
BuildRoot:   /tmp/%{name}-%{version}-root

%description
GNOME based spreadsheet.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/share/apps/Productivity

make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

install gnumeric.desktop $RPM_BUILD_ROOT/usr/X11R6/share/apps/Productivity

strip $RPM_BUILD_ROOT/usr/X11R6/{bin/*,lib/gnumeric/plugins/lib*so.*.*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755, root, root) /usr/X11R6/bin/*
/usr/X11R6/lib/gnumeric
/usr/X11R6/share/apps/Productivity/*
/usr/X11R6/share/gnumeric

%lang(es) /usr/X11R6/share/locale/es*/LC_MESSAGES/gnumeric.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/gnumeric.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/gnumeric.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/gnumeric.mo
%lang(ko) /usr/X11R6/share/locale/ko/LC_MESSAGES/gnumeric.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/gnumeric.mo

%changelog
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
