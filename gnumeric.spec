Summary:	The GNOME spreadsheet
Name:		gnumeric
Version:	0.25
Release:	1
Copyright:	GPL
Group:		X11/Applications/Spreadsheets
Group(pl):	X11/Aplikacje/Arkusze kalkulacyjne
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/gnumeric/
BuildRequires:	guile-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRequires:	ORBit-devel
BuildRequires:	gnome-libs-devel
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
