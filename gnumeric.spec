# _without_gb

%include	/usr/lib/rpm/macros.perl
Summary:	The GNOME spreadsheet
Summary(es):	La hoja de calculo del GNOME
Summary(pl):	Arkusz kalkulacyjny GNOME
Summary(pt_BR):	A planilha do GNOME
Summary(ru):	üÌÅËÔÒÏÎÎÙÅ ÔÁÂÌÉÃÙ ÄÌÑ GNOME
Summary(uk):	åÌÅËÔÒÏÎÎ¦ ÔÁÂÌÉÃ¦ ÄÌÑ GNOME
Summary(zh_CN):	LinuxÏÂµÄExcel -- GNOMEµç×Ó±í¸ñ 
Name:		gnumeric
Version:	1.1.11
Release:	0.1
Epoch:		1
License:	GPL
Group:		X11/Applications
Vendor:		Gnumeric List <gnumeric-list@gnome.org>
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/gnumeric/1.1/%{name}-%{version}.tar.bz2
#Icon:		gnumeric.xpm
URL:		http://www.gnome.org/gnumeric/
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	docbook-utils
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	perl
BuildRequires:	python-devel >= 2.2
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
Requires:	python-modules
Requires(post,postun): /sbin/ldconfig
Requires(post):	GConf2
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
Bazuj±cy na GNOME arkusz kalkulacyjny. Je¶li znasz arkusz Excel to
jeste¶ gotów na u¿ywanie Gnumerica. Starali¶my siê sklonowaæ wszystkie
dobre cechy i byæ kompatybilnym z Excelem w sensie u¿yteczno¶ci.

%description -l pt_BR
Este pacote instala a planilha do GNOME, que foi feita para substituir
qualquer planilha comercial, pois uma quantidade razoável de trabalho
foi (e está sendo) colocada para torná-la a melhor possível.

%description -l ru
Gnumeric - ÜÔÏ ĞÒÏÇÒÁÍÍÁ ÜÌÅËÔÒÏÎÎÙÈ ÔÁÂÌÉÃ ÄÌÑ GNOME.

%description -l uk
Gnumeric - ÃÅ ĞÒÏÇÒÁÍÁ ÅÌÅËÔÒÏÎÎÉÈ ÔÁÂÌÉÃØ ÄÌÑ GNOME.

%prep
%setup -q

%build
export LC_ALL=C
#rm -f missing acinclude.m4
#%{__libtoolize}
#%{__gettextize}
#%{__aclocal} -I macros
#%{__autoheader}
#%{__autoconf}
#%{__automake}
#GNOME_LIBCONFIG_PATH=/usr/lib; export GNOME_LIBCONFIG_PATH
%configure \
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

# .la files are use less in this case
rm -r $RPM_BUILD_ROOT%{_libdir}/gnumeric/%{version}*/plugins/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
GCONF_CONFIG_SOURCE="`%{_bindir}/gconftool-2 --get-default-source`" \
%{_bindir}/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null 
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/bonobo/servers/*
%dir %{_libdir}/gnumeric
%dir %{_libdir}/gnumeric/%{version}*
%dir %{_libdir}/gnumeric/%{version}*/plugins
%dir %{_libdir}/gnumeric/%{version}*/plugins/*
%attr(755,root,root) %{_libdir}/gnumeric/%{version}*/plugins/*/*.so
%{_libdir}/gnumeric/%{version}*/plugins/*/*.xml
%{_libdir}/gnumeric/%{version}*/plugins/*/*.py
%{_libdir}/gnumeric/%{version}*/plugins/gnome-glossary/glossary-po-header
%dir %{_datadir}/gnumeric
%dir %{_datadir}/gnumeric/%{version}*
%{_datadir}/gnumeric/%{version}*/plot-types.xml
%{_datadir}/gnumeric/%{version}*/glade
%{_datadir}/gnumeric/%{version}*/gnome-2.0
%{_datadir}/gnumeric/%{version}*/idl
%{_datadir}/gnumeric/%{version}*/autoformat-templates
%{_datadir}/gnumeric/%{version}*/templates
%dir %{_datadir}/gnumeric/%{version}*/share
%dir %{_datadir}/gnumeric/%{version}*/share/gnome
%dir %{_datadir}/gnumeric/%{version}*/share/gnome/help
# FIXME: this is for ?
%{_datadir}/mc/*
%{_datadir}/mime-info/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
%{_applnkdir}/Office/Spreadsheets/*
%{_sysconfdir}/gconf/schemas/*
