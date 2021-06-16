#
# Conditional build:
%bcond_without	apidocs	# gtk-doc based API documentation

Summary:	GNOME To Do - application to manage your personal tasks
Summary(pl.UTF-8):	GNOME To Do - aplikacja do zarządzania osobistymi zadaniami
Name:		gnome-todo
Version:	40.1
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-todo/40/%{name}-%{version}.tar.xz
# Source0-md5:	deae69c8866ff5adb96607955ab45e73
Patch0:		%{name}-doc-build.patch
URL:		https://wiki.gnome.org/Apps/Todo
BuildRequires:	evolution-data-server-devel >= 3.33.2
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.58.0
BuildRequires:	gnome-online-accounts-devel >= 3.2.0
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gtk4-devel >= 4.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.14}
BuildRequires:	libadwaita-devel
BuildRequires:	libpeas-devel >= 1.17
BuildRequires:	libportal-devel >= 0.4
BuildRequires:	meson >= 0.41.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
# for todoist plugin (disabled in src/plugins/meson.build as of 40.0)
#BuildRequires:	json-glib-devel
#BuildRequires:	rest-devel >= 0.7
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.58.0
Requires:	evolution-data-server >= 3.33.2
Requires:	glib2 >= 1:2.58.0
Requires:	gnome-online-accounts >= 3.2.0
Requires:	gtk4 >= 4.0
Requires:	hicolor-icon-theme
Requires:	libpeas >= 1.17
Requires:	libportal >= 0.4
Suggests:	libpeas-loader-python3 >= 1.17
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
Requires:	evolution-data-server-devel >= 3.33.2
Requires:	glib2-devel >= 1:2.58.0
Requires:	gtk4-devel >= 4.0
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
BuildArch:	noarch

%description apidocs
API documentation for GNOME To Do.

%description apidocs -l pl.UTF-8
Dokumentacja API GNOME To Do.

%prep
%setup -q
%patch0 -p1

%build
%meson build \
	%{?with_apidocs:-Ddocumentation=true}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-todo
%{_libdir}/girepository-1.0/Gtd-1.0.typelib
%{_datadir}/dbus-1/services/org.gnome.Todo.service
%{_datadir}/glib-2.0/schemas/org.gnome.todo.background.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.todo.gschema.xml
%{_datadir}/metainfo/org.gnome.Todo.appdata.xml
%{_desktopdir}/org.gnome.Todo.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Todo.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Todo.Devel.svg
%{_iconsdir}/hicolor/symbolic/actions/builder-view-left-pane-symbolic.svg
%{_iconsdir}/hicolor/symbolic/actions/drag-handle-symbolic.svg
%{_iconsdir}/hicolor/symbolic/actions/mail-inbox-symbolic.svg
%{_iconsdir}/hicolor/symbolic/actions/view-tasks-*-symbolic.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Todo-symbolic.svg

%files devel
%defattr(644,root,root,755)
%{_includedir}/gnome-todo
%{_pkgconfigdir}/gnome-todo.pc
%{_datadir}/gir-1.0/Gtd-1.0.gir

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gnome-todo
%endif
