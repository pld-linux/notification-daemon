Summary:	Notification Daemon
Summary(pl.UTF-8):	Demon powiadomień
Name:		notification-daemon
Version:	0.5.0
Release:	3
License:	GPL v2+
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/notification-daemon/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	18919b2aa2a88b71a40f59393edf70d0
URL:		http://www.galago-project.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	dbus-glib-devel >= 0.78
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gnome-common
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk-devel >= 0.4
BuildRequires:	libnotify-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libwnck-devel
BuildRequires:	pkgconfig
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2 >= 2.14.0
Requires:	dbus >= 0.91
Provides:	dbus(org.freedesktop.Notifications)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A daemon that displays passive pop-up notifications as per the Desktop
Notifications spec.

%description -l pl.UTF-8
Demon wyświetlający pasywne wyskakujące (pop-up) powiadomienia zgodnie
ze specyfikacją Desktop Notifications.

%prep
%setup -q

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/notification-daemon-1.0/engines/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install notification-daemon.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall notification-daemon.schemas

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/notification-properties
%dir %{_libdir}/notification-daemon-1.0
%dir %{_libdir}/notification-daemon-1.0/engines
%attr(755,root,root) %{_libdir}/notification-daemon-1.0/engines/*.so
%attr(755,root,root) %{_libexecdir}/notification-daemon
%{_datadir}/dbus-1/services/*.service
%dir %{_datadir}/notification-daemon
%{_datadir}/notification-daemon/notification-properties.ui
%{_iconsdir}/hicolor/*/apps/notification-properties.png
%{_iconsdir}/hicolor/*/apps/notification-properties.svg
%{_desktopdir}/notification-properties.desktop
%{_sysconfdir}/gconf/schemas/notification-daemon.schemas
