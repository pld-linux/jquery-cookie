%define		plugin	cookie
Summary:	jQuery Cookie plugin
Name:		jquery-%{plugin}
Version:	1.2.0
Release:	1
License:	MIT / GPL
Group:		Applications/WWW
Source0:	https://github.com/carhartl/jquery-cookie/archive/v%{version}.tar.gz
# Source0-md5:	573ad639cbfeb66760300dfaaff95322
URL:		http://plugins.jquery.com/cookie/
BuildRequires:	js
BuildRequires:	rpmbuild(macros) > 1.268
BuildRequires:	closure-compiler
Requires:	jquery >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
A simple, lightweight utility plugin for reading, writing and deleting
cookies.

%prep
%setup -q

%build
install -d build
# compress .js
for js in jquery.cookie.js; do
	out=build/${js#*/jquery.}
%if 0%{!?debug:1}
	closure-compiler --js $js --charset UTF-8 --js_output_file $out
	js -C -f $out
%else
	cp -p $js $out
%endif
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p jquery.cookie.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
cp -p build/jquery.cookie.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md
%{_appdir}
