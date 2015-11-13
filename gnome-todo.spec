Summary:	GNOME To Do - application to manage your personal tasks
Summary(pl.UTF-8):	GNOME To Do - aplikacja do zarządzania osobistymi zadaniami
Name:		gnome-todo
Version:	3.18.1
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-todo/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	b37b38c7f1ec50bebb3ce84119b3b2f6
URL:		https://wiki.gnome.org/Apps/Todo
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	evolution-data-server-devel >= 3.18.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnome-online-accounts-devel >= 3.2.0
BuildRequires:	gtk+3-devel >= 3.16.0
BuildRequires:	intltool >= 0.40.6
BuildRequires:	libical-devel >= 0.43
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.44.0
Requires:	evolution-data-server >= 3.18.0
Requires:	glib2 >= 1:2.44.0
Requires:	gnome-online-accounts >= 3.2.0
Requires:	gtk+3 >= 3.16.0
Requires:	hicolor-icon-theme
Requires:	libical >= 0.43
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME To Do is a small application to manage your personal tasks. It
uses GNOME technologies, and so it has complete integration with the
GNOME desktop environment.

%description -l pl.UTF-8
GNOME To Do to mała aplikacja do zarządzania osobistymi zadaniami.
Wykorzystuje mechanizmy GNOME, więc całkowicie integruje się ze
środowiskiem graficznym GNOME.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

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
%{_datadir}/appdata/org.gnome.Todo.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Todo.service
%{_datadir}/glib-2.0/schemas/org.gnome.todo.gschema.xml
%{_desktopdir}/org.gnome.Todo.desktop
%{_iconsdir}/hicolor/*x*/apps/gnome-todo.png
%{_iconsdir}/hicolor/symbolic/apps/gnome-todo-symbolic.svg