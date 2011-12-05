%define		plugin	cookie
Summary:	jQuery Cookie plugin
Name:		jquery-%{plugin}
Version:	1.0
Release:	2
License:	MIT / GPL
Group:		Applications/WWW
Source0:	https://github.com/carhartl/jquery-cookie/tarball/master#/%{plugin}.tgz
Patch0:		issue-13.patch
# Source0-md5:	d1be69258e0b0745e871b067fbf6cfac
URL:		http://plugins.jquery.com/project/Cookie
BuildRequires:	js
BuildRequires:	rpmbuild(macros) > 1.268
BuildRequires:	yuicompressor
Requires:	jquery >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
A simple, lightweight utility plugin for reading, writing and deleting
cookies.

%prep
%setup -qc
mv *-%{name}-*/* .
%patch0 -p1

%build
install -d build
# compress .js
yuicompressor --charset UTF-8 jquery.cookie.js -o build/jquery.cookie.js
js -C -f build/jquery.cookie.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p build/jquery.cookie.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
