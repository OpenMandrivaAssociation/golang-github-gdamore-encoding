%global goipath         github.com/gdamore/encoding
%global commit          b23993cbb6353f0e6aa98d0ee318a34728f628b9

%gometa

%global common_description %{expand:
Package encoding provides a number of encodings that are missing from the
standard Go encoding package.

We hope that we can contribute these to the standard Go library someday. It
turns out that some of these are useful for dealing with I/O streams coming
from non-UTF friendly sources.

The UTF8 Encoder is also useful for situations where valid UTF-8 might be
carried in streams that contain non-valid UTF; in particular I use it for
helping me cope with terminals that embed escape sequences in otherwise valid
UTF-8.
}

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Various character map encodings missing from golang.org/x/net/encoding
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(golang.org/x/text/encoding)
BuildRequires: golang(golang.org/x/text/transform)
BuildRequires: golang(github.com/smartystreets/goconvey/convey)

%description devel
%{common_description}

This package contains library source intended for building other packages
which use import path with %{goipath} prefix.


%prep
%gosetup -q


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%doc README.md
%license LICENSE


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitb23993c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.3.20180607gitb23993c
- Re-template against More Go Packaging guidelines

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20151215gitb23993c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20151215gitb23993c
- Add commit date to revision

* Fri Aug 18 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.gitb23993c
- Initial package for Fedora
