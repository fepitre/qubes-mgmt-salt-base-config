%{!?version: %define version %(cat version)}

Name:      qubes-mgmt-salt-base-config
Version:   %{version}
Release:   1%{?dist}
Summary:   Qubes+Salt Management base configuration for SaltStack's Salt Infrastructure automation and management system
License:   GPL 2.0
URL:	   http://www.qubes-os.org/

Group:     System administration tools
BuildArch: noarch
Requires:  salt
Requires:  salt-minion
Requires:  qubes-mgmt-salt-config
Requires:  qubes-mgmt-salt-base-overrides
Requires:  qubes-mgmt-salt-base-overrides-libs
Requires:  qubes-mgmt-salt-base-topd

%define _builddir %(pwd)

%description
Qubes+Salt Management base configuration for SaltStack's Salt Infrastructure
automation and management system.

%prep
# we operate on the current directory, so no need to unpack anything
# symlink is to generate useful debuginfo packages
rm -f %{name}-%{version}
ln -sf . %{name}-%{version}
%setup -T -D

%build

%install
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir} BINDIR=%{_bindir} SBINDIR=%{_sbindir} SYSCONFDIR=%{_sysconfdir}

%post

# disable formula which used to be in this package
rm -f /srv/salt/_tops/base/config.top
rm -f /srv/pillar/_tops/base/config.top
rm -f /srv/pillar/_tops/base/config.modules.top
rm -f /srv/pillar/_tops/dom0/config.top
rm -f /srv/pillar/_tops/dom0/config.modules.top

%files
%defattr(-,root,root)
%doc LICENSE README.rst

%attr(750, root, root) %dir /srv/salt/qubes
/srv/salt/qubes/directories.sls
/srv/salt/qubes/directories.top
/srv/salt/qubes/files/locale.sls
/srv/salt/qubes/files/pillar.sls
/srv/salt/qubes/files/top.sls
/srv/salt/qubes/LICENSE
/srv/salt/qubes/README.rst
/srv/salt/qubes/user-dirs.sls
/srv/salt/qubes/user-dirs.top

/srv/pillar/vmtype.jinja

%changelog
