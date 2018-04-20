Name:		switchboard
Version:	1
Release:	1%{?dist}
Summary:    Local URL shortcut HTTP server

%global commit 15e59ec8c06045ea5a2fe8ec6621869057131279
%global shortcommit 15e59ec
%global commitdate 20180420
%global import_path github.com/nixprime/switchboard
%global forked_import_path github.com/cfallin/switchboard
%global repo switchboard

Group:		Network Servers
License:	MIT
URL:		https://%{import_path}
Source0:	https://%{forked_import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

BuildRequires:	compiler(go-compiler)
Requires:	systemd libcap

%description


%prep
%setup -q -n %{repo}-%{commit}


%build
%gobuild -o switchboard

%install
install -d %{buildroot}%{_bindir}
install -p -m 755 switchboard %{buildroot}%{_bindir}
install -d %{buildroot}/lib/systemd/system
install -p -m 644 systemd/switchboard.service %{buildroot}/lib/systemd/system
install -d %{buildroot}%{_sysconfdir}
install -p -m 644 switchboard.conf %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_docdir}
install -p -m 644 README.md LICENSE %{buildroot}%{_docdir}

%files
%doc %{_docdir}/README.md
%doc %{_docdir}/LICENSE
%{_bindir}/switchboard
%config %{_sysconfdir}/switchboard.conf
/lib/systemd/system/switchboard.service

%post

if [ -x `which setcap` ]; then
    setcap cap_net_bind_service+ep %{_bindir}/switchboard
else
    chmod 1777 %{_bindir}/switchboard
fi

%changelog

* Fri Apr 20 2018 Chris Fallin <cfallin@c1f.net> - 1.0.0-1
- Initial packaging.
