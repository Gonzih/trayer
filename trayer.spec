Name:		trayer
Version:	1.1
Release:	1%{?dist}
Summary:	trayer-srg is a lightweight GTK2-based systray

Group:		Applications/Productivity
License:	MIT
URL:		https://github.com/sargon/trayer-srg/blob/master

# The source for this package was pulled from upstream's git on May 31 2012. 
# Use the following commands to generate the tarball:
# git clone https://github.com/sargon/trayer-srg.git && tar -xzf trayer-srg/*
Source:		https://github.com/bryanbickford/trayer/blob/master/%{name}-%{version}.tar.gz

BuildRequires:	gtk2-devel
Requires:	libXmu-devel

%description
trayer is a systray for alternative desktop environments.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
make PREFIX=$RPM_BUILD_ROOT/usr install

%files
%defattr(-,root,root,-)
%doc COPYING CREDITS CHANGELOG README TODO
%{_bindir}/%{name}

%changelog
* Thu May 31 2012 Bryan Bickford <bryan@unhwildhats.com> 1.1
- initial build
