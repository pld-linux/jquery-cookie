%define		plugin	cookie
Summary:	jQuery Cookie plugin
Name:		jquery-%{plugin}
Version:	1.1
Release:	1
License:	MIT / GPL
Group:		Applications/WWW
Source0:	https://github.com/carhartl/jquery-cookie/tarball/v1.1/%{name}-%{version}.tgz
# Source0-md5:	18f71cea2801bcbe1da2aa810c73833c
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

%build
install -d build
# compress .js
%{__sed} -e 's,/\*!,/*,' jquery.cookie.js > build/tmp.js
yuicompressor --charset UTF-8 build/tmp.js -o build/jquery.cookie.js
js -C -f build/jquery.cookie.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p jquery.cookie.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
cp -p build/jquery.cookie.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md
%{_appdir}
