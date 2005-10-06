Summary:	Notification Daemon
Name:		notification-daemon
Version:	0.2.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:		http://www.galago-project.org/files/releases/source/notification-daemon/%{name}-%{version}.tar.gz
# Source0-md5:	056043b929eeaa2f1217e2fbd014745c
URL:		http://www.galago-project.org/
BuildPrereq:	dbus-devel >= 0.30
Requires:	dbus >= 0.30
BuildRoot:	%{_tmppath}/%{name}-%{version}-root-%(id -u -n)

%description
A daemon that displays passive pop-up notifications as per the
Desktop Notifications spec.

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
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_libexecdir}/*
%{_datadir}/dbus-1/services/*.service
%{_sysconfdir}/dbus-1/system.d/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dbus-1/system.d/notification-daemon.conf
