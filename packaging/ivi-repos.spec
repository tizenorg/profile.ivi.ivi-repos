%bcond_with emulator

Name:       ivi-repos
Summary:    Tizen IVI Repos
Version:    8
Release:    1
Group:      Automotive/Configuration
BuildArch:  noarch
License:    GPL-2.0
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.bz2

%description
This package installs the .repo files for Tizen IVI images

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/etc/zypp/repos.d
%if %{with emulator}
type='emul-'
%endif
install -m 0644 ivi-$type*.repo %{buildroot}/etc/zypp/repos.d

%files
%defattr(-,root,root,-)
%dir %{_sysconfdir}/zypp
%dir %{_sysconfdir}/zypp/repos.d
%config /etc/zypp/repos.d/*.repo
