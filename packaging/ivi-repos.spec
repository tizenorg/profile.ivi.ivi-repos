%bcond_with emulator

Name:       ivi-repos
Summary:    Tizen IVI Repos
Version:    7
Release:    0
Group:      Base/Configuration
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
install -m 0644 ivi-emul-snapshot.repo %{buildroot}/etc/zypp/repos.d
install -m 0644 ivi-emul-daily.repo %{buildroot}/etc/zypp/repos.d
%else
%ifarch %arm
install -m 0644 ivi-arm-snapshot.repo %{buildroot}/etc/zypp/repos.d
install -m 0644 ivi-arm-daily.repo %{buildroot}/etc/zypp/repos.d
%else
install -m 0644 ivi-snapshot.repo %{buildroot}/etc/zypp/repos.d
install -m 0644 ivi-daily.repo %{buildroot}/etc/zypp/repos.d 
%endif
%endif

%files
%defattr(-,root,root,-)
%if %{with emulator}
%config /etc/zypp/repos.d/ivi-emul-snapshot.repo
%config /etc/zypp/repos.d/ivi-emul-daily.repo
%else
%ifarch %arm
%config /etc/zypp/repos.d/ivi-arm-snapshot.repo
%config /etc/zypp/repos.d/ivi-arm-daily.repo
%else
%config /etc/zypp/repos.d/ivi-snapshot.repo
%config /etc/zypp/repos.d/ivi-daily.repo
%endif
%endif

