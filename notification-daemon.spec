Summary:	Notification Daemon
Summary(pl):	Demon powiadomieñ
Name:		notification-daemon
Version:	0.3.3
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.galago-project.org/files/releases/source/notification-daemon/%{name}-%{version}.tar.gz
# Source0-md5:	a809ceac2aad20510e5dd5d969a5c20c
URL:		http://www.galago-project.org/
BuildRequires:	dbus-glib-devel >= 0.36
BuildRequires:	glib2-devel >= 2.2.2
BuildRequires:	gtk+2-devel >= 1:2.2.0
BuildRequires:	libsexy-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libwnck-devel
BuildRequires:	pkgconfig
Requires(post,preun):	GConf2
Requires:	dbus >= 0.36
BuildRoot:	%{_tmppath}/%{name}-%{version}-root-%(id -u -n)

%description
A daemon that displays passive pop-up notifications as per the Desktop
Notifications spec.

%description -l pl
Demon wy¶wietlaj±cy pasywne wyskakuj±ce (pop-up) powiadomienia zgodnie
ze specyfikacj± Desktop Notifications.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install notification-daemon.schemas

%preun
%gconf_schema_uninstall notification-daemon.schemas

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libexecdir}/*
%{_datadir}/dbus-1/services/*.service
%{_sysconfdir}/gconf/schemas/notification-daemon.schemas
