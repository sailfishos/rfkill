Name:       rfkill

Summary:    rfkill utility
Version:    0.5
Release:    1
Group:      System Environment/Base
License:    ISC
URL:        https://github.com/sailfishos/rfkill
Source0:    %{name}-%{version}.tar.gz

%description
rfkill is a tool to use /dev/rfkill.

%package doc
Summary:    Documentation for rfkill
Group:      Documentation
Requires:   %{name} = %{version}-%{release}
Requires:   %{name} = %{version}

%description doc
Documentation for rfkill.

%prep
%setup -q -n %{name}-%{version}/rfkill

%build
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%{_sbindir}/rfkill

%files doc
%defattr(-,root,root,-)
%{_datadir}/man/man8/rfkill.8.gz
