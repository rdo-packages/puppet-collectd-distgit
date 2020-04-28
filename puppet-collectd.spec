%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-collectd
%global commit 4686e16d3b869dcaea29125c742cd514509815fd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-collectd
Version:        12.0.0
Release:        1%{?alphatag}%{?dist}
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
* Thu Oct 3 2019 RDO <dev@lists.rdoproject.org> 11.0.0-1.785a71bgit
- Update to post 11.0.0 (785a71bd4be0d0e7e96aa6acea3c2120430058fc)




# REMOVEME: error caused by commit https://github.com/voxpupuli/puppet-collectd/commit/785a71bd4be0d0e7e96aa6acea3c2120430058fc
