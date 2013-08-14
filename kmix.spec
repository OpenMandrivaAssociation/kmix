Name:		kmix
Version:	4.11.0
Release:	1
Epoch:		3
Summary:	KDE Digital Mixer
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org/applications/multimedia/kmix/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kmix-4.9.2-nodisplay.patch
# Adjust popup widget layout
# Device icons should no longer hit window border with some styles
Patch1:		kmix-4.10.3-layout.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libcanberra)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
Requires:	kdebase4-runtime
Obsoletes:	kdemultimedia4-core < 3:4.5.71
Conflicts:	kdemultimedia4-devel < 3:4.8.95
Conflicts:	kde4-audiocd < 3:4.8.95

%description
KMix is an application to allow you to change the volume of your sound
card. Though small, it is full-featured, and it supports several
platforms and sound drivers.

%files
%{_kde_appsdir}/kmix
%{_kde_appsdir}/plasma/services/mixer.operations
%{_kde_bindir}/kmix
%{_kde_bindir}/kmixctrl
%{_kde_iconsdir}/*/*/*/*
%{_kde_applicationsdir}/kmix.desktop
%{_kde_services}/kmixctrl_restore.desktop
%{_kde_services}/plasma-engine-mixer.desktop
%{_kde_services}/kded/kmixd.desktop
%{_kde_libdir}/libkdeinit4_kmix*
%{_kde_libdir}/kde4/kded_kmixd.so
%{_kde_libdir}/kde4/plasma_engine_mixer.so
%{_kde_autostart}/restore_kmix_volumes.desktop
%{_kde_autostart}/kmix_autostart.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kmix.control.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmix.mixer.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmix.mixset.xml
%{_kde_docdir}/HTML/en/kmix

#------------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.4-1
- New version 4.10.4

* Wed May 22 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.3-2
- Add patch to adjust popup widget layout (device icons should no longer hit
  window border with some styles)

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.2-2
- New version 4.9.2
- Add kmix-4.9.2-nodisplay patch

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.0-1
- New version 4.9.0

* Sun Jul 22 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.97-1
- New version 4.8.97

* Wed Jul 11 2012 Andrey Bondrov <abondrov@mandriva.org> 3:4.8.95-1
+ Revision: 808878
- imported package kmix


* Tue Jul 10 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.95-1
- Follow upstream and move kmix from kdemultimedia4 to own package
