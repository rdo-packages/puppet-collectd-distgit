%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-module-collectd
%global commit eb1e0a95cb62fc6cd41f0a2c60fcdf34e7eaf596
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-collectd
Version:        5.3.0
Release:        1%{?alphatag}%{?dist}
Summary:        Puppet module for Collectd
License:        ASL 2.0

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/collectd/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/collectd/



%files
%{_datadir}/openstack-puppet/modules/collectd/


%changelog
* Thu Feb 09 2017 Alfredo Moralejo <amoralej@redhat.com> 5.3.0-1.eb1e0a9git
- Ocata update 5.3.0 (eb1e0a95cb62fc6cd41f0a2c60fcdf34e7eaf596)

