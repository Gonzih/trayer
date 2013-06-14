Name:		trayer-srg
Version:	1.1
Release:	0%{?dist}
Summary:	A lightweight GTK2-based systray

Group:		Applications/Productivity
License:	MIT

# The source for this package was pulled from upstream's git on Jun 14 2013.
# Use the following commands to generate the tarball:
# git clone https://github.com/sargon/trayer-srg.git
# tar -czf trayer-1.1-0.tar.gz trayer-src/*
Source:		https://github.com/Gonzih/trayer/blob/master/%{name}-%{version}-0.tar.gz

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
* Fri Jun 14 2013 Max Gonzih <gonzih@gmail.com> 1.1-0
- initial build
