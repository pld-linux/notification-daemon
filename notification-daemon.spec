Summary:	Notification Daemon
Summary(pl.UTF-8):	Demon powiadomień
Name:		notification-daemon
Version:	0.3.7
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.galago-project.org/files/releases/source/notification-daemon/%{name}-%{version}.tar.bz2
# Source0-md5:	cbeae0f29a15ff93f0b763d9e1cdf1de
URL:		http://www.galago-project.org/
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libsexy-devel >= 0.1.8
BuildRequires:	libstdc++-devel
BuildRequires:	libwnck-devel
BuildRequires:	pkgconfig
BuildRequires:	autoconf
BuildRequires:	automake
Requires(post,preun):	GConf2 >= 2.14.0
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
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
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

%preun
%gconf_schema_uninstall notification-daemon.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/notification-daemon-1.0
%dir %{_libdir}/notification-daemon-1.0/engines
%attr(755,root,root) %{_libdir}/notification-daemon-1.0/engines/*.so
%attr(755,root,root) %{_libdir}/notification-daemon
%{_datadir}/dbus-1/services/*.service
%{_sysconfdir}/gconf/schemas/notification-daemon.schemas
