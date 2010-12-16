%define		plugin	cookie
Summary:	jQuery Cookie plugin
Name:		jquery-%{plugin}
# no version known, so pick the lowest
Version:	0.1
Release:	1
License:	MIT / GPL
Group:		Applications/WWW
Source0:	https://github.com/carhartl/jquery-cookie/tarball/master#/%{plugin}.tgz
# Source0-md5:	06563fe2bd9cf5fc348bae666205b901
URL:		https://github.com/carhartl/jquery-cookie
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

%build
install -d build
# compress .js
yuicompressor --charset UTF-8 jquery.cookie.js -o build/jquery.cookie.js
js -C -f build/jquery.cookie.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a build/jquery.cookie.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
