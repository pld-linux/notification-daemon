Summary:	Notification Daemon
Summary(pl):	Demon powiadomieñ
Name:		notification-daemon
Version:	0.2.2
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.galago-project.org/files/releases/source/notification-daemon/%{name}-%{version}.tar.gz
# Source0-md5:	056043b929eeaa2f1217e2fbd014745c
URL:		http://www.galago-project.org/
BuildRequires:	dbus-glib-devel >= 0.30
BuildRequires:	glib2-devel >= 2.2.2
BuildRequires:	gtk+2-devel >= 1:2.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
Requires:	dbus >= 0.30
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

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libexecdir}/*
%{_datadir}/dbus-1/services/*.service
%{_sysconfdir}/dbus-1/system.d/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/notification-daemon.conf
