Name:		trayer-srg
Version:	1.1
Release:	1%{?dist}
Summary:	A lightweight GTK2-based systray

Group:		Applications/Productivity
License:	MIT

# The source for this package was pulled from upstream's git on May 31 2012. 
# Use the following commands to generate the tarball:
# git clone https://github.com/sargon/trayer-srg.git
# && tar -czf trayer-1.1.tar.gz trayer-1.1/*
Source:		https://github.com/bryanbickford/trayer/blob/master/%{name}-%{version}-1.tar.gz

BuildRequires:	gtk2-devel,libXmu-devel

%description
trayer is a systray for alternative desktop environments.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
make PREFIX=$RPM_BUILD_ROOT/usr install

%files
%doc COPYING CREDITS CHANGELOG README TODO
%{_bindir}/trayer

%changelog
* Mon Jul 09 2012 Bryan Bickford <bryan@unhwildhats.com> 1.1-1
- rpm bug fixes
* Thu May 31 2012 Bryan Bickford <bryan@unhwildhats.com> 1.1-0
- initial build
