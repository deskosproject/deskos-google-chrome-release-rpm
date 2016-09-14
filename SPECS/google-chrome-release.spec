Name:           google-chrome-release
Version:        1.0
Release:        1%{?dist}
Summary:        Google Chrome repository configuration

Group:          System Environment/Base
License:        BSD
URL:            http://google.com/chrome
Source0:        google-chrome
Source1:        google-chrome.repo
Source2:        RPM-GPG-KEY-google-chrome
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch

%description
Google Chrome repository configuration.

%prep
#%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/etc/default
install -m 644 %SOURCE0 $RPM_BUILD_ROOT/etc/default/

install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 %SOURCE1 $RPM_BUILD_ROOT/etc/yum.repos.d/

install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 %SOURCE2 $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
/etc/pki/rpm-gpg/RPM-GPG-KEY-google-chrome
/etc/default/google-chrome
%config(noreplace) /etc/yum.repos.d/google-chrome.repo

%changelog
* Fri Apr 15 2016 Ricardo Arguello <rarguello@deskosproject.org> - 1.0-1
- Initial release
