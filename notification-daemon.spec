Summary:	Notification Daemon
Summary(pl):	Demon powiadomieñ
Name:		notification-daemon
Version:	0.3.5
Release:	4
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.galago-project.org/files/releases/source/notification-daemon/%{name}-%{version}.tar.gz
# Source0-md5:	7977c4c15139f9d53ddbfa8af707270f
Patch0:		%{name}-icon-data.patch
URL:		http://www.galago-project.org/
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libsexy-devel >= 0.1.8
BuildRequires:	libstdc++-devel
BuildRequires:	libwnck-devel
BuildRequires:	pkgconfig
Requires(post,preun):	GConf2 >= 2.14.0
Requires:	dbus >= 0.91
BuildRoot:	%{_tmppath}/%{name}-%{version}-root-%(id -u -n)

%description
A daemon that displays passive pop-up notifications as per the Desktop
Notifications spec.

%description -l pl
Demon wy¶wietlaj±cy pasywne wyskakuj±ce (pop-up) powiadomienia zgodnie
ze specyfikacj± Desktop Notifications.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/notification-daemon-1.0/engines/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install notification-daemon.schemas

%preun
%gconf_schema_uninstall notification-daemon.schemas

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/notification-daemon-1.0
%dir %{_libdir}/notification-daemon-1.0/engines
%attr(755,root,root) %{_libdir}/notification-daemon-1.0/engines/*.so
%attr(755,root,root) %{_libdir}/notification-daemon
%{_datadir}/dbus-1/services/*.service
%{_sysconfdir}/gconf/schemas/notification-daemon.schemas
