%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-module-collectd
%global commit 4a3843cdad526adb1527a6ad9ba503ae9b7d6361
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-collectd
Version:        5.1.0
Release:        2%{?alphatag}%{?dist}'
Summary:        Puppet module for Collectd
License:        Apache-2.0

URL:            https://github.com/puppet-community/puppet-collectd

Source0:        https://github.com/pdxcat/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-concat
Requires:       puppet >= 2.7.0

%description
Puppet module for Collectd

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/module-collectd/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/module-collectd/



%files
%{_datadir}/openstack-puppet/modules/module-collectd/


%changelog
* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 5.1.0-2.4a3843c.git
- Newton update 5.1.0 (4a3843cdad526adb1527a6ad9ba503ae9b7d6361)

* Wed Sep 21 2016 Haikel Guemar <hguemar@fedoraproject.org> - 5.1.0-1.d50e5ae.git
- Newton update 5.1.0 (d50e5ae34f5963f73625c1ed30cab1399d5610a4)


