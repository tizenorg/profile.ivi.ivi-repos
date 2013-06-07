Name:       ivi-repos
Summary:    Tizen IVI Repos
Version:    1
Release:    1
Group:      Base/Configuration
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
install -m 0644 ivi-snapshot.repo %{buildroot}/etc/zypp/repos.d
install -m 0644 ivi-daily.repo %{buildroot}/etc/zypp/repos.d 

%files
%defattr(-,root,root,-)
%config /etc/zypp/repos.d/ivi-snapshot.repo
%config /etc/zypp/repos.d/ivi-daily.repo

