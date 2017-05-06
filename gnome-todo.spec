Summary:	GNOME To Do - application to manage your personal tasks
Summary(pl.UTF-8):	GNOME To Do - aplikacja do zarządzania osobistymi zadaniami
Name:		gnome-todo
Version:	3.24.0.1
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-todo/3.24/%{name}-%{version}.tar.xz
# Source0-md5:	0f9312e4c67e5f23549bd2ebb5512fc2
URL:		https://wiki.gnome.org/Apps/Todo
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	evolution-data-server-devel >= 3.18.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnome-online-accounts-devel >= 3.2.0
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libical-devel >= 0.43
BuildRequires:	libpeas-devel >= 1.17
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.44.0
Requires:	evolution-data-server >= 3.18.0
Requires:	glib2 >= 1:2.44.0
Requires:	gnome-online-accounts >= 3.2.0
Requires:	gtk+3 >= 3.22.0
Requires:	hicolor-icon-theme
Requires:	libical >= 0.43
Requires:	libpeas >= 1.17
Suggests:	libpeas-loader-python3
Suggests:	python3-pygobject3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME To Do is a small application to manage your personal tasks. It
uses GNOME technologies, and so it has complete integration with the
GNOME desktop environment.

%description -l pl.UTF-8
GNOME To Do to mała aplikacja do zarządzania osobistymi zadaniami.
Wykorzystuje mechanizmy GNOME, więc całkowicie integruje się ze
środowiskiem graficznym GNOME.

%package devel
Summary:	Header files for GNOME To Do
Summary(pl.UTF-8):	Pliki nagłówkowe GNOME To Do
Group:		X11/Development/Libraries
Requires:	evolution-data-server-devel >= 3.18.0
Requires:	glib2-devel >= 1:2.44.0
Requires:	gtk+3-devel >= 3.22.0
Requires:	libpeas-devel >= 1.17

%description devel
This package provides header files required for GNOME To Do plugins
development.

%description devel -l pl.UTF-8
Pakiet dostarcza pliki nagłówkowe potrzebne do tworzenia wtyczek do
GNOME To Do.

%package apidocs
Summary:	GNOME To Do API documentation
Summary(pl.UTF-8):	Dokumentacja API GNOME To Do
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for GNOME To Do.

%description apidocs -l pl.UTF-8
Dokumentacja API GNOME To Do.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnome-todo
%dir %{_libdir}/gnome-todo
%dir %{_libdir}/gnome-todo/plugins
%dir %{_libdir}/gnome-todo/plugins/score
%{_libdir}/gnome-todo/plugins/score/score.plugin
%dir %{_libdir}/gnome-todo/plugins/score/score
%{_libdir}/gnome-todo/plugins/score/score/*.py
%dir %{_libdir}/gnome-todo/plugins/unscheduled-panel
%{_libdir}/gnome-todo/plugins/unscheduled-panel/unscheduled-panel.plugin
%dir %{_libdir}/gnome-todo/plugins/unscheduled-panel/unscheduled-panel
%{_libdir}/gnome-todo/plugins/unscheduled-panel/unscheduled-panel/*.py
%{_libdir}/girepository-1.0/Gtd-1.0.typelib
%{_datadir}/appdata/org.gnome.Todo.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Todo.service
%{_datadir}/glib-2.0/schemas/org.gnome.todo.background.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.todo.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.todo.enums.xml
%{_datadir}/gnome-todo
%{_desktopdir}/org.gnome.Todo.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.Todo.png
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Todo-symbolic.svg

%files devel
%defattr(644,root,root,755)
%{_includedir}/gnome-todo
%{_pkgconfigdir}/gnome-todo.pc
%{_datadir}/gir-1.0/Gtd-1.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gnome-todo

