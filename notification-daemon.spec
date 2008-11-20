Summary:	Notification Daemon
Summary(pl.UTF-8):	Demon powiadomień
Name:		notification-daemon
Version:	0.4.0
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.galago-project.org/files/releases/source/notification-daemon/%{name}-%{version}.tar.bz2
# Source0-md5:	e61eff9782551d81045bb53e8a801d58
URL:		http://www.galago-project.org/
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	intltool
BuildRequires:	libsexy-devel >= 0.1.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel
BuildRequires:	pkgconfig
BuildRequires:	autoconf
BuildRequires:	automake
Requires(post,preun):	GConf2 >= 2.14.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	hicolor-icon-theme
Requires:	dbus >= 0.91
BuildRoot:	%{_tmppath}/%{name}-%{version}-root-%(id -u -n)

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
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall notification-daemon.schemas

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/notification-properties
%dir %{_libdir}/notification-daemon-1.0
%dir %{_libdir}/notification-daemon-1.0/engines
%attr(755,root,root) %{_libdir}/notification-daemon-1.0/engines/*.so
%attr(755,root,root) %{_libdir}/notification-daemon
%{_datadir}/dbus-1/services/*.service
%dir %{_datadir}/notification-daemon
%{_datadir}/notification-daemon/notification-properties.glade
%{_iconsdir}/hicolor/*/apps/notification-properties.png
%{_iconsdir}/hicolor/*/apps/notification-properties.svg
%{_desktopdir}/notification-properties.desktop
%{_sysconfdir}/gconf/schemas/notification-daemon.schemas
