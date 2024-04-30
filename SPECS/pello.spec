Name:           pello
Version:        0.1.1
Release:        1%{?dist}
Summary:        Hello World example implemented in Python

License:        GPLv3+
URL:            https://example.com/%{name}
Source0:        https://example.com/%{name}/release/%{name}-%{version}.tar.gz

BuildRequires:  python3
Requires:       python3
Requires:       bash

BuildArch:      noarch

%description
The long-tail description for our Hello World Example implemented in
Python.

%prep
%setup -q


%build

python3 -m compileall pello.py


%install

mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/usr/lib/%{name}

cat > %{buildroot}%{_bindir}/%{name} <<-EOF
#!/bin/bash
/usr/bin/python3 /usr/lib/%{name}/%{name}.pyc
EOF

chmod 0755 %{buildroot}%{_bindir}/%{name}

install -m 0644 %{name}.py* %{buildroot}/usr/lib/%{name}/
%post -p /usr/bin/python3
print("This is {} code".format("python"))


%files
%dir /usr/lib/%{name}/
%{_bindir}/%{name}
/usr/lib/%{name}/%{name}.py*



%changelog
* Tue Apr 30 2024 Jeffrey Bucher <jeffiscow@fedoraproject.org>
- First pello package
- Example second item in the changelog for version-release 0.1.1-1
