Name:		nixprime-switchboard
Version:	1.0.0
Release:	2%{?dist}
Summary:    Local URL shortcut HTTP server

%global commit 090c9cd44e168b8e03448082370aaaddc0b9e8f1
%global commitdate 20180420
%global import_path github.com/nixprime/switchboard
%global forked_import_path github.com/cfallin/switchboard
%global repo switchboard

Group:		Network Servers
License:	MIT
URL:		https://%{import_path}
Source0:	https://%{forked_import_path}/archive/%{commit}/%{repo}-%{commit}.tar.gz

BuildRequires:	compiler(go-compiler)
Requires:	systemd libcap

%description


%prep
%setup -q -n %{repo}-%{commit}


%build
%gobuild -o nixprime-switchboard

%install
install -d %{buildroot}%{_bindir}
install -p -m 755 nixprime-switchboard %{buildroot}%{_bindir}
install -d %{buildroot}/lib/systemd/system
install -p -m 644 systemd/nixprime-switchboard.service %{buildroot}/lib/systemd/system
install -d %{buildroot}%{_sysconfdir}
install -p -m 644 nixprime-switchboard.conf %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_docdir}
install -p -m 644 README.md LICENSE %{buildroot}%{_docdir}

%files
%doc %{_docdir}/README.md
%doc %{_docdir}/LICENSE
%{_bindir}/nixprime-switchboard
%config %{_sysconfdir}/nixprime-switchboard.conf
/lib/systemd/system/nixprime-switchboard.service

%post

setcap cap_net_bind_service+ep %{_bindir}/nixprime-switchboard

%changelog

* Fri Apr 20 2018 Chris Fallin <cfallin@c1f.net> - 1.0.0-2
- Renamed from switchboard to nixprime-switchboard to avoid package name
  conflict.

* Fri Apr 20 2018 Chris Fallin <cfallin@c1f.net> - 1.0.0-1
- Initial packaging.
