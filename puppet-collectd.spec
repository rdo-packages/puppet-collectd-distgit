%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-collectd
%global commit f0b4d8507ec2719fae6b91e36a6f0d8c665987e8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-collectd
Version:        XXX
Release:        XXX
Summary:        Puppet module for Collectd
License:        ASL 2.0

URL:            https://github.com/voxpupuli/%{upstream_name}

Source0:        https://github.com/voxpupuli/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz
Patch0001:      0001-Add-backwards-compatibility-in-transition-to-Stdlib-.patch

BuildArch:      noarch

BuildRequires:  git
Requires:       puppet-stdlib
Requires:       puppet-concat
Requires:       puppet >= 2.7.0

%description
Puppet module for Collectd

%prep
%autosetup -n %{name}-%{upstream_version} -S git

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/collectd/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/collectd/



%files
%{_datadir}/openstack-puppet/modules/collectd/


%changelog

# REMOVEME: error caused by commit https://github.com/voxpupuli/puppet-collectd/commit/b2f7e70fd8f54f62ecaa43dd43031c818fdc9465
