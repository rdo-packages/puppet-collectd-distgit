Name:           puppet-collectd
Version:        XXX
Release:        XXX
Summary:        Puppet module for Collectd
License:        Apache-2.0

URL:            https://github.com/puppet-community/puppet-collectd

Source0:        https://github.com/pdxcat/puppet-module-collectd/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-concat
Requires:       puppet >= 2.7.0

%description
Puppet module for Collectd

%prep
%setup -q -n %{name}-%{version}

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
