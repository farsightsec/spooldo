# this is creates an executable package and a development package
%global debug_package   %{nil}
Name:		spooldo		
Version:	0.8.1
Release:	1%{?dist}
Summary:	Spool directory processing utility

License:	Apache-2.0	
URL:		https://github.com/farsightsec/spooldo
Source0:	https://github.com/farsightsec/spooldo/archive/refs/tags/tags/v%{version}.tar.gz

BuildRequires:	python3-devel python3-setuptools

%description
spooldo is a script for continuously processing the files that accumulate in
a directory.
It takes three parameters on the command line: the "incoming" directory, "active" directory, and the "archive" directory. The incoming and active
"active" directory, and the "archive" directory. The incoming and active
directories are required; the archive directory is optional. spooldo
continuously links new files in the incoming directory into the active
directory, and then unlinks them from the incoming directory.

%prep
%setup -q -n spooldo-%{version}
%build

%install
install -D -m 0755 spooldo %{buildroot}/%{_bindir}/spooldo

%files
%doc LICENSE README
/usr/bin/spooldo

%post

chmod +x /usr/bin/spooldo


%changelog

