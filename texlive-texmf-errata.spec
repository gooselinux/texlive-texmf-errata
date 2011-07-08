# This spec file is based on texjive project created by Michael A. Peters.
# Adopted and modified for Fedora users by Jindrich Novy.

Name:		texlive-texmf-errata
Version:	2007
Release:	7.1%{?dist}
Summary:	Errata for texlive-texmf
Group:		Applications/Publishing
License:	Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:		http://tug.org/texlive/
Source999:	texlive-errata-readme
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
This package is where errata to the texlive-texmf package will appear, when
needed.

%package afm
Group:		Applications/Publishing
Summary:	Errata for texlive-texmf-afm

%description afm
This package is where errata to the texlive-texmf-afm package will appear,
when needed.

%package dvips
Group:		Applications/Publishing
Summary:	Errata for texlive-texmf-dvips

%description dvips
This package is where bug fixes to the texlive-texmf-dvips package will appear,
when needed.

%package fonts
Group:		Applications/Publishing
Summary:	Bug fixes for texlive-texmf-fonts

%description fonts
This package is where bug fixes to the texlive-texmf-fonts package will appear,
when needed.

%package latex
Group:		Applications/Publishing
Summary:	Errata for texlive-texmf-latex

%description latex
This package is where errata to the texlive-texmf-latex package will appear,
when needed.

%package doc
Group:		Applications/Publishing
Summary:	Errata for texlive-doc
Obsoletes:	texlive-doc-errata < 2007-1
Provides:	texlive-doc-errata = %{version}-%{release}

%description doc
This package includes errata to the texlive documentation.

%package east-asian
Group:		Applications/Publishing
Summary:	Errata for texlive-texmf-east-asian
Obsoletes:	texlive-texmf-errata-japanese < 2007-3
Provides:	texlive-texmf-errata-japanese = %{version}-%{release}

%description east-asian
This package is where errata to the texlive-texmf-east-asian package will appear,
when needed.

%package context
Group:		Applications/Publishing
Summary:	Errata for texlive-texmf-context

%description context
This package is where errata to the texlive-texmf-context package will appear,
when needed.

%package xetex
Group:		Applications/Publishing
Summary:	Errata for texlive-texmf-xetex

%description xetex
This package is where errata to the texlive-texmf-xetex package will appear,
when needed.

%prep


%build


%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_datadir}/texmf-errata/doc/texlive
install -d -m755 %{buildroot}%{_datadir}/texmf-errata/dvips
install -d -m755 %{buildroot}%{_datadir}/texmf-errata/fonts/afm
install -d -m755 %{buildroot}%{_datadir}/texmf-errata/tex/latex
install -d -m755 %{buildroot}%{_datadir}/texmf-errata/ptex
install -d -m755 %{buildroot}%{_datadir}/texmf-errata/jbibtex
install -m644 %{SOURCE999} %{buildroot}%{_datadir}/texmf-errata/doc/texlive/README
touch %{buildroot}%{_datadir}/texmf-errata/ls-R


%clean
rm -rf %{buildroot}

# turn these off until there is a need for them
#%%%post
#%%#[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :

#%%%post afm
#%%#[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :

#%%%post common
#%%#[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :

#%%%post dvips
#%%#[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :

#%%%post fonts
#%%#[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :

#%%%post latex
#%%#[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :

#%%%post -n texlive-doc-errata
#%%#[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :

#%%%postun
#%%#[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :

#%%%postun afm
#%%#[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :

#%%%postun common
#%%#[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :

#%%%postun dvips
#%%#[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :

#%%%postun fonts
#%%#[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :

#%%%postun latex
#%%#[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :

#%%%postun -n texlive-doc-errata
#%%#[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :


%files
%defattr(-,root,root,-)
%dir %{_datadir}/texmf-errata
%dir %{_datadir}/texmf-errata/tex

%files afm
%defattr(-,root,root,-)
%dir %{_datadir}/texmf-errata
%dir %{_datadir}/texmf-errata/fonts
%dir %{_datadir}/texmf-errata/fonts/afm

%files dvips
%defattr(-,root,root,-)
%dir %{_datadir}/texmf-errata
%dir %{_datadir}/texmf-errata/dvips

%files fonts
%defattr(-,root,root,-)
%dir %{_datadir}/texmf-errata
%dir %{_datadir}/texmf-errata/fonts
%ghost %{_datadir}/texmf-errata/ls-R

%files latex
%defattr(-,root,root,-)
%dir %{_datadir}/texmf-errata
%dir %{_datadir}/texmf-errata/tex
%dir %{_datadir}/texmf-errata/tex/latex

%files doc
%defattr(-,root,root,-)
%dir %{_datadir}/texmf-errata
%doc %{_datadir}/texmf-errata/doc/

%files east-asian
%defattr(-,root,root,-)
%dir %{_datadir}/texmf-errata
%doc %{_datadir}/texmf-errata/ptex/
%doc %{_datadir}/texmf-errata/jbibtex/

%files context
%defattr(-,root,root,-)

%files xetex
%defattr(-,root,root,-)

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2007-7.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2007-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2007-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Ondrej Vasik <ovasik@redhat.com> - 2007-5
- do own directories properly(#474028)

* Mon Mar 03 2008 Jindrich Novy <jnovy@redhat.com> - 2007-4
- add texlive-texmf-errata-xetex

* Thu Feb 28 2008 Jindrich Novy <jnovy@redhat.com> - 2007-3
- rename japanese to east-asian
- fix description, obsolete old japanese package

* Tue Feb 19 2008 Jindrich Novy <jnovy@redhat.com> - 2007-2
- add errata packages for japanese/ConTeXt

* Mon Jan 14 2008 Jindrich Novy <jnovy@redhat.com> - 2007-1
- texlive-doc-errata -> texlive-texmf-errata-doc

* Tue Sep 18 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.10
- remove common subpackage

* Wed Aug 15 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.9
- update License tag, it texmf-errata doesn't contain anything
  but will contain the stuff licensed under the same license
  like texlive-texmf

* Tue Aug 07 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.8
- bump

* Tue Jul 24 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.7
- fix summary of latex errata subpackage
- use better rehashing when needed
- update README file

* Wed Jul 18 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.6
- sync with texlive and texlive-texmf packages

* Wed Jul 04 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.5
- bump release again

* Mon Jul 02 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.4
- sync with texlive and texlive-texmf packages

* Thu Feb 15 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.1.20070212.rc
- update to TeXLive 2007 release candidate
- clean buildroot in %%install

* Tue May 30 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.3
- some directory ownership cleanup

* Mon May 28 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.2
- initial mock build

* Fri May 26 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.1
- initial spec file
