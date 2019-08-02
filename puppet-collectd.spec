%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-module-collectd
%global commit 93c8d0bd32bb5610652f30e785ba6644fc82a8b6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-collectd
Version:        10.0.2
Release:        0%{?alphatag}%{?dist}
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
* Fri Aug 02 2019 Mattthias Runge <mrunge@redhat.com> - 10.0.2
- sync with rocky version to support feature backports

* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 8.0.2-0.93c8d0bgit
- Update to 8.0.2-rc0 (93c8d0bd32bb5610652f30e785ba6644fc82a8b6)



