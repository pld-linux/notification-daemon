Summary:	Notification Daemon
Summary(pl.UTF-8):	Demon powiadomień
Name:		notification-daemon
Version:	0.7.1
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/notification-daemon/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	6ef69d56ac727e8d3ad69e1abdbe98c5
URL:		http://www.galago-project.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-devel >= 0.11
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk3-devel >= 0.4
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
Requires:	dbus >= 1.0.0
Requires:	glib2 >= 1:2.28.0
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
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libexecdir}/notification-daemon
%{_desktopdir}/notification-daemon.desktop
