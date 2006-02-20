# TODO
# - use system lib/HTMLSax3
# - WAKKA_CONFIG
Summary:	Small, lightweight, handy, expandable Wiki-clone
Summary(pl):	Ma³y, lekki, porêczny, rozszerzalny klon Wiki
Name:		wacko
Version:	4.2
Release:	0.1
License:	BSD
Group:		Applications/WWW
Source0:	http://wackowiki.com/files/%{name}.r%{version}.tar.gz
# Source0-md5:	589eef29697be4f04635f1742ab2040d
URL:		http://wackowiki.com/WackoWiki
BuildRequires:	sed >= 4.0
Requires:	webapps
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}
%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}

%description
Small, lightweight, handy, expandable Wiki-clone written in PHP4.

This code was forked from WakkaWiki 0.1.2, with some patches from ChS,
wikini.net, some new actions from WakkaWiki.de and essential amount of
our own sourcecode.

%description -l pl
Ma³y, lekki, porêczny, rozszerzalny klon Wiki napisany w PHP4.

Ten kod wywodzi siê z WakkaWiki 0.1.2 z pewn± liczb± ³at z ChS,
wikini.net, nowymi akcjami z WakkaWiki.de i znacz±c± ilo¶ci± w³asnego
kodu ¼ród³owego.

%prep
%setup -q -n %{name}.r%{version}
find . -type f -print0 | xargs -0 sed -i -e 's,\r$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir}}
cp -a *.php $RPM_BUILD_ROOT%{_appdir}
cp -a *.conf $RPM_BUILD_ROOT%{_appdir}
cp -a _cache actions classes db files formatters handlers images js lang lib setup themes xml $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/*
%lang(ru) %doc readme.rus
%{_appdir}
