%global milestone .0rc0
%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-collectd
%global commit acd970c429ebbdc0d3e2e11c7c66979eae63d3c6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-collectd
Version:        13.0.1
Release:        0.1%{?milestone}%{?alphatag}%{?dist}
Summary:        Puppet module for Collectd
License:        ASL 2.0

URL:            https://github.com/voxpupuli/%{upstream_name}

Source0:        https://github.com/voxpupuli/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Tue Sep 28 2021 RDO <dev@lists.rdoproject.org> 13.0.1-0.1.0rc0.acd970cgit
- Update to post 13.0.1 (acd970c429ebbdc0d3e2e11c7c66979eae63d3c6)


