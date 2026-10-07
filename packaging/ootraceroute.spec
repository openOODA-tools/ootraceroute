Name:           ootraceroute
Version:        0.1.0
Release:        1%{?dist}
Summary:        Traces packet hops across networks with AS number lookups and latency maps.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ootraceroute
Source0:        ootraceroute-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ootraceroute is a sovereign, capability-bounded HOP TRACER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ootraceroute
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ootraceroute-uninstall

%files
/usr/bin/ootraceroute
/usr/bin/ootraceroute-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
