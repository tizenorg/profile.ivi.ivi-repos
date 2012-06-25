Name:       ivi-repos-auto
Summary:    Tizen IVI Repos Auto
Version:    0.4
Release:    1
Group:      System/Libraries
License:    LGPLv2.1
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.bz2

%description
This package installs the .repo files for Tizen IVI automotive images

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/etc/zypp/repos.d
install -m 0755 tizen-base.repo %{buildroot}/etc/zypp/repos.d
install -m 0755 tizen-ivi.repo %{buildroot}/etc/zypp/repos.d
install -m 0755 tizen-non-oss.repo %{buildroot}/etc/zypp/repos.d

%post

%files
%defattr(-,root,root,-)
/etc/zypp/repos.d/*
